.. note:: 

    こんにちは！SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Facebookコミュニティで、Raspberry Pi、Arduino、ESP32について深く学び、愛好者と交流しましょう。

    **なぜ参加するべきか？**

    - **専門的なサポート**: 購入後の問題や技術的な課題を、コミュニティやサポートチームと一緒に解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換し、スキルを向上させましょう。
    - **最新情報の先行公開**: 新製品の発表やプレビューにいち早くアクセスできます。
    - **特別割引**: 最新製品を特別価格で購入できます。
    - **イベントやプレゼント企画**: さまざまなキャンペーンやプレゼント企画に参加できます。

    👉 さあ、一緒に学び、創造しましょう！[|link_sf_facebook|] をクリックして、今すぐ参加！

.. _py_alarm_lamp:

7.3 アラームサイレンランプの作成
=======================================================

このプロジェクトでは、 **Raspberry Pi Pico 2** を使用して **アラームサイレンランプ** を作成します。このデバイスは、警察車両や緊急車両の点滅ライトとサイレン音をシミュレートします。PWM（パルス幅変調）、割り込み処理、LEDやブザーなどの複数のコンポーネントの制御を学ぶ楽しいプロジェクトです。

**必要なもの**

このプロジェクトで使用するコンポーネントは以下のとおりです。

すべての部品を一括で揃える便利なキットはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名称
        - キット内容
        - リンク
    *   - Newton Lab Kit
        - 450点以上
        - |link_newton_lab_kit|


個別に購入する場合は、以下のリンクを利用してください。

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
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 6
        - :ref:`cpn_transistor`
        - 1 (S8050)
        - |link_transistor_buy|
    *   - 7
        - :ref:`cpn_resistor`
        - 3 (1KΩ, 220Ω, 10KΩ)
        - |link_resistor_buy|
    *   - 8
        - パッシブ :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|
    *   - 9
        - :ref:`cpn_capacitor`
        - 1 (104)
        - |link_capacitor_buy|
    *   - 10
        - :ref:`cpn_slide_switch`
        - 1
        - 

**コンポーネントの理解**

* **パッシブブザー**: 外部信号を受けて音を出します。PWMを使用して異なる周波数を生成し、サイレン効果を作り出します。
* **LED**: サイレンの点滅をシミュレートするために、輝度を変化させます。
* **スライドスイッチ**: アラームのON/OFFを切り替えます。
* **NPNトランジスタ (S8050)**: PicoのGPIOピンだけでは十分な電流を供給できないため、ブザーを駆動するために使用します。
* **抵抗とコンデンサ**: スライドスイッチのチャタリング防止と安定した信号取得のために使用します。


**回路図**

|sch_alarm_siren_lamp|

* GP17はスライドスイッチの中央ピンに接続され、10KΩの抵抗とコンデンサ（フィルター）を並列にGNDへ接続することで、スイッチが左右に切り替えられた際に安定したHIGHまたはLOWレベルを出力できるようにします。  
* GP15がHIGHになると、NPNトランジスタが導通し、パッシブブザーが鳴り始めます。このブザーは、周波数が徐々に上昇するようにプログラムされており、サイレン音を再現します。  
* GP16にはLEDが接続され、サイレンの点滅をシミュレートするために、周期的に輝度が変化するようにプログラムされています。  

**配線図**

|wiring_alarm_siren_lamp|


**コードの記述**

MicroPythonスクリプトを作成し、スライドスイッチの状態に応じてブザーとLEDを制御します。

.. note::

    * ``7.3_alarm_siren_lamp.py`` を ``newton-lab-kit/micropython`` から開くか、Thonnyにコードをコピーし、「Run」をクリックするか、F5キーを押してください。
    * インタプリタが MicroPython (Raspberry Pi Pico) COMxx に設定されていることを確認してください。

.. code-block:: python 

    import machine
    import utime

    # ブザーとLED用のPWMを初期化
    buzzer = machine.PWM(machine.Pin(15))
    led = machine.PWM(machine.Pin(16))
    led.freq(1000)  # LEDのPWM周波数を設定

    # スライドスイッチを初期化
    switch = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_DOWN)

    # 値を異なる範囲にマッピングする関数
    def interval_mapping(x, in_min, in_max, out_min, out_max):
        # in_min と in_max が同じ場合、ゼロ除算を防ぐ
        if in_max - in_min == 0:
            return out_min
        return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

    # メインループ
    try:
        while True:
            if switch.value() == 1:
                # アラームON
                # 周波数と輝度を増加
                for i in range(0, 100, 2):
                    # 'i' をLEDの輝度とブザーの周波数にマッピング
                    brightness = interval_mapping(i, 0, 100, 0, 65535)
                    frequency = interval_mapping(i, 0, 100, 500, 2000)
                    
                    # LEDの輝度を設定
                    led.duty_u16(brightness)
                    
                    # ブザーの周波数とデューティサイクルを設定
                    buzzer.freq(frequency)
                    buzzer.duty_u16(32768)  # 50%デューティサイクル
                    
                    utime.sleep(0.01)
                    
                # 周波数と輝度を減少
                for i in range(100, 0, -2):
                    brightness = interval_mapping(i, 0, 100, 0, 65535)
                    frequency = interval_mapping(i, 0, 100, 500, 2000)
                    
                    led.duty_u16(brightness)
                    buzzer.freq(frequency)
                    buzzer.duty_u16(32768)
                    
                    utime.sleep(0.01)
            else:
                # アラームOFF
                # LEDとブザーをオフにする
                led.duty_u16(0)
                buzzer.duty_u16(0)
                utime.sleep(0.1)
    except KeyboardInterrupt:
        # クリーンアップ処理
        buzzer.deinit()
        led.deinit()
        print("Program stopped.")

コードを実行後、スライドスイッチをONに切り替えると、  
ブザーがサイレン音を鳴らし、LEDが点滅します。  
スイッチをOFFにすると、アラームが停止します。

**コードの解説**

#. 初期化:

   * **buzzer**: GP15に接続されたPWMオブジェクト
   * **led**: GP16に接続されたPWMオブジェクト（1kHzで輝度を滑らかに調整）
   * **switch**: GP17に接続された入力ピン（内部プルダウン抵抗付き）

#. 値の範囲マッピング関数:

   ある範囲の値を別の範囲に変換し、ループ変数を周波数や輝度にスケーリングするのに便利。

   .. code-block:: python

        # Function to map values from one range to another
        def interval_mapping(x, in_min, in_max, out_min, out_max):
            # Ensure in_min != in_max to avoid division by zero
            if in_max - in_min == 0:
                return out_min
            return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

#. メインループ:

   * スイッチの状態を確認
   * スイッチがON（ ``switch.value() == 1`` ）の場合:
     
     * 2つのループでサイレン効果を作成:
     * 周波数と輝度の増加
     * 周波数と輝度の減少
     * ブザーの周波数は500Hzから2000Hzまで変化
     * LEDの輝度は消灯から最大輝度まで変化し、再び暗くなる

     .. code-block:: python

        if switch.value() == 1:
            # Alarm is ON
            # Increase frequency and brightness
            for i in range(0, 100, 2):
                # Map 'i' to LED brightness and buzzer frequency
                brightness = interval_mapping(i, 0, 100, 0, 65535)
            ...

                utime.sleep(0.01)

   * スイッチがOFFの場合、LEDとブザーをオフにする。

     .. code-block:: python

            else:
                # Alarm is OFF
                # Turn off LED and buzzer
                led.duty_u16(0)
                buzzer.duty_u16(0)
                utime.sleep(0.1)

   * 例外処理: キーボード割り込み（Ctrl+C）をキャッチし、PWMオブジェクトを適切に終了。

     .. code-block:: python
    
        except KeyboardInterrupt:
            # Clean up
            buzzer.deinit()
            led.deinit()
            print("Program stopped.")

**さらなる実験**

* サイレン効果の調整:

  * ``interval_mapping`` の周波数範囲を変更し、音の高さを調整
  * ループの遅延（ ``utime.sleep(0.01)`` ）を変更して、サイレンの速度を調整

* 追加のLEDを使う:

  * 異なる色のLEDを追加して、よりダイナミックなライト効果を作成
  * 複数のGPIOピンとPWMチャネルを使用

* モーションセンサーを使用:

  スライドスイッチの代わりにPIRセンサーを接続し、動きを検出したときにアラームを作動させる。

* リモート制御の追加:

  赤外線受信モジュールを使用して、リモコンでアラームを制御。


**まとめ**


このプロジェクトでは、Raspberry Pi Pico 2を使ってアラームサイレンランプを構築しました。PWMを活用して、ブザーの周波数とLEDの輝度を制御する方法を学びました。  
この技術を応用すれば、防犯システム、緊急警報、クリエイティブなライトエフェクトなど、さまざまなプロジェクトに活用できます。
