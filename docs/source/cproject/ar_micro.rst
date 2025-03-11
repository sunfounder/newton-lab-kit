.. note::

    こんにちは、FacebookでのSunFounder Raspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について一緒にもっと深く探求しましょう。

    **参加する理由**

    - **エキスパートサポート**：コミュニティやチームの支援を受けて、販売後の問題や技術的な課題を解決します。
    - **学びと共有**：スキル向上のためのヒントやチュートリアルを交換します。
    - **独占プレビュー**：新製品の発表や先行公開に早期アクセス。
    - **特別割引**：最新製品の独占割引を楽しめます。
    - **祭りのプロモーションとギブアウェイ**：ギブアウェイや祝祭のプロモーションに参加します。

    👉 私たちと一緒に探索し、創造しませんか？[|link_sf_facebook|]をクリックして今日から参加しましょう！

.. _ar_micro:

2.8 優しく押して
==========================

このレッスンでは、Raspberry Pi Pico 2を使用して **マイクロスイッチ** （リミットスイッチとも呼ばれます）を利用し、押されたか放されたかを検出する方法を学びます。マイクロスイッチは、信頼性が高く頻繁な動作に耐えるため、電子レンジのドアやプリンターのカバー、3Dプリンターのエンドストップなどのデバイスによく使用されています。

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
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_capacitor`
        - 1(104)
        - |link_capacitor_buy|
    *   - 7
        - :ref:`cpn_micro_switch`
        - 1
        - 

**マイクロスイッチの理解**

マイクロスイッチには通常、三つのピンがあります：

|img_micro_switch|

- **コモン（C）**：中央のピン。
- **ノーマリーオープン（NO）**：スイッチが **押された** ときにコモンピンに接続されます。
- **ノーマリークローズド（NC）**：スイッチが **押されていない** ときにコモンピンに接続されます。

適切にスイッチを接続することで、GPIOピンの電圧レベルを読み取ることにより、スイッチが押されたときを検出できます。

**回路図**

|sch_limit_sw|

デフォルトでは、GP14は低く、押されるとGP14は高くなります。

10K抵抗の目的は、押す間GP14を低く保つことです。

機械式スイッチを押すと、接点がバウンスし、開閉状態の間で複数回素早く遷移することがあります。GP14とGNDの間に接続されたコンデンサは、このノイズをフィルタリングするのに役立ちます。

* **スイッチが押されていない場合**：

  * **コモン（C）**ピンは **NC** ピンに接続され、それが **GND** に接続されています。
  * **GP14**は **LOW**（0V）を読み取ります。

* **スイッチが押された場合**：

  * **コモン（C）**ピンは **NO** ピンに接続され、それが **3.3V** に接続されています。
  * **GP14**は **HIGH** （3.3V）を読み取ります。

**配線図**

|wiring_limit_sw|


**コードの書き方**

マイクロスイッチが押されたときを検出して、シリアルモニターにメッセージを表示するシンプルなプログラムを書きます。

.. note::

   * ファイル ``2.8_press_gently.ino`` を ``newton-lab-kit/arduino/2.8_press_gently`` から開くことができます。
   * またはこのコードを **Arduino IDE** にコピーしてください。
   * **Raspberry Pi Pico 2** ボードと正しいポートを選択し、「Upload」をクリックしてください。

.. code-block:: Arduino

   const int switchPin = 14;   // マイクロスイッチに接続されたGPIOピン
   int switchState = 0;

   void setup() {
     Serial.begin(115200);       // シリアルモニターを115200ボーで初期化
     pinMode(switchPin, INPUT);  // スイッチピンを入力として設定
   }

   void loop() {
     switchState = digitalRead(switchPin);  // スイッチの状態を読み取る

     if (switchState == HIGH) {
       Serial.println("The switch is pressed!");
     } else {
       Serial.println("The switch is not pressed.");
     }
     delay(200);  // シリアルモニターを過負荷にしないための小さな遅延
   }

コードが実行され、シリアルモニターが開かれると、マイクロスイッチを押して放すことができます。
シリアルモニターは、スイッチを押すと「スイッチが押されました！」と表示し、放すと「スイッチは押されていません。」と表示します。

**コードの理解**

#. シリアル通信の初期化：

   115200ボーでシリアル通信を開始します。これにより、シリアルモニターにメッセージを表示できます。

   .. code-block:: Arduino

        Serial.begin(115200);

#. スイッチピンの設定：

   switchPin（GP14）を入力として設定し、スイッチの状態を読み取ります。

   .. code-block:: Arduino

        pinMode(switchPin, INPUT);

#. スイッチ状態の読み取り：

   スイッチの現在の状態を読み取ります。押されたときはHIGH、押されていないときはLOWになります。

   .. code-block:: Arduino

        switchState = digitalRead(switchPin);

#. スイッチ押下への対応：

   スイッチが押されているかどうかに基づいてメッセージを表示します。

   .. code-block:: Arduino

        if (switchState == HIGH) {
          Serial.println("The switch is pressed!");
        } else {
          Serial.println("The switch is not pressed.");
        }


**内部プルアップ抵抗を使用するオプション**

回路を簡素化し、コンポーネント数を減らしたい場合は、Picoの内部プルアップ抵抗を使用することができます。

* スイッチが押されたとき、GP14はGNDに接続されるため、LOW（0）を読み取ります。
* スイッチが押されていないとき、内部プルアップ抵抗のため、GP14はHIGHを読み取ります。

* 回路の変更：

  外部の10KΩ抵抗とコンデンサを取り除きます。

* マイクロスイッチの接続：

  * **コモン（C）端子**：PicoのGP14に接続。
  * **ノーマリーオープン（NO）端子**：PicoのGNDに接続。
  * **ノーマリークローズド（NC）端子**：接続しない。

* コードの変更：

  .. code-block:: Arduino

        const int switchPin = 14;   // マイクロスイッチに接続されたGPIOピン
        int switchState = 0;

        void setup() {
          Serial.begin(115200);          // シリアルモニターを115200ボーで初期化
          pinMode(switchPin, INPUT_PULLUP);  // 内部プルアップ抵抗を有効に
        }

        void loop() {
          switchState = digitalRead(switchPin);  // スイッチの状態を読み取る

          if (switchState == LOW) {
            Serial.println("The switch is pressed!");
          } else {
            Serial.println("The switch is not pressed.");
          }
          delay(200);  // シリアルモニターを過負荷にしないための小さな遅延
        }

**スイッチのデバウンス**

機械式スイッチは、接点のバウンスによりノイズが発生することがあります。読み取りの信頼性を向上させるために、ソフトウェアデバウンスを実装することができます。


.. code-block:: Arduino

    const int switchPin = 14;   // マイクロスイッチに接続されたGPIOピン
    int switchState = 0;        // スイッチの現在の状態
    int lastSwitchState = HIGH; // スイッチの前の状態
    unsigned long lastDebounceTime = 0;  // 最後の状態変更の時間
    unsigned long debounceDelay = 50;    // デバウンス時間（ミリ秒）

    void setup() {
      Serial.begin(115200);
      pinMode(switchPin, INPUT_PULLUP);
    }

    void loop() {
      int reading = digitalRead(switchPin);

      if (reading != lastSwitchState) {
        lastDebounceTime = millis();
      }

      if ((millis() - lastDebounceTime) > debounceDelay) {
        if (reading != switchState) {
          switchState = reading;

          if (switchState == LOW) {
            Serial.println("The switch is pressed!");
          } else {
            Serial.println("The switch is not pressed.");
          }
        }
      }

      lastSwitchState = reading;
    }

* 前の状態から読み取りが変わったかどうかを確認します。
* 変わっていた場合は、 ``lastDebounceTime`` をリセットします。
* 読み取りがデバウンス遅延を超えて安定した場合、新しい状態を有効とみなします。

**結論**

このレッスンでは、Raspberry Pi Picoを使用してマイクロスイッチが押されたり放されたりするのを検出する方法を学びました。また、回路内にプルダウン抵抗を実装して信頼性の高い読み取りを保証する方法や、回路を簡素化するための内部プルアップ抵抗の使用方法を見ました。さらに、機械式スイッチのノイズに対処するためのデバウンスについても学びました。

**さらなる探求**

* **LEDの制御**：スイッチが押されたときにLEDを点灯するようにコードを修正します。
* **複数のスイッチ**：異なる入力を検出するために、さらにマイクロスイッチを追加してみてください。
* **カウンターの作成**：スイッチが押された回数を数えて表示します。
