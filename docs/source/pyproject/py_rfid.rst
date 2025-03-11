.. note:: 

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者と一緒に深く学びましょう。

    **参加する理由**

    - **専門家のサポート**: 購入後の問題や技術的な課題を、コミュニティやチームのサポートを受けて解決できます。
    - **学び・共有**: ヒントやチュートリアルを交換して、スキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先行公開情報をいち早く手に入れましょう。
    - **特別割引**: 新製品に対する特別割引を楽しめます。
    - **祝祭キャンペーンやプレゼント**: プレゼントキャンペーンやシーズンプロモーションに参加できます。

    👉 一緒に探求し、創造的な活動をしてみませんか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _py_rfid:

6.5 RFIDインターフェース
===========================================

このレッスンでは、 **Radio Frequency Identification (RFID)** 技術をRaspberry Pi Pico 2でどのように使用するかを学びます。RFIDは、リーダーとタグの間で無線通信を可能にし、識別、認証、データの保存に利用できます。

**必要なもの**

このプロジェクトには、以下のコンポーネントが必要です。 

キットを購入するのが便利です。こちらのリンクからご覧いただけます：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - このキットに含まれるアイテム
        - リンク
    *   - Newton Lab Kit	
        - 450+
        - |link_newton_lab_kit|


また、以下のリンクから個別に購入することもできます。

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - 番号
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
        - 複数
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_mfrc522`
        - 1
        - |link_rfid_buy|

**RFIDの理解**

RFID技術は、物体に取り付けられたタグを自動的に識別・追跡するために、電磁場を利用します。タグには電子的に保存された情報が含まれており、視線を合わせることなく遠隔で読み取ることができます。

* **RFIDリーダー（MFRC522）**: RFIDタグと通信するためにラジオ波を発信するデバイスです。
* **RFIDタグ**: 小さなカードやキーフォブなどの物で、マイクロチップとアンテナを内蔵しています。パッシブ（バッテリーなし）またはアクティブ（バッテリー駆動）があります。

**回路図**

|sch_rfid|

**配線図**

|wiring_rfid|


**コードの作成**

以下の2つのスクリプトを作成します：

.. note::

    ここでは、 ``mfrc522`` フォルダ内のライブラリを使用する必要があります。Picoにアップロードされているか確認し、詳細なチュートリアルについては :ref:`add_libraries_py` を参照してください。

1. RFIDタグへのデータ書き込み：

   * ``mfrc522`` ライブラリの ``SimpleMFRC522`` クラスを使用して、RFIDリーダーとのやり取りを簡素化します。
   * リーダーは指定されたSPIピンで初期化されます。
   * ユーザーに書き込むデータの入力を促します。
   * ユーザーにタグをリーダーの近くに置くよう指示します。
   * ``reader.write(data)`` を使用して、データをタグに書き込みます。

   .. note::

       ``newton-lab-kit/micropython`` から ``6.5_rfid_write.py`` ファイルを開くか、このコードをThonnyにコピーして、「実行」ボタンをクリックするか、F5キーを押して実行します。

   .. code-block:: python

        from mfrc522 import SimpleMFRC522
        from machine import Pin, SPI

        # RFIDリーダーの初期化
        reader = SimpleMFRC522(spi_id=0, sck=18, mosi=19, miso=16, cs=17, rst=9)

        def write_to_tag():
            try:
                data = input("Enter data to write to the tag: ")
                print("Place your tag near the reader...")
                reader.write(data)
                print("Data written successfully!")
            finally:
                pass  # 必要ならクリーンアップ処理

        write_to_tag()

   実行後、次のようになります：

   * プログラムが次のメッセージを表示します：

     .. code-block::

       Enter data to write to the tag:"

   * You input the text you want to write to the RFID tag and press Enter.
   * The program then shows:

     .. code-block::

       Place your tag near the reader...

   * You place the RFID tag near the reader module.
   * After successfully writing the data, it displays:

     .. code-block::

       Data written successfully!

2. RFIDタグからのデータ読み取り：

   * ユーザーにタグをリーダーの近くに置くよう指示します。
   * ``reader.read()`` を使用して、タグのIDと保存されているテキストを読み取ります。
   * タグのIDと読み取ったデータを表示します。

   .. note::

       ``newton-lab-kit/micropython`` から ``6.5_rfid_read.py`` ファイルを開くか、このコードをThonnyにコピーして、「実行」ボタンをクリックするか、F5キーを押して実行します。

   .. code-block:: python
   
       from mfrc522 import SimpleMFRC522
       from machine import Pin, SPI
   
       # RFIDリーダーの初期化
       reader = SimpleMFRC522(spi_id=0, sck=18, mosi=19, miso=16, cs=17, rst=9)
   
       def read_from_tag():
           try:
               print("Place your tag near the reader...")
               id, text = reader.read()
               print("Tag ID: {}".format(id))
               print("Data: {}".format(text.strip()))
           finally:
               pass  # 必要ならクリーンアップ処理
   
       read_from_tag()

   実行後、プログラムが「タグをリーダーの近くに置いてください...」というメッセージを表示します。 
   RFIDタグをMFRC522リーダーモジュールに近づけると、プログラムはコンソールに取得した情報を表示します。出力は次のようになります：

   .. code-block:: 

       Tag ID: 1234567890
       Data: Your stored message

**コードの理解**

* **RFID通信**: MFRC522モジュールは、ラジオ波を使用してRFIDタグと通信します。タグが範囲内にあると、リーダーはタグのメモリにデータを読み取ったり書き込んだりできます。
* **SPIインターフェース**: このモジュールは、SPIプロトコルを介してPicoと通信し、高速なデータ転送を可能にします。
* **データ保存**: RFIDタグには限られた容量の保存領域があり、IDや短いテキストなどの小さなデータの保存に適しています。

**用途**

* **アクセス制御システム**: RFIDタグをキーとして、ドアやデバイスのロックを解除します。
* **在庫管理**: RFIDタグを使って、倉庫や店舗でのアイテムの追跡を行います。
* **出席管理システム**: RFIDタグを使って、個人の出席を記録します。

**さらなる実験**

* **複数タグ**: 複数のタグに異なるデータを書き込み、それを読み取ってみましょう。
* **セキュリティ対策**: 不正アクセスを防ぐための基本的な認証を実装しましょう。
* **データフォーマット**: JSONやCSVなど、より複雑なアプリケーションのために構造化データを保存しましょう。

**結論**

このレッスンでは、Raspberry Pi Pico 2とRFIDリーダーを接続し、RFIDタグにデータを読み書きする方法を学びました。この技術は、識別、追跡、そして自動化におけるさまざまな用途に広がりを見せています。
