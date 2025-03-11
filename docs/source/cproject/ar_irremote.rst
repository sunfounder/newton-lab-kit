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

.. _ar_irremote:

6.4 赤外線リモコンを使う
==========================================================

このレッスンでは、 **赤外線 (IR) リモコン** と **IR 受信モジュール** を Raspberry Pi Pico 2 で使用する方法を学びます。  
IR リモコンの信号を受信・デコードすることで、ワイヤレスでプロジェクトを操作できるようになります。

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
        - :ref:`cpn_ir_receiver`  
        - 1  
        - |link_receiver_buy|  

**赤外線通信の仕組み**

赤外線通信は、赤外線を利用してワイヤレスでデータを送信する技術です。 テレビや DVD プレーヤーなどの家電製品では、IR リモコンが広く使用されています。

* **IR 送信機（リモコン）**: ボタンを押すと、特定のコードが赤外線信号として送信される。  
* **IR 受信機**: 赤外線信号を受信し、電気信号に変換してデコードする。  

**回路図**

|sch_irrecv|

**配線図**

|wiring_irrecv|


**コードの記述**

IR 受信機を初期化し、IR 信号を受信、デコードしてシリアルモニターにボタンの情報を表示するプログラムを作成します。

.. note::

    * ``6.4_ir_remote_control.ino`` を ``newton-lab-kit/arduino/6.4_ir_remote_control`` から開くことができます。  
    * または、このコードを **Arduino IDE** にコピーしてください。  
    * **Raspberry Pi Pico 2** ボードを選択し、適切なポートを設定して「Upload」をクリックしてください。  
    * ``IRremote`` ライブラリを使用するため、 **Library Manager** からインストールしてください。

      .. image:: img/lib_ir.png

.. code-block:: arduino

    #define SEND_PWM_BY_TIMER

    #include <IRremote.hpp>  // IRremote ライブラリをインクルード

    const int receiverPin = 17;  // IR 受信モジュールの接続ピンを定義

    void setup() {
      // Start serial communication at a baud rate of 115200
      Serial.begin(115200);
      // Initialize the IR receiver on the specified pin with LED feedback enabled
      IrReceiver.begin(receiverPin, ENABLE_LED_FEEDBACK);
    }

    void loop() {
      if (IrReceiver.decode()) {  // Check if the IR receiver has received a signal
        bool result = 0;
        String key = decodeKeyValue(IrReceiver.decodedIRData.command);
        if (key != "ERROR") {
          Serial.println(key);  // 読み取ったキーをシリアルモニターに表示
          delay(100);
        }
        IrReceiver.resume();  // 次の信号を受信する準備
      }
    }

    // 受信した IR 信号を対応するキーに変換する関数
    String decodeKeyValue(long result) {
      switch (result) {
        case 0x45: return "POWER";
        case 0x47: return "MUTE";
        case 0x46: return "MODE";
        case 0x44: return "PLAY/PAUSE";
        case 0x40: return "BACKWARD";
        case 0x43: return "FORWARD";
        case 0x7: return "EQ";
        case 0x15: return "-";
        case 0x9: return "+";
        case 0x19: return "CYCLE";
        case 0xD: return "U/SD";
        case 0x16: return "0";
        case 0xC: return "1";
        case 0x18: return "2";
        case 0x5E: return "3";
        case 0x8: return "4";
        case 0x1C: return "5";
        case 0x5A: return "6";
        case 0x42: return "7";
        case 0x52: return "8";
        case 0x4A: return "9";
        case 0x0: return "ERROR";
        default: return "ERROR";
      }
    }

コードをアップロードし、IR リモコンのボタンを押すと、シリアルモニターに対応するキーが表示されます。

.. code-block:: arduino

    BACKWARD
    CYCLE
    POWER
    MODE
    EQ
    5
    9

.. note::

  新しいリモコンには、電池を絶縁するためのプラスチック片が付いている場合があります。 取り外してから使用してください。


**コードの解説**

#. **ヘッダーと定数の定義**

   * ``#define SEND_PWM_BY_TIMER``: PWM 信号をタイマーで送信するためのマクロ。ただし、このコードでは使用されていないため、不要な記述の可能性がある。  
   * ``#include <IRremote.hpp>``: ``IRremote`` ライブラリをインクルードし、IR 信号の送受信機能を利用可能にする。  
   * ``const int receiverPin = 17;``: IR 受信モジュールを接続する GPIO ピン（17）を定義。

#. セットアップ関数

   * ``Serial.begin(115200);``: シリアル通信を 115200 baud で初期化し、デバッグやデータのやり取りを可能にする。  
   * ``IrReceiver.begin(receiverPin, ENABLE_LED_FEEDBACK);``: 指定した ``receiverPin`` で IR 受信機を初期化し、信号受信時に LED を点灯する機能を有効化。  

   .. code-block:: arduino

      void setup() {
        Serial.begin(115200);
        IrReceiver.begin(receiverPin, ENABLE_LED_FEEDBACK);
      }

#. ループ関数

   * ``if (IrReceiver.decode())``: IR 受信機が有効な信号を受信したか確認。受信していればデコード処理へ進む。  
   * ``decodeKeyValue(IrReceiver.decodedIRData.command)``: 受信した IR コマンドを、人間が識別しやすいキー名（例: "POWER" や "MUTE"）に変換。  
   * ``Serial.println(key);``: 変換されたキー名をシリアルモニターに表示。  
   * ``delay(100);``: 連続して同じ信号が送信されるのを防ぐための短いディレイを追加。  
   * ``IrReceiver.resume();``: 受信バッファをクリアし、次の IR 信号を受信する準備をする。  

   .. code-block:: arduino

      void loop() {
        if (IrReceiver.decode()) {
          bool result = 0;
          String key = decodeKeyValue(IrReceiver.decodedIRData.command);
          if (key != "ERROR") {
            Serial.println(key);
            delay(100);
          }
          IrReceiver.resume();
        }
      }

#. ``decodeKeyValue`` 関数

   * 受信した IR コード（long 型の値） を、対応するリモコンのボタン名に変換する。  
   * switch文を使用し、各ボタンに対応する IR コードを照合。  
   * 例: 0x45を受信すると"POWER"、0x47 を受信すると"MUTE"と認識。  
   * 照合できない場合は "ERROR" を返す。  

   .. code-block:: arduino

      String decodeKeyValue(long result) {
        switch (result) {
          case 0x45: return "POWER";
          case 0x47: return "MUTE";
          case 0x46: return "MODE";
          ...
          case 0x4A: return "9";
          case 0x0: return "ERROR";
          default: return "ERROR";
        }
      }

**トラブルシューティング**

* IR 信号が表示されない場合  
  * IR 受信機が正しく GPIO 17 に接続されているか確認。  
  * 受信機に電源（VCC/GND）が供給されていることをチェック。  
  * ``receiverPin`` の定義が適切であるかコードを確認。  

* 誤った信号が表示される場合  
  * 使用するリモコンが IR 受信機と互換性があるか確認。  
  * ``decodeKeyValue`` 関数のコードが、リモコンのボタン配置と一致しているかチェック。  
  * 汎用リモコンを使用して正しい信号を確認。  

* 不明なコマンドが表示される場合  
  * ``decodeKeyValue`` 関数を更新し、リモコン固有の IR コードを追加。  
  * IR デコードツールを使用し、リモコンの正確な信号を特定。  

* 信号干渉の可能性  
  * リモコンと IR 受信機の間に障害物がないか確認。  
  * 他の IR 発光デバイス（例: テレビ、エアコン）からの干渉がないかチェック。  

**さらに応用するには？**

* IR 信号でデバイスを制御する  
  デコードした IR 信号を使用して、LED、モーター、サーボなどのデバイスをリモート制御。  

* 汎用リモコンの作成  

  ``decodeKeyValue()`` 関数を拡張し、さまざまなリモコンの IR コードに対応させる。  

* フィードバックの追加 

  LCD や OLED ディスプレイを使用して、受信した IR コマンドを視覚的に表示。  

**まとめ**

このレッスンでは、 **Raspberry Pi Pico を使用して IR リモコンの信号を受信・デコードする方法** を学びました。  
IRremote ライブラリを活用することで、簡単にリモコン入力を解読し、プロジェクトにワイヤレス制御を組み込めます。  
この技術を応用すれば、 **リモコン操作のデバイス、スマートホーム、IoT システム** など、さまざまなプロジェクトの開発が可能になります。
