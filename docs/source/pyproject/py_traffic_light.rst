.. note:: 

    こんにちは、SunFounder Raspberry Pi & Python & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Python、ESP32について、仲間と一緒により深く学びましょう。

    **なぜ参加するのか？**

    - **専門家によるサポート**：購入後の問題や技術的な課題に対して、コミュニティやチームのサポートを受けられます。
    - **学びと共有**：スキル向上のためのヒントやチュートリアルを交換しましょう。
    - **限定プレビュー**：新製品の発表や先行情報をいち早く手に入れることができます。
    - **特別割引**：最新製品に対する独占的な割引をお楽しみいただけます。
    - **お祭りプロモーションやプレゼント**：プレゼントや季節限定プロモーションに参加できます。

    👉 一緒に探索し、創造していきませんか？ [|link_sf_facebook|] をクリックして今すぐ参加しましょう！

.. _py_traffic_light:

7.6 信号機コントローラの作成
==============================================================

このプロジェクトでは、Raspberry Pi Pico 2、3つのLED（赤、黄、緑）、および4桁の7セグメントディスプレイを使用して **信号機コントローラ** を作成します。このシステムは、実際の信号機の動作をシミュレートし、各信号の残り時間を7セグメントディスプレイに表示します。

**必要なもの**

このプロジェクトには以下のコンポーネントが必要です。

セットで購入するのが便利です。こちらからご確認ください：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - キット内アイテム
        - リンク
    *   - Newton Lab Kit	
        - 450+
        - |link_newton_lab_kit|

また、個別に購入する場合は以下のリンクをご参照ください。

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
        - :ref:`cpn_resistor`
        - 7（220Ω）
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_4_dit_7_segment`
        - 1
        - 
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|
    *   - 8
        - :ref:`cpn_led`
        - 3
        - |link_led_buy|

**コンポーネントの理解**

* **LED**：信号機を表します。これらを制御して、標準的な信号機の動作をシミュレートします。
* **4桁の7セグメントディスプレイ**：各信号のカウントダウンタイマーを表示します。
* **74HC595シフトレジスタ**：ピン数を節約しながら、複数の出力（ディスプレイのセグメントや桁）を制御できます。


**回路図**

|sch_traffic_light|


* この回路は、 :ref:`py_74hc_4dig` をベースに、3つのLEDを追加したものです。
* 3つの赤、黄、緑のLEDはそれぞれGP7～GP9に接続されています。

**配線図**

|wiring_traffic_light| 

**コードを書く**

このプロジェクトでは、次のことを行うMicroPythonスクリプトを書きます：

* 信号機の動作を制御する。
* 7セグメントディスプレイにカウントダウンタイマーを表示する。
* シフトレジスタを使ってディスプレイを制御する。

.. note::

    * ``7.6_traffic_light.py`` を ``newton-lab-kit/micropython`` から開くか、コードをThonnyにコピーして「実行」ボタンを押すか、F5キーを押して実行してください。
    * 正しいインタープリター（MicroPython（Raspberry Pi Pico））が選択されていることを確認してください。COMxx。

.. code-block:: python

    import machine
    import utime
    from machine import Timer

    # LEDのピンを初期化
    led_pins = [7, 8, 9]  # 緑、黄、赤のLEDをGP7、GP8、GP9に接続
    leds = [machine.Pin(pin, machine.Pin.OUT) for pin in led_pins]

    # 各信号の色の持続時間（秒）を定義 [緑、黄、赤]
    light_time = [30, 5, 30]  # [緑、黄、赤]

    # 各桁の2進数コード（0～9）
    SEGMENT_CODES = [
        0x3F,  # 0
        0x06,  # 1
        0x5B,  # 2
        0x4F,  # 3
        0x66,  # 4
        0x6D,  # 5
        0x7D,  # 6
        0x07,  # 7
        0x7F,  # 8
        0x6F   # 9
    ]

    # 74HC595の制御ピンを初期化
    SDI = machine.Pin(18, machine.Pin.OUT)   # シリアルデータ入力（DS）
    RCLK = machine.Pin(19, machine.Pin.OUT)  # レジスタクロック（STCP）
    SRCLK = machine.Pin(20, machine.Pin.OUT) # シフトレジスタクロック（SHCP）

    # 桁選択ピン（共通カソード）
    digit_pins = [
        machine.Pin(10, machine.Pin.OUT),  # 桁1
        machine.Pin(11, machine.Pin.OUT),  # 桁2
        machine.Pin(12, machine.Pin.OUT),  # 桁3
        machine.Pin(13, machine.Pin.OUT)   # 桁4
    ]

    # 74HC595にデータを送信する関数
    def shift_out(data):
        RCLK.low()
        for bit in range(7, -1, -1):
            SRCLK.low()
            bit_val = (data >> bit) & 0x01
            SDI.value(bit_val)
            SRCLK.high()
        RCLK.high()

    # 特定の位置に桁を表示する関数
    def display_digit(position, digit):
        # すべての桁を消灯
        for dp in digit_pins:
            dp.high()
        # セグメントデータを送信
        shift_out(SEGMENT_CODES[digit])
        # 選択された桁をアクティブ化（共通カソードはアクティブロー）
        digit_pins[position].low()
        # 桁が見えるように小さな遅延を追加
        utime.sleep_ms(5)
        # 桁を消灯
        digit_pins[position].high()

    # 4桁ディスプレイに数字を表示する関数
    def display_number(number):
        # 数字を桁ごとに分解
        digits = [
            (number // 1000) % 10,
            (number // 100) % 10,
            (number // 10) % 10,
            number % 10
        ]
        # 各桁を素早く表示
        for i in range(4):
            display_digit(i, digits[i])

    # 現在の状態に基づいてLEDを更新する関数
    def update_leds(state):
        # 状態: 0 = 緑、1 = 黄、2 = 赤
        for i in range(3):
            leds[i].value(0)
        leds[state].value(1)

    # タイマー変数
    counter = light_time[0]  # 緑の信号の時間から開始
    current_state = 0  # 0 = 緑、1 = 黄、2 = 赤

    # タイマー割り込みコールバック関数（信号機の状態とカウントを更新）
    def timer_callback(t):
        global counter, current_state
        counter -= 1
        if counter <= 0:
            current_state = (current_state + 1) % 3  # 状態を循環
            counter = light_time[current_state]  # 新しい状態に対するカウンタをリセット
            update_leds(current_state)

    # タイマーを初期化
    timer = Timer(period=1000, mode=Timer.PERIODIC, callback=timer_callback)

    # 初期LED状態
    update_leds(current_state)

    # メインループ
    try:
        while True:
            display_number(counter)
    except KeyboardInterrupt:
        timer.deinit()
        print("Program stopped.")

コードが実行されると、最初に緑のLEDが点灯し、ディスプレイに30からのカウントダウンが表示されます。
30秒後、黄色のLEDが点灯し、ディスプレイに5からのカウントダウンが表示されます。
その後、赤のLEDが点灯し、ディスプレイに30からのカウントダウンが表示されます。
このサイクルは無限に繰り返されます。


**コードの理解**

#. インポートと初期化:

   * ``machine``: ハードウェア関連の機能にアクセスするためのモジュール。
   * ``utime``: 時間に関連する関数を提供するモジュール。
   * ``Timer``: ハードウェアタイマーを作成するために使用される。

#. LEDの初期化:

   赤、黄、緑のLEDのGPIOピンを定義し、それぞれを出力として初期化します。

   .. code-block:: python

        led_pins = [7, 8, 9]  # 緑、黄、赤のLEDはそれぞれGP7、GP8、GP9に接続
        leds = [machine.Pin(pin, machine.Pin.OUT) for pin in led_pins]

#. 信号機のタイミング:

   各信号機状態の継続時間（秒単位）を指定します。

   .. code-block:: python

        light_time = [30, 5, 30]  # [緑、黄、赤]

#. ディスプレイ関数:

   * ``display_digit(digit)``: 特定の桁をディスプレイに表示。
   * ``shift_out(data)``: シフトレジスタにデータを送信。
   * ``display_number(num)``: 数字を桁ごとに分解し、マルチプレクシングを使用して表示。

#. ``update_leds(state)`` 関数:

   * 現在の信号機状態に基づいてLEDの状態を更新。
   * すべてのLEDを消灯した後、現在の状態に対応するLEDを点灯。

   .. code-block:: python

        def update_leds(state):
            # 状態: 0 = 緑、1 = 黄、2 = 赤
            for i in range(3):
                leds[i].value(0)
            leds[state].value(1)

#. ``timer_callback(t)`` 関数:

   * タイマー割り込みコールバック関数。
   * カウンタを毎秒減算。
   * カウンタがゼロになると、次の信号機状態にサイクルし、カウンタをリセット。

   .. code-block:: python

        def timer_callback(t):
            global counter, current_state
            counter -= 1
            if counter <= 0:
                current_state = (current_state + 1) % 3  # 状態を循環
                counter = light_time[current_state]  # 新しい状態のためにカウンタをリセット
                update_leds(current_state)

#. メインの実行:

   * 初期変数: 初期状態を緑に設定し、カウンタを初期化。

     .. code-block:: python

        counter = light_time[0]  # 緑の信号機の継続時間で開始
        current_state = 0  # 0 = 緑、1 = 黄、2 = 赤
     
   * タイマーの初期化: 1000ミリ秒（1秒）ごとにタイマーコールバックを呼び出す周期的タイマーを作成。


     .. code-block:: python

        timer = Timer(period=1000, mode=Timer.PERIODIC, callback=timer_callback)

   * 初期LED状態の設定: 最初に正しいLEDが点灯していることを確認。

     .. code-block:: python

        update_leds(current_state)

   * メインループ: 無限ループでカウントダウンタイマーを表示。キーボード割り込み（例：Ctrl+C）でタイマーを安全に停止し、終了。


     .. code-block:: python

        try:
            while True:
                display_number(counter)
        except KeyboardInterrupt:
            timer.deinit()
            print("Program stopped.")


**さらに実験**


* タイミングの調整:

  ``light_time`` リストを変更して、各信号機の継続時間を調整します。

* 歩行者信号の追加:

  ボタンや追加のLEDを実装して、歩行者信号をシミュレートします。

* ディスプレイの改善:

  時間がほぼ終了した際にLEDを点滅させるなどの機能を追加します。

* 実際の信号機のシミュレーション:

  左折信号や交差点の複数信号など、より複雑なシーケンスを追加します。

**結論**

あなたはRaspberry Pi Pico 2を使用して信号機制御システムを正常に構築しました！このプロジェクトは、マイクロコントローラーを使ってLEDやディスプレイなどのハードウェアを制御し、タイマーと割り込みを使ってリアルタイムのアプリケーションを作成する方法を示しています。

このプロジェクトを拡張し、新しい機能を追加したり、より大きなシステムに統合したりしてみてください。
