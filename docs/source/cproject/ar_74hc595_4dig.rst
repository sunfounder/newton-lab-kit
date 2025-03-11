.. note:: 
    FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Raspberry Pi、Arduino、ESP32についての知識を深め、同じ趣味を持つ仲間と交流しましょう。

    **なぜ参加するのか？**

    - **専門的なサポート**: コミュニティとチームの支援を受けて、販売後の問題や技術的な課題を解決します。
    - **学びと共有**: ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**: 新製品の発表や先行プレビューに早期アクセスが可能です。
    - **特別な割引**: 最新製品の独占的な割引を楽しみましょう。
    - **祭りのプロモーションとギブアウェイ**: ギブアウェイや休日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造しませんか？[|link_sf_facebook|]をクリックして今すぐ参加してください！

.. _ar_74hc_4dig:

5.3 4桁7セグメントディスプレイで時間カウンターを作成する
==============================================================

このレッスンでは、 **4桁7セグメントディスプレイ** を使用して、Raspberry Pi Pico 2 でシンプルな時間カウンターを作成する方法を学びます。ディスプレイは1秒ごとにカウントアップし、経過秒数を表示します。

**必要なもの**

このプロジェクトでは、以下のコンポーネントが必要です。

以下のリンクからキットを購入すると便利です。

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名称	
        - このキットに含まれるアイテム
        - リンク
    *   - Newton Lab Kit	
        - 450+
        - |link_newton_lab_kit|


また、以下のリンクから個別に購入することもできます。

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - 番号
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


**4桁7セグメントディスプレイの理解**

4桁7セグメントディスプレイは、4つの個別の7セグメントディスプレイが1つのモジュールに統合されたものです。各桁は同じセグメント制御ライン（ **a** ～ **g** および **dp** ）を共有しますが、各桁には独自の **共通カソード** 制御があります。この構成により、どの桁をアクティブにするかを制御できます。

異なる数字を各桁に表示するためには、 **マルチプレクシング** という技術を使用します。これは、桁ごとに高速で切り替えて更新することで、すべての桁が同時に表示されているように見せる技術です。これは視覚残像の原理を利用したものです。

|4digit_control_pins|

**回路図**

|sch_4dig|

この回路の配線の基本原理は :ref:`py_74hc_led` とほぼ同じですが、異なる点は、Q0～Q7が4桁7セグメントディスプレイのa～gピンに接続されることです。

さらに、G10～G13は、どの7セグメントディスプレイを動作させるかを制御します。

**配線図**

|wiring_4dig|

* **セグメント接続（220Ω抵抗を通して）:**

  * **Q0** → セグメント **a**
  * **Q1** → セグメント **b**
  * **Q2** → セグメント **c**
  * **Q3** → セグメント **d**
  * **Q4** → セグメント **e**
  * **Q5** → セグメント **f**
  * **Q6** → セグメント **g**
  * **Q7** → セグメント **dp**（小数点）

* **共通カソード接続（桁選択ピン）:**

  * **桁1（左端桁）:** **GP10** に接続
  * **桁2:** **GP11** に接続
  * **桁3:** **GP12** に接続
  * **桁4（右端桁）:** **GP13** に接続

**コードの記述**

.. note::

   * ``5.3_time_counter.ino`` を ``newton-lab-kit/arduino/5.3_time_counter`` フォルダから開くことができます。
   * または、以下のコードを **Arduino IDE** にコピーしてください。
   * **Raspberry Pi Pico 2** ボードを選択し、適切なポートを選択して「アップロード」をクリックしてください。

.. code-block:: arduino

    // Define the connection pins for the shift register
    #define DATA_PIN 18   // DS (Serial Data Input)
    #define LATCH_PIN 19  // STCP (Storage Register Clock)
    #define CLOCK_PIN 20  // SHCP (Shift Register Clock)

    // Define the digit control pins for the 4-digit 7-segment display
    const int digitPins[4] = { 10, 11, 12, 13 };  // DIG1, DIG2, DIG3, DIG4

    // Segment byte maps for numbers 0-9
    const byte digitCodes[10] = {
      // Pgfedcba
      0b00111111,  // 0
      0b00000110,  // 1
      0b01011011,  // 2
      0b01001111,  // 3
      0b01100110,  // 4
      0b01101101,  // 5
      0b01111101,  // 6
      0b00000111,  // 7
      0b01111111,  // 8
      0b01101111   // 9
    };

    unsigned long previousMillis = 0;  // Stores the last time the display was updated
    unsigned int counter = 0;          // Counter value

    void setup() {
      // Initialize the shift register pins
      pinMode(DATA_PIN, OUTPUT);
      pinMode(LATCH_PIN, OUTPUT);
      pinMode(CLOCK_PIN, OUTPUT);

      // Initialize the digit control pins
      for (int i = 0; i < 4; i++) {
        pinMode(digitPins[i], OUTPUT);
        digitalWrite(digitPins[i], HIGH);  // Turn off all digits
      }
    }

    void loop() {
      unsigned long currentMillis = millis();

      // Update the counter every 1000 milliseconds (1 second)
      if (currentMillis - previousMillis >= 1000) {
        previousMillis = currentMillis;
        counter++;  // Increment the counter
        if (counter > 9999) {
          counter = 0;  // Reset counter after 9999
        }
      }

      // Display the counter value
      displayNumber(counter);
    }

    void displayNumber(int num) {
      // Break the number into digits
      int digits[4];
      digits[0] = num / 1000;        // Thousands
      digits[1] = (num / 100) % 10;  // Hundreds
      digits[2] = (num / 10) % 10;   // Tens
      digits[3] = num % 10;          // Units

      // Display each digit
      for (int i = 0; i < 4; i++) {
        digitalWrite(digitPins[i], LOW);  // Activate digit
        shiftOutDigit(digitCodes[digits[i]]);
        delay(5);                          // Small delay for multiplexing
        digitalWrite(digitPins[i], HIGH);  // Deactivate digit
      }
    }

    void shiftOutDigit(byte data) {
      // Send data to the shift register
      digitalWrite(LATCH_PIN, LOW);
      shiftOut(DATA_PIN, CLOCK_PIN, MSBFIRST, data);
      digitalWrite(LATCH_PIN, HIGH);
    }

コードをアップロードすると、4桁7セグメントディスプレイが「0000」からカウントを開始し、1秒ごとに1ずつ増加します。
カウントの進行は次のようになります：0000、0001、0002、...、9999、その後0000にリセットされます。

**コードの理解**

#. 制御ピンの定義:

   * ``DATA_PIN (DS)``: 74HC595にシリアルデータを送信
   * ``LATCH_PIN (STCP)``: シフトレジスタのデータを出力ピンに固定
   * ``CLOCK_PIN (SHCP)``: シフトレジスタへのデータ送信を制御

   .. code-block:: arduino

      #define DATA_PIN   18  // DS (シリアルデータ入力)
      #define LATCH_PIN  19  // STCP (ストレージレジスタクロック)
      #define CLOCK_PIN  20  // SHCP (シフトレジスタクロック)
  
#. 桁制御ピンの定義:

   * 各桁の共通カソードは個別のGPIOピンに接続されます。
   * LOW に設定するとその桁が有効になり、HIGH で無効になります。

   .. code-block:: arduino

      const int digitPins[4] = {10, 11, 12, 13}; // DIG1, DIG2, DIG3, DIG4
  
#. セグメントのバイトマップ作成:

   * 各バイトは、共通カソードの7セグメントディスプレイに表示する数字 (0～9) のセグメントを表します。
   * 各ビットはセグメント a から g および dp に対応しています。

   .. code-block:: arduino

      const byte digitCodes[10] = {
        0b00111111, // 0
        0b00000110, // 1
        0b01011011, // 2
        0b01001111, // 3
        0b01100110, // 4
        0b01101101, // 5
        0b01111101, // 6
        0b00000111, // 7
        0b01111111, // 8
        0b01101111  // 9
      };

#. セットアップ関数:

   * ``DATA_PIN`` 、 ``LATCH_PIN`` 、 ``CLOCK_PIN`` を出力ピンとして設定。
   * すべての桁制御ピンを ``HIGH`` に設定し、最初はすべての桁を無効化。

   .. code-block:: arduino

      void setup() {
        // シフトレジスタのピンを初期化
        pinMode(DATA_PIN, OUTPUT);
        pinMode(LATCH_PIN, OUTPUT);
        pinMode(CLOCK_PIN, OUTPUT);

        // 桁制御ピンの初期化
        for (int i = 0; i < 4; i++) {
          pinMode(digitPins[i], OUTPUT);
          digitalWrite(digitPins[i], HIGH); // 初期状態で全桁をオフ
        }
      }

#. ループ関数:

   * ``millis()`` を使用し、プログラムをブロックせずに経過時間を追跡。
   * ``counter`` を1秒ごとに増加し、9999を超えたらリセット。

   .. code-block:: arduino

      void loop() {
        unsigned long currentMillis = millis();

        // 1000ミリ秒 (1秒) ごとにカウンターを更新
        if (currentMillis - previousMillis >= 1000) {
          previousMillis = currentMillis;
          counter++; // カウントを増加
          if (counter > 9999) {
            counter = 0; // 9999を超えたらリセット
          }
        }

        // カウンター値を表示
        displayNumber(counter);
      }

#. 数値の表示:

   * ``counter`` の値を千の位、百の位、十の位、一の位に分割。
   * 各桁を順番にアクティブにし、対応するセグメントデータを送信後、非アクティブに。
   * 高速で桁を切り替えることで、すべての桁が同時に点灯しているように見せる。

   .. code-block:: arduino

      void displayNumber(int num) {
        // 数値を個々の桁に分解
        int digits[4];
        digits[0] = num / 1000;         // 千の位
        digits[1] = (num / 100) % 10;   // 百の位
        digits[2] = (num / 10) % 10;    // 十の位
        digits[3] = num % 10;           // 一の位

        // 各桁を順番に表示
        for (int i = 0; i < 4; i++) {
          digitalWrite(digitPins[i], LOW); // 現在の桁を有効化

          // 現在の桁に対応するセグメントデータを送信
          shiftOutDigit(digitCodes[digits[i]]);

          delay(5);                        // マルチプレクシングのための短い遅延
          digitalWrite(digitPins[i], HIGH); // 現在の桁を無効化
        }
      }

#. セグメントデータのシフト出力:

   * 74HC595シフトレジスタにセグメントデータを送信。
   * ``shiftOut()`` を使用して、最上位ビット (``MSBFIRST``) から1ビットずつ送信。
   * ``LATCH_PIN`` をトグルして出力ピンにデータをラッチ。

   .. code-block:: arduino

      void shiftOutDigit(byte data) {
        // シフトレジスタにデータを送信
        digitalWrite(LATCH_PIN, LOW);
        shiftOut(DATA_PIN, CLOCK_PIN, MSBFIRST, data);
        digitalWrite(LATCH_PIN, HIGH);
      }
  

**さらなる実験**

* リセットボタンを追加する:

   ボタンをPicoに接続し、押したらカウンターがリセットされるようにします。

* 異なるデータを表示する:

   センサーの値 (温度や光の強さ) を表示するようにコードを変更できます。

* ストップウォッチを作成する:

   スタート、ストップ、リセット機能を追加し、ストップウォッチとして使用できるようにします。


**結論**

このプロジェクトでは、シフトレジスタを使用して4桁7セグメントディスプレイを制御する方法を学びました。 ``millis()`` を利用して適切なタイミング管理を行い、表示の滑らかさを損なうことなく正確な時間カウンターを実現しました。
