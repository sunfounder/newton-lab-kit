.. note::

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！ラズベリーパイ、アルドゥイーノ、ESP32について、同じ趣味を持つ人々とさらに深く探求しましょう。

    **参加する理由は？**

    - **専門家によるサポート**: コミュニティとチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学びと共有**: 技術を磨くためのヒントやチュートリアルを交換しましょう。
    - **独占プレビュー**: 新製品の発表やちら見せに早期アクセスが可能です。
    - **特別割引**: 最新製品を特別割引価格でお楽しみください。
    - **祝祭プロモーションとギブアウェイ**: ギブアウェイや休日のプロモーションに参加しましょう。

    👉 私たちと一緒に探求し、創造しませんか？[|link_sf_facebook|]をクリックして今すぐ参加！

.. _ar_photoresistor:

2.12 光を感じる
=====================

このレッスンでは、 **フォトレジスター** （光依存型抵抗器またはLDRとも呼ばれる）をRaspberry Pi Pico 2と共に使用して光の強度を測定する方法を学びます。フォトレジスターは受け取る光の量に基づいて抵抗値が変化します。明るい光では抵抗値が低くなり、周囲の光の変化を検出するのに理想的です。

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
        - :ref:`cpn_photoresistor`
        - 1
        - |link_photoresistor_buy|


**回路図**

|sch_photoresistor|


この回路では、10Kの抵抗器とフォトレジスターが直列に接続され、電圧分割器を形成しています。GP28はフォトレジスターの電圧を読み取り、10Kの抵抗器は電流を制限することで保護します。

* **明るい光**: フォトレジスターの抵抗値が減少し、その電圧とGP28の読み取り値が低下します。強い光の下で、その抵抗値はほぼゼロに近づき、GP28はほぼ0を読み取ります。この時、10Kの抵抗器が保護役割を果たし、3.3VとGNDが短絡するのを防ぎます。
* **暗闇**: フォトレジスターの抵抗値が増加し、その電圧とGP28の値が上がります。完全な暗闇では、その抵抗値はほぼ無限大に近く（10Kの抵抗器は無視できます）、GP28はほぼ1023を読み取ります。

計算式は以下の通りです。

.. code-block::

  Digital Value = (Analog Voltage/3.3V) * 1023


**配線図**

|wiring_photoresistor|


**コードの書き方**


.. note::

   * ファイル ``2.12_feel_the_light.ino`` を ``newton-lab-kit/arduino/2.12_feel_the_light`` から開くことができます。
   * あるいは、このコードを **Arduino IDE** にコピーしてください。
   * **Raspberry Pi Pico 2** ボードと正しいポートを選択し、「Upload」をクリックします。

.. code-block:: Arduino

   const int sensorPin = 28;   // GP28（ADC2）に接続されたフォトレジスター

   void setup() {
     Serial.begin(115200);    // シリアルモニターを初期化
   }

   void loop() {
     // フォトレジスターからアナログ値を読み取る
     int sensorValue = analogRead(sensorPin);
     // シリアルモニターにセンサー値を出力
     Serial.println(sensorValue);
     delay(500);  // 次の読み取り前に半秒待つ
   }

コードが実行され、シリアルモニターが開かれている時：

* センサー値の観察：

  フォトレジスターからのアナログ値を表す数字の流れが見えるはずです。

* フォトレジスターとのインタラクション：

  * フラッシュライトやランプをフォトレジスターに当てると、センサー値は減少します（光が多いほど抵抗が減少するため）。
  * フォトレジスターを手で覆ったり、暗い場所に置くと、センサー値は増加します（光が少ないほど抵抗が増加するため）。

**コードの理解**

#. センサーピンの定義：

   sensorPinをGPIO 28に割り当てます。これはアナログ入力に接続されています。

   .. code-block:: arduino

        const int sensorPin = 28;   // GP28（ADC2）に接続されたフォトレジスター

#. シリアル通信の初期化：

   シリアル通信を開始し、シリアルモニターにメッセージを出力できるようにします。

   .. code-block:: arduino

        Serial.begin(115200);

#. アナログ値の読み取り：

   sensorPinでアナログ電圧を読み取り、0から1023の間の値を返します。

   .. code-block:: arduino

        int sensorValue = analogRead(sensorPin);

#. センサー値の出力：

   センサー値をシリアルモニターに出力します。

   .. code-block:: arduino

        Serial.println(sensorValue);

#. ディレイの追加：

   次の読み取りまで500ミリ秒待ちます。

   .. code-block:: arduino

        delay(500);

**電圧への変換**

実際に読み取られる電圧値を見たい場合は、コードを以下のように修正できます：

.. code-block:: arduino

   const int sensorPin = 28;   // GP28（ADC2）に接続されたフォトレジスター

   void setup() {
     Serial.begin(115200);    // シリアルモニターを初期化
   }

    void loop() {
      int sensorValue = analogRead(sensorPin);
      // アナログ読み取りを電圧に変換
      float voltage = sensorValue * (3.3 / 1023.0);
      Serial.print("Sensor Value: ");
      Serial.print(sensorValue);
      Serial.print("  Voltage: ");
      Serial.print(voltage);
      Serial.println(" V");
      delay(500);
    }

**さらなる探求**

* 光に基づいてLEDを制御する：

  フォトレジスターを使用して、光のレベルに基づいてLEDの明るさを制御するか、オン/オフします。

* データログ：

  環境の変化を監視するために、時間とともに光の強度を記録します。

* ナイトライトの作成：

  暗くなると自動的に点灯するライトを作成します。

**まとめ**

このレッスンでは、フォトレジスターをRaspberry Pi Picoと共に使用して光の強度を測定する方法を学びました。電圧分割回路からアナログ電圧を読み取ることにより、光のレベルの変化を検出し、この情報をプロジェクトに活用できます。
