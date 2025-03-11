.. note::

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者と一緒にもっと深く探求しましょう。

    **参加する理由**

    - **専門的サポート**：コミュニティとチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学びと共有**：スキルを向上させるためのヒントやチュートリアルを交換しましょう。
    - **独占プレビュー**：新製品の発表や先行情報を早期に入手。
    - **特別割引**：最新製品の独占的な割引を楽しむことができます。
    - **祭りのプロモーションとギフト**：ギフト企画や祝祭のプロモーションに参加します。

    👉 私たちと一緒に探索し、創造してみませんか？クリックして[|link_sf_facebook|]今日から参加！

.. _py_somato_controller:

7.11 ソマトセンサリーコントローラーの構築
===========================================

このエキサイティングなプロジェクトでは、Raspberry Pi Pico 2、MPU6050加速度計・ジャイロスコープモジュール、およびサーボモーターを使用して **ソマトセンサリーコントローラー** を作成します。このデバイスは、手の傾きを特にキャプチャし、それをサーボモーターの動きに変換します。この技術は、手術用ロボットやロボットアームなど、ロボティクスと遠隔操作システムに使用される技術と似ています。

**必要なもの**

このプロジェクトには、以下のコンポーネントが必要です。

便利なキットを購入することをお勧めします。こちらがリンクです：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名称
        - このキットのアイテム
        - リンク
    *   - ニュートンラボキット
        - 450以上
        - |link_newton_lab_kit|

また、以下のリンクから個別に購入することもできます。


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - コンポーネント
        - 数量
        - リンク

    *   - 1
        - :ref:`cpn_pico_2`
        - 1
        - |link_pico2_buy|
    *   - 2
        - マイクロUSBケーブル
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - 数本
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_mpu6050`
        - 1
        - 
    *   - 6
        - :ref:`cpn_servo`
        - 1
        - |link_servo_buy|

**コンポーネントの理解**

* **MPU6050 加速度計・ジャイロスコープ**：X、Y、Z軸に沿った加速度と角速度を測定する6軸モーショントラッキングデバイス。手の傾きを検出するために使用します。
* **サーボモーター**：特定の角度に移動するよう制御できるモーター。MPU6050によって検出された動きを模倣するために使用します。

**回路図**

|sch_somato|

MPU6050は、各方向の加速値に基づいて姿勢角を計算します。

プログラムは、姿勢角の変化に応じてサーボの対応する偏角を制御します。

**配線図**

|wiring_somatosensory_controller| 

**コードの作成**

次のようなMicroPythonスクリプトを書きます：

* MPU6050から加速度計のデータを読み取ります。
* 手の傾き角を計算します。
* サーボモーターを制御して傾きを模倣します。

.. note::

    * ``7.11_somatosensory_controller.py`` を ``newton-lab-kit/micropython`` から開くか、Thonnyにコードをコピーして、「Run」をクリックするかF5を押してください。
    * 正しいインタプリタが選択されていることを確認してください：MicroPython (Raspberry Pi Pico).COMxx。
    * ``imu.py`` および ``vector3d.py`` がPicoにアップロードされているか確認してください。詳細なチュートリアルは :ref:`add_libraries_py` を参照してください。

.. code-block:: python

    from imu import MPU6050
    from machine import I2C, Pin, PWM
    import utime
    import math

    # MPU6050用のI2C通信を初期化
    i2c = I2C(1, scl=Pin(7), sda=Pin(6))
    mpu = MPU6050(i2c)

    # GP15上のサーボモーター用のPWMを初期化
    servo = PWM(Pin(15))
    servo.freq(50)  # サーボの周波数を50Hzに設定

    # 角度をPWMデューティサイクルにマップする関数
    def angle_to_duty(angle):
        # 角度(0-180)をデューティサイクル(0.5ms - 2.5msパルス幅)に変換
        # デューティサイクルの範囲は50Hzで0.5msから2.5msの2%から12%
        duty_cycle = (angle / 18) + 2
        duty_u16 = int(duty_cycle / 100 * 65535)
        return duty_u16

    # 加速度計データから傾き角を取得する関数
    def get_tilt_angle():
        accel = mpu.accel
        x = accel.x
        y = accel.y
        z = accel.z
        angle = math.atan2(y, z) * (180 / math.pi)
        return angle + 90  # 角度を0から180の範囲に調整

    # メインループ
    try:
        while True:
            angle = get_tilt_angle()
            if angle < 0:
                angle = 0
            elif angle > 180:
                angle = 180
            duty = angle_to_duty(angle)
            servo.duty_u16(duty)
            utime.sleep(0.1)
    except KeyboardInterrupt:
        servo.deinit()
        print("Program stopped.")

プログラムを開始したら、手を上下に傾けてください。
サーボモーターはその傾きに合わせて動き、手の動きに応じて反応します。
サーボモーターが手の動きにどのように反応するかを観察してください。

**コードの理解**

#. 初期化：

   * **I2C通信**：MPU6050からデータを読み取るための設定。
   * **サーボモーターPWM**：50Hzの周波数でGP15に初期化。

#. 角度計算：

   * ``get_tilt_angle()``：加速度計のデータに基づいて傾斜角度を計算します。計算された角度は0度から180度の範囲に調整されます。

   .. code-block:: python

        def get_tilt_angle():
            accel = mpu.accel
            x = accel.x
            y = accel.y
            z = accel.z
            angle = math.atan2(y, z) * (180 / math.pi)
            return angle + 90  # 角度を0～180度の範囲に調整

#. サーボ制御：

   * ``angle_to_duty(angle)``：角度をサーボモーターの適切なPWMデューティサイクルに変換します。
   * デューティサイクル計算：サーボモーターは0.5ms（0度）から2.5ms（180度）のパルスを50Hzで受け取ります。

   .. code-block:: python

        def angle_to_duty(angle):
            # 角度（0～180）をデューティサイクル（0.5ms - 2.5msのパルス幅）に変換
            # デューティサイクルの範囲は、50Hzで0.5ms～2.5msに対応する2％～12％
            duty_cycle = (angle / 18) + 2
            duty_u16 = int(duty_cycle / 100 * 65535)
            return duty_u16

#. メインループ：

   * 傾斜角度を読み取ります。
   * 角度を調整して、0～180度の範囲に収めます。
   * その角度に基づいてサーボの位置を設定します。
   * ジッターを防ぐために短い遅延を挿入します。
   * キーボードインタラプトをキャプチャして、サーボを安全に停止します。

   .. code-block:: python

        try:
            while True:
                angle = get_tilt_angle()
                if angle < 0:
                    angle = 0
                elif angle > 180:
                    angle = 180
                duty = angle_to_duty(angle)
                servo.duty_u16(duty)
                utime.sleep(0.1)
        except KeyboardInterrupt:
            servo.deinit()
            print("Program stopped.")

**トラブルシューティング**

* サーボが動かない：

  * サーボに正しく電源が供給されているか確認してください。
  * 信号線がGP15に接続されていることを確認してください。
  * Picoとサーボ間でグラウンドが接続されていることを確認してください。

* 動きが不正確：

  * MPU6050がしっかりと固定されており、過度に揺れていないことを確認してください。
  * 必要に応じて角度計算を調整してください。

* プログラムエラー：

  * imu.pyとvector3d.pyが正しくアップロードされているか確認してください。
  * コード内にタイプミスやインデントのエラーがないかチェックしてください。

**拡張と強化**

* 複数のサーボ制御：

  * 他の軸の動きを制御するためにサーボを追加します。
  * 他の軸回転を処理するためにコードを拡張します。

* ワイヤレス通信：

  BluetoothやWi-Fiモジュールを使用して、センサーデータをサーボを制御する別のデバイスに送信します。

* データスムージング：

  センサーの読み取り値を平滑化するためにフィルタ（例：カルマンフィルタ）を実装します。

* 視覚的フィードバック：

  OLEDまたはLCDディスプレイを追加して、リアルタイムで角度データを表示します。

**結論**

このプロジェクトでは、ヒトの動きをキャプチャして機械的な動きに変換する身体感覚コントローラーを作成しました。このプロジェクトは、センサーとアクチュエーターが連携して、ロボティクスやリモート操作に使用されるようなインタラクティブシステムを作り出す方法を示しています。

さらに機能を追加したり、他のシステムに統合したりして、このプロジェクトを拡張してください。
