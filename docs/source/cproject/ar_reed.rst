.. note::

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！ラズベリーパイ、アルドゥイーノ、ESP32について、同じ趣味を持つ人々とさらに深く探求しましょう。

    **参加する理由は？**

    - **専門家によるサポート**: コミュニティとチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学びと共有**: 技術を磨くためのヒントやチュートリアルを交換しましょう。
    - **独占プレビュー**: 新製品の発表やちら見せに早期アクセスが可能です。
    - **特別割引**: 最新製品を特別割引価格でお楽しみください。
    - **祝祭プロモーションとギブアウェイ**: ギブアウェイや休日のプロモーションに参加しましょう。

    👉 私たちと一緒に探求し、創造しませんか？[|link_sf_facebook|]をクリックして今すぐ参加！

.. _ar_reed:

2.9 磁力を感じる
===============================

このレッスンでは、Raspberry Pi Pico 2を使用して **リードスイッチ** により磁場の存在を検出する方法を探ります。リードスイッチは、磁場を利用して動作するシンプルな電気スイッチです。磁石がスイッチに近づくと、内部の接点が閉じて電気回路が完成します。

**必要なもの**

このプロジェクトには、以下のコンポーネントが必要です。

全てのキットを購入するのが便利ですが、こちらがリンクです：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - このキットのアイテム
        - リンク
    *   - Newton Lab Kit
        - 450以上
        - |link_newton_lab_kit|


個別に購入することもできます。以下のリンクからどうぞ。


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
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_reed`
        - 1
        - 


**リードスイッチの理解**

リードスイッチは、ガラスカプセル内に密封された2枚の薄い金属リードから構成されます。これらのリードは強磁性材料でできており、わずかに離れた位置に配置されています。磁場がない場合、リードは分離され、スイッチは**開**状態です。磁石がスイッチに近づくと、リードは磁化され、互いに引き寄せられて回路が閉じます。

* **磁石が近くにない場合**: スイッチは **開** ; 回路は未完成です。
* **磁石が近くにある場合**: スイッチは **閉** ; 回路は完成です。

|img_reed_sche|

**回路図**

|sch_reed|

デフォルトでは、GP14は低く、リードスイッチに近づく磁石がある場合に高くなります。

10KΩの抵抗器の目的は、磁石が近くにないときにGP14を安定した低レベルに保つことです。

* **磁石が近くにない場合**:

  * リードスイッチは **開** です。
  * **GP14** はプルダウン抵抗を通じて **GND** に接続されます。
  * GPIOピンは**LOW** (0)を読み取ります。

* **磁石が近くにある場合**:

  * リードスイッチは **閉** です。
  * **GP14** はリードスイッチを通じて **3.3V** に接続されます。
  * GPIOピンは **HIGH** (1)を読み取ります。

**配線図**

|wiring_reed|


**コードの書き方**

.. note::

   * ファイル ``2.9_feel_the_magnetism.ino`` を ``newton-lab-kit/arduino/2.9_feel_the_magnetism`` から開くことができます。
   * あるいは、このコードを **Arduino IDE** にコピーしてください。
   * **Raspberry Pi Pico 2** ボードと正しいポートを選択し、「Upload」をクリックします。

.. code-block:: Arduino


   const int reedPin = 14;    // リードスイッチに接続されたGPIOピン
   int reedState = 0;

   void setup() {
     Serial.begin(115200);       // 115200ボーでシリアルモニターを初期化
     pinMode(reedPin, INPUT);    // リードピンを入力として設定
   }

   void loop() {
     reedState = digitalRead(reedPin);  // リードスイッチの状態を読み取り

     if (reedState == HIGH) {
       Serial.println("Magnet Detected!");
     } else {
       Serial.println("No Magnet.");
     }
     delay(500);  // シリアルモニターを溢れさせないように遅延
   }

コードが実行されている間、シリアルモニターが開いているとき：

* **磁石が近くにない場合**: 「磁石なし。」と表示されます。
* **磁石が近くにある場合**: リードスイッチに磁石を近づけると、「磁石を検出！」と表示されます。

**コードの理解**

#. シリアル通信の初期化:

   115200のボーでシリアル通信を開始します。これにより、シリアルモニターにメッセージを出力することができます。

   .. code-block:: Arduino

        Serial.begin(115200);

#. リードピンの設定:
 
   reedPin (GP14)を入力として設定し、リードスイッチの状態を読み取ります。

   .. code-block:: Arduino

        pinMode(reedPin, INPUT);

#. リードスイッチの状態の読み取り:

   リードスイッチの現在の状態を読み取ります。磁石が近いとき（スイッチ閉）はHIGH、磁石がないとき（スイッチ開）はLOWです。

   .. code-block:: Arduino

        reedState = digitalRead(reedPin);

#. 磁石の存在に対する反応:

   リードスイッチに磁石が近いかどうかに基づいてメッセージを出力します。

   .. code-block:: Arduino

        if (reedState == HIGH) {
          Serial.println("Magnet Detected!");
        } else {
          Serial.println("No Magnet.");
        }


**リードスイッチと割り込みの活用** 

* **割り込みの基本**  

  例えば、本を読んでいるときに誰かが肩を叩いて質問してきたとします。本を読むのを一時中断し、質問に答えた後、また読書に戻ります。このような動作は、マイクロコントローラにおける「割り込み」の仕組みと似ています。

  割り込みを使用すると、プログラムは重要なイベントに即座に反応し、通常のプログラムの流れを一時的に停止して、割り込みサービスルーチン（ISR）と呼ばれる特定の処理を実行します。処理が完了すると、プログラムは中断した場所から再開されます。

* **割り込みを使う理由**  

  リードスイッチに割り込みを使用することで、マイクロコントローラは磁石を検出した際に即座に反応できます。これにより、 ``loop()`` 内でリードスイッチの状態を常に監視（ポーリング）する必要がなくなり、処理の効率が向上します。また、バッテリー駆動のアプリケーションでは電力消費を抑えることができます。

* **割り込みを使ったコードの記述**  

  割り込みを活用して磁石の検出を行うようにプログラムを変更してみましょう。

  .. code-block:: Arduino

        const int reedPin = 14;            // リードスイッチが接続されたGPIOピン
        volatile bool magnetDetected = false;  // 磁石の検出状態を示すフラグ

        void setup() {
          Serial.begin(115200);               // シリアルモニターを初期化
          pinMode(reedPin, INPUT);            // リードスイッチピンを入力に設定
          attachInterrupt(digitalPinToInterrupt(reedPin), onMagnetChange, CHANGE);  // 割り込みを設定
        }

        void loop() {
          if (magnetDetected) {
            Serial.println("Magnet Present!");
          } else {
            Serial.println("Waiting for magnet...");
          }
          delay(1000);                         // シリアルモニターの出力を抑制するために遅延
        }

        void onMagnetChange() {
          // リードスイッチの現在の状態を基にフラグを更新
          magnetDetected = digitalRead(reedPin) == HIGH;  // HIGHなら磁石検出、LOWなら未検出
        }


  .. code-block:: Arduino

        attachInterrupt(digitalPinToInterrupt(reedPin), onMagnetChange, CHANGE);
    
  * ``digitalPinToInterrupt(reedPin)``: 指定したピン番号を対応する割り込み番号に変換します。
  * ``onMagnetChange``: 割り込みが発生した際に実行されるISR（割り込みサービスルーチン）。
  * ``CHANGE``: ピンの状態が変化（HIGH → LOW または LOW → HIGH）したときに割り込みを発生させます。


**まとめ**  

このレッスンでは、Raspberry Pi Picoとリードスイッチを使用して磁場を検出する方法を学びました。また、割り込みを活用することで、センサーの状態を ``loop()`` 内で常に監視する必要なく、効率的にイベントに応答できることを学びました。組み込みプログラミングにおいて、割り込みの使い方を理解することは、より応答性の高いアプリケーションを作成するための重要なスキルとなります。

**さらなる応用**  

* **ドアセンサー**: リードスイッチを使用して、ドアが開いた際にアラームを作動させるシンプルなセキュリティシステムを作成。
* **回転数の計測**: 磁石を回転するオブジェクトに取り付け、リードスイッチを使用して1分間あたりの回転数（RPM）をカウント。
* **防犯システム**: 複数のリードスイッチを組み合わせて、窓やドアの状態を監視する防犯システムを構築。

**参考資料**  

* `attachInterrupt() - Arduinoリファレンス <https://www.arduino.cc/reference/en/language/functions/external-interrupts/attachinterrupt/>`_

