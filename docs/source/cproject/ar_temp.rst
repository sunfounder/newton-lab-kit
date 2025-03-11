.. note:: 

    こんにちは！SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community（Facebook）へようこそ！Raspberry Pi、Arduino、ESP32に情熱を持つ仲間たちと一緒に、さらに深く探求しましょう。

    **なぜ参加するのか？**

    - **専門的なサポート**：コミュニティやチームからのサポートを受けて、販売後の問題や技術的な課題を解決します。
    - **学びと共有**：技術的なヒントやチュートリアルを交換し、スキルを高めます。
    - **独占的なプレビュー**：新製品のアナウンスや先行公開に早期アクセスが可能です。
    - **特別割引**：最新製品を独占的な割引価格で楽しむことができます。
    - **祭りのプロモーションとギブアウェイ**：ギブアウェイやホリデープロモーションに参加しましょう。

    👉 私たちと探索し、創造してみませんか？[|link_sf_facebook|]をクリックして今日から参加しましょう！

.. _ar_temp:

2.13 温度計
===========================

このレッスンでは、Raspberry Pi Pico 2と **サーミスタ** を使用して温度を測定する方法を学びます。サーミスタは温度によって抵抗値が大きく変化するタイプの抵抗器です。ここでは、温度が上がると抵抗値が下がるネガティブ温度係数（NTC）サーミスタを使用します。

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
        - 1 (10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_thermistor`
        - 1
        - |link_thermistor_buy|

**サーミスタの理解**

NTCサーミスタは温度感応型の抵抗器です。温度が上昇するとその抵抗値が下がります。電圧分割回路に組み込むことで、温度変化に応じて変化する抵抗値を測定することができます。Raspberry Pi Pico 2のアナログ・デジタルコンバータ（ADC）を使用してこの電圧を読み取り、対応する温度を計算することができます。

**回路図**

|sch_temp|

この回路では、10KΩの抵抗器とNTCサーミスタが電圧分割器を形成しており、GP28がサーミスタの電圧を読み取ります。10KΩの抵抗器は、電流を制限することで保護も提供します。

* **高温時**：サーミスタの抵抗値は下がり、その電圧とGP28の読み取り値も下がります。温度が十分に高いと、抵抗値はほぼゼロに近づき、GP28はほぼ0を読み取ります。
* **低温時**：サーミスタの抵抗値は上がり、その電圧とGP28の値も上がります。極端な寒さでは、抵抗値はほぼ無限大になり、GP28はほぼ1023を読み取ります。

10KΩの抵抗器は、3.3VとGNDが直接接続されるのを防ぎ、短絡を防ぎます。

**配線図**

|wiring_temp|



**コードの書き方**

.. note::

   * ``2.13_thermometer.ino`` を ``newton-lab-kit/arduino/2.13_thermometer`` から開くことができます。
   * または、このコードを **Arduino IDE** にコピーしてください。
   * **Raspberry Pi Pico 2** ボードを選択し、適切なポートを設定した後、「Upload」をクリックしてください。

.. code-block:: arduino

    // ピンの定義
    const int thermistorPin = 28;  // サーミスタはGP28（ADC2）に接続

    // サーミスタと計算のための定数
    const float BETA = 3950;       // サーミスタのベータ値（メーカー提供）
    const float SERIES_RESISTOR = 10000; // 10KΩの抵抗
    const float NOMINAL_RESISTANCE = 10000; // 25°Cでの抵抗値（メーカー提供）
    const float NOMINAL_TEMPERATURE = 25.0; // 基準温度25°C

    void setup() {
      Serial.begin(115200);  // シリアルモニタを初期化
    }

    void loop() {
      // サーミスタからアナログ値を読み取る
      int adcValue = analogRead(thermistorPin);
      // ADC値を電圧に変換
      float voltage = adcValue * (3.3 / 1023.0);
      // サーミスタの抵抗値を計算
      float resistance = (voltage * SERIES_RESISTOR) / (3.3 - voltage);
      // ベータ式を使用してケルビン単位で温度を計算
      float temperatureK = 1 / ( (1 / (NOMINAL_TEMPERATURE + 273.15)) + (1 / BETA) * log(resistance / NOMINAL_RESISTANCE) );
      // ケルビンから摂氏に変換
      float temperatureC = temperatureK - 273.15;
      // 摂氏から華氏に変換
      float temperatureF = (temperatureC * 9.0 / 5.0) + 32.0;

      // 温度読み取りを表示
      Serial.print("Temperature: ");
      Serial.print(temperatureC);
      Serial.print(" °C, ");
      Serial.print(temperatureF);
      Serial.println(" °F");

      delay(1000);  // 次の読み取りまで1秒待つ
    }

コードが実行されてシリアルモニターが開いている場合：

* 摂氏と華氏での温度が表示されます。
* サーミスタを指でやさしく持つと、サーミスタが温まるにつれて温度が上昇します。
* サーミスタに冷たい空気を吹きかけたり、冷たい物体を近づけると、温度が下がります。

**コードの理解**

#. ピンと定数の定義：

   サーミスタの読み取りに使用するGPIOピンを割り当てます。

   .. code-block:: arduino

        const int thermistorPin = 28;  // サーミスタはGP28（ADC2）に接続されています

#. 計算のための定数：

   温度を決定する計算に使用される定数です。

   .. code-block:: arduino

        const float BETA = 3950;       // サーミスタのベータ値
        const float SERIES_RESISTOR = 10000; // 10KΩの抵抗
        const float NOMINAL_RESISTANCE = 10000; // 25°Cでの抵抗値
        const float NOMINAL_TEMPERATURE = 25.0; // 摂氏25度

#. アナログ値の読み取り：

   thermistorPinでアナログ電圧を読み取り、0から1023の値を返します。

   .. code-block:: arduino

        int adcValue = analogRead(thermistorPin);

#. 電圧の計算：

   ADC値を実際の電圧に変換します。

   .. code-block:: arduino

        float voltage = adcValue * (3.3 / 1023.0);

#. サーミスタ抵抗の計算：

   電圧分割式を使用してサーミスタの抵抗値を計算します。

   .. code-block:: arduino

        float resistance = (voltage * SERIES_RESISTOR) / (3.3-voltage);

#. 温度の計算：

   .. code-block:: arduino

        float temperatureK = 1 / ( (1 / (NOMINAL_TEMPERATURE + 273.15)) + (1 / BETA) * log(resistance / NOMINAL_RESISTANCE) );
        float temperatureC = temperatureK - 273.15;
        float temperatureF = (temperatureC * 9.0 / 5.0) + 32.0;

#. 温度の表示：

   シリアルモニターに摂氏と華氏で温度を出力します。

   .. code-block:: arduino

        Serial.print("Temperature: ");
        Serial.print(temperatureC);
        Serial.print(" °C, ");
        Serial.print(temperatureF);
        Serial.println(" °F");

#. 遅延：

   次の読み取りまで1秒待ちます。

   .. code-block:: arduino

        delay(1000);

**温度計算の理解**

* スタインハート-ハート方程式：

スタインハート-ハート方程式は、温度の関数としてサーミスタの抵抗をモデル化します：

|temp_format|

* ``T`` はサーミスタの温度（ケルビン）。
* ``T0`` は基準温度で、通常は25°C（ケルビンで273.15 + 25）。
* ``B`` は材料のベータパラメータで、このキットで使用されるNTCサーミスタのベータ係数は3950です。
* ``R`` は測定される抵抗。
* ``R0`` は基準温度T0での抵抗で、このキットのNTCサーミスタの25°Cでの抵抗は10キロオームです。

**精度についての注意**

* サーミスタは非線形デバイスで、ベータ方程式は近似値を提供します。
* より広い範囲でより正確な温度測定を行うために、スタインハート-ハート方程式を使用できます。
* 正確なアプリケーションには校正が必要になる場合があります。

**さらなる探求**

* **LCDに温度表示**：

  コンピューターなしで温度読み取りを表示するためにLCDディスプレイを接続します。

* **データロギング**：

  環境の変化を監視するために時間とともに温度読み取りを記録します。

* **温度制御デバイス**：

  温度読み取りを使用してファンやヒーターを制御します。

**まとめ**

このレッスンでは、Raspberry Pi Picoを使用してサーミスタで温度を測定する方法を学びました。電圧分割を作成し、ベータ方程式を使用してアナログ値を読み取り、抵抗を計算し、摂氏および華氏で温度を決定しました。

