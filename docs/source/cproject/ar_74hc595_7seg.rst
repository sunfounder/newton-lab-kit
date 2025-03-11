.. note::

    こんにちは！SunFounder Raspberry Pi & Arduino & ESP32 愛好者コミュニティ（Facebook）へようこそ！Raspberry Pi、Arduino、ESP32 に関する知識を深め、仲間たちと一緒に楽しみましょう。

    **参加するメリット**  

    - **専門的なサポート**：購入後の問題や技術的な課題を、コミュニティメンバーやチームのサポートで解決。  
    - **学びと共有**：ヒントやチュートリアルを交換し、スキルを向上。  
    - **最新情報の先行公開**：新製品の発表やプレビューをいち早くチェック。  
    - **特別割引**：最新製品を会員限定の特別価格で購入可能。  
    - **イベント & プレゼント企画**：プレゼントキャンペーンや季節ごとのプロモーションに参加可能。  

    👉 一緒にものづくりを楽しみましょう！[|link_sf_facebook|] をクリックして、今すぐ参加！  

.. _ar_74hc_7seg:

5.2 数字の表示
===========================================================

このレッスンでは、 **7セグメントディスプレイ** と **74HC595シフトレジスタ** を使用して、Raspberry Pi Pico 2 で数字を表示する方法を学びます。7セグメントディスプレイは、デジタル時計、電卓、家電製品などで数値情報を表示するために広く使用される電子部品です。

74HC595シフトレジスタを組み合わせることで、Pico の少数の GPIO ピンだけで7セグメントディスプレイの全セグメントを制御でき、他のコンポーネントのための I/O 資源を節約できます。

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
        - 1 (220Ω)  
        - |link_resistor_buy|  
    *   - 6  
        - :ref:`cpn_7_segment`  
        - 1  
        - |link_7segment_buy|  
    *   - 7  
        - :ref:`cpn_74hc595`  
        - 1  
        - |link_74hc595_buy|  

**7セグメントディスプレイの仕組み**  

7セグメントディスプレイは、0〜9の数字を表示するために、 **a** から **g** の7つのLEDセグメントが「8の字」型に配置されている部品です。さらに、小数点を表示するための **dp** という8つ目のLEDも搭載されています。  

こちらが各セグメントのラベルです：

|img_7seg_cathode|

**共通カソード** の7セグメントディスプレイでは、すべてのカソード（負極）が共通のグランド（GND）に接続されています。

**回路図**

|sch_74hc_7seg|

この回路の基本的な配線原理は、 :ref:`py_74hc_led` の場合とほぼ同じですが、Q0～Q7が7セグメントディスプレイの a ～ g ピンに接続されている点が異なります。

.. list-table:: Wiring
    :widths: 15 25
    :header-rows: 1

    *   - 74HC595
        - 7セグメントディスプレイ
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

**コードの作成**

このコードでは、74HC595シフトレジスタにシリアルデータを送信し、7セグメントディスプレイを制御します。
ディスプレイは0から9までの数字を順番に表示します。

.. note::

   * ``5.2_number_display.ino`` を ``newton-lab-kit/arduino/5.2_number_display`` から開くことができます。
   * または、このコードを **Arduino IDE** にコピーして使用できます。
   * **Raspberry Pi Pico 2** ボードと適切なポートを選択し、「アップロード」をクリックしてください。

.. code-block:: arduino

    // 74HC595 に接続するピンを定義
    const int DS = 0;    // GPIO 0 -> DS (Pin 14)
    const int SHCP = 1;  // GPIO 1 -> SHCP (Pin 11)
    const int STCP = 2;  // GPIO 2 -> STCP (Pin 12)

    // 7セグメントディスプレイに表示する数字 0-9 の 16進数コード
    const byte numArray[] = {
      0x3F, // 0: 00111111
      0x06, // 1: 00000110
      0x5B, // 2: 01011011
      0x4F, // 3: 01001111
      0x66, // 4: 01100110
      0x6D, // 5: 01101101
      0x7D, // 6: 01111101
      0x07, // 7: 00000111
      0x7F, // 8: 01111111
      0x6F  // 9: 01101111
    };

    void setup() {
      // 制御ピンを出力に設定
      pinMode(DS, OUTPUT);
      pinMode(SHCP, OUTPUT);
      pinMode(STCP, OUTPUT);
    }

    void loop() {
      // 0から9まで順番に表示
      for (int num = 0; num < 10; num++) {
        // データをセットするため STCP を LOW にする
        digitalWrite(STCP, LOW);

        // シフトレジスタにデータを送信
        shiftOut(DS, SHCP, MSBFIRST, numArray[num]);

        // STCP を HIGH にしてデータを出力ピンに適用
        digitalWrite(STCP, HIGH);

        delay(1000); // 1秒間表示
      }

      // 0-9を表示後、すべてのセグメントをオフにする
      digitalWrite(STCP, LOW);
      shiftOut(DS, SHCP, MSBFIRST, 0x00);
      digitalWrite(STCP, HIGH);
      delay(1000); 
    }

コードをアップロードすると、ディスプレイは0から9までの数字を順番に1秒間表示します。
9まで表示した後、すべてのセグメントをオフにして1秒待ち、再び0からカウントを開始します。


**コードの理解**

#. 制御ピンの定義:

   * ``DS (Data Serial Input)``: シフトレジスタにシリアルデータを受信する。
   * ``SHCP (Shift Register Clock Input)``: シフトレジスタへのデータシフトを制御する。
   * ``STCP (Storage Register Clock Input)``: シフトレジスタから出力ピンへのデータラッチを制御する。

   .. code-block:: arduino

        const int DS = 0;    // GPIO 0 -> DS (Pin 14)
        const int SHCP = 2;  // GPIO 2 -> SHCP (Pin 11)
        const int STCP = 1;  // GPIO 1 -> STCP (Pin 12)

#. データパターンの作成:

   * ``numArray``: 共通カソード7セグメントディスプレイで0～9を表示するための16進コードを格納する配列。
   * 各16進数値は、特定の数字を表示するために点灯させる必要があるセグメントに対応。

   .. code-block:: arduino

        const byte numArray[] = {
          0x3F, // 0: 00111111
          0x06, // 1: 00000110
          0x5B, // 2: 01011011
          0x4F, // 3: 01001111
          0x66, // 4: 01100110
          0x6D, // 5: 01101101
          0x7D, // 6: 01111101
          0x07, // 7: 00000111
          0x7F, // 8: 01111111
          0x6F  // 9: 01101111
        };

   例えば、7セグメントディスプレイに「1」を表示する場合、b, c をHIGHにし、a, d, e, f, g, dp をLOWにする必要があります。

   |img_1_segment|

   つまり、バイナリ値「00000110」を設定する必要があり、可読性のために16進表記の「0x06」を使用します。

#. セットアップ関数:

   * ``DS`` 、 ``SHCP`` 、 ``STCP`` ピンを出力として設定し、シフトレジスタにデータを送信する準備を行う。

   .. code-block:: arduino

        void setup() {
          // 制御ピンを出力として設定
          pinMode(DS, OUTPUT);
          pinMode(SHCP, OUTPUT);
          pinMode(STCP, OUTPUT);
        }

#. ループ関数: ``numArray`` 配列の各パターンを ``for`` ループで順番に表示。

   * データのシフトアウト:

     * ``shiftOut`` は1ビットずつデータを送信。
     * ``MSBFIRST`` は最上位ビットから送信することを示す。

     .. code-block:: arduino

        shiftOut(DS, SHCP, MSBFIRST, numArray[num]);

   * データのラッチ:

     * ``STCP`` を ``LOW`` に設定し、シフトレジスタに新しいデータを準備。
     * データを送信後、 ``STCP`` を ``HIGH`` にして7セグメントディスプレイの出力ピンに適用。

     .. code-block:: arduino

        digitalWrite(STCP, LOW);
        // shiftOut(...)
        digitalWrite(STCP, HIGH);

   * ``delay(500);`` を挿入し、各数字の視認性を高めるために0.5秒の遅延を追加。

   * すべてのセグメントをオフにする: 0～9を表示した後、 ``0x00`` を送信してすべてのセグメントをオフにする。ディスプレイは1秒間オフになり、ループが繰り返される。

     .. code-block:: arduino

        digitalWrite(STCP, LOW);
        shiftOut(DS, SHCP, MSBFIRST, 0x00);
        digitalWrite(STCP, HIGH);
        delay(1000);

**トラブルシューティング**

* 数字が表示されない場合:

  * 配線をすべて確認する。
  * 74HC595が適切に電源供給されていることを確認する。
  * PicoのGPIOピンがシフトレジスタに正しく接続されていることを確認する。
  * 7セグメントディスプレイが正しく接続されており、各セグメントに適切な抵抗が入っていることを確認する。

* 表示される数字が間違っている場合:

  * numArray 配列の16進コードを再確認する。
  * シフトレジスタの出力が正しいセグメントに接続されていることを確認する。

* ちらつきや不安定な表示がある場合:

  * 電源接続が安定しているか確認する。
  * 各セグメントの電流制限抵抗が適切に接続されていることを確認する。

**セグメントコードの理解**

各セグメントコードは、特定の数字を表示するために点灯する必要があるセグメントに対応します。

* **0**: Segments a, b, c, d, e, f (code 0x3F)
* **1**: Segments b, c (code 0x06)
* **2**: Segments a, b, g, e, d (code 0x5B)
* **3**: Segments a, b, c, d, g (code 0x4F)
* **4**: Segments b, c, f, g (code 0x66)
* **5**: Segments a, c, d, f, g (code 0x6D)
* **6**: Segments a, c, d, e, f, g (code 0x7D)
* **7**: Segments a, b, c (code 0x07)
* **8**: Segments a, b, c, d, e, f, g (code 0x7F)
* **9**: Segments a, b, c, d, f, g (code 0x6F)

**さらに探求しよう**

* 複数の7セグメントディスプレイを制御する

  - 74HC595シフトレジスタを複数連結し、複数の7セグメントディスプレイを制御。

* LEDアニメーションの実装

  - データパターンを変更し、動的なアニメーションやスクロールテキストを作成。

* センサーとの統合

  - 温度センサーや光センサーと組み合わせて、リアルタイムデータを表示。

* デジタル時計の作成

  - 複数の7セグメントディスプレイとリアルタイムクロック（RTC）モジュールを使用し、デジタル時計を構築。

* 小数点やインジケーターの追加

  - 小数点(dp)やコロン(:)などの追加インジケーターを使用して、より複雑なディスプレイを作成。


**結論**

このレッスンでは、 **Raspberry Pi Pico** と 74HC595 シフトレジスタ を使用して 7セグメントディスプレイ を制御する方法を学びました。シフトレジスタにシリアルデータを送信することで、限られたGPIOピンで複数の出力を効果的に管理できます。この技術を利用することで、より多くのLEDやディスプレイ、その他の周辺機器を追加してプロジェクトを拡張することが可能になります。
