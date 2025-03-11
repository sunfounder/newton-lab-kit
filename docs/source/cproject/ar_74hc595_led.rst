.. note::

    こんにちは！SunFounder Raspberry Pi & Arduino & ESP32 愛好者コミュニティ（Facebook）へようこそ！Raspberry Pi、Arduino、ESP32 に関する知識を深め、仲間たちと一緒に楽しみましょう。

    **参加するメリット**  

    - **専門的なサポート**：購入後の問題や技術的な課題を、コミュニティメンバーやチームのサポートで解決。  
    - **学びと共有**：ヒントやチュートリアルを交換し、スキルを向上。  
    - **最新情報の先行公開**：新製品の発表やプレビューをいち早くチェック。  
    - **特別割引**：最新製品を会員限定の特別価格で購入可能。  
    - **イベント & プレゼント企画**：プレゼントキャンペーンや季節ごとのプロモーションに参加可能。  

    👉 一緒にものづくりを楽しみましょう！[|link_sf_facebook|] をクリックして、今すぐ参加！  

.. _ar_74hc_led:

5.1 74HC595 シフトレジスタの使用
===========================================================

このレッスンでは、 **74HC595シフトレジスタ** を使用して、Raspberry Pi Pico 2 のわずかな GPIO ピンで複数の LED を制御する方法を学びます。 **74HC595** は、シリアル入力を並列出力に変換することができる集積回路（IC）であり、GPIO ピンが限られている場合に、多数の出力を制御するのに非常に便利です。

**必要なもの**  

このプロジェクトでは、以下のコンポーネントが必要です。  

すべて揃ったキットを購入すると便利です。リンクはこちら：  

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名称  
        - キットに含まれるアイテム  
        - リンク  
    *   - Newton Lab Kit  
        - 450点以上  
        - |link_newton_lab_kit|  

個別に購入する場合は、以下のリンクからどうぞ。  

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
        - Micro USB ケーブル  
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



**74HC595シフトレジスタの仕組み**  

**74HC595** は、 8ビットのシリアル入力・並列出力 を持つシフトレジスタで、出力ラッチを備えています。 シリアルデータを入力し、並列出力へ変換できるため、Pico の 3 本の GPIO ピンだけで 8 つの出力を制御できます。

**74HC595 の主要ピン：**

|img_74jc595_pin|

* **DS (Pin 14)**: シリアルデータ入力  
* **SHCP (Pin 11)**: シフトレジスタクロック入力  
* **STCP (Pin 12)**: ストレージレジスタクロック入力（ラッチピン）  
* **OE (Pin 13)**: 出力イネーブル（Low アクティブ、GND に接続）  
* **MR (Pin 10)**: マスターリセット（Low アクティブ、3.3V に接続）  
* **Q0-Q7 (Pins 15, 1-7)**: 並列出力ピン  
* **VCC (Pin 16)**: 3.3V に接続  
* **GND (Pin 8)**: GND に接続  

**回路図**

|sch_74hc_led|

**配線図**

|wiring_74hc_led|

**コードの記述**

Raspberry Pi Pico からシリアルデータを送信し、74HC595 シフトレジスタを介して LED を順番に点灯させるプログラムを作成します。

.. note::

   * ``5.1_microchip_74hc595.ino`` を ``newton-lab-kit/arduino/5.1_microchip_74hc595`` から開くことができます。  
   * または、このコードを **Arduino IDE** にコピーしてください。  
   * **Raspberry Pi Pico 2** ボードを選択し、適切なポートを設定して「Upload」をクリックしてください。  

.. code-block:: arduino

  // 74HC595 に接続するピンを定義
  const int DS = 0;   // GPIO 0 -> DS (Pin 14)
  const int SHCP = 1; // GPIO 1 -> SHCP (Pin 11)
  const int STCP = 2; // GPIO 2 -> STCP (Pin 12)

  // LED を制御するバイナリパターン
  int datArray[] = {
    0b00000000, // All LEDs off
    0b00000001, // LED 0 on
    0b00000011, // LEDs 0 and 1 on
    0b00000111, // LEDs 0, 1, and 2 on
    0b00001111, // LEDs 0, 1, 2, and 3 on
    0b00011111, // LEDs 0 to 4 on
    0b00111111, // LEDs 0 to 5 on
    0b01111111, // LEDs 0 to 6 on
    0b11111111  // All LEDs on
  };

  void setup() {
    // Initialize the control pins as outputs
    pinMode(DS, OUTPUT);
    pinMode(SHCP, OUTPUT);
    pinMode(STCP, OUTPUT);
  }

  void loop() {
    // Iterate through each pattern in datArray
    for (int num = 0; num < 9; num++) {
      // Set STCP to LOW to prepare for data
      digitalWrite(STCP, LOW);

      // Shift out the data to the shift register
      shiftOut(DS, SHCP, MSBFIRST, datArray[num]);

      // Set STCP to HIGH to latch the data to the output pins
      digitalWrite(STCP, HIGH);

      delay(500); // Wait for half a second before the next pattern
    }

    // Turn off all LEDs after the sequence
    digitalWrite(STCP, LOW);
    shiftOut(DS, SHCP, MSBFIRST, 0b00000000);
    digitalWrite(STCP, HIGH);
    delay(500);
  }

コードをアップロードすると、 ``datArray`` に定義されたパターンに従い、74HC595 に接続された LED が順番に点灯します。  
すべての LED が点灯した後、順番に消灯します。

**コードの理解**

#. 制御ピンの定義:

   * ``DS (Data Serial Input)``: シリアルデータを受信  
   * ``SHCP (Shift Register Clock Input)``: データをシフトレジスタに転送  
   * ``STCP (Storage Register Clock Input)``: データを出力ピンにラッチ  

   .. code-block:: arduino

      const int DS = 0;   // GPIO 0 -> DS (Pin 14)
      const int SHCP = 1; // GPIO 1 -> SHCP (Pin 11)
      const int STCP = 2; // GPIO 2 -> STCP (Pin 12)

#. データパターンの作成:

   * ``datArray`` 配列に、LED を制御するバイナリパターンを格納  
   * 各ビットが LED の状態を表し、1 で点灯、0 で消灯  

   .. code-block:: arduino

      int datArray[] = {
        0b00000000, // すべての LED をオフ
        0b00000001, // LED 0 をオン
        0b00000011, // LED 0, 1 をオン
        0b00000111, // LED 0, 1, 2 をオン
        0b00001111, // LED 0, 1, 2, 3 をオン
        0b00011111, // LED 0 から 4 までをオン
        0b00111111, // LED 0 から 5 までをオン
        0b01111111, // LED 0 から 6 までをオン
        0b11111111  // すべての LED をオン
      };

#. セットアップ関数:

   ``DS``, ``SHCP``, ``STCP`` ピンを出力として設定し、シフトレジスタにデータを送信できるようにする。

   .. code-block:: arduino

      void setup() {
        // Initialize the control pins as outputs
        pinMode(DS, OUTPUT);
        pinMode(SHCP, OUTPUT);
        pinMode(STCP, OUTPUT);
      }

#. ループ関数: ``for`` ループで ``datArray`` 内の各パターンを順番に適用  

   * データのシフト出力

     * ``shiftOut`` で 1 ビットずつデータを送信  
     * ``MSBFIRST`` を指定し、最上位ビットから送信  

     .. code-block:: arduino

        shiftOut(DS, SHCP, MSBFIRST, datArray[num]);

   * データのラッチ  

     * ``STCP`` を ``LOW`` にしてデータの受信準備  
     * データ送信後、 ``STCP`` を ``HIGH`` にして出力ピンへ反映  

     .. code-block:: arduino

        digitalWrite(STCP, LOW);
        // shiftOut(...)
        digitalWrite(STCP, HIGH);

   * ディレイ処理  

     ``delay(500);`` で 0.5 秒ごとに LED の状態を更新  

   * LED の消灯

     すべての LED を消灯するために 0b00000000 を送信  

     .. code-block:: arduino

        digitalWrite(STCP, LOW);
        shiftOut(DS, SHCP, MSBFIRST, 0b00000000);
        digitalWrite(STCP, HIGH);
        delay(500);

**トラブルシューティング**

* LED が点灯しない場合 

  - 配線を再確認  
  - 74HC595 に電源が供給されているか確認  
  - Pico の GPIO ピンが正しく接続されているかチェック  

* LED の動作が異常な場合  

  - ``datArray`` のバイナリパターンを見直す  
  - LED に適切な抵抗が接続されているか確認  

**さらなる発展**

* 他のデバイスの制御 

  74HC595 を使ってリレーやモーターなどを制御可能  

* シフトレジスタのカスケード接続 

  複数の 74HC595 を直列に接続し、出力を拡張  

* LED パターンの作成  

  datArrayを変更して、より複雑な LED アニメーションを作成  

* センサーとの統合  

  センサーと組み合わせて、インタラクティブなシステムを構築  

* LED マトリックスの作成  

  複数のシフトレジスタを使用し、大規模な LED マトリックスを構築  

**まとめ**  

このレッスンでは、Raspberry Pi Pico の 3 本の GPIO ピンを使用し、74HC595 シフトレジスタを介して複数の LED を制御する方法を学びました。 この技術を活用することで、GPIO ピンの使用を最小限に抑えながら、より複雑でインタラクティブな電子工作を実現できます。 シリアルデータを並列出力に変換し、効率的に LED やその他のアクチュエータ、ディスプレイを管理できるようになります。
