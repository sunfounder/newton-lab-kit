.. note::

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！ラズベリーパイ、アルドゥイーノ、ESP32について、同じ趣味を持つ人々とさらに深く探求しましょう。

    **参加する理由は？**

    - **専門家によるサポート**: コミュニティとチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学びと共有**: 技術を磨くためのヒントやチュートリアルを交換しましょう。
    - **独占プレビュー**: 新製品の発表やちら見せに早期アクセスが可能です。
    - **特別割引**: 最新製品を特別割引価格でお楽しみください。
    - **祝祭プロモーションとギブアウェイ**: ギブアウェイや休日のプロモーションに参加しましょう。

    👉 私たちと一緒に探求し、創造しませんか？[|link_sf_facebook|]をクリックして今すぐ参加！

.. _ar_pot:

2.11 ノブを回す
==========================

このレッスンでは、Raspberry Pi Pico 2の内蔵アナログ・デジタル変換器（ADC）を使用してアナログ入力を読み取り、その入力を使ってLEDの明るさを制御する方法を探ります。具体的には、可変抵抗器であるポテンショメータをアナログ入力デバイスとして使用します。ポテンショメータのノブを回すことで、Picoによって読み取られる電圧レベルを調整し、その後、パルス幅変調（PWM）を介してLEDの明るさを制御します。


**アナログ入力について**

これまで、デジタル入力と出力に取り組んできましたが、これらはON（高電圧）かOFF（低電圧）のどちらかです。しかし、多くの実世界の信号はアナログであり、値の範囲にわたって連続的に変化することができます。例には、光の強さ、温度、音のレベルがあります。

Raspberry Pi Pico 2には内蔵ADCがあり、アナログ電圧を読み取り、コードで処理できるデジタル値に変換することができます。

ADCは次の式を使用してポテンショメータからのアナログ電圧をデジタル値に変換します：

.. code-block::

  デジタル値 = (アナログ電圧 / 3.3V) * 1023

**PicoのADCピン**

|pin_adc|

Picoにはアナログ入力に使用できる3つのGPIOピンがあります：

* **GP26** (ADC0)
* **GP27** (ADC1)
* **GP28** (ADC2)

さらに、後のレッスンで探る内部に接続された温度センサー（ADC4）への第四のADCチャネルもあります。

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
        - 1(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_potentiometer`
        - 1
        - |link_potentiometer_buy|

**回路図**

|sch_pot|

**配線図**

|wiring_pot|


**コードの書き方**


.. note::

   * ファイル ``2.11_turn_the_knob.ino`` を ``newton-lab-kit/arduino/2.11_turn_the_knob`` から開くことができます。
   * あるいは、このコードを **Arduino IDE** にコピーしてください。
   * **Raspberry Pi Pico 2** ボードと正しいポートを選択し、「Upload」をクリックします。

.. code-block:: Arduino

   // ピンの定義
   const int potPin = 28;   // GP28 (ADC2)に接続されたポテンショメータ
   const int ledPin = 15;   // GP15 (PWM対応)に接続されたLED

   void setup() {
     // デバッグ用のシリアル通信を初期化
     Serial.begin(115200);
     // LEDピンを出力として設定
     pinMode(ledPin, OUTPUT);
   }

   void loop() {
     // ポテンショメータからアナログ値を読み取り（0-1023）
     int sensorValue = analogRead(potPin);
     // デバッグ用にセンサ値を出力
     Serial.println(sensorValue);

     // センサ値をPWM値（0-255）にマッピング
     int brightness = map(sensorValue, 0, 1023, 0, 255);
     // LEDの明るさを設定
     analogWrite(ledPin, brightness);

     // 安定のための小さな遅延
     delay(10);
   }

コードが実行され、シリアルモニターが開かれているとき：

* ポテンショメータのノブを回すと、LEDの明るさが滑らかに暗から明に変わるべきです。
* ポテンショメータを調整すると、約0から1023の範囲でアナログ値が表示されるはずです。

**コードの理解**

#. ピンの定義：

   ポテンショメータとLEDに使用されるGPIOピンを割り当てます。

   .. code-block:: Arduino

        const int potPin = 28;   // GP28 (ADC2)に接続されたポテンショメータ
        const int ledPin = 15;   // GP15 (PWM対応)に接続されたLED

#. シリアル通信の初期化：

   シリアル通信を開始し、シリアルモニターにメッセージを出力できるようにします。

   .. code-block:: Arduino

        Serial.begin(115200);

#. アナログ値の読み取り：

   potPin (GP28)でアナログ電圧を読み取り、0から1023の間の値を返します。

   .. code-block:: Arduino

        int sensorValue = analogRead(potPin);

#. センサ値の出力：

   デバッグ目的で現在のセンサ値をシリアルモニターに出力します。

   .. code-block:: Arduino

        Serial.println(sensorValue);

#. センサ値のマッピング：

   センサ値（0-1023）をPWM出力に適した明るさ値（0-255）に変換します。

   .. code-block:: Arduino

        int brightness = map(sensorValue, 0, 1023, 0, 255);

#. LEDの明るさの設定：

   ledPin (GP15)でPWMデューティサイクルを設定することにより、LEDの明るさを調整します。

   .. code-block:: Arduino

        analogWrite(ledPin, brightness);

#. 小さな遅延の追加：

   読み取りを安定させ、ループが速すぎるのを防ぐために短い遅延を挿入します。

   .. code-block:: Arduino

        delay(10);

**さらなる探求**

* **電圧の表示**: コードを修正して、ポテンショメータから読み取った実際の電圧を計算して表示します。

  .. code-block:: Arduino

        // ピンの定義
        const int potPin = 28;  // GP28 (ADC2)に接続されたポテンショメータ
        const int ledPin = 15;  // GP15 (PWM対応)に接続されたLED
        
        void setup() {
          // デバッグ用のシリアル通信を初期化
          Serial.begin(115200);
          // LEDピンを出力として設定
          pinMode(ledPin, OUTPUT);
        }
        
        void loop() {
          // ポテンショメータからアナログ値を読み取り（0-1023）
          int sensorValue = analogRead(potPin);
        
          // デバッグ用にセンサ値を出力
          Serial.println(sensorValue);
        
          // 実際の電圧を計算して表示
          float voltage = sensorValue * (3.3 / 1023.0);
          Serial.print("Voltage: ");
          Serial.print(voltage);
          Serial.println(" V");
        
          // センサ値をPWM値（0-255）にマッピング
          int brightness = map(sensorValue, 0, 1023, 0, 255);
          // LEDの明るさを設定
          analogWrite(ledPin, brightness);
        
          // 安定のための小さな遅延
          delay(10);
        }

* **複数のLEDを制御する**: 複数のポテンショメータを使用して、異なるLEDやRGB LEDの色を制御します。
* **他のセンサーとの使用**: ポテンショメータを光依存型抵抗（LDR）などの別のアナログセンサーに置き換えて、周囲の光に基づいてLEDを制御します。


**コンセプトの説明**

* アナログ・デジタル変換（ADC）：

  * PicoのADCは、ポテンショメータからのアナログ電圧をデジタル値に変換します。
  * 0Vから3.3Vの電圧範囲が0から1023の数値に変換されます。

* パルス幅変調（PWM）：

  * PWMは、デジタルピンをHIGHとLOWの状態で迅速に切り替えることにより、アナログ電圧をシミュレートする技術です。
  * 信号がHIGHになる時間の割合（デューティサイクル）を調整することで、LEDやモーターのようなデバイスを制御できます。

* 値のマッピング：

  * ``map()`` 関数は、ある範囲の値を別の範囲にスケーリングします。
  * この場合、ポテンショメータの0-1023の範囲をPWMの0-255の範囲にマッピングします。


**まとめ**

このレッスンでは、Raspberry Pi PicoのADCを使用してポテンショメータからアナログ入力を読み取り、その入力を使用してPWMを介してLEDの明るさを制御する方法を学びました。この基本的なスキルを身につけることで、さまざまなアナログセンサーとインターフェースし、出力を比例的に制御することができます。
