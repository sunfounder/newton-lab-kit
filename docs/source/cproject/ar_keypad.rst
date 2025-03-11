.. note::

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Raspberry Pi、Arduino、ESP32についてもっと深く学びましょう。

    **参加する理由**

    - **エキスパートサポート**：コミュニティやチームからのサポートで販売後の問題や技術的な課題を解決。
    - **学びと共有**：スキル向上のためのヒントやチュートリアルを交換。
    - **独占プレビュー**：新製品の発表や先行プレビューへの早期アクセス。
    - **特別割引**：最新製品の独占割引を楽しむ。
    - **祭りのプロモーションとギフト**：ギフトや休日のプロモーションに参加。

    👉 私たちと一緒に探索し、創造してみませんか？クリック[|link_sf_facebook|]して今日参加しましょう！

.. _ar_keypad:

4.2 4x4キーパッドの使用
=================================================

このレッスンでは、 **4x4マトリックスキーパッド** をRaspberry Pi Pico 2に接続して、どのキーが押されたかを検出する方法を学びます。マトリックスキーパッドは、電卓、電話、自動販売機、セキュリティシステムなどで数値入力用に一般的に使用されています。

**必要なもの**

このプロジェクトには、以下のコンポーネントが必要です。

全キットを購入するのが便利ですが、こちらがリンクです：

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
        - :ref:`cpn_keypad`
        - 1
        - |link_keypad_buy|

**4x4キーパッドの理解**

4x4キーパッドは以下を含みます：

* **16のキー** が4行4列に配置されています。
* **8つのピン**：4つは行に、4つは列に接続されています。

キーを押すと、特定の行と列が接続され、行と列の番号に基づいてキーを識別できます。

こちらがキーの配置です：

|img_keypad|

**回路図**

|sch_keypad_ar|


キーボードの行（G2〜G5）は高い状態に設定されています；G6〜G9のいずれかが高い状態で読み取られた場合、どのキーが押されたかがわかります。

例えば、G6が高い状態で読み取られた場合、数字キー1が押されたということです；これは、数字キー1の制御ピンがG2とG6に接続されており、数字キー1が押されるとG2とG6が一緒に接続され、G6も高い状態になるからです。

**配線**

|wiring_keypad_ar|


**コードの書き方**


.. note::

    * ファイル ``4.2_4x4_keypad.ino`` を ``newton-lab-kit/arduino/4.2_4x4_keypad`` から開くことができます。
    * またはこのコードを **Arduino IDE** にコピーします。
    * **Raspberry Pi Pico 2** ボードと正しいポートを選択し、"Upload"をクリックします。
    * ここでは ``Adafruit Keypad`` ライブラリを使用しています。 **ライブラリマネージャー** からインストールできます。

      .. image:: img/lib_ad_keypad.png

.. code-block:: arduino

    #include "Adafruit_Keypad.h"

    // 行と列の数を定義
    const byte ROWS = 4;
    const byte COLS = 4;

    // キーパッドのキーマップを定義
    char keys[ROWS][COLS] = {
      { '1', '2', '3', 'A' },
      { '4', '5', '6', 'B' },
      { '7', '8', '9', 'C' },
      { '*', '0', '#', 'D' }
    };

    // キーパッドの行のピンアウトに接続
    byte rowPins[ROWS] = { 2, 3, 4, 5 };

    // キーパッドの列のピンアウトに接続
    byte colPins[COLS] = { 6, 7, 8, 9 };

    // Keypadオブジェクトを作成
    Adafruit_Keypad myKeypad = Adafruit_Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

    void setup() {
      // シリアル通信を初期化
      Serial.begin(115200);

      // キーパッドを初期化
      myKeypad.begin();
    }

    void loop() {
      // キーの状態を更新
      myKeypad.tick();

      // 新しいキーパッドイベントがあるかどうかを確認
      while (myKeypad.available()) {
        // キーパッドイベントを読み取る
        keypadEvent e = myKeypad.read();

        // イベントがキーの押下であるかを確認
        if (e.bit.EVENT == KEY_JUST_PRESSED) {
          // シリアルモニターにキーの値を出力
          Serial.println((char)e.bit.KEY);
        }
      }

      delay(10); // 安定性向上のための短い遅延
    }

コードをアップロードした後、キーパッドの任意のキーを押してください。対応するキーのラベル（例えば、「1」、「A」）がシリアルモニターに表示されるはずです。

各キーの押下が正確に検出され、表示されることを確認してください。すべてのキーをテストして、機能が正しく動作していることを確認してください。

**Understanding the Code**

#. ライブラリの取り込み：

   この行は、キーパッドとの対話に役立つ関数を提供するAdafruit Keypadライブラリを含みます。

   .. code-block:: arduino

      #include "Adafruit_Keypad.h"

#. キーパッドレイアウトの定義：

   ``ROWS`` と ``COLS`` はキーパッドの寸法を定義します。 ``keys`` はキーパッド上の各キーのラベルを表す2次元配列です。

   .. code-block:: arduino

      const byte ROWS = 4;
      const byte COLS = 4;

      char keys[ROWS][COLS] = {
        { '1', '2', '3', 'A' },
        { '4', '5', '6', 'B' },
        { '7', '8', '9', 'C' },
        { '*', '0', '#', 'D' }
      };

#. GPIOピンへのキーパッドの接続：

   ``rowPins`` と ``colPins`` はそれぞれキーパッドの行と列に接続されるGPIOピンを格納する配列です。

   .. code-block:: arduino

      byte rowPins[ROWS] = { 2, 3, 4, 5 };
      byte colPins[COLS] = { 6, 7, 8, 9 };

#. キーパッドオブジェクトの初期化：

   この行は ``Adafruit_Keypad`` クラスのインスタンスを作成し、キーマップとピンの設定で初期化します。

   .. code-block:: arduino

      Adafruit_Keypad myKeypad = Adafruit_Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

#. 設定関数：

   シリアル通信をデバッグ用に初期化し、キーパッドを起動します。

   .. code-block:: arduino

      void setup() {
        Serial.begin(115200);    // シリアル通信を115200ボーで初期化
        myKeypad.begin();        // キーパッドを初期化
      }

#. ループ関数：

   * キーイベントを継続的にチェックします。
   * キーが押されると、そのキーの値をシリアルモニターに出力します。

   .. code-block:: arduino

      void loop() {
        myKeypad.tick(); // キーの状態を更新

        while (myKeypad.available()) {
          keypadEvent e = myKeypad.read(); // キーパッドイベントを読み取る

          if (e.bit.EVENT == KEY_JUST_PRESSED) {
            Serial.println((char)e.bit.KEY); // 押されたキーを印刷
          }
        }
        delay(10); // 安定性向上のための短い遅延
      }

**Further Exploration**

* キーデバウンスの実装：

  機械的ノイズによる誤トリガーをフィルタリングするデバウンス技術を実装して、キー検出の信頼性を向上させます。

* パスワード入力システムの作成：

  キーパッドを使用してパスワードを入力し、プロジェクト内の特定の機能へのアクセスを制御します。

* 他のコンポーネントとの統合：

  キーパッドをLCDディスプレイ、LED、ブザーなどと組み合わせて、より複雑なユーザーインターフェースを作成します。

* シンプルな電卓の構築：

  キーパッドを使用して数字を入力し、LCDに表示される基本的な算術演算を実行します。

**Conclusion**

このレッスンでは、Adafruit Keypadライブラリを使用してRaspberry Pi Picoに4x4マトリックスキーパッドを接続する方法を学びました。キー押下を検出することで、キーベースの入力システム、パスワード入力メカニズムなど、インタラクティブなプロジェクトを作成できます。キーパッド入力の読み取りと処理の方法を理解することは、エレクトロニクスプロジェクトでユーザーフレンドリーなインターフェースを構築するために不可欠です。
