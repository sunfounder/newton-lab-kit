.. note::

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！ラズベリーパイ、アルドゥイーノ、ESP32について、同じ趣味を持つ人々とさらに深く探求しましょう。

    **参加する理由は？**

    - **専門家によるサポート**: コミュニティとチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学びと共有**: 技術を磨くためのヒントやチュートリアルを交換しましょう。
    - **独占プレビュー**: 新製品の発表やちら見せに早期アクセスが可能です。
    - **特別割引**: 最新製品を特別割引価格でお楽しみください。
    - **祝祭プロモーションとギブアウェイ**: ギブアウェイや休日のプロモーションに参加しましょう。

    👉 私たちと一緒に探求し、創造しませんか？[|link_sf_facebook|]をクリックして今すぐ参加！

.. _ar_relay:


2.16 リレーを使って別の回路を制御する
=========================================

このレッスンでは、Raspberry Pi Pico 2と **リレー** を使用して別の回路を制御する方法を学びます。リレーは、低電圧回路（Picoなど）で高電圧回路を操作できるスイッチのようなものです。例えば、リレーを使ってランプやその他の電化製品のオン/オフを切り替えることで、家電の自動化が可能になります。


**必要なもの**

このプロジェクトには、以下のコンポーネントが必要です。

全てのキットを購入するのが便利ですが、こちらがリンクです：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - このキットのアイテム
        - リンク
    *   - Newton Lab Kit
        - 450以上
        - |link_newton_lab_kit|


個別に購入することもできます。以下のリンクからどうぞ。

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
        - 1(220Ω), 1(1KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 7
        - :ref:`cpn_diode`
        - 1
        - 
    *   - 8
        - :ref:`cpn_relay`
        - 1
        - |link_relay_buy|
    *   - 9
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 10
        - :ref:`cpn_power_module`
        - 1
        -  
    *   - 11
        - 9Vバッテリー
        - 1
        -


**回路図**

|sch_relay_1|

* **リレーの動作**:
  
  * Picoが **高信号** （3.3V）をGP15に出力すると、トランジスタが動作し、リレーのコイルに電流が流れます。
  * コイルが励磁されることでスイッチが作動し、接続された負荷（ライトやモーターなど）がオンになります。
  * スイッチが作動すると「カチッ」という音がし、回路が切り替わったことがわかります。

* フライバックダイオード:
  
  * リレーのコイルがオフになったときに発生する逆起電力からトランジスタを保護するために、ダイオードをリレーのコイルと並列に配置します。

**配線図**

|wiring_relay_1|

**コードの書き方**

.. note::

   * ファイル ``2.16_relay.ino`` を ``newton-lab-kit/arduino/2.16_relay`` から開くことができます。
   * あるいは、このコードを **Arduino IDE** にコピーしてください。
   * **Raspberry Pi Pico 2** ボードと正しいポートを選択し、「Upload」をクリックします。

.. code-block:: arduino

   const int relayPin = 15;  // トランジスタのベースに接続されたGPIOピン

   void setup() {
     pinMode(relayPin, OUTPUT);
     digitalWrite(relayPin, LOW);  // 起動時にリレーをオフにする
   }

   void loop() {
     // リレーをオンにする
     digitalWrite(relayPin, HIGH);
     Serial.println("Relay ON");
     delay(2000);  // 2秒間待機

     // リレーをオフにする
     digitalWrite(relayPin, LOW);
     Serial.println("Relay OFF");
     delay(2000);  // 2秒間待機
   }

コードをアップロードすると、リレーが2秒ごとに「カチッ」と作動し、オン/オフを繰り返します。

**コードの理解**

#. **リレーピンの定義**:
  
   GPIO15を ``relayPin`` として定義し、トランジスタ経由でリレーを制御します。

   .. code-block:: arduino

        const int relayPin = 15;  // GPIO pin connected to the transistor base

#. **ピンの初期設定**:

   ``relayPin`` を出力モードに設定し、初期状態でリレーをオフにします。

   .. code-block:: arduino

        void setup() {
          pinMode(relayPin, OUTPUT);
          digitalWrite(relayPin, LOW);  // Ensure the relay is off at startup
        }

#. リレーの制御:

   * ``relayPin`` を ``HIGH`` に設定すると、トランジスタがオンになり、リレーのコイルが励磁される。  
   * 2秒間待機する。  
   * ``relayPin`` を ``LOW`` に設定すると、トランジスタがオフになり、リレーのコイルの励磁が解除される。  
   * さらに2秒間待機する。  
   * このサイクルを無限に繰り返す。  

   .. code-block:: arduino

        // Turn the relay on
        digitalWrite(relayPin, HIGH);
        Serial.println("Relay ON");
        delay(2000);  // Wait for 2 seconds

        // Turn the relay off
        digitalWrite(relayPin, LOW);
        Serial.println("Relay OFF");
        delay(2000);  // Wait for 2 seconds

**さらなる実験**  

* **タイマーを設定する**: リレーを10分間オンにし、その後自動でオフにするようにコードを修正する。  
* **家電の制御**: 適切な手順に従うことで、高電圧のデバイス（ライトやファンなど）をリレーに接続し、自動化を行うことができる。  

  * 外部回路を安全に制御する方法を示すために、ブレッドボード電源モジュールを使用して外部5V電源を追加し、LEDを駆動する。この方法は、リレーを使用して高電圧の家電製品を制御する仕組みをシミュレートする。回路の変更方法は以下の通り：

    |sch_relay_2|  
  
    |wiring_relay_2|  

  * リレーを制御するコード:  

    .. code-block:: arduino
    
       const int relayPin = 15;  // トランジスタのベースに接続されたGPIOピン

       void setup() {
         pinMode(relayPin, OUTPUT);
         digitalWrite(relayPin, LOW);  // 起動時にリレーをオフにする
       }

       void loop() {
         // リレーをオンにする
         digitalWrite(relayPin, HIGH);
         Serial.println("Relay ON");
         delay(2000);  // 2秒間待機

         // リレーをオフにする
         digitalWrite(relayPin, LOW);
         Serial.println("Relay OFF");
         delay(2000);  // 2秒間待機
       }

    リレーが作動すると（GP15がHIGHを出力）、リレーの Normally Open（NO） 端子と Common（C） 端子が接続され、外部5V電源がLEDへ流れる。これにより、リレーが外部回路を制御できることを確認できる。

    リレーがオフになると（GP15がLOWを出力）、 NO 端子と C 端子の接続が解除され、LEDの電源が遮断される。


**高電圧機器を制御する際の安全対策**  

この例では、リレー制御を示すためにLEDと5V電源を使用しているが、実際に高電圧の家電を制御する場合は、以下の点に注意すること。  

* **適切な電圧・電流定格を確認**: 使用するリレーが制御対象の電圧・電流に適合していることを確認する。  
* **絶縁の確保**: 低電圧の制御回路（Pico）と高電圧の負荷回路を適切に絶縁する。  
* **ヒューズやブレーカーの使用**: ショートや過電流による損傷を防ぐため、適切な保護回路を導入する。  
* **専門家の助言を受ける**: 高電圧回路を扱う際は、必ず専門家の助言を得て、安全を確保する。  

このプロジェクトは、タイマーやセンサーを組み合わせて、ランプやファンなどを自動制御するホームオートメーションの基礎となる。  

**NC端子の使用**  

* 制御対象の回路を COM 端子と NC 端子の間に接続すると：  

  * リレーが作動していないとき、回路は閉じて（ON）いる。  
  * リレーが作動すると、回路が開き（OFF）になる。  
  * 例: 外部デバイスの制御  
  * 注意: 高電圧のデバイスを制御する際は、十分な知識と安全対策を備えた上で行うこと。  

* 小型DCモーターや他のデバイスを制御する場合：  

  * LEDの代わりに制御したいデバイスを接続する。  
  * デバイスの電圧・電流要件が適切であることを確認する。  
  * 適切な電源を供給する。  
  * デバイスをリレーの COM 端子と NO（またはNC） 端子に直列接続する。  

**まとめ**  

このレッスンでは、リレーとRaspberry Pi Picoを使用して別の回路を制御する方法を学びました。トランジスタを介してリレーのコイルをスイッチングすることで、高電流の負荷を安全に制御し、PicoのGPIOピンに負担をかけずに運用できるようになります。リレーを活用することで、さまざまなデバイスや家電製品の自動制御が可能になり、より高度なプロジェクトへ発展させることができます。
