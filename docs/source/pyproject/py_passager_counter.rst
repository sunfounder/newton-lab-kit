.. note:: 

    こんにちは！FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者と一緒により深く学びましょう。

    **参加する理由は？**

    - **専門的なサポート**: コミュニティやチームの支援を受けて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: スキルを向上させるためのヒントやチュートリアルを交換しましょう。
    - **限定プレビュー**: 新製品の発表やプレビューをいち早くチェックできます。
    - **特別割引**: 最新製品の限定割引をお楽しみいただけます。
    - **フェスティブプロモーションとプレゼント**: ギブアウェイやホリデープロモーションに参加できます。

    👉 さあ、一緒に探求し、作成する準備はできましたか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _py_passage_counter:

7.4 乗客カウンターの作成
=======================================================

このレッスンでは、Raspberry Pi Pico 2、PIR（パッシブ赤外線）モーションセンサー、4桁の7セグメントディスプレイを使用して、 **乗客カウンター** を作成します。このデバイスは、PIRセンサーでモーションが検出されるたびにその回数をカウントし、7セグメントディスプレイにそのカウントを表示します。これは、公共の場所で足元の交通量を監視するために使われるカウンターの仕組みをシミュレートしています。

**必要なもの**

このプロジェクトには以下のコンポーネントが必要です。

全キットを購入するのが便利です。リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - キットに含まれるアイテム
        - リンク
    *   - Newton Lab Kit	
        - 450以上
        - |link_newton_lab_kit|

下記のリンクから個別に購入することもできます。


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
        - :ref:`cpn_resistor`
        - 4(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_4_dit_7_segment`
        - 1
        - 
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|
    *   - 8
        - :ref:`cpn_pir`
        - 1
        - |link_pir_buy|

**コンポーネントの理解**

* **PIRモーションセンサー**: 赤外線（IR）光を測定して物体の動きを検出します。動きが検出されると、高い信号を出力します。
* **4桁7セグメントディスプレイ**: 0000から9999までの数字を表示できます。シフトレジスタを使用して、GPIOピンを少なくしてディスプレイを制御します。
* **74HC595シフトレジスタ**: 8ビットのシリアル入力、パラレル出力のシフトレジスタです。少ないGPIOピンで複数の出力を制御できます。

**回路図**

|sch_passager_counter| 

* この回路は、 :ref:`py_74hc_4dig` を基に、PIRモジュールが追加されたものです。
* PIRセンサーは、誰かが通過すると約2.8秒間の高い信号を送信します。
* PIRモジュールには2つのポテンショメーターがあります。1つは感度を調整し、もう1つは検出距離を調整します。PIRモジュールを最適に動作させるためには、両方を反時計回りに最後まで回してください。

    |img_PIR_TTE|

**配線図**

|wiring_passager_counter| 

**コードの作成**

次に、以下の機能を持つMicroPythonスクリプトを作成します：

* PIRセンサーを使用して動きを検出します。
* 動きが検出されるたびにカウンターをインクリメントします。
* 現在のカウントを4桁の7セグメントディスプレイに更新します。
* マルチプレクシングを使用してディスプレイを制御します。

.. note::

    * ``7.4_passager_counter.py`` を ``newton-lab-kit/micropython`` から開くか、コードをThonnyにコピーして、「実行」またはF5を押してください。
    * 正しいインタプリタが選択されていることを確認してください：MicroPython（Raspberry Pi Pico）。COMxx。

.. code-block:: python

    from machine import Pin
    import utime

    # PIRセンサーのピンを定義
    pir_sensor = Pin(16, Pin.IN)

    # カウンターを初期化
    count = 0

    # 各数字の2進数コード（0-9）
    SEGMENT_CODES = [
        0x3F,  # 0
        0x06,  # 1
        0x5B,  # 2
        0x4F,  # 3
        0x66,  # 4
        0x6D,  # 5
        0x7D,  # 6
        0x07,  # 7
        0x7F,  # 8
        0x6F   # 9
    ]

    # 74HC595の制御ピンを初期化
    SDI = machine.Pin(18, machine.Pin.OUT)   # シリアルデータ入力（DS）
    RCLK = machine.Pin(19, machine.Pin.OUT)  # レジスタクロック（STCP）
    SRCLK = machine.Pin(20, machine.Pin.OUT) # シフトレジスタクロック（SHCP）

    # 7セグメントディスプレイの各桁の選択ピン（共通カソード）
    digit_pins = [
        machine.Pin(10, machine.Pin.OUT),  # 桁1
        machine.Pin(11, machine.Pin.OUT),  # 桁2
        machine.Pin(12, machine.Pin.OUT),  # 桁3
        machine.Pin(13, machine.Pin.OUT)   # 桁4
    ]

    # 74HC595にデータを送信する関数
    def shift_out(data):
        RCLK.low()
        for bit in range(7, -1, -1):
            SRCLK.low()
            bit_val = (data >> bit) & 0x01
            SDI.value(bit_val)
            SRCLK.high()
        RCLK.high()

    # 特定の位置に数字を表示する関数
    def display_digit(position, digit):
        # すべての桁をオフにする
        for dp in digit_pins:
            dp.high()
        # セグメントデータを送信
        shift_out(SEGMENT_CODES[digit])
        # 選択された桁をアクティブにする（共通カソードはアクティブロー）
        digit_pins[position].low()
        # 数字が見えるように小さな遅延を加える
        utime.sleep_ms(5)
        # 桁をオフにする
        digit_pins[position].high()

    # 4桁の数字を表示する関数
    def display_number(number):
        # 各桁の数字を抽出
        digits = [
            (number // 1000) % 10,
            (number // 100) % 10,
            (number // 10) % 10,
            number % 10
        ]
        # 各桁を迅速に表示
        for i in range(4):
            display_digit(i, digits[i])

    # PIRセンサーの割り込みハンドラ
    def pir_handler(pin):
        global count
        count += 1
        if count > 9999:
            count = 0

    # PIRセンサーの割り込み設定
    pir_sensor.irq(trigger=Pin.IRQ_RISING, handler=pir_handler)

    # メインループ
    while True:
        # 常にディスプレイを更新
        display_number(count)

コードが実行されると、7セグメントディスプレイが初期化され、0000が表示されます。
PIRセンサーの前に動くと、カウントが1つずつ増加します。
カウントが9999に達すると、0000にリセットされます。

**コードの理解**

#. インポートとピン定義：

   * ``machine.Pin``: GPIOピンを制御するために使用。
   * ``utime``: 時間関連の機能を提供。
   * 74HC595を制御するためにSDI、SRCLK、RCLKピンを定義。
   * PIRセンサー用の ``pir_sensor`` をGP16に入力ピンとして定義。

#. セグメントコード：

   * ``SEGMENT_CODES``: 7セグメントディスプレイに0から9までの数字を表示するための2進数コードリストです。各バイトは点灯すべきセグメントを示します。

   .. code-block:: python

        # 7セグメントディスプレイのセグメントコード（共通カソード）
        SEGMENT_CODES = [
            0x3F,  # 0
            0x06,  # 1
            0x5B,  # 2
            0x4F,  # 3
            0x66,  # 4
            0x6D,  # 5
            0x7D,  # 6
            0x07,  # 7
            0x7F,  # 8
            0x6F   # 9
        ]

#. カウンターの初期化：

   * ``count``: モーションが検出されるたびに増加するカウントを保持するグローバル変数。

#. ``shift_out`` 関数の定義：

   * 74HC595に8ビットのデータを送信します。
   * 最上位ビット（MSB）からデータをシフトして送信します。
   * シフトクロックとレジスタクロックを適切にパルスします。

   .. code-block:: python

        def shift_out(data):
            RCLK.low()
            for bit in range(7, -1, -1):
                SRCLK.low()
                bit_val = (data >> bit) & 0x01
                SDI.value(bit_val)
                SRCLK.high()
            RCLK.high()

#. ``display_digit`` 関数の定義：

* すべての桁をオフにします。
* 数字に対応するセグメントコードを送信します。
* 指定された桁をアクティブにするため、そのピンを低電位に設定します。
* 数字が見えるように小さな遅延を加えます。
* 表示後、桁をオフにします。

   .. code-block:: python

        def display_digit(position, digit):
            for dp in digit_pins:
                dp.high()
            shift_out(SEGMENT_CODES[digit])
            digit_pins[position].low()
            utime.sleep_ms(5)
            digit_pins[position].high()


#. ``display_number`` 関数の定義:

   * 数字から各桁を抽出します。
   * 各桁を迅速に表示するために ``display_digit`` を呼び出し、マルチプレクシング効果を作成します。

   .. code-block:: python

        def display_number(number):
            # 個々の桁を抽出
            digits = [
                (number // 1000) % 10,
                (number // 100) % 10,
                (number // 10) % 10,
                number % 10
            ]
            # 各桁を迅速に表示
            for i in range(4):
                display_digit(i, digits[i])

#. PIR インタラプトハンドラー:

   * ``pir_handler``: PIR センサーが動きを検知すると自動的に呼び出される関数です。
   * カウント変数をインクリメントします。
   * カウントが 9999 を超えると、カウントを 0 にリセットします。

   .. code-block:: python

        def pir_handler(pin):
            global count
            count += 1
            if count > 9999:
                count = 0

#. PIR センサー インタラプト設定:

   ``pir_sensor.irq``: PIR センサーからの立ち上がりエッジ信号（つまり、動きが検知された時）で ``pir_handler`` を呼び出すインタラプトを設定します。

   .. code-block:: python

        pir_sensor.irq(trigger=Pin.IRQ_RISING, handler=pir_handler)

#. メインループ:

   ``display_number(count)`` を継続的に呼び出して、現在のカウントをディスプレイに表示します。

   .. code-block:: python

        while True:
            display_number(count)

**トラブルシューティング**

* 表示の問題:

  * 表示が正しく数字を表示しない場合、セグメントコードと配線接続を確認してください。
  * シフトレジスタが正しく接続されており、データが正しい順番でシフトされていることを確認してください。

* PIR センサーの感度:

  * PIR センサーには、感度や遅延を調整するためのポテンショメータがある場合があります。
  * これらを調整して、環境に適した動き検出を行ってください。
  * PIR センサーは動きの検出後、再度検出する前に短い遅延があることを考慮してください。

* カウントの精度:

  * 動きの多い環境では、カウントが急速に増加する可能性があります。
  * PIR センサーのデバウンス処理を追加するか、カウント頻度を制限するロジックを検討してください。

**拡張と改善**

* リセットボタン:

  別の GPIO ピンに接続されたプッシュボタンを追加して、押されたときにカウントをゼロにリセットできるようにします。

* 双方向カウント:

  2つの PIR センサーを戦略的に配置し、動きの方向（出入り）を検出してカウントを増減させます。

* データロギング:

  時間とともにカウントを記録できるようにプログラムを拡張し、データを Pico に保存するか、コンピュータに送信して分析します。

* 表示の改善:

  LCD ディスプレイを使用して、タイムスタンプ、総カウント、メッセージなどの追加情報を表示します。

* ネットワーク接続:

  Pico をネットワークに接続（ESP8266 などの Wi-Fi モジュールを使用）し、サーバーやクラウドサービスにデータを送信してリモート監視を行います。

**結論**

このレッスンでは、Raspberry Pi Pico 2、PIR モーションセンサー、4桁の 7セグメントディスプレイを使用して実用的な乗客カウンターを作成する方法を学びました。このプロジェクトは、マイクロコントローラがセンサーや出力デバイスとどのように連携し、リアルタイムでデータを収集・表示するかを示しています。

コードやハードウェアを使って新しい機能を追加したり、機能性を改善したりすることができます。このプロジェクトは、データ分析、リモート監視、または他のセンサーやデバイスとの統合を含むより複雑なシステムの基盤として活用できます。
