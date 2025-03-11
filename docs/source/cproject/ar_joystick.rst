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

.. _ar_joystick:

4.1 ジョイスティックの値を読み取る
===================================

このレッスンでは、 **joystick** を Raspberry Pi Pico 2 に接続し、アナログ値の取得とボタン入力の検出方法を学びます。 ジョイスティックは、X軸（左右）、Y軸（上下）の 2 軸の移動を検知できる入力デバイスで、 さらに押し込むことで Z 軸のボタン機能も持っています。

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
        - :ref:`cpn_resistor`  
        - 1 (10KΩ)  
        - |link_resistor_buy|  
    *   - 6  
        - :ref:`cpn_joystick`  
        - 1  
        -  

**ジョイスティックの仕組み**

一般的なジョイスティックモジュールは、2 つの ポテンショメーター（可変抵抗）を内蔵し、  
それぞれの軸方向のアナログ値を取得できます。

* **X軸ポテンショメーター**: 左右の動きを測定。  
* **Y軸ポテンショメーター**: 上下の動きを測定。  
* **Z軸（スイッチ）**: ジョイスティックを押し込むことで作動するデジタルボタン。  

X軸・Y軸のアナログ値を読み取ることで、ジョイスティックの位置を取得し、  
Z軸ボタンを使うことで押下を検出できます。

**回路図**

|sch_joystick|

ジョイスティックの **SW（スイッチ）ピン** は 10KΩ のプルアップ抵抗で接続されています。  
これにより、ボタンが押されていない状態で **安定した HIGH レベル** を保つことができます。  
プルアップ抵抗がない場合、スイッチが浮いた状態になり、不安定な値（0 または 1）が出力される可能性があります。

**配線図**

|wiring_joystick|

**コードの記述**

.. note::

    * ``4.1_toggle_the_joystick.ino`` を ``newton-lab-kit/arduino/4.1_toggle_the_joystick`` から開くことができます。  
    * または、このコードを **Arduino IDE** にコピーしてください。  
    * **Raspberry Pi Pico 2** ボードを選択し、適切なポートを設定して「Upload」をクリックしてください。  

.. code-block:: arduino

   // ピンの定義
   const int joystickX = 26;  // GP26 (ADC0) -> VRx
   const int joystickY = 27;  // GP27 (ADC1) -> VRy
   const int joystickSW = 22; // GP22 -> SW（ボタン）

   void setup() {
     // Initialize serial communication at 115200 baud
     Serial.begin(115200);

     // Initialize the joystick switch pin as input
     pinMode(joystickSW, INPUT_PULLUP);

   }

   void loop() {
     // X軸・Y軸のアナログ値を読み取る
     int xValue = analogRead(joystickX);
     int yValue = analogRead(joystickY);

     // ボタンの状態を読み取る
     int buttonState = digitalRead(joystickSW);

     // シリアルモニターにジョイスティックの値を表示
     Serial.print("X: ");
     Serial.print(xValue);
     Serial.print(" | Y: ");
     Serial.print(yValue);
     Serial.print(" | Button: ");
     Serial.println(buttonState == LOW ? "Pressed" : "Released");

     delay(500); // 500ミリ秒ごとに値を更新
   }

コードが実行されている間にシリアルモニターが開いているとき:

* ジョイスティックを異なる方向（左、右、上、下）に動かし、シリアルモニターでX軸とY軸の値がそれに応じて変化するのを観察する。
* ジョイスティックのボタン（Z軸）を押し、ボタンの状態が「Released」から「Pressed」へと変わるのを観察する。

**Understanding the Code**

#. ピンの定義:

   * ``joystickX`` と ``joystickY`` ：ジョイスティックのX軸とY軸に接続されたアナログピン。
   * ``joystickSW``：ジョイスティックのボタン（Z軸）に接続されたデジタルピン。

#. 初期設定関数:

   * デバッグとモニタリング用のシリアル通信を初期化する。
   * ジョイスティックのボタンピンを内部プルアップ抵抗を使用して入力として設定し、入力を安定させる。

   .. code-block:: arduino

        void setup() {
          Serial.begin(115200); // シリアル通信を115200ボーで初期化
          pinMode(joystickSW, INPUT_PULLUP); // プルアップ抵抗を使用してジョイスティックのボタンを入力に設定
        }
  
#. ``loop()`` 関数:

   * アナログ値の読取:
       
     ジョイスティックのX軸とY軸の現在位置を読取る。値の範囲は0から1023で、これはアナログ電圧レベルに対応する。
   
     .. code-block:: arduino
   
           int xValue = analogRead(joystickX);
           int yValue = analogRead(joystickY);
       
   * ボタン状態の読取:
       
     ジョイスティックのボタンの状態を読取る。 ``LOW`` は押された状態を、 ``HIGH`` は離された状態を示す。
   
     .. code-block:: arduino
   
           int buttonState = digitalRead(joystickSW);
       
   * シリアルモニターへの出力:
       
     シリアルモニターに現在のジョイスティックの位置とボタンの状態を出力してデバッグとモニタリングを行う。
   
     .. code-block:: arduino
   
       Serial.print("X: ");
       Serial.print(xValue);
       Serial.print(" | Y: ");
       Serial.print(yValue);
       Serial.print(" | Button: ");
       Serial.println(buttonState == LOW ? "Pressed" : "Released");

**Further Exploration**

* アナログ値のアクションへのマッピング:
  
  * ジョイスティックの位置に基づいてサーボやLED、その他のアクチュエータを制御する。

* デッドゾーンの実装:
  
  * ジョイスティックの中心位置周辺にデッドゾーンを設定し、わずかなジョイスティックの振動による意図しない動作を防ぐ。

* 他のセンサーとの組み合わせ:
  
  * 加速度計や距離センサーなど他のセンサーとジョイスティックを統合し、より複雑なインタラクションを作成する。

* ゲームコントローラーの作成:
  
  * 複数のジョイスティックとボタンを使用して、シンプルなゲームやロボット制御用のカスタムゲームコントローラーを構築する。

**Conclusion**

このレッスンでは、Raspberry Pi Picoにジョイスティックを接続し、X軸とY軸からアナログ値を読み取り、Z軸のボタン押下を検出する方法を学びました。このセットアップは、リモコン、ロボティクス、インタラクティブなインスタレーションなど、さまざまなプロジェクトの入力方法として使用できます。ジョイスティックの値を読み取り、解釈する方法を理解することで、応答性の高いダイナミックなアプリケーションを作成できます。
