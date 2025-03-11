.. note::

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！ラズベリーパイ、アルドゥイーノ、ESP32について、同じ趣味を持つ人々とさらに深く探求しましょう。

    **参加する理由は？**

    - **専門家によるサポート**: コミュニティとチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学びと共有**: 技術を磨くためのヒントやチュートリアルを交換しましょう。
    - **独占プレビュー**: 新製品の発表やちら見せに早期アクセスが可能です。
    - **特別割引**: 最新製品を特別割引価格でお楽しみください。
    - **祝祭プロモーションとギブアウェイ**: ギブアウェイや休日のプロモーションに参加しましょう。

    👉 私たちと一緒に探求し、創造しませんか？[|link_sf_facebook|]をクリックして今すぐ参加！

.. _ar_rfid:

6.5 RFIDの活用
===========================================

このレッスンでは、Raspberry Pi Pico 2を使用して **RFID（Radio Frequency Identification）** 技術を活用する方法を学びます。RFIDは、リーダーとタグの間で無線通信を行い、識別、認証、データの保存などに利用できます。

**必要なもの**

このプロジェクトでは、以下のコンポーネントを使用します。

キットを購入すると便利ですが、以下のリンクから個別に購入することもできます。

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名称
        - このキットに含まれるアイテム
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
        - :ref:`cpn_mfrc522`
        - 1
        - |link_rfid_buy|

**RFIDの仕組み**

RFIDは電磁場を利用し、タグが取り付けられた物体を自動で識別・追跡します。タグには電子データが保存されており、直接視認しなくても読み取ることができます。

* **RFIDリーダー（MFRC522）**: RFIDタグと通信するために電波を発信するデバイス。
* **RFIDタグ**: カードやキーフォブの形状をした小型デバイスで、マイクロチップとアンテナを内蔵。電池を必要としない **パッシブ型** と、バッテリーを搭載した **アクティブ型** がある。

**回路図**

|sch_rfid|

**配線図**

|wiring_rfid|


**コードの記述**

MFRC522 RFIDリーダーを初期化し、タグをスキャンしてUID（ユニークID）を読み取るプログラムを作成します。

.. note::

   * ``MFRC522`` ライブラリを使用します。 **ライブラリマネージャ** からインストールできます。

      .. image:: img/lib_mfrc522.png


1. RFIDタグへのデータ書き込み

   .. note::

      * ``6.5_rfid_read.ino`` を ``newton-lab-kit/arduino/6.5_rfid_read`` から開く。
      * もしくは、以下のコードを **Arduino IDE** にコピーする。
      * **Raspberry Pi Pico 2** を選択し、適切なポートを指定して「Upload」をクリック。

.. code-block:: arduino

    #include <SPI.h>
    #include <MFRC522.h>

    // RFIDモジュールの接続ピンを定義
    #define SS_PIN 17    // SDAピンをGPIO 17 (SPI SS) に接続
    #define RST_PIN 9    // RSTピンをGPIO 9 に接続

    MFRC522 mfrc522(SS_PIN, RST_PIN); // MFRC522インスタンスの作成

    void setup() {
      // シリアル通信の初期化
      Serial.begin(115200);
      while (!Serial); // シリアルポートが接続されるまで待機

      // SPIバスの初期化
      SPI.begin();

      // RFIDリーダーの初期化
      mfrc522.PCD_Init();
         Serial.println("RFID Writer Initialized!");
   
    }

    void loop() {
      // シリアルバッファにデータがあるか確認
      if (Serial.available() > 0) {
        String data = Serial.readStringUntil('#'); // '#'が来るまで読み取る
        data.trim(); // 余分な空白を削除

        // 新しいRFIDカードを待機
           Serial.println("Place your RFID tag near the reader...");
        if (!mfrc522.PICC_IsNewCardPresent()) {
          return;
        }

        // カードを選択
        if (!mfrc522.PICC_ReadCardSerial()) {
          return;
        }

        // キーAを使用して認証
        MFRC522::MIFARE_Key key;
        for (byte i = 0; i < 6; i++) {
          key.keyByte[i] = 0xFF;
        }

        byte block = 4; // 書き込むブロック
        byte sector = mfrc522.PICC_GetUid()->uidByte[0] % 32; // セクタ計算

        MFRC522::StatusCode status;
        status = mfrc522.PCD_Authenticate(MFRC522::PICC_CMD_MF_AUTH_KEY_A, block, &key, &(mfrc522.uid));
        if (status != MFRC522::STATUS_OK) {
             Serial.print("Authentication failed: ");
          Serial.println(mfrc522.GetStatusCodeName(status));
          return;
        }

        // 書き込むデータ（16バイト）
        byte buffer[18];
        data.getBytes(buffer, sizeof(buffer));
        buffer[16] = 0x00; // パディング
        buffer[17] = 0x00; // パディング

        // データをブロックに書き込み
        status = mfrc522.MIFARE_Write(block, buffer, 16);
        if (status != MFRC522::STATUS_OK) {
             Serial.print("Write failed: ");
          Serial.println(mfrc522.GetStatusCodeName(status));
          return;
        }

           Serial.println("Data written successfully!");
      }
    }

コードをアップロードした後の挙動:

* シリアルモニターには次のように表示されます:

  .. code-block::

        RFID Reader Initialized!
        Place your RFID tag near the reader...

* 書き込みたいデータを入力し、最後に ``#`` を追加します。例:

  .. code-block::

     Hello World#

* RFIDタグをリーダーの近くに置くと、シリアルモニターには確認メッセージが表示されます:

  .. code-block::

        Data written successfully!

2. RFIDタグの読み取り:

   .. note::

      * ``6.5_rfid_read.ino`` を ``newton-lab-kit/arduino/6.5_rfid_read`` から開くことができます。
      * または、以下のコードを **Arduino IDE** にコピーしてください。
      * **Raspberry Pi Pico 2** ボードと正しいポートを選択し、「Upload」をクリックしてください。

   .. code-block:: arduino

        #include <SPI.h>
        #include <MFRC522.h>

        // RFIDモジュールの接続ピンを定義
        #define SS_PIN 17    // SDAピンをGPIO 17 (SPI SS) に接続
        #define RST_PIN 9    // RSTピンをGPIO 9 に接続

        MFRC522 mfrc522(SS_PIN, RST_PIN); // MFRC522インスタンスの作成

        void setup() {
          // シリアル通信の初期化
          Serial.begin(115200);
          while (!Serial); // シリアルポートが接続されるまで待機

          // SPIバスの初期化
          SPI.begin();

          // RFIDリーダーの初期化
          mfrc522.PCD_Init();
          Serial.println("RFID Reader Initialized!");
        }

        void loop() {
          // 新しいRFIDカードの探索
          if ( ! mfrc522.PICC_IsNewCardPresent()) {
            return;
          }

          // カードを選択
          if ( ! mfrc522.PICC_ReadCardSerial()) {
            return;
          }

          // カードのUIDを読み取る
          Serial.print("UID tag :");
          String content= "";
          byte letter;
          for (byte i = 0; i < mfrc522.uid.size; i++) {
             content.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
             content.concat(String(mfrc522.uid.uidByte[i], HEX));
          }
          Serial.println(content);

          // UIDに関連するデータを表示
          if (userData.length() > 0) {
            Serial.print("Associated Data: ");
            Serial.println(userData);
          } else {
            Serial.println("No data associated with this UID.");
          }
        }

コードをアップロードした後の挙動:

* シリアルモニターには次のように表示されます:

  .. code-block::

        RFID Reader Initialized!

  *  RFIDタグ（キーホルダーやカードなど）をMFRC522 RFIDモジュールの近くに置くと、シリアルモニターにはUIDと保存されたデータが表示されます:

  .. code-block::

        UID tag : 04 A3 1B 7C 3E
        Data on tag: HelloWorld

**トラブルシューティング**


* 読み取りができない場合:


  * 特にSPIライン（SCK、MOSI、MISO、SS）の配線を確認してください。
  * RFIDモジュールが電源を受け取っていることを確認してください（VCCおよびGND）。
  * コード内のGPIOピン設定が正しいことを確認してください。

* 読み取り値が正しくない場合:

  * MFRC522モジュールと互換性のあるRFIDタグを使用してください。
  * 別のRFIDタグを試して、タグ固有の問題でないことを確認してください。

* 書き込みに失敗する場合:

  * RFIDタグがロックされていないか、書き込み保護されていないか確認してください。
  * 認証キーがタグのキーと一致していることを確認してください。
  * データバッファが正しくフォーマットされ、16バイト以内であることを確認してください。

* 電波干渉がある場合:

  * RFIDモジュールを他の電子機器の近くに設置しないでください。
  * RFIDタグの通信を妨げる物理的な障害物がないことを確認してください。

**さらなる応用**

* アクセス制御システム:

  RFIDタグで制御するドアロックシステムを構築する。

* 在庫管理:

  RFIDタグを利用して物品の管理や自動カウントを行う。

* RFID認証システム:

  ユーザーログインやデバイスアクセスのための安全な認証システムを開発する。

* 他のセンサーとの統合:

  RFIDと温度センサーや動作センサーを組み合わせて、総合的な監視システムを構築する。

**まとめ**

このレッスンでは、MFRC522 RFIDモジュールを用いてRaspberry Pi PicoとRFIDシステムを接続する方法を学びました。SPI通信プロトコルとMFRC522ライブラリを活用することで、RFIDタグの読み書きを簡単に実装できます。これにより、アクセス制御、在庫管理、インタラクティブなプロジェクトなど、幅広い応用が可能になります。
読み取りと書き込みを行う方法を学びました。SPI通信プロトコルとMFRC522ライブラリを活用することで、アクセス制御や在庫管理など、多様な用途にRFID技術を応用できます。
