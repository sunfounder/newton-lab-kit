.. note::

    こんにちは、FacebookでのSunFounder Raspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Raspberry Pi、Arduino、ESP32についての知識を深め、同じ趣味を持つ人々との交流を楽しみましょう。

    **参加する理由**

    - **エキスパートサポート**：コミュニティやチームからの支援を受けて、販売後の問題や技術的な課題を解決します。
    - **学びと共有**：スキルアップのためのヒントやチュートリアルを交換します。
    - **独占プレビュー**：新製品の発表や先行公開へのアクセスを得られます。
    - **特別割引**：最新製品に対する独占割引を楽しみます。
    - **祭りのプロモーションとギブアウェイ**：ギブアウェイや祝祭のプロモーションに参加します。

    👉 私たちと一緒に探検し、創造しませんか？クリック[|link_sf_facebook|]して今日から参加しましょう！

.. _ar_lcd:

3.4 液晶ディスプレイ（LCD1602）
=====================================

このレッスンでは、Raspberry Pi Pico 2を使用して **1602 LCD** でテキストを表示する方法を学びます。LCD1602はキャラクターベースの液晶ディスプレイで、2行に16文字を表示できるため、メッセージ、センサー読み取り値、またはステータスアップデートなどの情報を表示するプロジェクトに理想的です。

マイクロコントローラーにLCDを直接接続する場合、多くのGPIOピンが必要になることがあり、プロジェクトの機能を制限する可能性があります。この問題を解決するために、 **I2Cインターフェース** を備えたLCD1602モジュールを使用できます。I2Cプロトコルは2本のデータライン（SDAとSCL）のみを使用し、わずか2本のGPIOピンでLCDを制御できるため、他のセンサーやデバイス用に他のピンを解放できます。

**Raspberry Pi Pico 2でのI2Cの理解**

Raspberry Pi Pico 2は、複数のGPIOピンを通じてI2C通信をサポートし、プロジェクトに柔軟性を提供します。I2C0とI2C1の2つのI2Cバスを持ち、それぞれ複数のピンセットにマップできます。

こちらはPico 2上のI2C対応ピンの内訳です：

|pin_i2c|

I2C0またはI2C1のいずれかに合うSDAとSCLピンの組み合わせを自由に選択できます。この柔軟性により、プロジェクト内の他の周辺機器とのピン競合を避けることができます。

**必要なもの**

このプロジェクトには、以下のコンポーネントが必要です。

全キットを購入する方が便利ですが、こちらがリンクです：

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
        - :ref:`cpn_i2c_lcd`
        - 1
        - |link_i2clcd1602_buy|

**回路図**

|sch_lcd_ar|

**配線図**

|wiring_lcd_ar|

**コードの書き方**

.. note::

    * ファイル ``3.4_liquid_crystal_display.ino`` を ``newton-lab-kit/arduino/3.4_liquid_crystal_display`` から開くことができます。
    * またはこのコードを **Arduino IDE** にコピーしてください。
    * **Raspberry Pi Pico 2** ボードと正しいポートを選択し、"Upload"をクリックしてください。
    * ここでは ``LiquidCrystal I2C`` ライブラリを使用しています。 **ライブラリマネージャー** からインストールできます。

      .. image:: img/lib_i2c_lcd.png

.. code-block:: arduino

  #include <Wire.h>
  #include <LiquidCrystal_I2C.h>

  // LCDのI2Cアドレスを設定（通常は0x27または0x3F）
  #define LCD_ADDRESS 0x27
  #define LCD_COLUMNS 16
  #define LCD_ROWS    2

  // I2Cアドレスと次元でライブラリを初期化
  LiquidCrystal_I2C lcd(LCD_ADDRESS, LCD_COLUMNS, LCD_ROWS);

  void setup() {
    // LCDを初期化
    lcd.init();
    lcd.backlight();  // バックライトを点灯

    // LCDにメッセージを表示
    lcd.setCursor(0, 0);  // 列0、行0
    lcd.print("Hello, World!");
    lcd.setCursor(0, 1);  // 列0、行1
    lcd.print("LCD1602 with I2C");
  }

  void loop() {
    // ここでは何も行わない
  }


Raspberry Pi Picoにコードをアップロードした後、LCDには以下が表示されるはずです：

* 最初の行に「Hello, World!」
* 二行目に「LCD1602 with I2C」


画面に何も表示されない場合は、LCDモジュールの背面にある小さなポテンショメータ（つまみ）を回してコントラストを調整し、テキストが見えるようにします。


**コードの解説**

#. ライブラリのインクルード：

   * ``Wire.h``：I2C通信を扱います。
   * ``LiquidCrystal_I2C.h``：I2C LCDとのやり取りを簡素化します。

#. LCDパラメータの定義：

   * ``LCD_ADDRESS``：LCDモジュールのI2Cアドレス。一般的なアドレスは0x27または0x3Fです。不明な場合は、I2Cスキャナースケッチを使用してアドレスを見つけることができます。

   .. code-block:: arduino

      #define LCD_ADDRESS 0x27
      #define LCD_COLUMNS 16
      #define LCD_ROWS    2

#. LCDの初期化：

   .. code-block:: arduino

      LiquidCrystal_I2C lcd(LCD_ADDRESS, LCD_COLUMNS, LCD_ROWS);

#. ``setup()`` 関数で：

   .. code-block:: arduino

      lcd.init();         // LCDを初期化します
      lcd.backlight();    // バックライトを点灯します

#. テキストの表示：

   .. code-block:: arduino

      lcd.setCursor(0, 0);  // カーソルを列0、行0に設定します
      lcd.print("Hello, World!");

      lcd.setCursor(0, 1);  // カーソルを列0、行1に設定します
      lcd.print("LCD1602 with I2C");

**シリアル入力を使用してLCDにテキストを表示する**

プログラムを改良して、シリアルモニターからの入力を読み取り、それをLCDに表示するようにします。

* 変更されたコード：

  .. code-block:: arduino

    #include <Wire.h>
    #include <LiquidCrystal_I2C.h>

    #define LCD_ADDRESS 0x27
    #define LCD_COLUMNS 16
    #define LCD_ROWS    2

    LiquidCrystal_I2C lcd(LCD_ADDRESS, LCD_COLUMNS, LCD_ROWS);

    void setup() {
      lcd.init();
      lcd.backlight();

      Serial.begin(115200);
      lcd.setCursor(0, 0);
      lcd.print("Enter text:");
    }

    void loop() {
      if (Serial.available() > 0) {
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("You typed:");

        String inputText = Serial.readStringUntil('\n');
        lcd.setCursor(0, 1);
        lcd.print(inputText);
      }
    }

  コードをアップロードした後、メッセージを入力して ``Enter`` キーを押すと、そのメッセージがLCDに表示されます。

* 説明：

  * シリアル入力の読み取り：シリアルポートにデータがあるかどうかを確認し、改行文字が出現するまで入力文字列を読み取ります。

   .. code-block:: arduino

      if (Serial.available() > 0) {
        String inputText = Serial.readStringUntil('\n');
        // ...
      }

  * シリアル入力をLCDに表示：

    .. code-block:: arduino

      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("You typed:");
      lcd.setCursor(0, 1);
      lcd.print(inputText);

**トラブルシューティング**

* LCDに表示されない：

  * LCDモジュールの背面にあるコントラスト調整用のポテンショメータを調整します。
  * 配線接続を確認します。
  * 正しいI2Cアドレスを使用していることを確認します。I2Cバス上のデバイスをスキャンすることができます。I2C LCD1602が正しく接続されていれば、アドレスが表示されます。デフォルトのアドレスは通常0x27ですが、場合によっては0x3Fのこともあります。

  .. code-block:: arduino

      #include <Wire.h>

      void setup() {
          Wire.begin();
          Serial.begin(115200);
          while (!Serial); // シリアル接続が確立されるまで待ちます
          Serial.println("\nI2C Scanner");
      }

      void loop() {
          byte error, address;
          int nDevices;

          Serial.println("Scanning...");

          nDevices = 0;
          for (address = 1; address < 127; address++) {
              Wire.beginTransmission(address);
              error = Wire.endTransmission();

              if (error == 0) {
                  Serial.print("I2C device found at address 0x");
                  if (address < 16) {
                      Serial.print("0");
                  }
                  Serial.println(address, HEX);

                  nDevices++;
              }else if (error == 4) {
                  Serial.print("Unknown error at address 0x");
                  if (address < 16) {
                      Serial.print("0");
                  }
                  Serial.println(address, HEX);
              }
          }
          if(nDevices == 0) {
              Serial.println("No I2C devices found\n");
          }else {
              Serial.println("done\n");
          }
          delay(5000); // 再スキャンまで5秒待ちます
      }

* 不正確な文字が表示される：

  * 緩んだ接続がないか確認します。
  * LCDが適切に初期化されていることを確認します。

**さらなる探求**

* カスタム文字：

  LCDにカスタム文字やシンボルを作成して表示します。

* センサーデータの表示：

  センサー（例えば、温度、湿度）からのデータを読み取り、その読み取り値をLCDに表示します。

* 複数のI2Cデバイス：

  複数のI2CデバイスをPicoに接続し、同時に管理します。

**結論**

このレッスンでは、I2C LCD1602ディスプレイをRaspberry Pi Picoで使用してテキストを表示する方法を学びました。I2Cインターフェースを利用することで、必要なGPIOピンの数を最小限に抑え、さらに複雑なプロジェクトに追加のセンサーや周辺機器を組み込むことが可能になります。
