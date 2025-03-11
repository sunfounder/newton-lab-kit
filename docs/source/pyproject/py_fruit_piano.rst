こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Raspberry Pi、Arduino、ESP32の更なる深掘りを、同じ興味を持つ仲間たちと一緒に楽しみましょう。

**なぜ参加するのか？**

- **エキスパートサポート**: 当コミュニティとチームの助けを借りて、販売後の問題や技術的な課題を解決。
- **学びと共有**: スキル向上のためのヒントやチュートリアルを交換。
- **独占プレビュー**: 新製品の発表やプレビューをいち早く手に入れる。
- **特別割引**: 最新製品の独占割引を楽しむ。
- **祭事プロモーションとギブアウェイ**: ギブアウェイや休日のプロモーションに参加。

👉 私たちと一緒に探索し、創造しませんか？クリック[|link_sf_facebook|]して今日参加しましょう！

.. _py_fruit_piano:

7.9 フルーツピアノの作成
=================================================

このプロジェクトでは、Raspberry Pi Pico 2、MPR121静電容量タッチセンサー、ブザー、RGB LEDを使用して **フルーツピアノ** を作成します。フルーツ（または任意の導電性オブジェクト）を静電容量タッチセンサーに接続することで、触れると音楽ノートを演奏し、カラフルな光を表示するピアノキーに変身させます。

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
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 4(1-1KΩ, 1-330Ω, 2-220Ω)
        - |link_resistor_buy|
    *   - 7
        - 受動 :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|
    *   - 8
        - :ref:`cpn_rgb`
        - 1
        - |link_rgb_led_buy|
    *   - 9
        - :ref:`cpn_mpr121`
        - 1
        - 


**コンポーネントの理解**

* **MPR121静電容量タッチセンサー**: 最大12のタッチ入力を処理できるタッチセンサーコントローラーです。接続された電極に触れることによって生じる静電容量の変化を検出します。
* **受動ブザー**: PWM信号で駆動すると音を出す電子部品です。異なる音楽ノートを演奏するために使用します。
* **RGB LED**: 赤、緑、青のLEDを一つのパッケージに組み合わせたLEDです。各色の強度を調整することで、幅広い色の範囲を生成できます。
* **フルーツや導電性オブジェクト**: フルーツ、金属オブジェクト、あるいは水など、MPR121に接続すると導電性タッチ入力として機能するアイテムです。

**回路図**

|sch_fruit_piano| 

フルーツをピアノの鍵盤に変えるには、MPR121の電極をフルーツ（例えばバナナの柄）に接続する必要があります。

初めに、MPR121は初期化され、各電極は現在の充電に基づいた値を取得します。導体（人間の体など）が電極に触れると、充電は移動して再バランスが取れます。
結果として、電極の値は初期値と異なり、メインコントロールボードに触れられたことを伝えます。
このプロセス中に、各電極の配線が安定していることを確認し、初期化時に充電がバランス良くなるようにしてください。



**配線図**

|wiring_fruit_piano| 


**コードの書き方**

MicroPythonスクリプトを書いて、次のことを行います：

* MPR121タッチセンサーを初期化。
* 接続されたフルーツからのタッチ入力を検出。
* ブザーで対応する音楽ノートを演奏。
* RGB LEDをランダムな色で点灯させる。

.. note::

    * ``7.9_fruit_piano.py`` を ``newton-lab-kit/micropython`` から開くか、Thonnyにコードをコピーして「実行」ボタンをクリックするか、F5キーを押してください。
    * 正しいインタプリタが選択されていることを確認してください：MicroPython（Raspberry Pi Pico）.COMxx。
    * ここでは ``mpr121.py`` というライブラリが必要です。Picoにアップロードされているか確認してください。詳細なチュートリアルは :ref:`add_libraries_py` を参照してください。

.. code-block:: python

    from mpr121 import MPR121
    from machine import Pin, I2C, PWM
    import time
    import urandom

    # MPR121静電容量タッチセンサー用のI2C接続を初期化
    i2c = I2C(1, sda=Pin(6), scl=Pin(7))
    mpr = MPR121(i2c)

    # 音符の周波数を定義（ヘルツ単位）
    NOTE_FREQUENCIES = [
        220,  # A3
        247,  # B3
        262,  # C4
        294,  # D4
        330,  # E4
        349,  # F4
        392,  # G4
        440,  # A4
        494,  # B4
        523,  # C5
        587,  # D5
        659   # E5
    ]

    # GP15でブザー用のPWMを初期化
    buzzer = PWM(Pin(15))

    # GP13（赤）、GP12（緑）、GP11（青）でRGB LED用のPWMを初期化
    red = PWM(Pin(13))
    green = PWM(Pin(12))
    blue = PWM(Pin(11))

    # LED用のPWM周波数を設定
    red.freq(1000)
    green.freq(1000)
    blue.freq(1000)

    # 音を鳴らす関数
    def play_tone(frequency):
        if frequency == 0:
            buzzer.duty_u16(0)
        else:
            buzzer.freq(frequency)
            buzzer.duty_u16(32768)  # 50%のデューティサイクル

    # 音を止める関数
    def stop_tone():
        buzzer.duty_u16(0)

    # RGB LEDにランダムな色を設定する関数
    def set_random_color():
        red.duty_u16(urandom.getrandbits(16))
        green.duty_u16(urandom.getrandbits(16))
        blue.duty_u16(urandom.getrandbits(16))

    # RGB LEDを消す関数
    def turn_off_led():
        red.duty_u16(0)
        green.duty_u16(0)
        blue.duty_u16(0)

    # メインループ
    try:
        last_touched = mpr.touched()
        while True:
            current_touched = mpr.touched()
            for i in range(12):
                pin_bit = 1 << i
                if current_touched & pin_bit and not last_touched & pin_bit:
                    # 電極iが触れられた
                    print("Pin {} touched".format(i))
                    play_tone(NOTE_FREQUENCIES[i])
                    set_random_color()
                if not current_touched & pin_bit and last_touched & pin_bit:
                    # 電極iが離された
                    print("Pin {} released".format(i))
                    stop_tone()
                    turn_off_led()
            last_touched = current_touched
            time.sleep(0.01)
    except KeyboardInterrupt:
        pass
    finally:
        stop_tone()
        turn_off_led()


.. note::
    
    プログラムを実行する前に、フルーツや導電性オブジェクトに触れないでください。これにより、適切な初期化が保証されます。

プログラムが開始された後、優しくフルーツに触れてください。

* ブザーは対応する音楽ノートを演奏します。
* RGB LEDはランダムな色で点灯します。
* 異なるフルーツに触れて異なるノートを演奏する実験をしてみてください。

**コードの理解**

#. 初期化：

   * **I2C接続**: MPR121センサーとの通信を設定します。
   * **PWM設定**: ブザーとRGB LEDピンのPWMを初期化します。

#. 音符の周波数：

   音楽ノート（A3からE5）に対応する周波数のリストです。

#. 関数：

   * ``play_tone(frequency)``: 指定された周波数で音を鳴らします。
   * ``stop_tone()``: ブザーを停止します。
   * ``set_random_color()``: RGB LEDにランダムな色を設定します。
   * ``turn_off_led()``: RGB LEDを消します。

#. メインループ：

   * **タッチ検出**: 電極のタッチイベントを継続的にチェックします。
   * **タッチ処理**：

     * 電極が触れられたとき、対応するノートを演奏し、RGB LEDを点灯させます。
     * 電極が離れたとき、音を停止し、LEDを消します。

   * **デバウンス**: バウンスの問題を防ぐための短い遅延（ ``time.sleep(0.01)`` ）。

#. 例外処理：

   * トライブロックを使用して、キーボード割り込み時に適切に終了できるようにします。
   * 最終的にブザーとLEDが消えることを保証します。

**トラブルシューティング**

* 音や光が出ない場合：

  * すべての配線接続を確認します。
  * MPR121がPicoに正しく接続されていることを確認します。
  * フルーツが電極にしっかり接続されていることを確認します。
  * ``mpr121.py`` がPicoに正しくアップロードされていることを確認します。

* タッチが検出されない場合：

  * 複数の電極に同時に触れていないことを確認します。
  * 配線を直接触らず、フルーツや導電性オブジェクトに触れます。
  * フルーツが乾燥していないことを確認します。湿ったフルーツはより良く導電します。

* 不安定な挙動：

  * Picoとセンサーが静電気にさらされていないことを確認します。
  * 配線と接続が安定していることを保持し、一貫した静電容量の読み取りを維持します。

**さらなる実験**

* 楽器の拡張：

  * 異なる導電材料（例：水、金属オブジェクト）をキーとして使用します。
  * 電極にマッピングする周波数を増やして、ノートの数を増やします。

* 視覚効果：

  * ``set_random_color()`` 関数を修正して特定の色パターンを作成します。
  * 視覚的な体験を向上させるために、より多くのLEDを追加します。

* 感度の調整：

  MPR121のタッチ閾値設定を実験して感度を調整します。

* 他のセンサーとの組み合わせ：

  環境条件に基づいて音や光の効果を変更するために、他のセンサー（例：光センサー）を統合します。

**まとめ**

Raspberry Pi Pico 2を使用してフルーツピアノを成功裏に構築しました！このプロジェクトは、静電容量タッチセンシングを音と光と組み合わせてインタラクティブな体験を作成する方法を示しています。導電性、タッチセンシング、クリエイティブなコーディングの原理を探る楽しい方法です。

このプロジェクトに新しい機能を追加したり、異なる材料で実験したり、追加のコンポーネントを統合したりして、さらに発展させてください。
