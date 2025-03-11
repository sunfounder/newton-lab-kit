.. note:: 

    こんにちは！SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community（Facebook）へようこそ！Raspberry Pi、Arduino、ESP32に情熱を持つ皆さんと共に、さらに深く探求しましょう。

    **参加する理由は？**

    - **専門的なサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：技術的なヒントやチュートリアルを交換し、スキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行公開に早期アクセスができます。
    - **特別割引**：最新製品を独占的な割引価格で楽しむことができます。
    - **祭りのプロモーションとギフト**：ギブアウェイやホリデープロモーションに参加しましょう。

    👉 私たちと探索し、創造してみませんか？[|link_sf_facebook|]をクリックして今日から参加しましょう！

.. _ar_ultrasonic:

6.1 超音波センサーを用いた距離測定
================================================

このレッスンでは、Raspberry Pi Pico 2を使用して **超音波センサーモジュール** で物体までの距離を測定する方法を学びます。超音波センサーは、ロボティクスや自動化システムで物体検出や距離測定によく使用されます。

**必要なもの**

このプロジェクトには以下のコンポーネントが必要です。

全てのキットを購入するのが便利です。リンクはこちらです：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名称
        - このキットに含まれるアイテム
        - リンク
    *   - Newton Lab Kit
        - 450+
        - |link_newton_lab_kit|

以下のリンクから個別に購入することもできます。

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
        - :ref:`cpn_ultrasonic`
        - 1
        - |link_ultrasonic_buy|

**超音波センサーの原理**

超音波センサーは、 **Trig** ピンから短い超音波パルスを発信し、 **Echo** ピンでそのエコーを聴取します。エコーが戻ってくるまでの時間を測定することで、音速を使用して物体までの距離を計算できます。

|ultrasonic_prin|

* **トリガーパルス**：Trigピンに10マイクロ秒の高いパルスを送ると測定が開始されます。
* **超音波バースト**：センサーは40kHzで8サイクルの超音波バーストを発します。
* **エコー受信**：Echoピンが高くなり、エコーが戻るまで高い状態が続きます。
* **時間測定**：Echoピンが高い状態を維持する時間を測定することで、距離を計算できます。

**回路図**

|sch_ultrasonic|

**配線図**

|wiring_ultrasonic|

**コードの書き方**

超音波センサーをトリガーして、エコー時間を測定し、物体までの距離を計算するプログラムを書きます。距離はシリアルモニターに表示されます。

.. note::

   * ``6.1_ultrasonic.ino`` ファイルを ``newton-lab-kit/arduino/6.1_ultrasonic`` から開くことができます。
   * または、このコードを **Arduino IDE** にコピーしてください。
   * **Raspberry Pi Pico 2** ボードを選択し、適切なポートを設定した後、「Upload」をクリックしてください。

.. code-block:: arduino

    // 接続ピンの定義
    const int trigPin = 17;  // GPIO 17 -> Trig
    const int echoPin = 16;  // GPIO 16 -> Echo

    void setup() {
      // シリアル通信を115200ボーで初期化
      Serial.begin(115200);
    
      // センサーピンの初期化
      pinMode(trigPin, OUTPUT);
      pinMode(echoPin, INPUT);
    }

    void loop() {
      long duration;
      float distance;

// センサーをトリガーして、Trigを10マイクロ秒間HIGHに設定
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);

// Echoピンを読み取り、マイクロ秒単位の持続時間を返す
duration = pulseIn(echoPin, HIGH);

// 距離をセンチメートルで計算
distance = duration * 0.034 / 2;

// シリアルモニターに距離を出力
Serial.print("距離: ");
Serial.print(distance);
Serial.println(" cm");

delay(500); // 次の測定まで0.5秒間待機

コードアップロード後、シリアルモニターはセンチメートル単位で距離を表示するはずです。

.. code-block::

    Distance: 25.3 cm
    Distance: 24.8 cm
    Distance: 24.5 cm

センサーからさまざまな距離に物体を置いてください。
物体を近づけたり遠ざけたりして、距離読み取りの変化を観察してください。

**コードの理解**

#. 接続ピンの定義:

   * ``trigPin``: 超音波パルスを送信。
   * ``echoPin``: 超音波パルスのエコーを受信。

   .. code-block:: arduino

        const int trigPin = 17;  // GPIO 17 -> Trig
        const int echoPin = 16;  // GPIO 16 -> Echo

#. セットアップ機能:

   * **シリアル通信**: ピコとコンピュータ間のデバッグ用通信を可能にする。
   * **ピンモード**: ``Trig`` ピンを ``OUTPUT`` として設定し、 ``Echo`` ピンを ``INPUT`` として設定。

   .. code-block:: arduino

        void setup() {
          // シリアル通信を115200ボーで初期化
          Serial.begin(115200);

          // センサーピンを初期化
          pinMode(trigPin, OUTPUT);
          pinMode(echoPin, INPUT);
        }

#. ループ機能:

   * **センサーのトリガー**: ``Trig`` ピンを10マイクロ秒間 ``HIGH`` に設定して超音波パルスを送信。パルスの終了時に ``Trig`` ピンを ``LOW`` に設定。

     .. code-block:: arduino

        digitalWrite(trigPin, HIGH);
        delayMicroseconds(10);
        digitalWrite(trigPin, LOW);

   * **エコーの読み取り**: ``Echo`` ピンが ``HIGH`` の状態を保持する持続時間（マイクロ秒単位）を測定し、エコーが戻るまでの時間を示す。

     .. code-block:: arduino

        duration = pulseIn(echoPin, HIGH);

   * **距離の計算**: 時間を距離（cm/マイクロ秒）に変換。パルスの往復時間を考慮して2で割る。

     .. code-block:: arduino

        distance = duration * 0.034 / 2;

   * **シリアル出力**: 計算された距離をリアルタイムでシリアルモニターに出力。

     .. code-block:: arduino

        Serial.print("Distance: ");
        Serial.print(distance);
        Serial.println(" cm");

   * **遅延**: シリアルモニターへの出力過多を防ぎ、測定間に時間を設けるために500ミリ秒の遅延を追加。

**トラブルシューティング**

* 読み取り値が表示されない:

  * TrigピンとEchoピンが正しく接続されていることを確認してください。
  * センサーが電力を受け取っているか（VCCおよびGND接続）を確認してください。
  * シリアルモニターが正しいボーレートに設定されているか確認してください。

* 読み取り値が不正確:

  * コード内の計算が正しいか確認してください。
  * 環境に適した音速定数（0.034）が正しいか確認してください（湿度や温度が音速に影響する可能性があります）。

* センサーの干渉:

  * 超音波パルスを妨げる可能性のある障害物や反射面がないか確認してください。
  * 誤った読み取りを引き起こす可能性のある他の超音波デバイスの近くにセンサーを置かないようにしてください。


**さらなる探求**

* LEDまたはディスプレイとの統合:

  * 複数のLEDを使用して視覚的な距離指示器を作成してください。
  * 7セグメントまたはLCDディスプレイを統合して、距離を数値で表示してください。

* 接近警報システムの作成:

  物体が非常に近いときに警報を鳴らすように、しきい値を設定してください。

* 簡易障害物回避ロボットの構築:

  超音波センサーを利用して障害物を検出し、それを回避しながらナビゲートしてください。

**結論**

このレッスンでは、ラズベリーパイ・ピコと超音波センサーモジュールを使用して物体までの距離を測定する方法を学びました。超音波パルスをトリガーし、エコー時間を測定することで、近くの物体の距離を正確に判定することができます。このプロジェクトは、ロボティクス、オートメーション、インタラクティブシステムにおけるより複雑なアプリケーションの基盤として役立ちます。

