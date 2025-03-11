.. note::
    
    こんにちは！FacebookでSunFounderのRaspberry Pi & Arduino & ESP32愛好者コミュニティに参加していただきありがとうございます！同じ興味を持つ仲間と一緒に、Raspberry Pi、Arduino、ESP32の更なる深掘りを楽しみましょう。

**参加する理由は？**

- **専門家によるサポート**：コミュニティやチームの支援を受けて、販売後の問題や技術的な課題を解決。
- **学びと共有**：スキルを高めるためのヒントやチュートリアルを交換。
- **独占プレビュー**：新製品発表や製品の先行試用のチャンス。
- **特別割引**：最新製品に対する独占的な割引を享受。
- **祝祭プロモーションとギフト**：ギフトや祝祭のプロモーションに参加。

👉 私たちと一緒に探求し、創造してみませんか？[|link_sf_facebook|]をクリックして今すぐ参加！

.. _py_74hc_7seg:

5.2 数字の表示
===========================================================

このレッスンでは、 **7セグメント表示器** とRaspberry Pi Pico 2、そして **74HC595シフトレジスタ** を使用して数字を表示する方法を学びます。7セグメント表示器は、デジタル時計、電卓、家電製品などで数値情報を表示するために一般的に使用される電子部品です。

74HC595シフトレジスタと7セグメント表示器を組み合わせることで、Picoの少数のGPIOピンだけを使用してすべてのセグメントを制御でき、他のコンポーネントのために貴重なI/Oリソースを節約できます。

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
        - 450+
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
        - 1(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_7_segment`
        - 1
        - |link_7segment_buy|
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|

**7セグメント表示器の理解**

7セグメント表示器は、数字0から9を表示するために、フィギュアエイトパターンに配置された7つのLED（セグメント）で構成されています。小数点を表示するための8番目のLEDもあります。各セグメントは **a** から **g** までラベル付けされ、小数点は **dp** とラベル付けされています。

こちらがセグメントのラベル付けです：

|img_7seg_cathode|

**共通カソード** の7セグメント表示器では、LEDのカソード（マイナス側）が共通のグラウンドに接続されています。



**回路図**

|sch_74hc_7seg|

ここでの配線原理は基本的に :ref:`py_74hc_led` と同じで、唯一の違いはQ0-Q7が7セグメント表示器のa〜gピンに接続されていることです。

.. list-table:: Wiring
    :widths: 15 25
    :header-rows: 1

    *   - 74HC595
        - LEDセグメント表示器
    *   - Q0
        - a
    *   - Q1
        - b
    *   - Q2
        - c
    *   - Q3
        - d
    *   - Q4
        - e
    *   - Q5
        - f
    *   - Q6
        - g
    *   - Q7
        - dp

**配線図**


|wiring_74hc_7seg|



**コードの記述**

0から9までの数字を7セグメント表示器に表示するMicroPythonプログラムを記述しましょう。

.. note::

    * ``5.2_number_display.py`` を ``newton-lab-kit/micropython`` から開くか、Thonnyにコードをコピーして「実行」をクリックするか、F5を押します。
    * 正しいインタープリタが選択されていることを確認してください：MicroPython (Raspberry Pi Pico).COMxx. 

.. code-block:: python

    import machine
    import utime

    # 各数字（0-9）に対するバイナリコードを定義
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
    SDI = machine.Pin(0, machine.Pin.OUT)   # シリアルデータ入力（DS）
    RCLK = machine.Pin(1, machine.Pin.OUT)  # レジスタクロック（STCP）
    SRCLK = machine.Pin(2, machine.Pin.OUT) # シフトレジスタクロック（SHCP）

    # 74HC595にデータを送信する関数
    def shift_out(data):
        RCLK.low()
        for bit in range(7, -1, -1):
            SRCLK.low()
            bit_val = (data >> bit) & 0x01
            SDI.value(bit_val)
            SRCLK.high()
        RCLK.high()

    # 0から9までの数字を表示するメインループ
    while True:
        for num in range(10):
            shift_out(SEGMENT_CODES[num])
            utime.sleep(0.5)

このコードを実行すると、7セグメントディスプレイに0から9までの数字が0.5秒ごとに順番に表示されます。これにより、カウントアップするようなエフェクトが作られ、9に達すると0に戻り、繰り返し続けます。

**Explanation of the Code**

#. モジュールのインポート:

   * ``machine``: GPIOピンやハードウェア機能へのアクセスを提供します。
   * ``utime``: 遅延を含む時間関連の関数を含みます。

#. セグメントコードの定義:

   各エントリは、特定の数字を表示するために点灯する必要があるセグメントを示します。可読性を高めるために、値は16進数で表記されています。
   
   .. code-block:: python

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

   例えば、7セグメントディスプレイに数字「1」を表示する場合、bとcをHIGHレベルにし、a, d, e, f, g, dgをLOWレベルにする必要があります。

   |img_1_segment|

   つまり、バイナリ表記では"00000110"（16進数表記では0x06）を設定する必要があります。


#. 制御ピンの初期化:

   Raspberry Pi PicoのGPIOピンを使用して、74HC595を制御します。

   .. code-block:: python

      SDI = machine.Pin(0, machine.Pin.OUT)
      RCLK = machine.Pin(1, machine.Pin.OUT)
      SRCLK = machine.Pin(2, machine.Pin.OUT)

#. ``shift_out`` 関数の定義:

   * 8ビットのデータを74HC595に送信します。
   * 最上位ビット（MSB）から順にデータを出力します。
   * シフトクロックとレジスタクロックを適切に制御します。

   .. code-block:: python

        def shift_out(data):
            RCLK.low()
            for bit in range(7, -1, -1):
                SRCLK.low()
                bit_val = (data >> bit) & 0x01
                SDI.value(bit_val)
                SRCLK.high()
            RCLK.high()

#. 数字を表示するメインループ:

   * 0から9までの数字を順に表示します。
   * ``shift_out`` を呼び出し、対応するセグメントコードを送信します。
   * 各表示間に0.5秒の遅延を入れます。

   .. code-block:: python

        while True:
            for num in range(10):
                shift_out(SEGMENT_CODES[num])
                utime.sleep(0.5)


**Understanding the Segment Codes**

各セグメントコードは、特定の数字を表示するために点灯させる必要があるセグメントに対応しています。

* **0**: セグメント a, b, c, d, e, f （コード 0x3F）
* **1**: セグメント b, c （コード 0x06）
* **2**: セグメント a, b, g, e, d （コード 0x5B）
* **3**: セグメント a, b, c, d, g （コード 0x4F）
* **4**: セグメント b, c, f, g （コード 0x66）
* **5**: セグメント a, c, d, f, g （コード 0x6D）
* **6**: セグメント a, c, d, e, f, g （コード 0x7D）
* **7**: セグメント a, b, c （コード 0x07）
* **8**: セグメント a, b, c, d, e, f, g （コード 0x7F）
* **9**: セグメント a, b, c, d, f, g （コード 0x6F）

**さらなる実験**

* 16進数キャラクターの表示:

  ``SEGMENT_CODES`` リストを拡張し、A-Fの文字を表示できるようにします。例えば、「A」を表示するには、セグメントコード0x77を使用します。

* カウンターの作成:

  コードを変更して、昇順または降順のカウンターを作成できます。ボタン入力を利用して、表示される数字を増減させることも可能です。

* 複数のディスプレイを制御:

  追加の74HC595シフトレジスタを使用し、複数の7セグメントディスプレイを制御できます。マルチプレクシングを実装することで、最小限のGPIOピンで複数のディスプレイを管理できます。

**まとめ**

このレッスンでは、Raspberry Pi Picoと74HC595シフトレジスタを使用して、7セグメントディスプレイに数字を表示する方法を学びました。各セグメントをバイナリコードで制御する方法を理解し、シフトレジスタを活用することで、限られたGPIOピンで効率的に複数の出力を管理できるようになります。

