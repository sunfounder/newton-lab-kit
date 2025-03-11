.. note:: 

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Raspberry Pi、Arduino、ESP32についてもっと深く探求しましょう。

**参加する理由?**

- **専門家のサポート**: コミュニティとチームからのサポートで販売後の問題や技術的な課題を解決。
- **学びと共有**: スキル向上のためのヒントやチュートリアルを交換。
- **独占プレビュー**: 新製品の発表や先行予告をいち早く入手。
- **特別割引**: 最新製品の独占割引を楽しむ。
- **祝祭プロモーションとギブアウェイ**: ギブアウェイや休日プロモーションに参加。

👉 一緒に探求し、創造してみませんか？クリック [|link_sf_facebook|] して今すぐ参加！

.. _py_guess_number:

7.7 「数字当てゲーム」の作成
=============================================================

このプロジェクトでは、Raspberry Pi Pico 2、4x4マトリックスキーパッド、そしてI2C LCD1602ディスプレイを使用して、インタラクティブな **数字当てゲーム** を構築します。ゲームは0から99までのランダムな数字を生成し、プレイヤーは交代でその数字を推測します。各プレイヤーの推測後、ゲームはその推測が高すぎたか低すぎたかに基づいて範囲を絞り込み、誰かが正しい数字を当てるまで続けます。

**必要なもの**

このプロジェクトには以下のコンポーネントが必要です。

キット全体を購入することは非常に便利です。こちらがリンクです：

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
        - :ref:`cpn_resistor`
        - 4(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_keypad`
        - 1
        - |link_keypad_buy|
    *   - 7
        - :ref:`cpn_i2c_lcd`
        - 1
        - |link_i2clcd1602_buy|

**コンポーネントの理解**

* **4x4マトリックスキーパッド**: 4行4列のマトリックスで配置された16個のボタンを持つキーパッドです。数字やコマンドの入力に使用します。
* **I2C LCD1602ディスプレイ**: 16x2文字のLCDディスプレイで、I2Cインターフェースを備えており、SDAとSCLの2本のデータラインのみを使用することで配線を簡略化します。

**回路図**

|sch_guess_number|

この回路は :ref:`py_keypad` に基づいており、押されたキーを表示するためのI2C LCD1602が追加されています。

**配線図**

|wiring_game_guess_number| 

配線を容易にするために、上の図では、マトリックスキーボードの列行と10K抵抗が同時にG10〜G13の穴に挿入されます。


**コードの書き方**

MicroPythonプログラムを書いて、以下の操作を行います：

* 0から99の間のランダムな数字を生成します。
* キーパッドからの入力を読み取ります。
* LCDディスプレイを更新して、ヒントとプレイヤーの入力を表示します。
* 各予想の後で範囲を絞り込みます。

.. note::

    * ``7.7_game_guess_number.py`` を ``newton-lab-kit/micropython`` から開くか、Thonnyにコードをコピーして「実行」ボタンをクリックするか、F5キーを押します。
    * 正しいインタープリタが選択されていることを確認してください：MicroPython (Raspberry Pi Pico).COMxx。 
    * ``lcd1602.py`` というライブラリを使用する必要がありますので、Picoにアップロードされているか確認してください。詳細なチュートリアルは :ref:`add_libraries_py` を参照してください。

.. code-block:: python

    from lcd1602 import LCD
    from machine import I2C, Pin
    import utime
    import urandom

    # LCD1602ディスプレイのためのI2C通信を初期化します
    i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)
    lcd = LCD(i2c)

    # 4x4マトリックスキーパッドのキャラクターマッピング
    keypad_map = [
        ["1", "2", "3", "A"],
        ["4", "5", "6", "B"],
        ["7", "8", "9", "C"],
        ["*", "0", "#", "D"]
    ]

    # 行と列のピンを定義します
    row_pins = [Pin(pin_num, Pin.OUT) for pin_num in [21, 20, 19, 18]]  # R1-R4
    col_pins = [Pin(pin_num, Pin.IN, Pin.PULL_DOWN) for pin_num in [13, 12, 11, 10]]  # C1-C4

    # キーパッドをスキャンする関数
    def read_keypad():
        for row_num, row_pin in enumerate(row_pins):
            row_pin.high()
            for col_num, col_pin in enumerate(col_pins):
                if col_pin.value() == 1:
                    row_pin.low()
                    return keypad_map[row_num][col_num]
            row_pin.low()
        return None

    # ゲーム変数を初期化する関数
    def init_game():
        global target_number, lower_bound, upper_bound, guess
        target_number = urandom.randint(0, 99)
        lower_bound = 0
        upper_bound = 99
        guess = ""
        lcd.clear()
        lcd.message("Press A to Start")

    # ディスプレイを更新する関数
    def update_display(message):
        lcd.clear()
        lcd.message(message)

    # メインプログラム
    init_game()
    game_started = False

    while True:
        key = read_keypad()
        if key:
            utime.sleep(0.2)  # デバウンスの遅延

            if not game_started:
                if key == "A":
                    game_started = True
                    update_display("Enter your guess:")
            else:
                if key in "0123456789":
                    if len(guess) < 2:
                        guess += key
                        update_display("Guess: {}\n{} < ? < {}".format(guess, lower_bound, upper_bound))
                elif key == "D":
                    if guess != "":
                        guess_number = int(guess)
                        if guess_number < lower_bound or guess_number > upper_bound:
                            update_display("Out of range!\n{} < ? < {}".format(lower_bound, upper_bound))
                        elif guess_number > target_number:
                            upper_bound = guess_number - 1
                            guess = ""
                            update_display("Too High!\n{} < ? < {}".format(lower_bound, upper_bound))
                        elif guess_number < target_number:
                            lower_bound = guess_number + 1
                            guess = ""
                            update_display("Too Low!\n{} < ? < {}".format(lower_bound, upper_bound))
                        else:
                            update_display("Correct!\nNumber is {}".format(target_number))
                            game_started = False
                            utime.sleep(2)
                            init_game()
                    else:
                        update_display("Enter a number")
                elif key == "A":
                    # ゲームを再開します
                    init_game()
                    game_started = True
                    update_display("Enter your guess:")
                elif key == "B":
                    # 現在の推測をクリアします
                    guess = ""
                    update_display("Guess cleared")
                elif key == "C":
                    # ヒントを表示するか、その他の機能
                    update_display("Hint not available")
        utime.sleep(0.1)

コードが実行された後、ゲームをプレイするための手順に従ってください：

* ゲームを開始：

  キーパッドの「A」キーを押します。

* 推測を入力：

  * 数字キーを使用してあなたの推測を入力します（0-99）。
  * 推測を送信するには「D」を押します。

* フィードバックを受け取る：

  * LCDはあなたの推測が高すぎる、低すぎる、または正しいかを示します。
  * 範囲はそれに応じて調整されます。

* ゲームに勝つ：

  * 正しい数字を推測すると、LCDに「Correct! Number is XX」と表示されます。
  * ゲームは短い遅延の後に自動的にリセットされます。

**コードの理解**

#. インポートと初期化：

   * ``lcd1602.LCD``: LCDディスプレイを制御するために。
   * ``machine.Pin``: GPIOピンとのやり取りのために。
   * ``urandom``: ランダムな数字を生成するために。
   * LCD1602ディスプレイのためのI2C通信を初期化します。

#. キーパッドスキャン機能（ ``read_keypad`` ）：

   * 一度に一つの行を高く設定します。
   * 任意の列が高く読み取られた場合、ボタンが押されたことを示します。
   * 押されたキーに対応する文字を返します。

   .. code-block:: python

        def read_keypad():
            for row_num, row_pin in enumerate(row_pins):
                row_pin.high()
                for col_num, col_pin in enumerate(col_pins):
                    if col_pin.value() == 1:
                        row_pin.low()
                        return keypad_map[row_num][col_num]
                row_pin.low()
            return None

#. ゲーム変数と初期化（ ``init_game`` ）：

   * ``target_number``: 0から99の間のランダムな数字。
   * ``lower_bound and upper_bound``: それぞれ0と99から始まります。
   * ``guess``: 現在の推測入力を格納する文字列。

   .. code-block:: python

        def init_game():
            global target_number, lower_bound, upper_bound, guess
            target_number = urandom.randint(0, 99)
            lower_bound = 0
            upper_bound = 99
            guess = ""
            lcd.clear()
            lcd.message("Press A to Start")

#. ディスプレイ更新機能（ ``update_display`` ）：

   LCDをクリアして、提供されたメッセージを表示します。

   .. code-block:: python

        # Display function
        def update_display(message):
            lcd.clear()
            lcd.message(message)

#. メインプログラムループ：

   * キー入力を待ち、ゲームロジックを処理します。
   * キー ``A`` : ゲームを開始または再開します。
   * 数字 ``0`` - ``9`` : 現在の推測番号を構築します。
   * キー ``D`` : 推測を送信し、範囲を更新します。
   * 推測が現在の範囲内にあるかどうかをチェックします。
   * 推測に基づいて ``lower_bound`` または ``upper_bound`` を更新します。
   * 次の入力のために推測をリセットします。
   * 推測が正しい場合は、成功メッセージを表示し、ゲームをリセットします。
   * キー ``B``: 現在の推測をクリアします。
   * キー ``C``: 追加の機能用（例：ヒント）。

   .. code-block:: python

        while True:
            key = read_keypad()
            if key:
                utime.sleep(0.2)  # デバウンスの遅延

                if not game_started:
                    if key == "A":
                        game_started = True
                        update_display("Enter your guess:")
        ...
        ...
            utime.sleep(0.1)

#. デバウンシングと遅延：

   * ``utime.sleep(0.2)``: キー押下後の短い遅延でデバウンス。
   * ``utime.sleep(0.1)``: メインループの小さな遅延でCPU使用を減らします。

**トラブルシューティング**

* LCDがテキストを表示しない：

  * SDAとSCLの接続（GP6とGP7）を確認します。
  * LCDが正しく電源供給されているかをチェックします。
  * LCDモジュールの裏にあるコントラストポテンショメータを調整します。

* キーパッドが反応しない：

  * すべての行と列の接続をチェックします。
  * 内部プルダウンを使用していない場合は、プルダウン抵抗が接続されていることを確認します。
  * キーパッドが正常に機能しているかを確認します。

* ランダム数が変更されない：

  * ``urandom`` が適切にインポートされ、使用されていることを確認します。
  * ランダムシードが初期化される必要があるかもしれません。

* ゲームロジックの問題：

  * 推測を処理するときの条件と範囲を再確認します。
  * 上限と下限が正しく更新されていることを確認します。


**拡張と改良**

* マルチプレイヤーサポートの追加：

  * 各プレイヤーが行う推測の数を追跡します。
  * プレイヤー間で順番を交代します。

* スコアリングシステムの実装：

  * 数字をどれだけ早く推測したかに基づいてポイントを授与します。
  * LCDにスコアを表示します。

* ヒントの提供：

  'C'キーを使用して、「数字は偶数です」または「数字は5の倍数です」といったヒントを提供します。

* 範囲の拡大：

  * ゲームを0から999の数字を推測するように変更します。
  * 表示と入力方法をそれに応じて調整します。

* 視覚的および音声フィードバック：

  追加のフィードバックを提供するために、LEDやブザーを追加します。

**結論**

Raspberry Pi Pico 2を使用してインタラクティブな「数字当てゲーム」を成功裏に構築しました！このプロジェクトは、ユーザー入力、ランダム数生成、およびディスプレイ出力を組み合わせて、楽しく魅力的なゲームを作り出しています。キーパッド、LCDディスプレイ、ゲームロジックのMicroPythonでの作業に慣れる絶好の方法です。

このゲームをさらに強化して新しい機能を追加したり、インタフェースを改善することが自由です。このプロジェクトは、より複雑なインタラクティブアプリケーションの基盤として機能することができます。
