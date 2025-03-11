.. note::

    こんにちは、FacebookでSunFounder Raspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Raspberry Pi、Arduino、ESP32の更なる深掘りを共にしましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームのサポートを受けて、アフターサービスの問題や技術的な課題を解決します。
    - **学びと共有**：スキル向上のためのヒントやチュートリアルを交換します。
    - **独占的プレビュー**：新製品のアナウンスやちら見せに早期アクセスできます。
    - **特別割引**：最新製品の独占割引を楽しめます。
    - **祭りのプロモーションとギフトの提供**：ギフトや休日のプロモーションに参加します。

    👉 私たちと一緒に探索し、創造しませんか？[|link_sf_facebook|]をクリックして今日から参加しましょう！

.. _ar_neopixel:

3.3 RGB LEDストリップの制御
===========================================================

このレッスンでは、Raspberry Pi Pico 2とMicroPythonを使用して **RGB LEDストリップ** （具体的にはWS2812タイプ）を制御する方法を学びます。

WS2812は、制御回路とRGBチップを5050サイズのLEDパッケージに統合したスマートLEDです。各LEDは独自の内蔵コントローラを持っており、単一のデータラインを使用して個々のLEDを個別に制御できます。これにより、ストリップ上の各LEDの色と明るさを独立して変更できます。


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
        - 数本
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_ws2812`
        - 1
        - |link_ws2812_buy|

**回路図**

|sch_ws2812|


**配線図**

|wiring_ws2812|

電流の引き込みに注意してください。PicoのVBUSピンは少数のLED（例えば8個）に電力を供給することができますが、より多くのLEDを使用する場合は、Picoの過負荷を防ぐために外部電源が必要になる場合があります。


**コードの書き方**

.. note::

    * ``3.3_rgb_led_strip.ino`` ファイルを ``newton-lab-kit/arduino/3.3_rgb_led_strip`` から開くことができます。
    * またはこのコードを **Arduino IDE** にコピーしてください。
    * **Raspberry Pi Pico 2** ボードと正しいポートを選択し、「Upload」をクリックしてください。
    * ここでは ``Adafruit_NeoPixel`` ライブラリを使用しています。 **ライブラリマネージャー** からインストールできます。

      .. image:: img/lib_neopixel.png

.. code-block:: arduino

  #include <Adafruit_NeoPixel.h>

  #define PIXEL_PIN    0    // ネオピクセルが接続されているデジタルIOピン
  #define PIXEL_COUNT  8    // ネオピクセルの数

  // NeoPixelストリップオブジェクトを宣言
  Adafruit_NeoPixel strip(PIXEL_COUNT, PIXEL_PIN, NEO_GRB + NEO_KHZ800);

  void setup() {
    strip.begin();           // NeoPixelライブラリを初期化
    strip.show();            // できるだけ早く全てのピクセルをOFFにする
  }

  void loop() {
    // 各ピクセルの色を設定
    strip.setPixelColor(0, strip.Color(255, 0, 0));   // 赤
    strip.setPixelColor(1, strip.Color(0, 255, 0));   // 緑
    strip.setPixelColor(2, strip.Color(0, 0, 255));   // 青
    strip.setPixelColor(3, strip.Color(255, 255, 0)); // 黄色
    strip.setPixelColor(4, strip.Color(0, 255, 255)); // シアン
    strip.setPixelColor(5, strip.Color(255, 0, 255)); // マゼンタ
    strip.setPixelColor(6, strip.Color(255, 255, 255)); // 白
    strip.setPixelColor(7, strip.Color(0, 0, 0));     // 消灯

    strip.show();  // ストリップを更新して新しい内容を表示
    delay(1000);   // 1秒待つ

    // 全てのピクセルを消灯
    strip.clear();
    strip.show();
    delay(1000);   // 1秒待つ
  }

コードをアップロードした後、LEDが異なる色で光り、1秒間点灯した後、1秒間消灯します。

**コードの理解**

#. ライブラリを含める：

   .. code-block:: arduino
    
      #include <Adafruit_NeoPixel.h>

#. 定数を定義する：

   * ``PIXEL_PIN``：LEDストリップのデータ入力に接続されたGPIOピン（GP0）。
   * ``PIXEL_COUNT``：ストリップ上のLEDの数。

#. ストリップの初期化：

   ``NEO_GRB + NEO_KHZ800``：色順と通信速度を指定します。

   .. code-block:: arduino
    
      Adafruit_NeoPixel strip(PIXEL_COUNT, PIXEL_PIN, NEO_GRB + NEO_KHZ800);
      
#. ``setup()`` 関数内：

   * ``strip.begin()``：NeoPixelライブラリを初期化します。
   * ``strip.show()``：全てのピクセルがオフであることを確認します。

#. ``loop()`` 関数内：

   * ``strip.setPixelColor(index, color)``：特定のピクセルの色を設定します。
   * ``strip.Color(r, g, b)``：赤、緑、青の成分（0-255）から24ビットの色値を生成します。
   * ``strip.show()``：更新された色データをストリップに送信します。
   * ``strip.clear()``：メモリ内のピクセルデータをクリアします（次の ``show()`` でピクセルがオフになります）。

**応用例：カラーワイプアニメーション**

各LEDが順番に点灯するシンプルなアニメーションを作成しましょう。

* ``colorWipe()`` 関数：指定された色で各ピクセルを順番に点灯させます。
* 異なる色で ``colorWipe()`` を呼び出してアニメーションを作成します。

.. code-block:: arduino
    
  #include <Adafruit_NeoPixel.h>

  #define PIXEL_PIN    0
  #define PIXEL_COUNT  8

  Adafruit_NeoPixel strip(PIXEL_COUNT, PIXEL_PIN, NEO_GRB + NEO_KHZ800);

  void setup() {
    strip.begin();
    strip.show(); // 全ピクセルをオフに初期化
  }

  void loop() {
    colorWipe(strip.Color(255, 0, 0), 50); // 赤
    colorWipe(strip.Color(0, 255, 0), 50); // 緑
    colorWipe(strip.Color(0, 0, 255), 50); // 青
  }

  void colorWipe(uint32_t color, int wait) {
    for(int i=0; i<strip.numPixels(); i++) {
      strip.setPixelColor(i, color);
      strip.show();
      delay(wait);
    }
  }

コードをアップロードした後、LEDは赤、緑、青と順番に点灯し、各色が1秒間点灯します。

**応用例：レインボーサイクルアニメーション**

* ``rainbowCycle()`` 関数：全ピクセルを通して虹色のサイクルを作成します。
* ネストされたループにより、色の滑らかな遷移を実現します。
* ``Wheel()`` 関数：0から255の位置で虹色を生成します。

.. code-block:: arduino
    
  #include <Adafruit_NeoPixel.h>

  #define PIXEL_PIN    0
  #define PIXEL_COUNT  8

  Adafruit_NeoPixel strip(PIXEL_COUNT, PIXEL_PIN, NEO_GRB + NEO_KHZ800);

  void setup() {
    strip.begin();
    strip.show(); // 全ピクセルをオフに初期化
  }

  void loop() {
    rainbowCycle(20); // ステップごとに20msの遅延でレインボーサイクルを実行
  }

  void rainbowCycle(int wait) {
    uint16_t i, j;

    for(j=0; j<256*5; j++) { // 色の輪を5サイクル
      for(i=0; i< strip.numPixels(); i++) {
        strip.setPixelColor(i, Wheel(((i * 256 / strip.numPixels()) + j) & 255));
      }
      strip.show();
      delay(wait);
    }
  }

  // 0から255の値を入力して色の値を取得します。
  // 色は r - g - b への遷移を経て r に戻ります。
  uint32_t Wheel(byte WheelPos) {
    if(WheelPos < 85) {
      return strip.Color(WheelPos * 3, 255 - WheelPos * 3, 0);
    } else if(WheelPos < 170) {
      WheelPos -= 85;
      return strip.Color(255 - WheelPos * 3, 0, WheelPos * 3);
    } else {
      WheelPos -= 170;
      return strip.Color(0, WheelPos * 3, 255 - WheelPos * 3);
    }
  }

コードをアップロードすると、LEDストリップが滑らかに色を変えながら虹色にサイクル表示されます。

**さらなる探求**

* カスタムアニメーションの作成：

  * 異なる色やアニメーションを試してみましょう。
  * 複数のアニメーション機能を組み合わせてみましょう。

* センサーに応答する：

  センサーからの入力を使用してLEDの色やパターンを変更します。

* ビジュアライザーの構築：

  音声入力に基づいてLEDを変化させる音楽ビジュアライザーを作成します。

**電力に関する考慮事項**

* 電流の引き出し：

  * 各LEDは全輝度で最大60mAを消費します。
  * 8つのLEDでは最大で480mAになります。
  * 電源が必要な電流を供給できることを確認してください。

* 外部電源：

  * 大きなストリップや高い輝度には、外部の5V電源を使用します。
  * 外部電源のグラウンドをPicoのグラウンドに接続してください。

**結論**

このレッスンでは、Raspberry Pi PicoとAdafruit NeoPixelライブラリを使用してWS2812 RGB LEDストリップを制御する方法を学びました。個々のピクセルを操作することで、プロジェクトに魅力的な視覚効果を作り出すことができます。

