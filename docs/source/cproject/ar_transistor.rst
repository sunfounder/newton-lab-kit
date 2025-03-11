.. note:: 

    こんにちは！SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community（Facebook）へようこそ！Raspberry Pi、Arduino、ESP32に情熱を持つ皆さんと共に、さらに深く探求しましょう。

    **なぜ参加するのか？**

    - **専門的なサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：技術的なヒントやチュートリアルを交換し、スキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行公開に早期アクセスができます。
    - **特別割引**：最新製品を独占的な割引価格で楽しむことができます。
    - **祭りのプロモーションとギブアウェイ**：ギブアウェイやホリデープロモーションに参加しましょう。

    👉 私たちと探索し、創造してみませんか？[|link_sf_facebook|]をクリックして今日から参加しましょう！

.. _ar_transistor:

2.15 トランジスタの2タイプ：NPNとPNP
=============================================

このレッスンでは、トランジスタの2つのタイプ、 **S8050（NPN）** と **S8550（PNP）** について学びます。トランジスタは一般的に電子スイッチとして使用され、この両タイプを使用してボタンでLEDを制御する方法を見ていきます。

|img_NPN&PNP|

* **NPN (S8050)**: このタイプのトランジスタは、 **ベース** に高い信号が適用されると **コレクター** から **エミッター** へ電流が流れることを可能にします。
* **PNP (S8550)**: PNPトランジスタの場合、 **ベース** に低い信号が適用されると **エミッター** から **コレクター** へ電流が流れます。

両方のトランジスタは似た目的で使われますが、信号制御においては逆の動作をします。これらのトランジスタを使用して、ボタンの入力に基づいてLEDを制御しましょう。


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
        - :ref:`cpn_resistor`
        - 3(220Ω, 1KΩ, 10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_button`
        - 1
        - |link_button_buy|
    *   - 8
        - :ref:`cpn_transistor`
        - 1(S8050/S8550)
        - |link_transistor_buy|

**NPN (S8050) トランジスタの配線**

|sch_s8050|

この回路では、ボタンを押すと **GP14** ピンに **高い信号** が送信されます。GP15が高い信号を出力すると、NPNトランジスタが導通し、LEDを通って電流が流れ、LEDが点灯します。

|wiring_s8050|

**PNP (S8550) トランジスタの配線**

|sch_s8550|

PNPトランジスタ回路では、ボタンはGP14に低い信号を出力し、押されると高くなります。GP15が **低い信号** を出力すると、PNPトランジスタが導通し、電流が流れてLEDが点灯します。

|wiring_s8550|

**コードの書き方**

.. note::

   * ``2.15_transistor.ino`` ファイルを ``newton-lab-kit/arduino/2.15_transistor`` から開くことができます。
   * または、このコードを **Arduino IDE** にコピーしてください。
   * **Raspberry Pi Pico 2** ボードを選択し、適切なポートを設定した後、「Upload」をクリックしてください。

.. code-block:: arduino

    // ピンの定義
    const int buttonPin = 14;  // ボタンはGP14に接続されています
    const int transistorPin = 15;  // トランジスタのベースはGP15に接続されています

    int buttonState = 0;  // ボタンの状態を保持する変数

    void setup() {
      pinMode(buttonPin, INPUT);
      pinMode(transistorPin, OUTPUT);
    }

    void loop() {
      // ボタンの状態を読み取る
      buttonState = digitalRead(buttonPin);

      // トランジスタを制御
      digitalWrite(transistorPin, buttonState);

      delay(10);  // デバウンシングのための小さな遅延
    }

**結果**

* NPNトランジスタ (S8050) の場合：

  ボタンを押すと、LEDが点灯します。
  ボタンを離すと、LEDが消灯します。

* PNPトランジスタ (S8550) の場合：

  ボタンを押すと、LEDが消灯します。
  ボタンを離すと、LEDが点灯します。

**コードの理解**

#. ボタンの状態の読み取り：

   ボタンの現在の状態を読み取ります。

   .. code-block:: arduino

        buttonState = digitalRead(buttonPin);

#. トランジスタの制御：

   * **NPNトランジスタの場合**：ボタンが押されている（ ``buttonState`` がHIGH）とき、トランジスタがオンになり、電流が流れてLEDが点灯します。
   * **PNPトランジスタの場合**：ボタンが押されている（ ``buttonState`` がHIGH）とき、トランジスタがオフになり（LOW）、ボタンが押されていないときにトランジスタがオンになります。

   .. code-block:: arduino

        digitalWrite(transistorPin, buttonState);

**さらなる探求**

* 大きな負荷の制御：

  Picoが直接提供できるよりも多くの電流を必要とするデバイス（モーターやリレーなど）を制御するためにトランジスタを使用します。

* トランジスタをアンプとして使用：

  トランジスタを使用して信号を増幅する方法を探求します。

* ダーリントンペアの実験：

  2つのトランジスタを使用してダーリントンペアを作成し、より高い電流ゲインを得ます。

**まとめ**

このレッスンでは、Raspberry Pi Picoとボタンを使用してLEDを制御するために、NPNおよびPNPトランジスタの使用方法を学びました。NPNとPNPトランジスタの違いを理解することは、スイッチングや増幅が必要な回路を設計する際に重要です。

