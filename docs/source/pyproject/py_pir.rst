.. note::

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者と共にさらに深く学びましょう。

    **なぜ参加するべきか？**

    - **専門家によるサポート**: 購入後の問題や技術的な課題を、コミュニティやチームからサポートを受けて解決できます。
    - **学び・共有**: ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先行公開情報をいち早くチェックできます。
    - **特別割引**: 最新の製品に対する限定割引をお楽しみいただけます。
    - **祝祭プロモーションやプレゼント**: プレゼントキャンペーンや季節のプロモーションに参加しましょう。

    👉 私たちと一緒に探求し、創造してみませんか？[|link_sf_facebook|]をクリックして、今すぐ参加してください！

.. _py_pir:


2.10 人間の動きを検出する
============================

このレッスンでは、Raspberry Pi Pico 2を使って **パッシブ赤外線（PIR）センサー** を利用し、人間の動きを検出する方法を学びます。PIRセンサーは、セキュリティシステムや自動照明、動き検出が必要な他のアプリケーションで広く使用されています。これらのセンサーは、温かい物体（人間や動物など）から放出される赤外線を検出します。


**必要なもの**

このプロジェクトには、以下の部品が必要です。

全ての部品を揃えたキットを購入するのが便利です。こちらのリンクからご覧ください：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - このキットの部品
        - リンク
    *   - Newton Lab Kit	
        - 450以上
        - |link_newton_lab_kit|

部品は以下のリンクから個別に購入することもできます。


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - 番号
        - 部品	
        - 数量
        - リンク

    *   - 1
        - :ref:`cpn_pico_2`
        - 1
        - |link_pico2_buy|
    *   - 2
        - Micro USBケーブル
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - 複数
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_pir`
        - 1
        - |link_pir_buy|


**回路図**

|sch_pir|

PIRモジュールが人の通過を検出すると、GP14がHIGHになります。それ以外の場合はLOWのままです。

.. note::

    PIRセンサーには2つのポテンショメーターがあります：

    * **感度調整**: 検出範囲を調整します。
    * **タイムディレイ調整**: 動きが検出された後、出力がHIGHのままでいる時間を調整します。

    初期テスト時には、両方のポテンショメーターを反時計回りに最小位置に設定してください。これにより、センサーは最も敏感で短い遅延設定となり、即座に反応を確認できます。

    |img_PIR_TTE|

**配線図**

|wiring_pir|


**コードの作成**

動きを検出するために、割り込みを使ってメッセージを表示するMicroPythonプログラムを作成します。

.. note::

    * ``2.10_detect_human_movement.py`` を ``newton-lab-kit/micropython`` から開くか、以下のコードをThonnyにコピーして、「実行」ボタンをクリックするか、F5キーを押して実行してください。

    * 正しいインタプリタ（MicroPython (Raspberry Pi Pico).COMxx）が選択されていることを確認してください。


.. code-block:: python

    import machine
    import utime

    # GP14を入力ピンとして初期化
    pir_sensor = machine.Pin(14, machine.Pin.IN)

    def motion_detected(pin):
        print("Motion detected!")

    # 上昇エッジで割り込みを設定
    pir_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=motion_detected)

    # メインループでは何もしません、割り込みが動きを検出します
    while True:
        utime.sleep(1)

コードが実行されると、以下の現象が観察されます：

* PIRセンサーの前で動きます。
* 動きが検出されると、コンソールに「動きが検出されました！」と表示されます。

**コードの理解**

#. モジュールのインポート：

   * ``import machine``: ハードウェア関連の関数を利用します。
   * ``import utime``: 時間関連の関数を使用します。

#. PIRセンサーのピンを初期化：

   * ``pir_sensor = machine.Pin(14, machine.Pin.IN)``: GP14を入力ピンとして設定します。

#. 割り込みハンドラを定義：

   * ``def motion_detected(pin)``: 動きが検出されたときに呼び出される関数です。
   * ``print("Motion detected!")``: メッセージをコンソールに表示します。

#. 割り込みを設定：

   * ``pir_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=motion_detected)``: PIRセンサーの上昇エッジで割り込みをトリガーするように設定します。

#. メインループ：

   * ``while True``: 無限ループを開始します。
   * ``utime.sleep(1)``: 1秒間スリープします。メインループでは何もしません。割り込みが動きの検出を処理します。

**動作時間を測定するためのコード例**

コードを修正して、動きの検出時間と検出間隔を測定することができます。

.. code-block:: python

    import machine
    import utime

    pir_sensor = machine.Pin(14, machine.Pin.IN)

    last_trigger_time = utime.ticks_ms()

    def pir_triggered(pin):
        global last_trigger_time
        current_time = utime.ticks_ms()
        duration = utime.ticks_diff(current_time, last_trigger_time)
        last_trigger_time = current_time

        if pir_sensor.value():
            print("Motion detected! Duration since last detection: {} ms".format(duration))
        else:
            print("Motion ended. Duration of motion: {} ms".format(duration))

    # 上昇エッジと下降エッジ両方に対して割り込みを設定
    pir_sensor.irq(trigger=machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING, handler=pir_triggered)

    while True:
        utime.sleep(1)

* 両方のエッジに対する割り込み： ``machine.Pin.IRQ_RISING`` | ``machine.Pin.IRQ_FALLING`` を使用して、上昇エッジと下降エッジの両方で割り込みを設定します。
* 時間の追跡：

  * ``utime.ticks_ms()`` を使用して、現在の時間をミリ秒単位で取得します。
  * トリガー間の時間を計算して、PIRセンサーの出力が ``HIGH`` または ``LOW`` の間、どれくらい続いたかを測定します。

**実用的なアプリケーション**

* **セキュリティシステム**: 不審者や不正な動きを検出します。
* **自動照明**: 動きが検出されたときにライトを点灯させます。
* **省エネルギー**: 一定期間動きが検出されない場合、デバイスの電源を切ります。

**トラブルシューティングのヒント**

* 偽のトリガー：

  * PIRセンサーは温度変化や日光などの環境要因に敏感です。
  * センサーを熱源や窓に向けて設置しないようにしましょう。

* センサーが動きを検出しない：

  * センサーが初期化されるまでに時間がかかることがあります（最大60秒）。
  * 感度ポテンショメーターを調整してください。

* 干渉：

  * センサーを電磁干渉を引き起こす可能性のある電子機器から遠ざけてください。

**結論**

Raspberry Pi Pico 2にPIRセンサーを統合することで、あなたのプロジェクトに動き検出機能を追加しました。センサー入力を読み取り、割り込みを処理する方法を理解することで、反応が速く効率的なプログラムを作成することができます。
