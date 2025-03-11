SunFounder Raspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ
--------------------------------------------------------------------------------

こんにちは！FacebookでSunFounderのRaspberry Pi & Arduino & ESP32愛好者コミュニティに参加していただきありがとうございます！同じ興味を持つ仲間と一緒に、Raspberry Pi、Arduino、ESP32の更なる深掘りを楽しみましょう。

**参加する理由は？**

- **専門家によるサポート**：コミュニティやチームの支援を受けて、販売後の問題や技術的な課題を解決。
- **学びと共有**：スキルを高めるためのヒントやチュートリアルを交換。
- **独占プレビュー**：新製品発表や製品の先行試用のチャンス。
- **特別割引**：最新製品に対する独占的な割引を享受。
- **祝祭プロモーションとギフト**：ギフトや祝祭のプロモーションに参加。

👉 私たちと一緒に探求し、創造してみませんか？[|link_sf_facebook|]をクリックして今すぐ参加！

.. _py_74hc_4dig:

5.3 4桁7セグメント表示器を使ったタイムカウンターの作成
============================================================

このレッスンでは、 **4桁7セグメント表示器** をRaspberry Pi Pico 2と組み合わせて、シンプルなタイムカウンターを作成する方法を学びます。表示器は毎秒カウントアップし、経過時間を秒単位で表示します。

**必要なもの**

このプロジェクトには以下のコンポーネントが必要です。

キット全体を購入するのが便利です。こちらがリンクです：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - このキットのアイテム
        - リンク
    *   - Newton Lab Kit	
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
        - 4(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_4_dit_7_segment`
        - 1
        - 
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|


**4桁7セグメント表示器の理解**

4桁7セグメント表示器は、単一モジュールに組み合わされた4つの個別の7セグメント表示器で構成されています。各桁は同じセグメント制御線（ **a** から **g** および **dp** ）を共有していますが、各桁には独自の **コモンカソード** 制御があります。この設定により、任意の時点でアクティブな桁を制御できます。

共有セグメント線を使用して各桁に異なる数字を表示するには、 **多重化** と呼ばれる技術を使用します。我々は桁を素早く切り替え、一度に一つの桁を更新しますが、視覚の持続性により、すべての桁が同時に表示されているように見えます。

|4digit_control_pins|

**回路図**

|sch_4dig|

ここでは配線原理は基本的に :ref:`py_74hc_led` と同じで、唯一の違いはQ0-Q7が4桁7セグメント表示器のa〜gピンに接続されていることです。

次にG10〜G13がどの7セグメント表示器を作動させるかを選択します。

**配線図**

|wiring_4dig|

* **セグメント接続（220Ω抵抗を介して）:**

  * **Q0** → セグメント **a**
  * **Q1** → セグメント **b**
  * **Q2** → セグメント **c**
  * **Q3** → セグメント **d**
  * **Q4** → セグメント **e**
  * **Q5** → セグメント **f**
  * **Q6** → セグメント **g**
  * **Q7** → セグメント **dp**（小数点）

* **コモンカソード接続（桁選択ピン）:**

  * **桁1（最も左の桁）:** Picoの **GP10** に接続
  * **桁2:** **GP11**に接続
  * **桁3:** **GP12**に接続
  * **桁4（最も右の桁）:** **GP13** に接続


**コードの記述**

MicroPythonプログラムを記述して、秒ごとにインクリメントし、4桁7セグメント表示器にカウントを表示するタイムカウンターを作成しましょう。

.. note::

    * ``5.3_time_counter.py`` を ``newton-lab-kit/micropython`` から開くか、コードをThonnyにコピーして「実行」をクリックするか、F5を押します。
    * 正しいインタープリタが選択されていることを確認してください：MicroPython (Raspberry Pi Pico).COMxx. 
    

.. code-block:: python

    import machine
    import utime

    # 各桁の数字（0-9）に対するバイナリコードの定義
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

    # 74HC595の制御ピンの初期化
    SDI = machine.Pin(18, machine.Pin.OUT)   # シリアルデータ入力（DS）
    RCLK = machine.Pin(19, machine.Pin.OUT)  # レジスタクロック（STCP）
    SRCLK = machine.Pin(20, machine.Pin.OUT) # シフトレジスタクロック（SHCP）

    # 桁選択ピン（コモンカソード）の初期化
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
        # すべての桁をオフにする
        for dp in digit_pins:
            dp.high()
        # セグメントデータを送信
        shift_out(SEGMENT_CODES[digit])
        # 選択した桁をアクティブにする（コモンカソードはアクティブロー）
        digit_pins[position].low()
        # 桁が見えるように少し遅延
        utime.sleep_ms(5)
        # 桁をオフにする
        digit_pins[position].high()

    # 4桁表示器に数値を表示する関数
    def display_number(number):
        # 個々の桁を抽出
        digits = [
            (number // 1000) % 10,
            (number // 100) % 10,
            (number // 10) % 10,
            number % 10
        ]
        # 各桁を迅速に表示
        for i in range(4):
            display_digit(i, digits[i])

    # メインループ
    counter = 0
    last_update = utime.ticks_ms()

    while True:
        # 1000 ms（1秒）ごとにカウンターを更新
        current_time = utime.ticks_ms()
        if utime.ticks_diff(current_time, last_update) >= 1000:
            counter += 1
            if counter > 9999:
                counter = 0
            last_update = current_time

        # 表示を継続的にリフレッシュ
        display_number(counter)

このコードを実行すると、4桁7セグメント表示器はカウンターとして機能し、表示される数値が1秒ごとに1増え、0から9999までカウントアップした後、0にリセットして繰り返し表示されます。

**コードの理解**

#. モジュールのインポート:

   * ``machine``: GPIOピンとハードウェア機能へのアクセスを提供します。
   * ``utime``: 遅延やタイミングのための時間関連の機能を含んでいます。

#. セグメントコードの定義:

   各エントリは、数字を表示するために点灯する必要があるセグメントに対応します。値は16進数形式です。

   .. code-block:: python

        # 各桁の数字（0-9）に対するバイナリコードの定義
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

#. 制御ピンの初期化:
   
   PicoのGPIOピンに74HC595の制御を割り当てます。

   .. code-block:: python

        SDI = machine.Pin(18, machine.Pin.OUT)
        RCLK = machine.Pin(19, machine.Pin.OUT)
        SRCLK = machine.Pin(20, machine.Pin.OUT)


#. 桁選択ピンの初期化:

   アクティブな桁を制御します。アクティブロー（コモンカソード）。

   .. code-block:: python

        digit_pins = [
            machine.Pin(10, machine.Pin.OUT),
            machine.Pin(11, machine.Pin.OUT),
            machine.Pin(12, machine.Pin.OUT),
            machine.Pin(13, machine.Pin.OUT)
        ]

#. ``shift_out`` 関数の定義:

   * 74HC595に8ビットのデータを送信します。
   * 最上位ビット（MSB）からデータをシフトアウトします。
   * シフトクロックとレジスタクロックを適切にパルスします。

   .. code-block:: python

        def shift_out(data):
            RCLK.low()
            for bit in range(7, -1, -1):
                SRCLK.low()
                bit_val = (data >> bit) & 0x01
                SDI.value(bit_val)
                SRCLK.high()
            RCLK.high()

#. ``display_digit`` 関数の定義:

   * すべての桁をオフにします。
   * 桁のセグメントコードを送信します。
   * 指定した桁のピンをローに設定してアクティブにします。
   * 桁を表示するために小さな遅延を追加します。
   * 表示後に桁をオフにします。

   .. code-block:: python

        def display_digit(position, digit):
            for dp in digit_pins:
                dp.high()
            shift_out(SEGMENT_CODES[digit])
            digit_pins[position].low()
            utime.sleep_ms(5)
            digit_pins[position].high()


#. ``display_number`` 関数の定義:

   * 数値から各桁を抽出します。
   * 各桁を迅速に表示するために、 ``display_digit`` を呼び出します。

   .. code-block:: python

        def display_number(number):
            # 個々の桁を抽出
            digits = [
                (number // 1000) % 10,
                (number // 100) % 10,
                (number // 10) % 10,
                number % 10
            ]
            # 各桁を迅速に表示
            for i in range(4):
                display_digit(i, digits[i])

#. メインループ:

   * 毎秒カウンターをインクリメントします。
   * 9999に達した後、カウンターをリセットします。
   * 表示をリフレッシュするために、 ``display_number`` を継続的に呼び出します。

   .. code-block:: python

        counter = 0
        last_update = utime.ticks_ms()

        while True:
            current_time = utime.ticks_ms()
            if utime.ticks_diff(current_time, last_update) >= 1000:
                counter += 1
                if counter > 9999:
                    counter = 0
                last_update = current_time

            display_number(counter)


**さらに実験する**



* リセットボタンを追加:

  Picoにボタンを接続して、押されたときにカウンターをリセットします。

* 異なるデータを表示:

  コードを変更して、温度や光のレベルなどのセンサー読み取り値を表示します。

* 表示の明るさを調整:

  ``display_digit`` 関数の ``utime.sleep_ms(5)`` 遅延を変更して、各桁が表示される時間を調整し、明るさに影響します。

* ストップウォッチを作成:

  スタート、ストップ、リセット機能を実装して、表示器をストップウォッチとして使用します。

**まとめ**

このレッスンでは、74HC595シフトレジスタを使用してRaspberry Pi Pico 2で4桁7セグメント表示器を使用する方法を学びました。多重化と効率的なタイミングを理解することで、最小限のGPIOピンを使用して複数桁の表示器に動的情報を表示できます。
