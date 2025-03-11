.. note::

    こんにちは！SunFounder Raspberry Pi & Arduino & ESP32 愛好者コミュニティ（Facebook）へようこそ！  
    Raspberry Pi、Arduino、ESP32 に関する知識を深め、仲間とともにものづくりを楽しみましょう。

    **なぜ参加するのか？**

    - **専門的なサポート**：購入後の問題や技術的な課題を、コミュニティメンバーやチームがサポート。  
    - **学びと共有**：ヒントやチュートリアルを交換し、スキルを向上。  
    - **最新情報の先行公開**：新製品の発表やプレビューをいち早くチェック。  
    - **特別割引**：最新製品を会員限定の特別価格で購入可能。  
    - **イベント & プレゼント企画**：プレゼントキャンペーンや季節ごとのプロモーションに参加可能。  

    👉 一緒にものづくりを楽しみませんか？[|link_sf_facebook|] をクリックして、今すぐ参加！  

.. _ar_dht11:

6.2 DHT11 を使った温度・湿度の測定
=======================================================

このレッスンでは、 **DHT11 温度・湿度センサー** を使用して、Raspberry Pi Pico 2 で環境データを取得する方法を学びます。 DHT11 は、低コストで扱いやすいデジタルセンサーであり、温度と湿度を測定し、キャリブレーション済みのデジタル信号を出力します。

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
        - :ref:`cpn_dht11`  
        - 1  
        - |link_dht22_buy|  


**DHT11 センサーの仕組み**

**DHT11** は、静電容量式湿度センサーとサーミスタを使用して、周囲の空気の温度と湿度を測定します。 データはデジタル信号として出力され、比較的簡単に扱えますが、データ取得には正確なタイミングが必要です。

* 温度範囲: 0–50°C（±2°C の精度）  
* 湿度範囲: 20–80% RH（±5% の精度）  
* サンプリングレート: 1Hz（1秒ごとに1回測定）

**回路図**

|sch_dht11|

**配線図**

|wiring_dht11|

**コードの記述**

このプログラムでは、DHT11 センサーから温度と湿度を取得し、シリアルモニターに表示します。

.. note::

    * ``6.2_dht11.ino`` を ``newton-lab-kit/arduino/6.2_dht11`` から開くことができます。  
    * または、このコードを **Arduino IDE** にコピーしてください。  
    * **Raspberry Pi Pico 2** ボードを選択し、適切なポートを設定して「Upload」をクリックしてください。  
    * ``DHT sensor library`` を使用するため、 **Library Manager** からインストールしてください。

      .. image:: img/lib_dht.png


.. code-block:: arduino

    #include <DHT.h>

    // 接続ピンの定義
    #define DHTPIN 16       // GPIO 16 -> DHT11 のデータピン
    #define DHTTYPE DHT11   // センサーの種類を定義

    // DHT オブジェクトの作成
    DHT dht(DHTPIN, DHTTYPE);

    unsigned long previousMillis = 0; // 最後に測定した時間
    const long interval = 2000;        // 測定間隔（ミリ秒）

    void setup() {
      // Initialize serial communication at 115200 baud
      Serial.begin(115200);
      Serial.println(F("DHT11 Sensor Test!"));

      // Initialize the DHT sensor
      dht.begin();
   
    }

    void loop() {
      unsigned long currentMillis = millis();

      // 指定した間隔ごとにセンサーを更新
      if (currentMillis - previousMillis >= interval) {
        previousMillis = currentMillis;

        // 湿度と温度の取得
        float humidity = dht.readHumidity();
        float temperatureC = dht.readTemperature();
        float temperatureF = dht.readTemperature(true);

        // 取得に失敗した場合の処理
        if (isnan(humidity) || isnan(temperatureC) || isnan(temperatureF)) {
          Serial.println(F("Failed to read from DHT sensor!"));
          return;
        }

        // 熱指数の計算
        float heatIndexC = dht.computeHeatIndex(temperatureC, humidity, false);
        float heatIndexF = dht.computeHeatIndex(temperatureF, humidity);

        // シリアルモニターに結果を表示
        Serial.print(F("Humidity: "));
        Serial.print(humidity);
        Serial.print(F("%  Temperature: "));
        Serial.print(temperatureC);
        Serial.print(F("°C "));
        Serial.print(temperatureF);
        Serial.print(F("°F  Heat index: "));
        Serial.print(heatIndexC);
        Serial.print(F("°C "));
        Serial.print(heatIndexF);
        Serial.println(F("°F"));
      }
    }

コードをアップロードすると、シリアルモニターに 2 秒ごとに温度と湿度が表示されます。

.. code-block::

    DHT11 Sensor Test!
    Humidity: 45.00%  Temperature: 25.00°C 77.00°F  Heat index: 25.00°C 77.00°F
    Humidity: 46.00%  Temperature: 25.50°C 78.00°F  Heat index: 25.50°C 78.00°F
    Humidity: 47.00%  Temperature: 26.00°C 79.00°F  Heat index: 26.00°C 79.00°F

* **湿度**: センサーをさまざまな湿度環境にさらし、測定値の変化を確認する。  
* **温度**: センサー周辺の温度を変化させ、測定結果の違いを観察する。  

**コードの解説**

#. ライブラリのインクルードと定数の定義

   * ``DHT.h``: DHT センサー用ライブラリをインクルードし、センサーとの通信を簡単にする。  
   * ``DHTPIN``: DHT11 のデータピンを接続する GPIO ピンを指定。  
   * ``DHTTYPE``: 使用する DHT センサーの種類（この場合は DHT11）を定義。  

   .. code-block:: arduino

        #include <DHT.h>
        #define DHTPIN 16       // GPIO 16 -> DHT11 のデータピン
        #define DHTTYPE DHT11    // センサーの種類を定義

#.  ``DHT``  オブジェクトの作成

   指定したデータピンとセンサータイプを用いて ``DHT`` オブジェクトを初期化。

   .. code-block:: arduino

        DHT dht(DHTPIN, DHTTYPE);

#. セットアップ関数

   * **シリアル通信の開始**: デバッグやデータ表示のため、シリアル通信を初期化。  
   * **DHT センサーの初期化**: 温度・湿度データの読み取り準備。  

   .. code-block:: arduino

        void setup() {
          // Initialize serial communication at 115200 baud
          Serial.begin(115200);
          Serial.println(F("DHT11 Sensor Test!"));

          // Initialize the DHT sensor
          dht.begin();
        }

#. ループ関数

   * ``millis()`` を用いたタイミング制御:

     ブロッキングを回避し、2秒ごと（2000ms）にセンサーを読み取る。

     .. code-block:: arduino

        if (currentMillis - previousMillis >= interval) {
          previousMillis = currentMillis;
          ...
        }

   * センサーのデータ取得:

     * ``dht.readHumidity()``: 現在の湿度を読み取る。  
     * ``dht.readTemperature()``: 摂氏（℃）の温度を取得。  
     * ``dht.readTemperature(true)``: 華氏（℉）の温度を取得。  

   * エラーハンドリング:

     測定値が取得できない場合（NaN を返した場合）、エラーメッセージを表示。

     .. code-block:: arduino

        if (isnan(humidity) || isnan(temperatureC) || isnan(temperatureF)) {
          Serial.println(F("Failed to read from DHT sensor!"));
          return;
        }

   * 熱指数の計算:

     * ``dht.computeHeatIndex(temperatureC, humidity, false)``: 摂氏の熱指数を計算。  
     * ``dht.computeHeatIndex(temperatureF, humidity)``: 華氏の熱指数を計算。  

   * データの表示:

     湿度・温度（摂氏/華氏）・熱指数をシリアルモニターに出力。

     .. code-block:: arduino

        Serial.print(F("Humidity: "));
        Serial.print(humidity);
        Serial.print(F("%  Temperature: "));
        Serial.print(temperatureC);
        Serial.print(F("°C "));
        Serial.print(temperatureF);
        Serial.print(F("°F  Heat index: "));
        Serial.print(heatIndexC);
        Serial.print(F("°C "));
        Serial.print(heatIndexF);
        Serial.println(F("°F"));

**トラブルシューティング**

* 測定値が表示されない場合:

  * 配線を再確認する。  
  * DHT11 センサーに正しく電源が供給されていることを確認。  
  * コード内の GPIO ピン番号が正しく設定されているか確認。  

* 測定値が異常な場合:

  * センサーが故障していないか確認する。  
  * DHT11 のデータシートを確認し、適切なタイミングでデータを取得しているか検証する。  

* センサーの干渉:

  * 他の電子機器の近くに設置すると測定値が影響を受ける可能性があるため、配置を調整する。  
  * センサーの測定面に障害物がないか確認する。  

**さらに応用するには？**

* ディスプレイとの連携:

  LCD や OLED ディスプレイを使用し、シリアルモニターなしで温度・湿度を表示する。

* 警告システムの作成:

  一定の温度や湿度を超えた際に、ブザーや LED で警告を発するシステムを実装。

* 他のセンサーと組み合わせる:

  DHT11 をモーションセンサーや照度センサーと組み合わせ、環境監視システムを構築。

* 気象ステーションの作成:

  気圧センサー、雨量計、風速計などを追加し、簡易的な天気観測システムを構築。

**まとめ**

このレッスンでは、Raspberry Pi Pico と DHT11 を使用して温度・湿度を測定し、その値を表示する方法を学びました。  
DHT ライブラリを活用することで、環境センシングを簡単にプロジェクトへ統合できます。  
さらに、LED インジケーターを追加することで、センサーの測定結果を視覚的にフィードバックし、システムのインタラクティブ性を向上させることができます。
