.. note::

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32について、仲間と一緒に深掘りして学びましょう。

    **なぜ参加するべきか？**

    - **専門家のサポート**: 購入後の問題や技術的な課題を、コミュニティやチームのサポートで解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換して、スキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先行公開にいち早くアクセスできます。
    - **特別割引**: 最新製品に対する独占的な割引を楽しめます。
    - **祝祭プロモーションやプレゼント**: プレゼント企画やホリデープロモーションに参加できます。

    👉 一緒に探求し、創造を楽しみたいですか？[|link_sf_facebook|] をクリックして、今すぐ参加しましょう！

.. _py_servo:

3.7 サーボモーターの動作
===========================

このレッスンでは、Raspberry Pi Pico 2を使って **サーボモーター** を制御する方法を学びます。サーボモーターは、0°から180°の間で特定の角度に回転することができるデバイスです。リモートコントロール玩具やロボット、精密な位置制御が必要なその他の用途に広く使用されています。

それでは、サーボを前後に揺らしてみましょう！

**必要なもの**

このプロジェクトでは、以下の部品が必要です。

セットで購入するのが便利です。こちらがリンクです：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - セット内容
        - リンク
    *   - Newton Lab Kit
        - 450+
        - |link_newton_lab_kit|

また、下記のリンクから個別に購入することもできます。

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
        - 数本
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_servo`
        - 1
        - |link_servo_buy|


**回路図**

|sch_servo|

**配線図**

|wiring_servo|

* オレンジの線は信号線で、GP15に接続します。
* 赤の線はVCCで、VBUS(5V)に接続します。
* 茶色の線はGNDで、GNDに接続します。

サーボは負荷がかかるとかなりの電流を消費することがあります。今回使用するのは小型のサーボで負荷も軽いため、PicoのVBUSピンから給電することで、この簡単な実験は問題なく動作します。大きなサーボや複数のサーボを使う場合は、外部電源の使用を検討してください。

**サーボアームの取り付け**

* サーボアーム（またはホーン）をサーボの出力シャフトに取り付けます。
* 必要に応じて、サーボに付属している小さなネジで固定します。

**コードの作成**

サーボが0°から180°まで前後に動くように、MicroPythonのプログラムを書きます。

.. note::

    * ``3.7_swinging_servo.py`` を ``newton-lab-kit/micropython`` フォルダから開くか、コードをThonnyにコピーして「実行」をクリックするか、F5を押して実行します。
    * 正しいインタープリタ（MicroPython（Raspberry Pi Pico）.COMxx）が選択されていることを確認してください。

.. code-block:: python

    import machine
    import utime

    # GP15ピンでPWMを初期化
    servo = machine.PWM(machine.Pin(15))
    servo.freq(50)  # 周波数を50Hzに設定

    # 角度をデューティサイクルに変換する関数
    def angle_to_duty(angle):
        min_duty = 1638  # 0.5msのパルス（0°）
        max_duty = 8192  # 2.5msのパルス（180°）
        duty = int(min_duty + (angle / 180) * (max_duty - min_duty))
        return duty

    while True:
        # サーボを0°から180°に動かす
        for angle in range(0, 181, 1):
            servo.duty_u16(angle_to_duty(angle))
            utime.sleep_ms(20)
        # サーボを180°から0°に戻す
        for angle in range(180, -1, -1):
            servo.duty_u16(angle_to_duty(angle))
            utime.sleep_ms(20)

コードが実行されると、サーボはスムーズに0°から180°の間を前後に動きます。


**コードの理解**

#. モジュールのインポート：

   * ``machine``: ハードウェア関連の機能にアクセスします。
   * ``utime``: 遅延など、時間関連の機能を提供します。

#. PWMの初期化：

   GP15ピンでPWMを設定します。サーボの標準周波数である50Hzに設定します。

   .. code-block:: python

      servo = machine.PWM(machine.Pin(15))
      servo.freq(50)

#. ``angle_to_duty`` 関数の定義：

   * この関数は、角度（0°〜180°）をサーボのデューティサイクルに対応する値に変換します。
   * ``min_duty`` と ``max_duty`` は、サーボ制御信号の最小と最大のパルス幅に対応します。
   * 計算によって、角度を適切なデューティサイクルにスケーリングします。

   .. code-block:: python

      def angle_to_duty(angle):
          min_duty = 1638  # 0.5msパルス幅
          max_duty = 8192  # 2.5msパルス幅
          duty = int(min_duty + (angle / 180) * (max_duty - min_duty))
          return duty

#. メインループでサーボを動かす：

   * サーボは0°から180°まで、1°ずつ角度を増加させます。
   * その後、180°から0°に戻ります。
   * ``utime.sleep_ms(20)`` は、動作をスムーズにするための小さな遅延を追加します。

   .. code-block:: python

      while True:
          for angle in range(0, 181, 1):
              servo.duty_u16(angle_to_duty(angle))
              utime.sleep_ms(20)
          for angle in range(180, -1, -1):
              servo.duty_u16(angle_to_duty(angle))
              utime.sleep_ms(20)

**コードのさらなる理解**

サーボは、特定のパルス幅を持つPWM信号を送ることによって制御されます。
サーボの標準は50HzのPWM信号（周期20ms）です。
各周期内のパルス幅がサーボの角度を決定します：

* 0.5msのパルス幅は0°に対応。
* 1.5msのパルス幅は90°に対応。
* 2.5msのパルス幅は180°に対応。

PWM信号のデューティサイクルを調整することによって、パルス幅を変更します。

``duty_u16()`` 関数は0から65535までの値を受け付けます。
パルス幅に対応するデューティサイクルを計算するためには：

.. code-block::

  Duty cycle = (Pulse Width / Period) * 65535

例えば、0.5msのパルス幅の場合：

.. code-block::

  Duty cycle = (0.5ms / 20ms) * 65535 ≈ 1638

**さらなる実験**

* **速度の変更**: ``utime.sleep_ms(20)`` の遅延を調整して、サーボの動作速度を速くしたり遅くしたりできます。
* **特定の角度に設定**: コードを変更して、サーボを特定の角度に動かすことができます。

  .. code-block:: python

    servo.duty_u16(angle_to_duty(90))  # 90°に移動

* **入力による制御**: ポテンショメーターやボタンを接続して、サーボの角度をインタラクティブに制御できます。

**重要な注意点**

* **電源供給**: サーボに十分な電力が供給されていることを確認してください。ジッターや不安定な動作が見られる場合は、外部の5V電源を使用してください。
* **過負荷を避ける**: サーボを物理的な限界（通常0°〜180°）を超えて強制的に動かさないようにしてください。サーボが損傷する原因となります。

**結論**

このレッスンでは、Raspberry Pi Pico 2を使ってサーボモーターを制御する方法を学びました。PWM信号を使ってサーボの角度を設定し、スムーズに動かす方法を理解しました。このスキルは、精密な動きが必要なロボティクスやオートメーションプロジェクトにおいて非常に重要です。
