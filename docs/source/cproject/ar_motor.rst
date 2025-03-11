.. note::

    こんにちは、FacebookでのSunFounder Raspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Raspberry Pi、Arduino、ESP32についてもっと深く探求し、同じ興味を持つ人々と交流しましょう。

    **参加する理由**

    - **エキスパートサポート**：コミュニティやチームからの支援を受けて、販売後の問題や技術的な課題を解決します。
    - **学びと共有**：スキルを高めるためのヒントやチュートリアルを交換します。
    - **独占プレビュー**：新製品の発表や先行公開に早期アクセスします。
    - **特別割引**：最新製品に対する独占割引を楽しみます。
    - **祭りのプロモーションとギブアウェイ**：ギブアウェイや祝祭のプロモーションに参加します。

    👉 私たちと一緒に探索し、創造しませんか？[|link_sf_facebook|]をクリックして今日から参加しましょう！

.. _ar_motor:

3.5 小型ファン（DCモーター）の制御
======================================

このレッスンでは、Raspberry Pi Pico 2と **L293Dモータードライバー** を使用して **DCモーター** （小型ファンのような）を制御する方法を学びます。L293Dを使えば、モーターの回転方向（時計回りと反時計回りの両方）を制御できます。DCモーターはPicoが直接提供できる電流よりも多くの電流を必要とするため、外部の電源を使用してモーターを安全に動かします。

**必要なもの**

このプロジェクトには、以下のコンポーネントが必要です。

全キットを購入する方が便利です。こちらがリンクです：

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
        - :ref:`cpn_l293d`
        - 1
        - 
    *   - 6
        - :ref:`cpn_motor`
        - 1
        - |link_motor_buy| 
    *   - 7
        - :ref:`cpn_power_module`
        - 1
        -  
    *   - 8
        - 9V電池
        - 1
        - 
 
**回路図**

|sch_motor|


L293Dはモータードライバーチップで、ENはL293Dが動作するために5Vに接続されます。1Aと2AはそれぞれGP15とGP14に接続された入力で、1Yと2Yはモーターの両端に接続された出力です。

Y（出力）はA（入力）と位相が同じなので、GP15とGP14にそれぞれ異なるレベルが与えられた場合、モーターの回転方向を変更することができます。


**配線図**

|wiring_motor|

この回路では、ボタンがRUNピンに接続されているのが見られます。これは、モーターが多くの電流を使用して動作するため、Picoがコンピュータから切断される可能性があり、ボタンを押す必要がある（Picoの **RUN** ピンが低レベルを受け取る）ためです。

DCモーターは高電流を必要とするため、安全性を考慮してここでは電源モジュールを使用してモーターに電力を供給します。


**コードの書き方**

.. note::

   * ファイル ``3.5_small_fan.ino`` を ``newton-lab-kit/arduino/3.5_small_fan`` から開くことができます。
   * またはこのコードを **Arduino IDE** にコピーしてください。
   * **Raspberry Pi Pico 2**ボードと正しいポートを選択し、「Upload」をクリックしてください。

.. code-block:: arduino

    const int IN1 = 15; // Input 1Aに接続されたGPIOピン
    const int IN2 = 14; // Input 2Aに接続されたGPIOピン

    void setup() {
      pinMode(IN1, OUTPUT);
      pinMode(IN2, OUTPUT);
    }

    void loop() {
      // モーターを時計回りに回転
      digitalWrite(IN1, HIGH);
      digitalWrite(IN2, LOW);
      delay(2000); // 2秒間動作

      // モーターを停止
      digitalWrite(IN1, LOW);
      digitalWrite(IN2, LOW);
      delay(1000); // 1秒間停止

      // モーターを反時計回りに回転
      digitalWrite(IN1, LOW);
      digitalWrite(IN2, HIGH);
      delay(2000); // 2秒間動作

      // モーターを停止
      digitalWrite(IN1, LOW);
      digitalWrite(IN2, LOW);
      delay(1000); // 1秒間停止
    }

コードをアップロードした後：

* モーターは一方向に2秒間回転します。
* 次に、1秒間停止します。
* 次に、反対方向に2秒間回転します。
* このサイクルは無限に繰り返されます。

**コードの理解**

#. 制御ピンの定義：

   .. code-block:: arduino

        const int IN1 = 15; // Input 1Aに接続
        const int IN2 = 14; // Input 2Aに接続

#. ピンモードの設定：

   .. code-block:: arduino

        void setup() {
          pinMode(IN1, OUTPUT);
          pinMode(IN2, OUTPUT);
        }

#. モーター方向の制御：

   * **時計回りの回転**：IN1をHIGHにし、IN2をLOWに設定することで、モーターが一方向に回転します。

   .. code-block:: arduino

        digitalWrite(IN1, HIGH);
        digitalWrite(IN2, LOW);

   * **反時計回りの回転**：IN1をLOWにし、IN2をHIGHに設定することで、モーターが反対方向に回転します。

   .. code-block:: arduino

        digitalWrite(IN1, LOW);
        digitalWrite(IN2, HIGH);


#. モーターの停止：

   両方の入力をLOWに設定し、モーターを停止します。

   .. code-block:: arduino

        digitalWrite(IN1, LOW);
        digitalWrite(IN2, LOW);

**さらなる探求**

* 速度制御：

  PWM対応のGPIOピンにEN1ピンを接続し、デューティサイクルを変化させることでモーターの速度を制御します。

* 複数モーターの制御：

  L293Dは2つのモーターを制御できます。別のモーターを追加して独立して制御してみてください。

* センサーの統合：

  より高度なモーター制御システムを作るために、リミットスイッチやエンコーダーなどのセンサーを組み込みます。


**安全上の注意**

* 電源：

  * 外部電源の電圧がモーターの定格電圧と一致することを確認してください。
  * Picoの3.3Vピンから直接モーターを駆動しないでください。

* 電流の引き出し：

  * モーターは特に起動時や停止時に大きな電流を引き出すことがあります。
  * 電源がモーターの電流要件に対応できることを確認してください。

* Picoのリセット：

  * 場合によっては、モーターの電流引き出しが原因で電圧が低下し、Picoがリセットされたり、接続が切断されたりすることがあります。
  * モーターの実行後にコードのアップロードに問題が生じた場合は、RUNピンを瞬時にGNDに接続してPicoを手動でリセットできます。

  |wiring_run_reset|


**結論**

このレッスンでは、Raspberry Pi PicoとL293Dモータードライバーを使用してDCモーターを制御する方法を学びました。L293Dへの入力を制御することで、モーターの回転方向を変更できます。この基本的な概念は、ロボティクス、オートメーション、モーターを使用する多くのアプリケーションにおいて不可欠です。
