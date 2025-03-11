.. note:: 

    こんにちは！SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community（Facebook）へようこそ！  
    ここでは、Raspberry Pi、Arduino、ESP32について、他の愛好家と一緒に深く学ぶことができます。

    **参加するメリット**

    - **専門的なサポート**：購入後の問題や技術的な課題を、コミュニティやチームの助けを借りて解決できます。
    - **学び＆共有**：ヒントやチュートリアルを交換し、スキルを向上させましょう。
    - **最新情報の先行公開**：新製品の発表やプレビューをいち早くチェックできます。
    - **特別割引**：最新製品を特別価格で購入できます。
    - **季節限定のプロモーション＆プレゼント企画**：キャンペーンやプレゼント企画に参加できます。

    👉 一緒に探求し、創造しませんか？今すぐ [|link_sf_facebook|] をクリックして参加しましょう！

.. _ar_servo:

3.7 サーボモーターのスイング
================================

このレッスンでは、 **サーボモーター** をRaspberry Pi Pico 2で制御する方法を学びます。サーボモーターは0°から180°の範囲で特定の角度に回転できる装置で、ラジコン玩具やロボットなど、精密な位置制御が求められる用途で広く使用されています。

それでは、サーボをスイングさせてみましょう！

**必要なもの**

このプロジェクトでは、以下のコンポーネントが必要です。 

すべてが揃ったキットを購入すると便利です。リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名称
        - このキットに含まれるアイテム
        - リンク
    *   - Newton Lab Kit
        - 450点以上
        - |link_newton_lab_kit|

また、以下のリンクから個別に購入することも可能です。

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - No.
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
        - :ref:`cpn_servo`
        - 1
        - |link_servo_buy|


**回路図**

|sch_servo|

**配線図**

|wiring_servo|

* オレンジの線は信号線で、GP15に接続。
* 赤の線はVCCで、VBUS（5V）に接続。
* 茶色の線はGNDで、GNDに接続。

サーボモーターは特に負荷がかかると比較的大きな電流を消費します。今回は小型サーボを軽負荷で使用するため、PicoのVBUSピンから給電可能ですが、大型サーボや複数のサーボを使用する場合は、外部電源を推奨します。

**サーボアームの取り付け**

* サーボの出力軸にアーム（ホーン）を取り付けます。
* 必要に応じて、付属の小さなネジで固定してください。

**コードを書いてみよう**

.. note::

   * ``3.7_swinging_servo.ino`` を ``newton-lab-kit/arduino/3.7_swinging_servo`` から開くことができます。
   * または以下のコードを **Arduino IDE** にコピーしてください。
   * **Raspberry Pi Pico 2** ボードを選択し、適切なポートを設定して「Upload」をクリックしてください。

.. code-block:: arduino

    #include <Servo.h>

    Servo myServo;  // サーボオブジェクトの作成

    void setup() {
      myServo.attach(15);  // GPIO 15 にサーボを接続
    }

    void loop() {
      // サーボを 0° から 180° まで動かす
      for (int angle = 0; angle <= 180; angle += 1) {
        myServo.write(angle);
        delay(15);  // 位置調整のために15ミリ秒待機
      }
      // サーボを 180° から 0° に戻す
      for (int angle = 180; angle >= 0; angle -= 1) {
        myServo.write(angle);
        delay(15);
      }
    }

コードをアップロードすると、サーボアームが0°から180°までスムーズにスイングし、再び0°に戻ります。  
もしサーボが動かない、または異常な動作をする場合は以下を確認してください。

* 配線が正しく接続されているか。
* サーボが適切に給電されているか。
* 機械的に動きを妨げる要因がないか。

**コードの理解**

#. ``Servo`` ライブラリのインクルード

   ``Servo`` ライブラリを読み込み、サーボ制御のための関数を使用できるようにします。

   .. code-block:: arduino

        #include <Servo.h>

#. ``Servo`` オブジェクトの作成

   ``Servo`` オブジェクト ``myServo`` を作成し、サーボを制御します。

   .. code-block:: arduino

        Servo myServo;

#. サーボのピンに接続

   myServo.attach(15); を使用して、GPIO 15 にサーボを接続します。

   .. code-block:: arduino

        myServo.attach(15);

#. サーボを動かす

   * 0°から180°まで1°ずつ動かしながら、delay(15) を入れてスムーズに回転させます。

   .. code-block:: arduino

        for (int angle = 0; angle <= 180; angle += 1) {
          myServo.write(angle);
          delay(15);
        }

   * 180°から0°まで逆方向に動かし、往復運動を作ります。

   .. code-block:: arduino

        for (int angle = 180; angle >= 0; angle -= 1) {
          myServo.write(angle);
          delay(15);
        }

**さらなる探求**

* 動作速度の調整  

  ``delay()`` の値を変更すると、サーボの動きを速くしたり遅くしたりできます。

* 特定の位置への移動 
  ``myServo.write(angle);`` を使用して、特定の角度に直接移動させることも可能です。

* インタラクティブな制御 

  ポテンショメーター（可変抵抗）を接続して、サーボの角度をリアルタイムで制御することもできます。

**まとめ**

このレッスンでは、Raspberry Pi PicoとServoライブラリを使用してサーボモーターを制御する方法を学びました。コードを調整することで、サーボを0°から180°の間で自由に動かすことができ、ロボットアームや精密制御が必要なプロジェクトに活用できます。
