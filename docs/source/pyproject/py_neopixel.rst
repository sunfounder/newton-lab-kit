.. note:: 

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者と共にさらに深く学びましょう。

    **参加する理由**

    - **専門家のサポート**: 購入後の問題や技術的な課題を、コミュニティやチームのサポートを通じて解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換し、スキルを向上させましょう。
    - **独占プレビュー**: 新製品の発表や先行情報にいち早くアクセスできます。
    - **特別割引**: 最新製品に対する独占的な割引を楽しめます。
    - **季節限定のプロモーションとギブアウェイ**: ギブアウェイや祝祭のプロモーションに参加できます。

    👉 一緒に探求し、創造しませんか？今すぐ [|link_sf_facebook|] をクリックして参加しましょう！

.. _py_neopixel:

3.3 RGB LEDストリップの制御
===========================================================

このレッスンでは、Raspberry Pi Pico 2とMicroPythonを使用して**RGB LEDストリップ**（特にWS2812タイプ）を制御する方法を学びます。

WS2812は、制御回路とRGBチップを5050サイズのLEDパッケージに統合したスマートLEDです。各LEDには独自のコントローラーが内蔵されており、単一のデータラインで個別にLEDを制御できます。これにより、ストリップ上の各LEDの色と明るさを独立して変更することが可能です。


**必要なもの**

このプロジェクトには、以下のコンポーネントが必要です。

全体キットを購入するのが便利です。リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名称	
        - セット内容
        - リンク
    *   - Newton Lab Kit	
        - 450+
        - |link_newton_lab_kit|

個別に購入することもできます。

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
        - :ref:`cpn_ws2812`
        - 1
        - |link_ws2812_buy|

**回路図**

|sch_ws2812|

**配線図**

|wiring_ws2812|

電流の消費に注意してください。PicoのVBUSピンは少数のLED（例えば8個）には電力を供給できますが、より多くのLEDを使用する場合はPicoが過負荷にならないよう、外部電源が必要になることがあります。

**コードの記述**

.. note::

    * ``newton-lab-kit/micropython`` から ``3.3_rgb_led_strip.py`` を開くか、コードをThonnyにコピーして「実行」ボタンをクリック、またはF5キーを押して実行します。
    * 正しいインタープリタ（MicroPython (Raspberry Pi Pico).COMxx）が選択されていることを確認してください。

    * ここでは ``ws2812.py`` ライブラリを使用します。Picoにアップロードされているか確認し、詳細なチュートリアルについては :ref:`add_libraries_py` をご参照ください。

.. code-block:: python

    import machine
    from ws2812 import WS2812

    # LEDストリップの初期化
    led_strip = WS2812(machine.Pin(0), 8)  # GP0を使用し、8個のLED

    # 各LEDの色を設定
    led_strip[0] = [255, 0, 0]     # 赤
    led_strip[1] = [0, 255, 0]     # 緑
    led_strip[2] = [0, 0, 255]     # 青
    led_strip[3] = [255, 255, 0]   # 黄
    led_strip[4] = [0, 255, 255]   # シアン
    led_strip[5] = [255, 0, 255]   # マゼンタ
    led_strip[6] = [255, 255, 255] # 白
    led_strip[7] = [128, 128, 128] # 灰色

    # LEDストリップを更新して色を表示
    led_strip.write()

このコードが実行されると、GP0ピンに接続された8個のWS2812 LEDストリップが以下の色を表示します：

* **LED 0**: 赤 (255, 0, 0)
* **LED 1**: 緑 (0, 255, 0)
* **LED 2**: 青 (0, 0, 255)
* **LED 3**: 黄 (255, 255, 0)
* **LED 4**: シアン (0, 255, 255)
* **LED 5**: マゼンタ (255, 0, 255)
* **LED 6**: 白 (255, 255, 255)
* **LED 7**: 灰色 (128, 128, 128)

**コードの理解**

#. ライブラリのインポート:

   * ``machine``: ハードウェア関連の機能を提供
   * ``WS2812``: WS2812 LEDストリップを制御するライブラリ

#. LEDストリップの初期化:

   * ``led_strip = WS2812(machine.Pin(0), 8)``: GP0ピンに接続された8個のLEDを持つLEDストリップを初期化

#. 色の設定:

   * ``led_strip[0] = [255, 0, 0]``: RGB値（赤、緑、青）を使用して、各LEDの色を設定（0〜255の範囲）

#. LEDストリップの更新:

   * ``led_strip.write()``: LEDストリップに色データを送信し、色を表示

**流れる虹色効果を作ってみよう！**

次に、ランダムに色を生成し、それをストリップ上でシフトさせて、カラフルな流れる光の効果を作成します。

.. code-block:: python

    import machine
    from ws2812 import WS2812
    import utime
    import urandom

    # LEDストリップのLED数
    NUM_LEDS = 8

    # 8個のLEDを持つLEDストリップの初期化
    led_strip = WS2812(machine.Pin(0), NUM_LEDS)

    def flowing_light():
        # 色をストリップ上でシフト
        for i in range(NUM_LEDS - 1, 0, -1):
            led_strip[i] = led_strip[i - 1]
        # 最初のLEDにランダムな色を生成
        led_strip[0] = [urandom.getrandbits(8), urandom.getrandbits(8), urandom.getrandbits(8)]
        # ストリップを更新
        led_strip.write()
        # スムーズなアニメーションのために少し待機
        utime.sleep_ms(100)

    # メインループ
    while True:
        flowing_light()


このコードが実行されると、LEDストリップはランダムな色で流れる動的な効果を表示し、各サイクルで新しいランダムな色がストリップの最初に追加され、最後に向かってシフトします。

**コードの理解**

#. ランダムカラー生成: 各コンポーネントが0〜255の範囲でランダムなRGB色を生成します。

   .. code-block:: python

        [urandom.getrandbits(8), urandom.getrandbits(8), urandom.getrandbits(8)]

#. 色のシフト: 各LEDの色を次の位置に移動させ、流れる効果を作り出します。

   .. code-block:: python

        for i in range(NUM_LEDS - 1, 0, -1):
            led_strip[i] = led_strip[i - 1]

#. 無限ループ: LEDストリップを更新し続けて、アニメーションを実行し続けます。

   .. code-block:: python

        while True:
            flowing_light()

**さらに実験してみよう**

* **速度調整**: ``utime.sleep_ms(100)`` を変更して、流れる効果の速度を速くしたり遅くしたりできます。
* **LEDを増やす**: より長いストリップがある場合、 ``WS2812(machine.Pin(0), number_of_leds)`` の数を変更してください。
* **カスタムアニメーション**: 様々なパターンや色の組み合わせを試して、自分だけのアニメーションを作りましょう。

**結論**

Raspberry Pi Pico 2とMicroPythonを使用してRGB LEDストリップを制御する方法を学びました！これにより、素晴らしい光のディスプレイやムードライト、さらにはインタラクティブなアートプロジェクトを作成するための可能性が広がります。
