.. note:: 

    こんにちは！SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community へようこそ！Facebookコミュニティで、Raspberry Pi、Arduino、ESP32について深く学び、愛好者と交流しましょう。

    **なぜ参加するべきか？**

    - **専門的なサポート**: 購入後の問題や技術的な課題を、コミュニティやサポートチームと一緒に解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換し、スキルを向上させましょう。
    - **最新情報の先行公開**: 新製品の発表やプレビューにいち早くアクセスできます。
    - **特別割引**: 最新製品を特別価格で購入できます。
    - **イベントやプレゼント企画**: さまざまなキャンペーンやプレゼント企画に参加できます。

    👉 さあ、一緒に学び、創造しましょう！[|link_sf_facebook|] をクリックして、今すぐ参加！

.. _py_74hc_led:

5.1 74HC595シフトレジスタの使用方法
===========================================================

このレッスンでは、 **74HC595シフトレジスタ** を使用し、Raspberry Pi Pico 2 のわずかなGPIOピンで複数のLEDを制御する方法を学びます。74HC595は、シリアル入力をパラレル出力に変換できるIC（集積回路）であり、限られたGPIOピンを有効活用する際に非常に便利です。

**必要なもの**

このプロジェクトでは、以下のコンポーネントが必要です。

全ての部品を含む便利なキットはこちらから購入できます：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名称
        - キット内容
        - リンク
    *   - Newton Lab Kit
        - 450点以上
        - |link_newton_lab_kit|


個別に購入する場合は、以下のリンクをご利用ください。


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
        - 8 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 8
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|



**74HC595シフトレジスタの理解**

**74HC595** は、8ビットのシリアル入力・パラレル出力を持つシフトレジスタで、シリアルデータを受信し、それをパラレル出力に変換できます。これにより、Raspberry Pi Picoの3本のGPIOピンで8つの出力を制御できます。

**74HC595の主要ピン:**

|img_74jc595_pin|

* **DS (Pin 14)**: シリアルデータ入力
* **SHCP (Pin 11)**: シフトレジスタクロック入力
* **STCP (Pin 12)**: ストレージレジスタクロック入力（ラッチピン）
* **OE (Pin 13)**: 出力イネーブル（Lowアクティブ、GNDに接続）
* **MR (Pin 10)**: マスターリセット（Lowアクティブ、3.3Vに接続）
* **Q0-Q7 (Pin 15, 1-7)**: パラレル出力
* **VCC (Pin 16)**: 3.3Vに接続
* **GND (Pin 8)**: GNDに接続

**回路図**

|sch_74hc_led|

**配線図**

|wiring_74hc_led|

**コードの記述**

次に、MicroPythonを使用して、74HC595を介してLEDを制御するプログラムを作成します。

.. note::

    * ``5.1_microchip_74hc595.py`` を ``newton-lab-kit/micropython`` フォルダから開くか、Thonnyにコードをコピーして、「Run」をクリックするかF5キーを押してください。

    * インタプリタが正しく選択されていることを確認してください（MicroPython (Raspberry Pi Pico) COMxx）。



.. code-block:: python 

    import machine
    import utime

    # 74HC595に接続するピンの定義
    SDI = machine.Pin(0, machine.Pin.OUT)   # シリアルデータ入力（DS）
    RCLK = machine.Pin(1, machine.Pin.OUT)  # レジスタクロック（STCP）
    SRCLK = machine.Pin(2, machine.Pin.OUT) # シフトレジスタクロック（SHCP）

    # 74HC595にデータを送信する関数
    def shift_out(data):
        for bit in range(8):
            # 最上位ビットを抽出して先に送信
            bit_val = (data & 0x80) >> 7
            SDI.value(bit_val)
            # シフトレジスタクロックをパルス
            SRCLK.high()
            utime.sleep_us(1)
            SRCLK.low()
            utime.sleep_us(1)
            # 次のビットのためにデータを左シフト
            data = data << 1
        # レジスタクロックをパルスしてデータをラッチ
        RCLK.high()
        utime.sleep_us(1)
        RCLK.low()
        utime.sleep_us(1)

    # シフトパターンをデモするメインループ
    while True:
        # LEDをQ0からQ7まで順番に点灯
        for i in range(8):
            data = 1 << i
            shift_out(data)
            utime.sleep(0.2)
        # LEDをQ7からQ0まで逆順に点灯
        for i in range(7, -1, -1):
            data = 1 << i
            shift_out(data)
            utime.sleep(0.2)
        # バーエフェクトを作成
        for i in range(9):
            data = (1 << i) - 1
            shift_out(data)
            utime.sleep(0.2)
        # すべてのLEDを消灯
        shift_out(0x00)
        utime.sleep(0.5)

このコードを実行すると、74HC595シフトレジスタに接続されたLEDがダイナミックな点灯パターンを示します。

* **最初のシーケンス**: LEDが左から右へ順番に点灯し、光が移動するようなエフェクトを作成します。
* **次のシーケンス**: LEDが右から左へ順番に点灯し、逆方向の動きを演出します。
* **バーエフェクト**: 左から順番にLEDが累積的に点灯し、すべてのLEDが点灯するまで増加します。
* **最終ステップ**: すべてのLEDを一時的に消灯し、シーケンスを繰り返します。

これにより、視覚的に魅力的な光の動きと、バーが徐々に成長するようなエフェクトが連続的にループします。

**コードの解説**

#. モジュールのインポート:

   * ``machine``: GPIOピンへのアクセスを提供
   * ``utime``: 時間関連の関数を含む

#. 制御ピンの定義:

   74HC595に接続するGPIOピンを定義。

   .. code-block:: python

      SDI = machine.Pin(0, machine.Pin.OUT)   # データ入力
      RCLK = machine.Pin(1, machine.Pin.OUT)  # ラッチクロック
      SRCLK = machine.Pin(2, machine.Pin.OUT) # シフトクロック

#. データ送信関数:

   * 8ビットのデータをシフトレジスタに送信
   * 最上位ビット（MSB）から順に送信
   * シフトレジスタクロック（SRCLK）をパルスしてデータをシフト
   * 全ビット送信後、レジスタクロック（RCLK）をパルスして出力をラッチ

   .. code-block:: python

      def shift_out(data):
          for bit in range(8):
              bit_val = (data & 0x80) >> 7
              SDI.value(bit_val)
              SRCLK.high()
              utime.sleep_us(1)
              SRCLK.low()
              utime.sleep_us(1)
              data = data << 1
          RCLK.high()
          utime.sleep_us(1)
          RCLK.low()
          utime.sleep_us(1)
    
#. メインループ:

   * LEDをQ0からQ7まで順に点灯

   .. code-block:: python

      for i in range(8):
          data = 1 << i
          shift_out(data)
          utime.sleep(0.2)


   * LEDをQ7からQ0まで逆順に点灯

   .. code-block:: python

      for i in range(7, -1, -1):
          data = 1 << i
          shift_out(data)
          utime.sleep(0.2)

   * LEDを順番に点灯し、バーを成長させるエフェクトを作成

   .. code-block:: python

      for i in range(9):
          data = (1 << i) - 1
          shift_out(data)
          utime.sleep(0.2)

   * すべてのLEDを消灯

   .. code-block:: python

     shift_out(0x00)
     utime.sleep(0.5)

**さらに実験する**

* カスタムパターンの作成:

  送信データを変更して、異なるLEDパターンを作成できます。例えば、交互にLEDを点灯する場合:

  .. code-block:: python

    shift_out(0b10101010)

* より多くのLEDを制御:

  複数の74HC595を連結して、より多くの出力を制御可能。最初のチップのQ7'（ピン9）を次のチップのDS（ピン14）に接続。

* センサーと統合:

  センサーやボタン入力を使用して、LEDパターンを動的に変更可能。

**まとめ**

このレッスンでは、74HC595シフトレジスタを使用し、Raspberry Pi Pico 2の限られたGPIOピンで出力を拡張する方法を学びました。GPIOピンが制約されるプロジェクトにおいて、多くの出力を制御する際に非常に有用な技術です。

