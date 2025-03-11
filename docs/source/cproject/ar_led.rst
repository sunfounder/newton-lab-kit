.. note::

    こんにちは、FacebookでのSunFounder Raspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について一緒にもっと深く探求しましょう。

    **参加する理由**

    - **エキスパートサポート**：コミュニティやチームからの支援を受けて、販売後の問題や技術的な課題を解決します。
    - **学びと共有**：スキル向上のためのヒントやチュートリアルを交換します。
    - **独占プレビュー**：新製品の発表や先行公開に早期アクセス。
    - **特別割引**：最新製品の独占割引を楽しめます。
    - **祭りのプロモーションとギブアウェイ**：ギブアウェイや祝祭のプロモーションに参加します。

    👉 私たちと一緒に探索し、創造しませんか？[|link_sf_facebook|]をクリックして今日から参加しましょう！

.. _ar_led:

2.1 Hello, LED!
=================

Raspberry Pi Pico 2を使った初めてのハードウェアプロジェクトへようこそ！このレッスンでは、MicroPythonを使用してLEDを点滅させる方法を学びます。このシンプルなプロジェクトは、物理コンピューティングの基本を理解し、コードでハードウェアを制御する方法を学ぶのに最適です。


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
        - 1(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|

**回路図**

|sch_led|

GPIOピンをHIGHまたはLOWに設定することで、そのピンの電圧出力を制御します。ピンがHIGHのとき、電流は抵抗器を介してLEDを流れ、それが点灯する原因となります。ピンがLOWのとき、電流は流れず、LEDは消灯します。

**配線図**

|wiring_led|

**コードの書き方**

.. note::

   * ファイル ``2.1_hello_led.ino`` を ``newton-lab-kit/arduino/2.1_hello_led`` から開くことができます。
   * またはこのコードを **Arduino IDE** にコピーしてください。
   * **Raspberry Pi Pico 2** ボードと正しいポートを選択し、「Upload」をクリックしてください。

.. code-block:: Arduino

    const int ledPin = 15;  // LEDに接続されたGPIOピン

    void setup() {
      pinMode(ledPin, OUTPUT);  // GPIOピンを出力として初期化
    }

    void loop() {
      digitalWrite(ledPin, HIGH);  // LEDを点灯
      delay(1000);                 // 1秒待つ
      digitalWrite(ledPin, LOW);   // LEDを消灯
      delay(1000);                 // 1秒待つ
    }

コードをアップロードした後、LEDが1秒間点灯し、1秒間消灯するのを見ることができるはずです。

**コードの理解**

#. 変数宣言：

   GPIOピン15に接続されたLEDに対応する値15を持つ定数整数 ``ledPin`` を宣言します。

   .. code-block:: Arduino

        const int ledPin = 15;

#. 設定機能：

   ``setup()`` 関数はボードが電源投入またはリセットされたときに一度実行されます。ここで ``ledPin`` を ``pinMode()`` を使用して出力ピンとして初期化します。

   .. code-block:: Arduino

        void setup() {
          pinMode(ledPin, OUTPUT);
        }

#. ループ機能：

   * ``setup()`` の後に繰り返し実行される ``loop()`` 関数。
   * ``digitalWrite()`` を使用して ``ledPin`` の電圧を設定します。 ``HIGH`` に設定すると3.3Vが供給され、LEDが点灯します。 ``LOW`` に設定すると電圧が0Vになり、LEDが消灯します。
   * ``delay(1000)`` 関数はオンとオフの状態の間に1秒間の一時停止を作ります。

   .. code-block:: Arduino

        void loop() {
          digitalWrite(ledPin, HIGH);
          delay(1000);
          digitalWrite(ledPin, LOW);
          delay(1000);
        }

**追加のヒント**

* **抵抗器の理解**：220Ωの抵抗器はLEDを流れる電流を制限し、LEDが焼損するのを防ぎます。
* **極性が重要**：LEDが正しく接続されていることを確認してください。長い脚は正のアノードで、GPIOピンに繋がる抵抗器に接続されるべきです。
* **実験**： ``delay(1000)`` の値を変更して、LEDの点滅速度を速くしたり遅くしたりしてみてください。

**結論**

おめでとうございます！Raspberry Pi Pico 2を使った最初のハードウェアプロジェクトを完成させました。このシンプルなLED点滅プロジェクトは、物理コンピューティングの世界への基本的な一歩です。ここから、ボタン、センサー、その他のコンポーネントを追加することで、より複雑なプロジェクトに挑戦できます。
