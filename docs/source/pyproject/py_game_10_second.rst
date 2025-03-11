こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Raspberry Pi、Arduino、ESP32の更なる深掘りを、同じ興味を持つ仲間たちと一緒に楽しみましょう。

**なぜ参加するのか？**

- **エキスパートサポート**: 当コミュニティとチームの助けを借りて、販売後の問題や技術的な課題を解決。
- **学びと共有**: スキル向上のためのヒントやチュートリアルを交換。
- **独占プレビュー**: 新製品の発表やプレビューをいち早く手に入れる。
- **特別割引**: 最新製品の独占割引を楽しむ。
- **祭事プロモーションとギブアウェイ**: ギブアウェイや休日のプロモーションに参加。

👉 私たちと一緒に探索し、創造しませんか？クリック[|link_sf_facebook|]して今日参加しましょう！

.. _py_10_second:

7.5 「10秒ゲーム」の作成
======================================================

このプロジェクトでは、Raspberry Pi Pico 2、傾斜スイッチ、4桁7セグメントディスプレイを使用して、楽しいゲーム「10秒ゲーム」を構築します。ゲームの目的は、魔法の杖（棒に取り付けられた傾斜スイッチを使用して模擬）を振ってタイマーを開始し、 **10.00秒** に最も近いところで再び振ってタイマーを停止することです。タイミングスキルをテストし、誰が真の時間の魔法使いか友人と競うのに最適な方法です！

**必要なもの**

このプロジェクトには、以下のコンポーネントが必要です。

キット全体を購入することが便利です。こちらがリンクです:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - このキットに含まれるもの
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
        - マイクロUSBケーブル
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
        - 5(4-220Ω, 1-10KΩ)
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
        - :ref:`cpn_tilt`
        - 1
        - 

**コンポーネントの理解**

* **傾斜スイッチ**: 傾きや動きを検出するセンサーです。傾けると回路が完成または断線し、振動や動きを検出できます。
* **4桁7セグメントディスプレイ**: 0000から9999までの数字を表示します。GPIOピンの数を減らしてディスプレイを制御するためにシフトレジスタを使用します。
* **74HC595シフトレジスタ**: 8ビットのシリアル入力、並列出力シフトレジスタで、少数のGPIOピンで複数の出力を制御できます。

**回路図**

|sch_10_second|


* この回路は :ref:`py_74hc_4dig` に基づいており、傾斜スイッチが追加されています。
* 傾斜スイッチが直立しているときはGP16が高く、傾いているときは低くなります。

**配線図**

|wiring_game_10_second| 

**コードの書き方**

MicroPythonスクリプトを書いて、次のことを行います：

* 傾斜スイッチを使用して振動を検出します。
* 傾斜スイッチに基づいてタイマーを開始および停止します。
* 4桁7セグメントディスプレイに経過時間を表示します。
* ディスプレイの制御にマルチプレクシングとシフトレジスタを使用します。

.. code-block:: python

    from machine import Pin
    import utime

    # 74HC595の制御ピンを初期化
    SDI = machine.Pin(18, machine.Pin.OUT)   # シリアルデータ入力（DS）
    RCLK = machine.Pin(19, machine.Pin.OUT)  # レジスタクロック（STCP）
    SRCLK = machine.Pin(20, machine.Pin.OUT) # シフトレジスタクロック（SHCP）

    # 0-9までの数字を表示するための7セグメントディスプレイのセグメントコード（共通カソード）
    SEGMENT_CODES = [0x3F,  # 0
                    0x06,  # 1
                    0x5B,  # 2
                    0x4F,  # 3
                    0x66,  # 4
                    0x6D,  # 5
                    0x7D,  # 6
                    0x07,  # 7
                    0x7F,  # 8
                    0x6F]  # 9

    # デジット選択ピンを初期化（共通カソード）
    digit_pins = [
        machine.Pin(10, machine.Pin.OUT),  # デジット1
        machine.Pin(11, machine.Pin.OUT),  # デジット2
        machine.Pin(12, machine.Pin.OUT),  # デジット3
        machine.Pin(13, machine.Pin.OUT)   # デジット4
    ]


    # 傾斜スイッチを初期化
    tilt_switch = Pin(16, Pin.IN, Pin.PULL_DOWN)

    # タイミング用の変数
    start_time = 0
    elapsed_time = 0
    counting = false

    # シフトレジスタにデータをシフトアウトする関数
    def shift_out(data):
        RCLK.low()
        for bit in range(7, -1, -1):
            SRCLK.low()
            bit_val = (data >> bit) & 0x01
            SDI.value(bit_val)
            SRCLK.high()
        RCLK.high()

    # 特定の位置にある数字を表示する関数
    def display_digit(position, digit):
        # すべてのデジットをオフにする
        for dp in digit_pins:
            dp.high()
        # セグメントデータを送信
        shift_out(SEGMENT_CODES[digit])
        # 選択されたデジットをアクティブにする（共通カソードはアクティブロー）
        digit_pins[position].low()
        # 数字が見えるように少し遅延を入れる
        utime.sleep_ms(5)
        # デジットをオフにする
        digit_pins[position].high()

    # 経過時間を表示する関数
    def display_time(time_ms):
        # 時間をセンチ秒（1秒の100分の1）に変換
        centiseconds = int(time_ms / 10)
        # 表示に収まるように9999に制限
        if centiseconds > 9999:
            centiseconds = 9999

        # 個々の数字を抽出
        digits = [
            (centiseconds // 1000) % 10,
            (centiseconds // 100) % 10,
            (centiseconds // 10) % 10,
            centiseconds % 10
        ]
        # 各数字を迅速に表示
        for i in range(4):
            display_digit(i, digits[i])

    # 傾斜スイッチの割り込みハンドラ
    def tilt_handler(pin):
        global counting, start_time, elapsed_time
        if not counting:
            # カウントを開始
            counting = True
            start_time = utime.ticks_ms()
        else:
            # カウントを停止
            counting = False
            elapsed_time = utime.ticks_diff(utime.ticks_ms(), start_time)

    # 傾斜スイッチの割り込みを設定
    tilt_switch.irq(trigger=Pin.IRQ_RISING, handler=tilt_handler)

    # メインループ
    while True:
        if counting:
            # 経過時間を計算
            current_time = utime.ticks_diff(utime.ticks_ms(), start_time)
            display_time(current_time)
        else:
            # 最終時間を表示
            display_time(elapsed_time)



コードが実行されると、4桁7セグメントディスプレイが初期化され、00.00を表示します。

* タイマーを開始：

  * 杖を振ったり、傾斜スイッチを傾けることで割り込みをトリガーします。
  * タイマーが00.00からカウントアップを開始します。

* タイマーを停止：

  * 再び杖を振ったり、スイッチを傾けます。
  * タイマーが停止し、最終時間を表示します。

* 目標：

  * 可能な限り10.00秒に近いところでタイマーを停止します。
  * 友人と競い、最も近いタイムを出した人を見つけましょう！

**コードの理解**
#. インポートとピン定義:

   * ``machine.Pin``: GPIOピンを制御するためのモジュール。
   * ``utime``: タイミング機能を提供するモジュール。
   * シフトレジスタを制御するためのSDI、SRCLK、およびRCLKピンを定義。
   * GP16に接続された傾斜スイッチをプルダウン抵抗で初期化。

#. セグメントコードと数字コード:

   * ``SEGMENT_CODES``: 7セグメントディスプレイに0～9の数字を表示するためのバイナリコードのリスト。
   * ``digit_pins``: 各ディスプレイの桁を選択するためのコード。コモンカソードディスプレイ用でアクティブLOW。

   .. code-block:: python

        # 7セグメントディスプレイの数字0～9のセグメントコード（コモンカソード）
        SEGMENT_CODES = [0x3F,  # 0
                        0x06,  # 1
                        0x5B,  # 2
                        0x4F,  # 3
                        0x66,  # 4
                        0x6D,  # 5
                        0x7D,  # 6
                        0x07,  # 7
                        0x7F,  # 8
                        0x6F]  # 9

        # 桁選択ピンの初期化（コモンカソード）
        digit_pins = [
            machine.Pin(10, machine.Pin.OUT),  # 桁1
            machine.Pin(11, machine.Pin.OUT),  # 桁2
            machine.Pin(12, machine.Pin.OUT),  # 桁3
            machine.Pin(13, machine.Pin.OUT)   # 桁4
        ]

#. タイミング用変数:

   * ``start_time``: タイマーが開始された時刻を記録。
   * ``elapsed_time``: タイマーが停止した時の経過時間を保持。
   * ``counting``: タイマーが動作中かどうかを示すフラグ。

#. ``shift_out`` 関数の定義:

   * 74HC595に8ビットのデータを送信。
   * 最上位ビット（MSB）からデータをシフトアウト。
   * シフトレジスタクロックとレジスタクロックを適切にパルス。

   .. code-block:: python

        def shift_out(data):
            RCLK.low()
            for bit in range(7, -1, -1):
                SRCLK.low()
                bit_val = (data >> bit) & 0x01
                SDI.value(bit_val)
                SRCLK.high()
            RCLK.high()

#. ``display_digit`` 関数の定義:

   * すべての桁を消灯。
   * 表示する数字のセグメントコードを送信。
   * 指定された桁のピンをLOWにして、その桁をアクティブに。
   * 数字を表示するための小さな遅延を追加。
   * 表示後、桁を消灯。

   .. code-block:: python

        def display_digit(position, digit):
            for dp in digit_pins:
                dp.high()
            shift_out(SEGMENT_CODES[digit])
            digit_pins[position].low()
            utime.sleep_ms(5)
            digit_pins[position].high()

#. ``display_time`` 関数:

   * 経過時間をミリ秒からセンチ秒（0.01秒）に変換。
   * 時間を個々の桁に分割。
   * マルチプレクシングを使用して、各桁を迅速に表示。

   .. code-block:: python

        def display_time(time_ms):
            # 時間をセンチ秒（0.01秒）に変換
            centiseconds = int(time_ms / 10)
            # 表示に合わせて9999に制限
            if centiseconds > 9999:
                centiseconds = 9999

            # 個々の桁を抽出
            digits = [
                (centiseconds // 1000) % 10,
                (centiseconds // 100) % 10,
                (centiseconds // 10) % 10,
                centiseconds % 10
            ]
            # 各桁を迅速に表示
            for i in range(4):
                display_digit(i, digits[i])

#. ``tilt_handler`` 関数:

   * 傾斜スイッチの割り込みによってトリガーされる。
   * カウント状態を切り替え。
   * カウント開始時に ``start_time`` を記録。
   * カウント停止時に ``elapsed_time`` を計算。

   .. code-block:: python

        def tilt_handler(pin):
            global counting, start_time, elapsed_time
            if not counting:
                # カウント開始
                counting = True
                start_time = utime.ticks_ms()
            else:
                # カウント停止
                counting = False
                elapsed_time = utime.ticks_diff(utime.ticks_ms(), start_time)

#. メインループ:
 
   * ``counting`` が ``True`` の場合、経過時間を継続的に更新して表示。
   * ``counting`` が ``False`` の場合、最終的な ``elapsed_time`` を表示。

   .. code-block:: python

        while True:
            if counting:
                # 経過時間を計算
                current_time = utime.ticks_diff(utime.ticks_ms(), start_time)
                display_time(current_time)
            else:
                # 最終時間を表示
                display_time(elapsed_time)

**トラブルシューティング**

* 表示に関する問題:

  * 表示が正しく数字を表示しない場合、セグメントコードと桁のコードを確認し、配線の接続をチェックしてください。
  * シフトレジスタが正しく接続され、データが正しい順番でシフトアウトされていることを確認してください。

* 傾斜スイッチの感度:

  * 傾斜スイッチが感度過剰または不十分な場合、その向きを調整するか、別のタイプに交換を検討してください。
  * 偽のトリガーを防ぐため、プルダウン抵抗が正しく接続されていることを確認してください。

* タイミング精度:

  * タイマーはシステムクロックに依存しており、わずかな誤差が生じる可能性があります。
  * 精度を向上させるため、外部のリアルタイムクロック（RTC）モジュールを使用してください。

**拡張と改善**

* 視覚効果:

  * タイマーが停止したときに点滅するLEDや色が変わるLEDを追加。
  * タイマーの開始と停止時に音声フィードバックを提供するためにブザーを使用。

* ハイスコアの記録:

  * コードを変更して、最高記録（10.00に最も近い時間）を保存。
  * 新しいハイスコアに対してお祝いのメッセージやアニメーションを表示。

* マルチプレイヤーモード:

  * 複数のプレイヤーが交代で遊べるようにし、各プレイヤーの時間を記録。
  * プレイヤー番号とそれぞれの時間を表示。

* 難易度レベル:

  * 目標タイム（例：5.00秒、15.00秒）を設定し、挑戦を増加させる。
  * 毎回異なる目標タイムをランダムに表示。

* 代替入力方法:

  * 傾斜スイッチをボタンや他のセンサーに置き換えてタイマーの開始と停止を行う。
  * 特定のジェスチャーを検出するためにモーションセンサーを使用。

**結論**

あなたは、Raspberry Pi Pico 2を使用して「10秒ゲーム」を成功裏に作成しました！このプロジェクトは、センサー入力、タイミング機能、およびディスプレイ制御を組み合わせて、インタラクティブでエンターテイメント性のあるゲームを作り出しています。マイクロコントローラーを使用して楽しく魅力的な体験を作る素晴らしい例です。

このプロジェクトは自由にカスタマイズや拡張が可能です。新しい機能を追加したり、デザインを改善したり、さらに多くのコンポーネントを統合することができます。可能性は無限大です。
