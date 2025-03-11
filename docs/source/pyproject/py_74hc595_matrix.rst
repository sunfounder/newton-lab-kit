.. note:: 

    こんにちは！SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Facebookコミュニティで、Raspberry Pi、Arduino、ESP32について深く学び、愛好者と交流しましょう。

    **なぜ参加するべきか？**

    - **専門的なサポート**: 購入後の問題や技術的な課題を、コミュニティやサポートチームと一緒に解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換し、スキルを向上させましょう。
    - **最新情報の先行公開**: 新製品の発表やプレビューにいち早くアクセスできます。
    - **特別割引**: 最新製品を特別価格で購入できます。
    - **イベントやプレゼント企画**: さまざまなキャンペーンやプレゼント企画に参加できます。

    👉 さあ、一緒に学び、創造しましょう！[|link_sf_facebook|] をクリックして、今すぐ参加！

.. _py_74hc_788bs:

5.4 8x8 LEDマトリックスでのグラフィック表示
===================================================================

このレッスンでは、 **Raspberry Pi Pico 2** と **74HC595シフトレジスタ2個** を使用して **8x8 LEDマトリックス** を制御する方法を学びます。各LEDを個別にコントロールすることで、パターンや簡単なグラフィックを表示できるようになります。

**必要なもの**

このプロジェクトでは、以下のコンポーネントが必要です。

すべてを一括で揃えるのに便利なキットはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名称
        - キット内容
        - リンク
    *   - Newton Lab Kit
        - 450点以上
        - |link_newton_lab_kit|


個別に購入する場合は、以下のリンクを利用してください。

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
        - :ref:`cpn_dot_matrix`
        - 1
        - 
    *   - 6
        - :ref:`cpn_74hc595`
        - 2
        - |link_74hc595_buy|

**8x8 LEDマトリックスの概要**

8x8 LEDマトリックスは、8行×8列に並んだ合計64個のLEDで構成されています。行と列に電圧を加えることで各LEDを個別に制御し、文字やパターンを表示できます。

このプロジェクトでは、 **74HC595シフトレジスタ2個** を使用してLEDマトリックスの行と列を制御し、少ないGPIOピンで多くの出力を管理します。

**回路図**

|sch_ledmatrix|

8x8 LEDドットマトリックスは、 **2つの74HC595シフトレジスタ** によって制御されます。1つは行を、もう1つは列を制御します。これらのICは **GP18、GP19、GP20** の3つのGPIOピンを共有し、PicoのI/Oポートを節約します。

Raspberry Pi Picoは一度に16ビットのバイナリデータを出力し、最初の8ビットが行、次の8ビットが列を制御する仕組みになっています。

**Q7' (ピン9)**: 1つ目の74HC595のシリアルデータ出力ピンが、2つ目の74HC595の **DS (ピン14)** に接続されることで、シフトレジスタを連結できます。

**配線手順**

配線は少し複雑ですが、手順を追って進めましょう。

**Step 1:**  まず、Pico、LEDドットマトリックス、および2つの74HC595チップをブレッド
ボードに挿入します。Picoの 3.3V と GND をブレッドボードの両サイドの穴に接続
し、その後、2つの74HC595の ピン16 と ピン10 を VCC に、 ピン13 と ピン8 を GND に接続します。

.. note::
   上記のFritzing画像では、ラベルのある側が下側になります。

|wiring_ledmatrix_4|

**ステップ2:**  
2つの74HC595の ピン11 を接続し、それをGP20に接続。続いて、ピン12をGP19に、
左側の74HC595の ピン14 をGP18に、ピン9を2つ目の74HC595のピン14に接続します。

|wiring_ledmatrix_3|

**Step 3:**  右側の74HC595は、LEDドットマトリックスの列を制御します。
対応関係は下表のとおりです。そのため、74HC595の*Q0-Q7 ピンは、
それぞれ ピン13、3、4、10、6、11、15、16 に対応しています。

+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **74HC595**        | **Q0** | **Q1** | **Q2** | **Q3** | **Q4** | **Q5** | **Q6** | **Q7** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **LED Dot Matrix** | **13** | **3**  | **4**  | **10** | **6**  | **11** | **15** | **16** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+

|wiring_ledmatrix_2|

**Step 4:**  次に、LEDドットマトリックスの ROW（行）を接続します。
左側の74HC595がLEDドットマトリックスの行を制御します。対応関係は下
表のとおりです。左側の74HC595のQ0-Q7ピンは、それぞれピン9、14、8、12、1、7、2、5に対応しています。

+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **74HC595**        | **Q0** | **Q1** | **Q2** | **Q3** | **Q4** | **Q5** | **Q6** | **Q7** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **LED Dot Matrix** | **9**  | **14** | **8**  | **12** | **1**  | **7**  | **2**  | **5**  |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+

|wiring_ledmatrix_1|


**コードの記述**

次に、MicroPythonでLEDマトリックスにパターンを表示するプログラムを作成します。

.. note::

    * ``5.4_8x8_pixel_graphics.py`` を ``newton-lab-kit/micropython`` から開くか、Thonnyにコードをコピーして「Run」をクリックするか、F5キーを押してください。
    * インタプリタが MicroPython (Raspberry Pi Pico) COMxx に設定されていることを確認してください。

.. code-block:: python 

    import machine
    import time

    # 74HC595シフトレジスタに接続するピンの定義
    sdi = machine.Pin(18, machine.Pin.OUT)   # シリアルデータ入力
    rclk = machine.Pin(19, machine.Pin.OUT)  # ストレージレジスタクロック（RCLK）
    srclk = machine.Pin(20, machine.Pin.OUT) # シフトレジスタクロック（SRCLK）

    # LEDマトリックスに「X」を表示するためのパターンデータ
    glyph = [0x7E, 0xBD, 0xDB, 0xE7, 0xE7, 0xDB, 0xBD, 0x7E]

    def hc595_in(dat):
        """
        Shifts 8 bits of data into the 74HC595 shift register.
        """
        for bit in range(7, -1, -1):
            srclk.low()
            sdi.value((dat >> bit) & 1)  # ビット単位でデータを出力
            srclk.high()
            time.sleep_us(1)  # 短い遅延を入れてタイミングを調整

    def hc595_out():
        """
        Latches the data from the shift register to the storage register,
        updating the outputs.
        """
        rclk.high()
        rclk.low()

    while True:
        for i in range(8):
            hc595_in(glyph[i])       # 現在の行のカラムデータを送信
            hc595_in(1 << i)         # 該当の行をアクティブ化
            hc595_out()              # ディスプレイを更新
            time.sleep_ms(1)         # 視覚的な残像効果のための遅延


このコードを実行すると、8x8 LEDマトリックスに「X」の形が表示されます。LEDが点灯し、マトリックス上に「X」のパターンを形成します。

**コードの解説**

#. モジュールのインポート:

   * ``machine``: GPIOピン制御などのハードウェア関連機能を提供
   * ``time``: タイミング制御のための遅延処理に使用

#. ピンの定義:

   * ``sdi``: シフトレジスタにシリアルデータを送信
   * ``rclk``: シフトレジスタのデータを出力ピンにラッチ
   * ``srclk``: 送信されたデータをシフトレジスタに移動

#. 「X」パターンの定義:

   * 各要素がLEDマトリックスの1行に対応
   * 16進数値は、その行の点灯（0）・消灯（1）の状態を示す
   * これにより、対称的な「X」の形がマトリックス上に描画される

   .. code-block:: python
    
        glyph = [0x7E, 0xBD, 0xDB, 0xE7, 0xE7, 0xDB, 0xBD, 0x7E]

#. ``hc595_in(dat)`` 関数:

   * 8ビットのデータ（ ``dat`` ）をシフトレジスタに順次送信
   * 最上位ビット（MSB）から順に処理
   * ``srclk`` ピンをトグルして各ビットをレジスタにシフト
   * ``sdi`` ピンが現在のビットの値に応じてHIGHまたはLOWを設定

   .. code-block:: python
    
        def hc595_in(dat):
            """
            Shifts 8 bits of data into the 74HC595 shift register.
            """
            for bit in range(7, -1, -1):
                srclk.low()
                sdi.value((dat >> bit) & 1)  # ビットごとにデータを送信
                srclk.high()
                time.sleep_us(1)  # 適切なタイミング調整

#. ``hc595_out()`` 関数:

   * シフトレジスタのデータをストレージレジスタにラッチ
   * ``rclk`` ピンの立ち上がりエッジでデータを出力ピンに適用

   .. code-block:: python
    
        def hc595_out():

            rclk.high()
            rclk.low()

#. メインループ:

   * ループ内でディスプレイを高速に更新し、「X」パターンを維持
   * ``for`` ループで各行（0～7）を順番に処理
   * ``hc595_in(1 << i)`` により1行ずつアクティブ化
   * ``hc595_in(glyph[i])`` で各行のカラムデータを送信
   * ``hc595_out()`` でラッチし、マトリックスを更新
   * ``time.sleep_ms(1)`` により各行を短時間表示し、視覚的に全体を同時点灯させる

   .. code-block:: python
    
        while True:
            for i in range(8):
                hc595_in(glyph[i])       # 現在の行のデータを送信
                hc595_in(1 << i)         # 行をアクティブにする
                hc595_out()              # LEDマトリックスを更新
                time.sleep_ms(1)         # 視覚的残像のための遅延


**さらなる実験**

* パターンの変更

  以下のパターンデータに置き換えることで、異なるグラフィックを表示可能。 ``pattern_heart`` または ``pattern_smile`` をコード内で使用すると、異なる形状を描画できる。

  .. code-block:: python

        # ハート形
        pattern_heart = [
            0b11111111,
            0b10011001,
            0b00000000,
            0b00000000,
            0b00000000,
            0b10000001,
            0b11000011,
            0b11100111
        ]

        # スマイルフェイス
        pattern_smile = [
            0b11000011,  # 行0
            0b10111101,  # 行1
            0b01011010,  # 行2
            0b01111110,  # 行3
            0b01011010,  # 行4
            0b01100110,  # 行5
            0b10111101,  # 行6
            0b11000011   # 行7
        ]


* Animating the Display 

  複数のパターンを作成し、順番に切り替えてアニメーションを実現しましょう。

  .. code-block:: python

        import machine
        import time
        
        # 74HC595シフトレジスタに接続するピンを定義
        sdi = machine.Pin(18, machine.Pin.OUT)   # シリアルデータ入力
        rclk = machine.Pin(19, machine.Pin.OUT)  # レジスタクロック（ラッチ）
        srclk = machine.Pin(20, machine.Pin.OUT) # シフトレジスタクロック
        
        # ハートの形
        pattern_heart = [
            0b11111111,
            0b10011001,
            0b00000000,
            0b00000000,
            0b00000000,
            0b10000001,
            0b11000011,
            0b11100111
        ]
        
        # スマイルフェイス
        pattern_smile = [
            0b11000011,  # 行0
            0b10111101,  # 行1
            0b01011010,  # 行2
            0b01111110,  # 行3
            0b01011010,  # 行4
            0b01100110,  # 行5
            0b10111101,  # 行6
            0b11000011   # 行7
        ]
        
        def hc595_in(dat):
            """
            Shift 8 bits of data into the 74HC595 shift register.
            """
            for bit in range(7, -1, -1):
                srclk.low()                            # データのシフト準備
                sdi.value((dat >> bit) & 1)            # データビットをセット
                srclk.high()                           # データをシフトレジスタへ送信
                time.sleep_us(1)                       # 短い遅延でタイミング調整
        
        def hc595_out():
            """
            Latch the shifted data to the output pins of the 74HC595.
            """
            rclk.high()                               # データをラッチ（立ち上がりエッジ）
            rclk.low()                                # 次のデータ送信準備
        
        def display_pattern(pattern):
            """
            Display a given 8x8 pattern on the LED matrix.
            """
            for _ in range(500):                      # 一定時間パターンを表示
                for i in range(8):
                    hc595_in(pattern[i])              # 現在の行のカラムデータを送信
                    hc595_in(1 << i)                  # 該当の行をアクティブ化
                    hc595_out()                       # 出力を更新
                    time.sleep_ms(1)                  # 視覚的な持続効果のための遅延
        
        while True:
            display_pattern(pattern_heart)            # ハートの形を表示
            display_pattern(pattern_smile)            # スマイルフェイスを表示

* Design Your Own Patterns

  各バイトはLEDマトリックスの1行を表し、ビットが0の箇所が点灯します。独自のパターンリストを作成して、オリジナルのデザインを作りましょう。

**Conclusion**

このレッスンでは、Raspberry Pi Pico 2と2つの74HC595シフトレジスタを使用して、8x8 LEDマトリックスを制御する方法を学びました。 ビット操作やシフトレジスタの活用方法を理解することで、マトリックス上にパターンやグラフィックを自由に表示できるようになります。