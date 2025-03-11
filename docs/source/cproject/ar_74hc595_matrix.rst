.. note::

    こんにちは！SunFounder Raspberry Pi & Arduino & ESP32 愛好者コミュニティ（Facebook）へようこそ！Raspberry Pi、Arduino、ESP32 に関する知識を深め、仲間たちと一緒に楽しみましょう。

    **参加するメリット**  

    - **専門的なサポート**：購入後の問題や技術的な課題を、コミュニティメンバーやチームのサポートで解決。  
    - **学びと共有**：ヒントやチュートリアルを交換し、スキルを向上。  
    - **最新情報の先行公開**：新製品の発表やプレビューをいち早くチェック。  
    - **特別割引**：最新製品を会員限定の特別価格で購入可能。  
    - **イベント & プレゼント企画**：プレゼントキャンペーンや季節ごとのプロモーションに参加可能。  

    👉 一緒にものづくりを楽しみましょう！[|link_sf_facebook|] をクリックして、今すぐ参加！  

.. _ar_74hc_788bs:

5.4 8x8 LEDマトリクスでグラフィックを表示する
===================================================================

このレッスンでは、Raspberry Pi Pico 2 と **74HC595 シフトレジスタ** を 2 つ使用し、 **8x8 LEDマトリクス** を制御する方法を学びます。  
個々の LED を制御し、パターンや簡単なグラフィックを表示します。

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
        - :ref:`cpn_dot_matrix`  
        - 1  
        -  
    *   - 6  
        - :ref:`cpn_74hc595`  
        - 2  
        - |link_74hc595_buy|  

**8x8 LEDマトリクスの仕組み**

8x8 LEDマトリクスは、8行×8列に配置された合計 64 個の LED で構成されます。 各 LED は、行と列の電圧制御によって個別に点灯させることができます。  
このプロジェクトでは、74HC595 シフトレジスタ を 2 つ使用して LED の行と列を制御し、Pico の GPIO ピンの使用数を節約します。

**回路図**

|sch_ledmatrix|

8x8 LEDドットマトリクスは、2つの **74HC595** シフトレジスタによって制御されます。1つは行（ROW）を、もう1つは列（COLUMN）を担当します。  
これらの2つのチップは、Raspberry Pi Pico の GPIO ピン GP18、GP19、GP20 を共有し、Pico の I/O ポートを大幅に節約できます。

Pico は 16 ビットのバイナリデータを一度に出力します。  
最初の 8 ビットは行を制御する 74HC595 に送信され、最後の 8 ビットは列を制御する 74HC595 に送信されます。  
これにより、ドットマトリクス上に特定のパターンを表示できます。

**Q7' (Pin 9)**:  
最初の 74HC595 のシリアルデータ出力ピンであり、2つ目の 74HC595 の **DS (Pin 14)** に接続します。  
これにより、複数の 74HC595 チップを直列に接続（カスケード接続）できます。

**配線図**

回路の構築はやや複雑なので、ステップごとに進めていきます。

**ステップ 1:**  
まず、Pico、LEDドットマトリクス、2つの 74HC595 をブレッドボードに挿入します。  
Pico の 3.3V と GND をブレッドボードの両側の電源ラインに接続し、  
2つの 74HC595 の Pin 16 および 10 を VCC（3.3V）に、Pin 13 および 8 を GND に接続します。

.. note::
   上の Fritzing 図では、ラベルが付いている側が下側になっています。

|wiring_ledmatrix_4|

**ステップ 2:**  
2 つの 74HC595 の Pin 11 を接続し、GP20 へ接続。  
また、Pin 12 を接続し、GP19 へ、左側の 74HC595 の Pin 14 を GP18 へ接続。  
さらに、1 つ目の 74HC595 の Pin 9 を 2 つ目の 74HC595 の Pin 14 へ接続。

|wiring_ledmatrix_3|

**ステップ 3:**  
右側の 74HC595 は LED ドットマトリクスの列を制御します。  
以下の表に対応関係を示しています。  
Q0～Q7 のピンは、それぞれ LED ドットマトリクスの Pin 13、3、4、10、6、11、15、16 にマッピングされます。

+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **74HC595**        | **Q0** | **Q1** | **Q2** | **Q3** | **Q4** | **Q5** | **Q6** | **Q7** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **LED Dot Matrix** | **13** | **3**  | **4**  | **10** | **6**  | **11** | **15** | **16** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+

|wiring_ledmatrix_2|

**ステップ 4:**  
次に、LED ドットマトリクスの行（ROW）を接続します。  
左側の 74HC595 が LED ドットマトリクスの行を制御します。  
以下の表に対応関係を示しています。  
Q0～Q7 のピンは、それぞれ LED ドットマトリクスの Pin 9、14、8、12、1、7、2、5 にマッピングされます。

+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **74HC595**        | **Q0** | **Q1** | **Q2** | **Q3** | **Q4** | **Q5** | **Q6** | **Q7** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **LED Dot Matrix** | **9**  | **14** | **8**  | **12** | **1**  | **7**  | **2**  | **5**  |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+

|wiring_ledmatrix_1|


**コードの記述**

.. note::

   * ``5.4_8x8_pixel_graphics.ino`` を ``newton-lab-kit/arduino/5.4_8x8_pixel_graphics`` から開くことができます。  
   * または、このコードを **Arduino IDE** にコピーしてください。  
   * **Raspberry Pi Pico 2** ボードを選択し、適切なポートを設定して「Upload」をクリックしてください。  

.. code-block:: arduino

    const int STcp = 19;  // 74HC595 の ST_CP（ラッチピン）
    const int SHcp = 20;  // 74HC595 の SH_CP（クロックピン）
    const int DS = 18;    // 74HC595 の DS（データピン）

    // 8x8 LED マトリクスに 'X' を表示するデータ配列
    byte datArray[] = {0x7E, 0xBD, 0xDB, 0xE7, 0xE7, 0xDB, 0xBD, 0x7E};

    void setup() {
      // Set pins as outputs
      pinMode(STcp, OUTPUT);
      pinMode(SHcp, OUTPUT);
      pinMode(DS, OUTPUT);
    }

    void loop()
    {
      for(int num = 0; num <8; num++)
      {
        digitalWrite(STcp, LOW); // ST_CP を LOW にしてデータ送信中の状態を維持
        shiftOut(DS,SHcp,MSBFIRST,datArray[num]);
        shiftOut(DS,SHcp,MSBFIRST,0x80>>num);      
        // ラッチピンを HIGH に戻し、シフトレジスタにデータ転送が完了したことを通知
        digitalWrite(STcp, HIGH); // ST_CP を HIGH にしてデータを確定
      }
    }



コードをアップロードすると、LED マトリクスに 'X' のパターンが表示されるはずです。  
もしパターンが正しく表示されない場合は、タイミングの調整や配線の確認を行ってください。

**コードの理解**

#. ピンの定義:

   * ``STcp (ST_CP)``: シフトされたデータを出力レジスタにラッチするためのピン
   * ``SHcp (SH_CP)``: シフトレジスタにデータを送るクロック信号
   * ``DS``: シフトレジスタに送信するシリアルデータ入力

   .. code-block:: arduino

      const int STcp = 19;  // 74HC595 の ST_CP（ラッチピン）
      const int SHcp = 20;  // 74HC595 の SH_CP（クロックピン）
      const int DS = 18;    // 74HC595 の DS（データピン）

#. データ配列（ ``datArray`` ）:

   * 各要素が LED マトリクスの 1 行を表します。
   * 16 進数の値は、その行で点灯（1）または消灯（0）する LED を表します。
   * これにより、マトリクス上に左右対称の 'X' 形状を描画できます。

   .. code-block:: arduino

      byte datArray[] = {0x7E, 0xBD, 0xDB, 0xE7, 0xE7, 0xDB, 0xBD, 0x7E};


#. セットアップ関数:

   シフトレジスタと通信するために制御ピンを出力として初期化します。

   .. code-block:: arduino

      void setup() {
        // Set pins as outputs
        pinMode(STcp, OUTPUT);
        pinMode(SHcp, OUTPUT);
        pinMode(DS, OUTPUT);
      }

#. ループ関数:

   * ``num`` の値（0 から 7）が、それぞれ LED マトリクスの行を表します。
   * ``0x80 >> num`` により、1 行ずつアクティブにして点灯させます。
   * ``shiftOut()`` を使用して、最上位ビット（ ``MSBFIRST`` ）から順にデータを送信。
   * ``STcp`` の状態を切り替えることでデータを確定させます。

   .. code-block:: arduino

      void loop()
      {
        for(int num = 0; num <8; num++)
        {
          digitalWrite(STcp,LOW); //ground ST_CP and hold low for as long as you are transmitting
          shiftOut(DS,SHcp,MSBFIRST,datArray[num]);
          shiftOut(DS,SHcp,MSBFIRST,0x80>>num);    
          //return the latch pin high to signal chip that it 
          //no longer needs to listen for information
          digitalWrite(STcp,HIGH); //pull the ST_CPST_CP to save the data
        }
      }

**トラブルシューティング**

* LED が点灯しない場合 

  * 電源接続を確認する  
  * シフトレジスタが正しく Pico に接続されていることを確認する  

* 表示が崩れる場合  

  * datArray内のパターンを再確認する  
  * 行と列の接続が間違っていないかチェックする  

* ちらつきや不安定な表示 

  * loop内のディレイを調整し、安定した表示を確認する  
  * 電源が LED 数に対して十分であるかを確認する  


**さらなる実験**

* パターンの変更  

  下記の配列を使用して、異なる図形を表示できます。  
  datArrayを ``pattern_heart`` や ``pattern_smile`` に置き換えて試してください。

  .. code-block:: arduino

      // ハート型パターン
      byte pattern_heart[] = {
        0xFF, // 11111111
        0x99, // 10011001
        0x00, // 00000000
        0x00, // 00000000
        0x00, // 00000000
        0x81, // 10000001
        0xC3, // 11000011
        0xE7  // 11100111
      };

      // スマイルフェイスパターン
      byte pattern_smile[] = {
        0xC3, // 11000011
        0xBD, // 10111101
        0x5A, // 01011010
        0x7E, // 01111110
        0x5A, // 01011010
        0x66, // 01100110
        0xBD, // 10111101
        0xC3  // 11000011
      };

* アニメーションの作成

  複数のパターンを切り替えてアニメーションを作成できます。

  .. code-block:: arduino

      const int STcp = 19;  // 74HC595 の ST_CP（ラッチピン）に接続
      const int SHcp = 20;  // 74HC595 の SH_CP（クロックピン）に接続
      const int DS = 18;    // 74HC595 の DS（データピン）に接続

      // ハート形パターン
      byte pattern_heart[] = { 0xFF, 0x99, 0x00, 0x00, 0x00, 0x81, 0xC3, 0xE7 };

      // スマイルフェイスパターン
      byte pattern_smile[] = { 0xC3, 0xBD, 0x5A, 0x7E, 0x5A, 0x66, 0xBD, 0xC3 };

      void setup() {
        // ピンを出力として設定
        pinMode(STcp, OUTPUT);
        pinMode(SHcp, OUTPUT);
        pinMode(DS, OUTPUT);
      }

      void latchData() {
        // シフトされたデータを 74HC595 の出力ピンにラッチ
        digitalWrite(STcp, HIGH);  // データをラッチ
        digitalWrite(STcp, LOW);   // 次のデータ送信に備える
      }

      void displayPattern(byte pattern[]) {
        for (int repeat = 0; repeat < 500; repeat++) {  // パターンを一定時間表示
          for (int row = 0; row < 8; row++) {
            // データ送信の開始
            digitalWrite(STcp, LOW);  // シフトデータ送信準備

            // 列データをシフトレジスタへ送信（現在の行のパターン）
            shiftOut(DS, SHcp, MSBFIRST, pattern[row]);

            // 行データを送信（1 行ずつアクティブに）
            shiftOut(DS, SHcp, MSBFIRST, 1 << row);

            // データをラッチして表示
            latchData();

            // 残像効果を利用するための短い遅延
            delay(1);
          }
        }
      }

      void loop() {
        // ハートとスマイルのパターンを交互に表示
        displayPattern(pattern_heart);  // ハートを表示
        displayPattern(pattern_smile);  // スマイルを表示
      }

**まとめ**

このレッスンでは、Raspberry Pi Pico と 2 つの 74HC595 シフトレジスタを使用して 8x8 LED マトリクスを制御する方法を学びました。  
シフトレジスタを活用することで、最小限の GPIO ピンで複数の LED を効率的に管理でき、  
より高度でインタラクティブなプロジェクトを実現できます。  
シリアルデータの送信方法やラッチ機能を理解することで、ダイナミックなパターンやグラフィックの作成が可能になります。

