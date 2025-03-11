.. note::

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について一緒に深く探求しましょう。

    **参加する理由**

    - **エキスパートサポート**：コミュニティやチームの支援を受けながら、販売後の問題や技術的な課題を解決します。
    - **学びと共有**：スキル向上のためのヒントやチュートリアルを交換します。
    - **独占プレビュー**：新製品の発表や先行公開に早期アクセスが可能です。
    - **特別割引**：最新製品の独占割引を楽しめます。
    - **祭りのプロモーションとギブアウェイ**：ギブアウェイや祝祭のプロモーションに参加します。

    👉 私たちと一緒に探索し、創造しませんか？[|link_sf_facebook|]をクリックして今日から参加しましょう！

.. _ar_led_bar:

2.2 レベルの表示
=============================

このレッスンでは、Raspberry Pi Pico 2を使用してLEDバーグラフを制御する方法を学びます。LEDバーグラフは、通常、音量、信号強度、またはその他の測定値などのレベルを表示するために使用される、一列に配列された10個のLEDで構成されています。LEDを順番に点灯させて、レベル表示効果を作り出します。

|img_led_bar_pin|


**必要なもの**

このプロジェクトには、以下のコンポーネントが必要です。

全キットを購入することは非常に便利です。こちらがリンクです：

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
        - :ref:`cpn_resistor`
        - 10(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led_bar`
        - 1
        - 

**回路図**

|sch_ledbar|

このプロジェクトでは、LEDバーグラフの10個のLEDがそれぞれRaspberry Pi Pico 2に接続されています。LEDのアノード（正極）はGPIOピンGP6からGP15に接続され、カソード（負極）は220Ωの抵抗を介してGND（グラウンド）ピンに接続されています。

**配線図**

|wiring_ledbar|

**コードの書き方**

.. note::

   * ファイル ``2.2_display_the_level.ino`` を ``newton-lab-kit/arduino/2.2_display_the_level`` から開くことができます。
   * またはこのコードを **Arduino IDE** にコピーしてください。
   * **Raspberry Pi Pico 2** ボードと正しいポートを選択し、「Upload」をクリックします。

.. code-block:: Arduino

    // LEDバーグラフに接続されたGPIOピンを定義
    const int ledPins[] = {6, 7, 8, 9, 10, 11, 12, 13, 14, 15};

    void setup() {
      // 各ピンを出力として初期化
      for (int i = 0; i < 10; i++) {
        pinMode(ledPins[i], OUTPUT);
      }
    }

    void loop() {
      // LEDを順番に点灯
      for (int i = 0; i < 10; i++) {
        digitalWrite(ledPins[i], HIGH); // LEDを点灯
        delay(500);                     // 500ミリ秒待つ
        digitalWrite(ledPins[i], LOW);  // LEDを消灯
        delay(500);                     // 500ミリ秒待つ
      }
    }    

コードをアップロードした後、バーグラフのLEDは順番に点灯し、レベル表示効果を生み出します。各LEDは0.5秒間点灯した後、次のLEDが点灯する前に消灯します。

**コードの解説**

#. LEDピンの定義：

   バーグラフの各LEDに接続されたGPIOピン番号を保持する配列 ``ledPins`` を作成します。

   .. code-block:: Arduino

      const int ledPins[] = {6, 7, 8, 9, 10, 11, 12, 13, 14, 15};

#. ピンの初期化：

   ``setup()`` 関数で、 ``ledPins`` 配列の各ピンを出力として設定します。

   .. code-block:: Arduino

      void setup() {
        for (int i = 0; i < 10; i++) {
          pinMode(ledPins[i], OUTPUT);
        }
      }

#. LEDの制御：

   ``loop()`` 関数では、 ``for`` ループを使用して各LEDを制御します。点灯させ、500ミリ秒待ち、消灯させ、次のLEDに移る前に再び500ミリ秒待ちます。

   .. code-block:: Arduino

      void loop() {
        for (int i = 0; i < 10; i++) {
          digitalWrite(ledPins[i], HIGH);
          delay(500);
          digitalWrite(ledPins[i], LOW);
          delay(500);
        }
      }

**さらなる実験**

* **順序を逆にする**：コードを修正して、LEDを逆順に点灯させます。

* **バウンス効果を作る**：最後のLEDに達した後、シーケンスを逆にして最初のLEDに戻ります。

  .. code-block:: Arduino
    
      void loop() {
        // 昇順シーケンス
        for (int i = 0; i < 10; i++) {
          digitalWrite(ledPins[i], HIGH);
          delay(200);
          digitalWrite(ledPins[i], LOW);
        }
        // 降順シーケンス
        for (int i = 8; i >= 0; i--) {
          digitalWrite(ledPins[i], HIGH);
          delay(200);
          digitalWrite(ledPins[i], LOW);
        }
      }

* **速度の調整**：遅延時間を変更して、LEDがより速くまたは遅く点灯するようにします。


**結論**

このレッスンでは、Raspberry Pi Picoを使用して複数のLEDを制御し、ループや遅延といったシンプルなプログラミング構造を用いて視覚効果を作り出す方法を学びました。この基礎的な知識は、LEDディスプレイやインジケーターを含むより高度なプロジェクトに不可欠です。
