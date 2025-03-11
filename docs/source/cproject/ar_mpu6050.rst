.. note::

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について一緒にもっと深く探求しましょう。

    **なぜ参加するのか？**

    - **エキスパートサポート**：コミュニティやチームの支援を受けて、販売後の問題や技術的な課題を解決します。
    - **学習と共有**：スキルアップのためのヒントやチュートリアルを交換します。
    - **独占的なプレビュー**：新製品の発表や先行公開に早期アクセスが可能です。
    - **特別な割引**：最新製品に対する独占的な割引を楽しみます。
    - **祭りのプロモーションとギブアウェイ**：ギブアウェイや休日のプロモーションに参加します。

    👉 私たちと一緒に探索し、創造してみませんか？[|link_sf_facebook|]をクリックして今日から参加しましょう！

.. _ar_mpu6050:

6.3 MPU-6050から読み取る
===============================

このレッスンでは、Raspberry Pi Pico 2を使用して **MPU-6050** 6軸モーショントラッキングセンサーとのインターフェースの方法を学びます。MPU-6050は3軸ジャイロスコープと3軸加速度計を組み合わせており、I2C通信プロトコルを介して生のセンサーデータを提供します。

**必要なもの**

このプロジェクトには、以下のコンポーネントが必要です。

全キットを購入するのが便利です。リンクはこちらです：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - このキットのアイテム
        - リンク
    *   - Newton Lab Kit	
        - 450以上
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
        - Micro USBケーブル
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - 複数
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_mpu6050`
        - 1
        - 

**MPU-6050センサーについて**

MPU-6050センサーは、ドローン、ロボティクス、ゲームデバイスなど、動きの追跡と向きの検出が必要なプロジェクトで広く使用されています。

* **加速度計**：X、Y、Z軸に沿った加速力を測定します。これには重力加速度も含まれるため、センサーの傾きや向きを判定することができます。
* **ジャイロスコープ**：X、Y、Z軸を中心とした回転速度を測定し、センサーがどれだけ速く回転しているかの情報を提供します。

**回路図**

|sch_mpu6050_ar|


**配線図**

|wiring_mpu6050_ar|

**コードの書き方**

MPU-6050センサーを初期化し、加速度とジャイロスコープのデータを読み取り、値をシリアルモニターに表示するプログラムを書きます。

.. note::

    * ``6.3_6axis_motion_tracking.ino`` ファイルを ``newton-lab-kit/arduino/6.3_6axis_motion_tracking`` から開くことができます。
    * またはこのコードを **Arduino IDE** にコピーしてください。
    * **Raspberry Pi Pico 2** ボードと正しいポートを選択し、「Upload」をクリックしてください。
    * ここでは ``Adafruit MPU6050`` ライブラリを使用しています。 **ライブラリマネージャー** からインストールできます。

      .. image:: img/lib_mpu6050.png

.. code-block:: arduino

    #include <Adafruit_MPU6050.h>
    #include <Wire.h>

    // MPU6050オブジェクトを作成
    Adafruit_MPU6050 mpu;

    void setup(void) {
      // シリアル通信を初期化
      Serial.begin(115200);

      Serial.println("Adafruit MPU6050 test!");

      // MPU6050を初期化する試み
      if (!mpu.begin()) {
        Serial.println("Failed to find MPU6050 chip");
        while (1) {
          delay(10);
        }
      }
      Serial.println("MPU6050 Found!");

      // 加速度計の範囲を設定
      mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
      Serial.print("Accelerometer range set to: ");
      switch (mpu.getAccelerometerRange()) {
        case MPU6050_RANGE_2_G:
          Serial.println("+-2G");
          break;
        case MPU6050_RANGE_4_G:
          Serial.println("+-4G");
          break;
        case MPU6050_RANGE_8_G:
          Serial.println("+-8G");
          break;
        case MPU6050_RANGE_16_G:
          Serial.println("+-16G");
          break;
      }

      // ジャイロスコープの範囲を設定
      mpu.setGyroRange(MPU6050_RANGE_500_DEG);
      Serial.print("Gyro range set to: ");
      switch (mpu.getGyroRange()) {
        case MPU6050_RANGE_250_DEG:
          Serial.println("+-250 deg/s");
          break;
        case MPU6050_RANGE_500_DEG:
          Serial.println("+-500 deg/s");
          break;
        case MPU6050_RANGE_1000_DEG:
          Serial.println("+-1000 deg/s");
          break;
        case MPU6050_RANGE_2000_DEG:
          Serial.println("+-2000 deg/s");
          break;
      }

      // フィルタ帯域幅を設定
      mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);
      Serial.print("Filter bandwidth set to: ");
      switch (mpu.getFilterBandwidth()) {
        case MPU6050_BAND_260_HZ:
          Serial.println("260 Hz");
          break;
        case MPU6050_BAND_184_HZ:
          Serial.println("184 Hz");
          break;
        case MPU6050_BAND_94_HZ:
          Serial.println("94 Hz");
          break;
        case MPU6050_BAND_44_HZ:
          Serial.println("44 Hz");
          break;
        case MPU6050_BAND_21_HZ:
          Serial.println("21 Hz");
          break;
        case MPU6050_BAND_10_HZ:
          Serial.println("10 Hz");
          break;
        case MPU6050_BAND_5_HZ:
          Serial.println("5 Hz");
          break;
      }

      Serial.println("");
      delay(100);
    }

    void loop() {
      // 新しいセンサーイベントで読み取りを取得
      sensors_event_t a, g, temp;
      mpu.getEvent(&a, &g, &temp);

      // 加速度値を出力
      Serial.print("Acceleration X: ");
      Serial.print(a.acceleration.x);
      Serial.print(" m/s^2, Y: ");
      Serial.print(a.acceleration.y);
      Serial.print(" m/s^2, Z: ");
      Serial.print(a.acceleration.z);
      Serial.println(" m/s^2");

      // ジャイロスコープ値を出力
      Serial.print("Rotation X: ");
      Serial.print(g.gyro.x);
      Serial.print(" rad/s, Y: ");
      Serial.print(g.gyro.y);
      Serial.print(" rad/s, Z: ");
      Serial.print(g.gyro.z);
      Serial.println(" rad/s");

      delay(500); // 必要に応じて遅延を調整
    }


コードをアップロードした後、シリアルモニターは連続して加速度と回転値を表示します。

.. code-block::

    Adafruit MPU6050 test!
    MPU6050 Found!
    加速度計の範囲が設定されました: +-8G
    ジャイロ範囲が設定されました: +-500 deg/s
    フィルタ帯域幅が設定されました: 21 Hz

    加速度 X: 0.00 m/s^2, Y: 0.00 m/s^2, Z: 9.81 m/s^2
    回転 X: 0.02 rad/s, Y: -0.01 rad/s, Z: 0.00 rad/s
    加速度 X: 0.10 m/s^2, Y: 0.05 m/s^2, Z: 9.76 m/s^2
    回転 X: 0.15 rad/s, Y: -0.05 rad/s, Z: 0.02 rad/s

MPU-6050センサーモジュールをゆっくりと回転させたり動かしたりしてください。
動きに応じて加速度と回転値の変化を観察してください。

**コードの理解**

#. ライブラリを含む定義定数：

   * ``Adafruit_MPU6050.h``: MPU6050ライブラリを含め、センサーとのやり取りを容易にします。
   * ``Wire.h``: I2C通信ライブラリを含めます。
   * ``mpu``: MPU6050オブジェクトを作成し、センサーとのインタラクションを行います。

#. セットアップ関数：

   * MPU6050の初期化：
   
     MPU6050センサーの初期化を試みます。成功しない場合は、エラーメッセージを出力してプログラムを停止します。
   
     .. code-block:: arduino
   
         Serial.println("Adafruit MPU6050 test!");
   
         // MPU6050の初期化を試みる
         if (!mpu.begin()) {
           Serial.println("Failed to find MPU6050 chip");
           while (1) {
             delay(10);
           }
         }
         Serial.println("MPU6050 Found!");

   * 加速度計の範囲：
   
     加速度計の範囲を±8Gに設定し、現在の範囲を出力します。
   
     .. code-block:: arduino
   
         mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
         Serial.print("Accelerometer range set to: ");
         switch (mpu.getAccelerometerRange()) {
           case MPU6050_RANGE_2_G:
             Serial.println("+-2G");
             break;
            ...
           case MPU6050_RANGE_16_G:
             Serial.println("+-16G");
             break;
         }
   
   * ジャイロスコープの範囲：
   
     ジャイロスコープの範囲を±500度/秒に設定し、現在の範囲を出力します。
   
     .. code-block:: arduino
   
         mpu.setGyroRange(MPU6050_RANGE_500_DEG);
         Serial.print("Gyro range set to: ");
         switch (mpu.getGyroRange()) {
           case MPU6050_RANGE_250_DEG:
             Serial.println("+-250 deg/s");
             break;
            ...
           case MPU6050_RANGE_2000_DEG:
             Serial.println("+-2000 deg/s");
             break;
         }
   
   * フィルタ帯域幅の設定：
   
     フィルタ帯域幅を21Hzに設定してノイズを減らし、現在の設定を出力します。
   
     .. code-block:: arduino
   
         mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);
         Serial.print("Filter bandwidth set to: ");
         switch (mpu.getFilterBandwidth()) {
           case MPU6050_BAND_260_HZ:
             Serial.println("260 Hz");
             break;
            ...
           case MPU6050_BAND_5_HZ:
             Serial.println("5 Hz");
             break;
         }

#. ループ関数：

   * センサーデータの読み取り：
   
     * ``sensors_event_t a, g, temp;``: 加速度計、ジャイロスコープ、温度データを格納するイベントオブジェクトを作成します。
     * ``mpu.getEvent(&a, &g, &temp);``: 最新のセンサーデータを取得します。
   
     .. code-block:: arduino
   
         sensors_event_t a, g, temp;
         mpu.getEvent(&a, &g, &temp);
   
   * センサーデータの出力：
   
     * **加速度**：X、Y、Z軸に沿った加速度値をメートル毎秒二乗（m/s²）で出力します。
     * **回転**：X、Y、Z軸を中心としたジャイロスコープ値（回転速度）をラジアン毎秒（rad/s）で出力します。
   
     .. code-block:: Arduino
   
       // 加速度値を出力
       Serial.print("Acceleration X: ");
       Serial.print(a.acceleration.x);
       ...
       Serial.print(g.gyro.y);
       Serial.print(" rad/s, Z: ");
       Serial.print(g.gyro.z);
       Serial.println(" rad/s");


**トラブルシューティング**


* データが表示されない場合：


  * 全ての配線接続、特にI2Cライン（SCLとSDA）を確認してください。
  * MPU-6050センサーが電力（VCCとGND接続）を受け取っていることを確認してください。
  * コード内で正しいGPIOピンが定義されていることを確認してください。

* 読み取り値が正しくない場合：

  * MPU-6050センサーがブレッドボードに適切に装着されていることを確認してください。
  * センサーの範囲とフィルタ設定が希望するアプリケーションに合っていることを確認してください。
  * 配線に緩い接続やショートがないかチェックしてください。

* センサーの干渉：

  * センサーを他の電子機器の近くに置かないようにしてください。干渉の原因となる可能性があります。
  * センサーの動きを阻害する物理的な障害物がないことを確認してください。

**さらなる探求**

* 他のセンサーとの組み合わせ：

  MPU-6050をGPSモジュール、磁力計、その他のセンサーと統合して、包括的なトラッキングシステムを作成します。

* モーションベースのゲームコントローラーの構築：

  MPU-6050を使用して動きと向きを検出し、モーションコントロールされるゲームデバイスを作成できます。

* 自己バランスロボットの作成：

  加速度計とジャイロスコープのデータを利用して、ロボットアプリケーションでのバランスと安定性を維持します。

* センサーフュージョンアルゴリズムの実装：

  加速度計とジャイロスコープのデータを組み合わせて、カルマンフィルターや補完フィルターのようなアルゴリズムを使用して向きの角度を計算します。

**結論**

このレッスンでは、Raspberry Pi PicoとMPU-6050 6軸モーショントラッキングセンサーとのインターフェース方法を学びました。Adafruit MPU6050ライブラリを利用することで、加速度計とジャイロスコープのデータを簡単に取得し解釈でき、動きと向きに基づく幅広いアプリケーションが可能になります。オプションのLEDインジケーターは、センサーの読み取りに基づいた視覚的フィードバックを提供する簡単な方法を追加し、プロジェクトのインタラクティビティを高めます。

