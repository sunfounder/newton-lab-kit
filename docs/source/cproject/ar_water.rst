.. note::

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！ラズベリーパイ、アルドゥイーノ、ESP32について、同じ趣味を持つ仲間ともっと深く掘り下げましょう。

    **なぜ参加するのか？**

    - **エキスパートサポート**: コミュニティやチームからのサポートで、購入後の問題や技術的な課題を解決。
    - **学びと共有**: スキル向上のためのヒントやチュートリアルを交換。
    - **独占プレビュー**: 新製品の発表や先行情報をいち早く入手。
    - **特別割引**: 最新製品の独占的な割引を楽しむ。
    - **祭りのプロモーションとギブアウェイ**: ギブアウェイや休日のプロモーションに参加。

    👉 私たちと一緒に探求し、創造してみませんか？クリックして今すぐ参加！[|link_sf_facebook|]

.. _ar_water:

2.14 水位検出
============================

このレッスンでは、Raspberry Pi Pico 2を使用して水の存在を検出したり、水位を測定する方法を学びます。このセンサーは、降雨検出、水位モニタリング、液体漏れアラートに関連するプロジェクトで一般的に使用されます。

**水センサーの仕組み**

水センサーには、水滴を検出したり水の量を測定したりするための露出した並列ワイヤートレースのシリーズがあります。水がこれらのトレースに接触すると、センサーはアナログ信号を出力します。センサーに接触する水の量が多いほど、出力値は高くなり、Raspberry Pi Pico 2のアナログ・デジタル変換器（ADC）で読み取ることができます。

|img_water_sensor|

* センサーを水に完全に浸さないでください。露出したトレースのあるエリアのみが水に接触するようにしてください。
* 電源を入れた状態で湿度の高い環境でセンサーを使用すると、プローブの腐食が早まる可能性があるため、測定時のみセンサーに電力を供給することをお勧めします。

**必要なもの**

このプロジェクトには、以下のコンポーネントが必要です。

キット全体を購入するのが確かに便利です。こちらがリンクです：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - このキットのアイテム
        - リンク
    *   - Newton Lab Kit	
        - 450以上
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
        - Micro USB Cable
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
        - :ref:`cpn_water_level`
        - 1
        - 


**回路図**

|sch_water|


**配線図**


|wiring_water|


**コードの書き方**

.. note::

   * ``newton-lab-kit/arduino/2.14_feel_the_water_level`` から ``2.14_feel_the_water_level.ino`` ファイルを開くことができます。
   * または、このコードを **Arduino IDE** にコピーします。
   * **Raspberry Pi Pico 2** ボードと正しいポートを選択し、「アップロード」をクリックします。

.. code-block:: arduino

   const int waterSensorPin = 28;  // Water sensor connected to GP28 (ADC2)

   void setup() {
     Serial.begin(115200);  // シリアルモニターを初期化
   }

   void loop() {
     // 水センサーからアナログ値を読み取る
     int sensorValue = analogRead(waterSensorPin);
     // シリアルモニターにセンサー値を表示
     Serial.print("水センサー値: ");
     Serial.println(sensorValue);
     delay(500);  // 再読み取り前に0.5秒待つ
   }

コードをアップロードした後、シリアルモニターを開くと、水センサーからのアナログ値を表す一連の数字が表示されるはずです。

* センサーが乾燥している場合、センサー値は低い（0に近い）はずです。
* センサーを水にゆっくりと浸し始めます。センサーのトレースがより多く水に浸かるにつれて、センサー値は増加するはずです。

**コードの理解**

#. センサーピンの定義:

   ``waterSensorPin`` をアナログ入力に接続されているGPIO 28に割り当てます。

   .. code-block:: arduino

      const int waterSensorPin = 28;  // Water sensor connected to GP28 (ADC2)


#. シリアル通信の初期化:

   シリアル通信を開始し、シリアルモニターにメッセージを表示できるようにします。

   .. code-block:: arduino

      Serial.begin(115200);

#. アナログ値の読み取り:

   ``waterSensorPin`` でアナログ電圧を読み取り、0から1023の間の値（10ビットADC用）を返します。

   .. code-block:: arduino

      int sensorValue = analogRead(waterSensorPin);

#. センサー値の出力:

   センサー値をシリアルモニターに出力します。

   .. code-block:: arduino

      Serial.print("Water Sensor Value: ");
      Serial.println(sensorValue);

#. 遅延の追加:

   次の読み取り前に500ミリ秒待ちます。

   .. code-block:: arduino

      delay(500);


**水センサーをデジタルセンサーとして使用する**

アナログ入力モジュールをデジタルセンサーとして使用するために、閾値を設定することができます。

* 閾値の決定:

  * センサーが乾燥しているときのセンサー値を読み取ります。
  * この値をベースラインとして使用します（例：乾燥値が約100の場合）。

* コードの修正:

   .. code-block:: arduino

      const int waterSensorPin = 28;  // Water sensor connected to GP28 (ADC2)
      const int threshold = 500;      // 閾値を設定

      void setup() {
        Serial.begin(115200);  // シリアルモニターを初期化
      }

      void loop() {
        // 水センサーからアナログ値を読み取る
        int sensorValue = analogRead(waterSensorPin);

        // センサー値が閾値を超えるか確認
        if (sensorValue > threshold) {
          Serial.println("Water Detected!");
        } else {
          Serial.println("No Water Detected.");
        }
        delay(500);  // 再読み取り前に0.5秒待つ
      }

センサーを潜在的な水漏れエリア近くに設置してください。
水がセンサーに接触すると、シリアルモニターに「水検出！」と表示されるはずです。

**安全上の注意**

* 短絡を避ける:

  * 接続が確実であり、センサーが露出したトレースを超えて水に浸からないようにしてください。
  * Picoやその他の電子部品に水が接触しないようにしてください。

* 腐食防止:

  * 長時間水に浸したままセンサーに電力を供給しないでください。
  * 使用後はセンサーをよく乾燥させて腐食を防いでください。


**さらなる探求**

* 水位アラーム:

  水が検出されたときに警告するために、ブザーやLEDを追加してください。

* 自動ポンプ制御:

  水位に基づいてポンプをオンまたはオフにするためにセンサーを使用してください。

* データロギング:

  分析のために時間をかけて水位の変化を記録してください。

**結論**

このレッスンでは、Raspberry Pi Picoを使用して水の存在を検出または水位を測定する方法を学びました。センサーからのアナログ値を読み取ることで、水位の変化をモニタリングし、プロジェクトに応じて適切に対応することができます。
