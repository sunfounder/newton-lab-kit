.. note:: 

    こんにちは！SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community（Facebook）へようこそ！Raspberry Pi、Arduino、ESP32に情熱を持つ皆と一緒に、さらに深く探求しましょう。

    **参加する理由は？**

    - **専門的サポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：技術的なヒントやチュートリアルを交換し、スキルアップを図りましょう。
    - **独占的なプレビュー**：新製品の発表やプレビューに早期アクセス。
    - **特別割引**：最新製品に対する独占的な割引を楽しめます。
    - **祭りのプロモーションとギフト**：ギブアウェイやホリデープロモーションに参加しましょう。

    👉 私たちと探索し、創造してみませんか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _ar_tilt:

2.6 傾けてみよう！
=======================

このレッスンでは、Raspberry Pi Pico 2を使用して傾きスイッチで向きの変化を検出する方法を学びます。傾きスイッチは、直立しているか傾いているかを感知できる簡単なデバイスで、動きの検出、向きの感知、または位置に基づいてトリガーとして使用するのに便利です。

**必要なもの**

このプロジェクトには以下のコンポーネントが必要です。

全てのキットを購入することは非常に便利です。リンクはこちらです：

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
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_tilt`
        - 1
        - 

**回路図**

|sch_tilt|

* **直立時（スイッチ閉）**：

  * 傾きスイッチは **3.3V** を直接 **GP14** に接続します。
  * GPIOピンは **HIGH** （1）を読み取ります。

* **傾いた時（スイッチ開）**：

  * 傾きスイッチは **3.3V** から **GP14** の接続を切断します。
  * プルダウン抵抗は **GP14** を **GND** に引っ張ります。
  * GPIOピンは **LOW** （0）を読み取ります。

**配線**

|wiring_tilt|


**コードの書き方**

.. note::

   * ``2.6_tilt_it.ino`` ファイルを ``newton-lab-kit/arduino/2.4_colorful_light`` から開くことができます。
   * または、このコードを **Arduino IDE** にコピーしてください。
   * **Raspberry Pi Pico 2** ボードを選択し、適切なポートを設定した後、「Upload」をクリックしてください。

.. code-block:: Arduino

   const int tiltPin = 14;  // 傾きスイッチに接続されたGPIOピン

   void setup() {
     Serial.begin(115200);       // シリアルモニターを115200ボーで初期化
     pinMode(tiltPin, INPUT);    // 傾きピンを入力として設定
   }

   void loop() {
     int tiltState = digitalRead(tiltPin);  // 傾きスイッチの状態を読み取る

     if (tiltState == HIGH) {
       Serial.println("The switch works!");
     }
     delay(100);  // シリアルモニターを過負荷にしないように少し遅延
   }

コードが実行されているとき、シリアルモニターが開かれ、ブレッドボードまたは傾きスイッチを傾けると、「スイッチは動作しています！」がシリアルモニターに表示されます。

**コードの理解**

#. シリアル通信の初期化：

   115200ボーでシリアル通信を開始します。これにより、シリアルモニターにメッセージを出力できます。

   .. code-block:: Arduino

        Serial.begin(115200);

#. 傾きピンの設定：

   ``tiltPin`` （GP14）を入力として設定し、傾きスイッチの状態を読み取ります。

   .. code-block:: Arduino

        pinMode(tiltPin, INPUT);


#. 傾きスイッチの状態の読み取り：

   傾きスイッチの現在の状態を読み取ります。直立時は ``HIGH`` 、傾いた時は ``LOW`` になります。

   .. code-block:: Arduino

        int tiltState = digitalRead(tiltPin);

#. 傾きへの対応：

   傾きスイッチが直立（閉）の場合、シリアルモニターにメッセージを表示します。

   .. code-block:: Arduino

        if (tiltState == HIGH) {
          Serial.println("The switch works!");
        }

**さらなる実験**

* **LEDの制御**：傾きスイッチが直立しているときにLEDを点灯し、傾いたときに消灯するようにコードを変更します。

  .. code-block:: Arduino

        const int tiltPin = 14;   // 傾きスイッチに接続されたGPIOピン
        const int ledPin = 15;    // LEDに接続されたGPIOピン

        void setup() {
          Serial.begin(115200);
          pinMode(tiltPin, INPUT);
          pinMode(ledPin, OUTPUT);
        }

        void loop() {
          int tiltState = digitalRead(tiltPin);

          if (tiltState == HIGH) {
            Serial.println("The switch works!");
            digitalWrite(ledPin, HIGH);  // LEDを点灯
          } else {
            digitalWrite(ledPin, LOW);   // LEDを消灯
          }
          delay(100);
        }

* **感度の調整**：傾きスイッチは感度が異なる場合があります。傾きの角度を調整して、スイッチがどの角度で作動するかを実験してみてください。

**まとめ**

このレッスンでは、Raspberry Pi Picoを使用して傾きスイッチで向きの変化を検出する方法を学びました。この基本的なスキルを身につけることで、警報、自動照明、またはインタラクティブなデバイスなど、動きや位置に反応するプロジェクトを作成できます。
