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

.. _ar_rgb:

2.4 カラフルなライト
=======================

このレッスンでは、RGB LEDとRaspberry Pi Pico 2を使用してさまざまな色を作成する方法を学びます。  
赤・緑・青の光の強さを調整することで、幅広い色を表現できます。この仕組みは **加法混色** の原理に基づいています。

**加法混色とは？**

加法混色とは、異なる色の光を組み合わせて新しい色を作る方法です。赤・緑・青の光を異なる割合で混ぜることで、可視光のあらゆる色を再現できます。例えば：

* **赤 + 緑 = 黄**
* **赤 + 青 = マゼンタ**
* **緑 + 青 = シアン**
* **赤 + 緑 + 青 = 白**

|img_rgb_mix|

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
        - :ref:`cpn_resistor`
        - 3(1-330Ω, 2-220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_rgb`
        - 1
        - |link_rgb_led_buy|


**回路図**

|sch_rgb|

PWMピン（GP13、GP14、GP15）が、それぞれRGB LEDの赤・緑・青のピンを制御し、共通カソードピンをGNDに接続します。  
各ピンのPWM値を変化させることで、異なる色を表示できます。


**配線図**

|img_rgb_pin|

RGB LEDには4本のピンがあります。最も長いピンは共通カソードピン（通常GNDに接続）で、その左隣が赤、その右に緑と青のピンがあります。

赤色LEDは、同じ電流でも他の色より明るく発光するため、より高い抵抗を使用します。

|wiring_rgb|


**コードを書いてみよう**

ペイントなどの描画ソフトで好きな色を選び、RGB LEDで再現できます。

.. note::

   * ``2.4_colorful_light.ino`` を ``newton-lab-kit/arduino/2.4_colorful_light`` から開くことができます。
   * または以下のコードを **Arduino IDE** にコピーしてください。
   * **Raspberry Pi Pico 2** ボードを選択し、適切なポートを設定して「Upload」をクリックしてください。

.. code-block:: Arduino

   // RGB LED に接続する GPIO ピンを定義
   const int redPin = 13;   // 赤ピン
   const int greenPin = 14; // 緑ピン
   const int bluePin = 15;  // 青ピン

   void setup() {
     // RGB LED の各ピンを出力として設定
     pinMode(redPin, OUTPUT);
     pinMode(greenPin, OUTPUT);
     pinMode(bluePin, OUTPUT);
   }

   // 色を設定する関数
   void setColor(unsigned char red, unsigned char green, unsigned char blue) {
     analogWrite(redPin, red);
     analogWrite(greenPin, green);
     analogWrite(bluePin, blue);
   }

    void loop() { 
     // 赤色
     setColor(255, 0, 0);
     delay(1000);

     // 緑色
     setColor(0, 255, 0);
     delay(1000);

     // 青色
     setColor(0, 0, 255);
     delay(1000);

     // 黄色（赤 + 緑）
     setColor(255, 255, 0);
     delay(1000);

     // シアン（緑 + 青）
     setColor(0, 255, 255);
     delay(1000);

     // マゼンタ（赤 + 青）
     setColor(255, 0, 255);
     delay(1000);

     // 白色（赤 + 緑 + 青）
     setColor(255, 255, 255);
     delay(1000);

     // 消灯
     setColor(0, 0, 0);
     delay(1000);
  }

コードをアップロードすると、RGB LEDは赤、緑、青、黄、シアン、マゼンタ、白の順に点灯し、最後に消灯します。各色は1秒間表示されます。

**コードの理解**

#. ピンの定義

   RGB LEDに接続されるGPIOピンを定義します。

   .. code-block:: Arduino

        const int redPin = 13;
        const int greenPin = 14;
        const int bluePin = 15;

#. ピンの初期化

   RGB LEDのピンを出力として設定します。

   .. code-block:: Arduino

        void setup() {
          pinMode(redPin, OUTPUT);
          pinMode(greenPin, OUTPUT);
          pinMode(bluePin, OUTPUT);
        }

#. 色の設定

   ``setColor`` 関数を使用し、PWM（パルス幅変調）を利用して色の明るさを調整します。

   .. code-block:: Arduino

        void setColor(unsigned char red, unsigned char green, unsigned char blue) {
          analogWrite(redPin, red);
          analogWrite(greenPin, green);
          analogWrite(bluePin, blue);
        }

#. 色のループ表示

   ``loop()`` 関数内で ``setColor()`` を呼び出し、異なる色を順番に表示し、それぞれ1秒間の遅延を加えます。

   .. code-block:: Arduino

        void loop() {
          // 赤色
          setColor(255, 0, 0);
          delay(1000);
          ...

          // 消灯
          setColor(0, 0, 0);
          delay(1000);
        }

**色の実験**

``setColor()`` のパラメータを変更することで、自由に色を作成できます。各値は0（オフ）から255（最大輝度）の範囲で調整できます。

* オレンジ: setColor(255, 165, 0);
* 紫: setColor(128, 0, 128);

特定の色のRGB値を知りたい場合は、カラーピッカーや **Paint** などのツールを使用してください。

**まとめ**

このレッスンでは、Raspberry Pi Picoを使用してRGB LEDを制御し、赤・緑・青の光を組み合わせてさまざまな色を作成する方法を学びました。  
この知識は、LEDディスプレイ、ムードライト、色制御が必要なプロジェクトに応用できます。
