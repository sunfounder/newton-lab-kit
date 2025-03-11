.. note:: 

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者と一緒にさらに深く学びましょう。

    **参加する理由**

    - **専門家のサポート**: 購入後の問題や技術的な課題を、コミュニティやチームのサポートを受けて解決できます。
    - **学び・共有**: ヒントやチュートリアルを交換して、スキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先行公開情報をいち早く手に入れましょう。
    - **特別割引**: 新製品に対する特別割引を楽しめます。
    - **祝祭キャンペーンやプレゼント**: プレゼントキャンペーンやシーズンプロモーションに参加できます。

    👉 一緒に探求し、創造的な活動をしてみませんか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _py_music_player:


7.8 RFIDミュージックプレイヤーの構築
========================================================

このプロジェクトでは、Raspberry Pi Pico 2、MFRC522 RFIDリーダー、パッシブバザー、WS2812 RGB LEDを使用して **RFIDミュージックプレイヤー** を作成します。RFIDタグに音符を記録し、それを読み取って、Picoが対応するメロディを再生し、カラフルなLED効果を表示します。このプロジェクトは、RFID技術と音楽生成を組み合わせており、RFIDカードやキーフォブにメロディを保存して共有できるようにします。

**必要なもの**

このプロジェクトでは、以下の部品が必要です。

キットを購入するのが便利です。こちらのリンクからご覧いただけます：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - キット内の部品
        - リンク
    *   - Newton Lab Kit	
        - 450+
        - |link_newton_lab_kit|

以下のリンクから個別に購入することもできます。


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - 番号
        - 部品	
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
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 1(1KΩ)
        - |link_resistor_buy|
    *   - 7
        - パッシブ :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|
    *   - 8
        - :ref:`cpn_mfrc522`
        - 1
        - |link_rfid_buy|
    *   - 9
        - :ref:`cpn_ws2812`
        - 1
        - |link_ws2812_buy|

**部品の理解**

* **MFRC522 RFIDリーダーモジュール**: SPIで通信する低コストのRFIDリーダー。13.56 MHzで動作するRFIDタグにデータの読み書きができます。
* **RFIDタグ/キーフォブ**: 小さなデータを保存できるパッシブデバイス。これらのタグに音符を記録します。
* **パッシブバザー**: PWM信号を駆動すると音を発生させる電子部品。音符を再生するために使用します。
* **WS2812 RGB LED**: NeoPixelとしても知られ、広範囲の色を表示でき、単一のデータラインで個別に制御できます。

**回路図**

|sch_music_player|

**配線図**

|wiring_rfid_music_player| 

**コード作成**

2つのスクリプトを作成します：

* ``6.5_rfid_write.py``: RFIDタグに音符を保存するためのスクリプト。
* ``7.8_rfid_music_player.py``: 保存された音符を読み取り、メロディを再生するスクリプト。

.. note::

    この時、 ``mfrc522`` フォルダ内のライブラリを使用する必要があります。Picoにアップロードされているか確認し、詳細なチュートリアルは :ref:`add_libraries_py` を参照してください。

#. ``6.5_rfid_write.py`` ファイルを ``newton-lab-kit/micropython`` から開くか、このコードをThonnyにコピーして、「実行」ボタンをクリックするか、F5キーを押して実行します。

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
                pass

        write_to_tag()

#. 実行後、シェルに ``EEFGGFEDCCDEEDD EEFGGFEDCCDEDCC`` と入力し、RFIDタグをリーダーに近づけて「歓喜の歌」の楽譜を保存します。確認メッセージ「データが正常に書き込まれました！」が表示されます。

#. ``7.8_rfid_music_player.py`` ファイルを ``newton-lab-kit/micropython`` から開くか、このコードをThonnyにコピーして、「実行」ボタンをクリックするか、F5キーを押して実行します。

   .. code-block:: python

        from mfrc522 import SimpleMFRC522
        import machine
        import time
        from ws2812 import WS2812
        import urandom

        # WS2812 LEDの設定
        # ピン0に8個のWS2812 LEDストリップを初期化
        ws = WS2812(machine.Pin(0), 8)

        # MFRC522 RFIDリーダーの設定
        # 特定のピンでSPIを使ってRFIDリーダーを初期化
        reader = SimpleMFRC522(spi_id=0, sck=18, miso=16, mosi=19, cs=17, rst=9)

        # バザー音符周波数（ヘルツ）
        NOTE_C4 = 262
        NOTE_D4 = 294
        NOTE_E4 = 330
        NOTE_F4 = 349
        NOTE_G4 = 392
        NOTE_A4 = 440
        NOTE_B4 = 494
        NOTE_C5 = 523

        # ピン15にバザー用PWMを初期化
        buzzer = machine.PWM(machine.Pin(15))

        # 音符周波数に対応する音符のリスト
        note = [NOTE_C4, NOTE_D4, NOTE_E4, NOTE_F4, NOTE_G4, NOTE_A4, NOTE_B4, NOTE_C5]

        # 指定された周波数と継続時間でバザーにトーンを再生する関数
        def tone(pin, frequency, duration):
         pin.freq(frequency)  # バザーの周波数を設定
         pin.duty_u16(30000)  # デューティサイクルを50%に設定
         time.sleep_ms(duration)  # 指定された継続時間だけ音を鳴らす
         pin.duty_u16(0)  # デューティサイクルを0にして音を止める

        # 指定されたインデックスでWS2812 LEDをランダムな色で点灯させる関数
        def lumi(index):
         for i in range(8):
             ws[i] = 0x000000  # すべてのLEDを消す
         ws[index] = int(urandom.uniform(0, 0xFFFFFF))  # 指定されたインデックスのLEDにランダムな色を設定
         ws.write()  # WS2812 LEDsに色データを書き込む

        # 音符テキストをインデックスにエンコードして、対応する音符を再生する関数
        words = ["C", "D", "E", "F", "G", "A", "B", "N"]  # 音符をテキスト文字にマッピング
        def take_text(text):
         string = text.replace(' ', '').upper()  # 空白を削除し、テキストを大文字に変換
         while len(string) > 0:
             index = words.index(string[0])  # テキスト内の最初の音符を検索
             tone(buzzer, note[index], 250)  # バザーで対応する音符を250ms再生
             lumi(index)  # 対応する音符のLEDを点灯
             string = string[1:]  # 次の文字に進む

        # RFIDカードから読み取って保存された楽譜を再生する関数
        def read():
         print("Reading...Please place the card...")
         id, text = reader.read()  # RFIDカードからIDと保存されたテキストを読み取る
         print("ID: %s\nText: %s" % (id, text))  # IDとテキストを表示
         take_text(text)  # カードに保存されたテキストから楽譜を再生

        # RFIDカードから読み取り、対応する楽譜を再生
        read()


#. 実行後、コンソールに「タグをリーダーの近くに置いてください...」と表示されます。

   RFIDタグをリーダーに近づけると：

   * Picoがタグのデータを読み取ります。
   * コンソールにタグのIDとテキストが表示されます。
   * バザーがタグに保存された音符に対応するメロディを再生します。
   * WS2812 LEDが音楽に合わせたエフェクトで点灯します。


**コードの理解**

* RFIDとのインタラクション：

  * ``SimpleMFRC522`` クラスはRFIDタグへの読み書きを簡素化します。
  * **データの書き込み**: ``write_to_tag()`` でユーザー入力がタグに書き込まれます。
  * **データの読み取り**: ``read_and_play()`` で、タグがリーダーに近づけられた時にデータが読み取られます。

* 音楽の再生：

  * **音符辞書**: ``note`` 文字が周波数にマッピングされます。
  * **音符の解析**: RFIDタグからのテキストはクリーンアップされ、1文字ずつ繰り返し処理されます。
  * **音符の再生**: 各文字に対応する周波数がバザーで再生されます。

* LEDエフェクト：

  * **WS2812制御**: ``ws`` オブジェクトはRGB LEDを制御します。
  * **LEDを点灯させる**: 音符ごとに、対応するLEDがランダムな色で点灯します。

* タイミング：

  * **音符の継続時間**: 各音符は300ミリ秒間再生されます。
  * **音符間の間隔**: 音符の間には100ミリ秒の短い間隔があります。

**さらに実験する**

* 自分のメロディを作成：

  * RFIDタグに異なる音符を記録します。
  * 音符C、D、E、F、G、A、B、N（休符）を使いましょう。
  * 自分の音楽RFIDタグを友達と共有できます。

* 音符の範囲を広げる：

  * 追加の周波数を定義して、さらに多くのオクターブを追加します。
  * 音符辞書を適宜更新します。

* 視覚的な改善：

  * light_led関数を変更して、さまざまなLEDパターンを作成します。
  * 音楽とLEDエフェクトをより密接に同期させます。

* 複数のタグで異なる曲を再生：

  * 複数のRFIDタグに異なるメロディをプログラムします。
  * シンプルなRFIDベースの音楽ライブラリを作成します。

**制限事項の理解**

* RFIDタグのデータ保存：

  * RFIDタグには保存容量が限られています（MFRC522の場合、通常は最大48文字まで）。
  * 音楽のシーケンスは簡潔に保ちましょう。

* 音質：

  * パッシブバザーは単純な音しか再生できません。
  * より良い音質を求めるなら、アクティブスピーカーを使い、DAC出力を使用してください。

* RFIDタグの互換性：

  MFRC522リーダーと互換性のあるRFIDタグを使用してください。

**結論**

あなたは、Raspberry Pi Pico 2を使ってRFIDミュージックプレイヤーを作成しました！このプロジェクトは、RFID技術、音楽生成、LED制御を組み合わせ、インタラクティブで楽しい体験を提供します。RFIDタグにメロディを保存することで、さまざまな曲を簡単に共有し、再生できるようになります。
