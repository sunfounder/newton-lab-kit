.. note:: 

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者とともにさらに深く学んでいきましょう。

    **参加する理由**

    - **専門家のサポート**: 購入後の問題や技術的な課題をコミュニティとチームのサポートで解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換して、スキルを高めましょう。
    - **独占プレビュー**: 新製品の発表や先行情報をいち早く入手できます。
    - **特別割引**: 最新製品に対する独占割引をお楽しみいただけます。
    - **祝祭プロモーションとギブアウェイ**: ギブアウェイや季節限定のプロモーションに参加できます。

    👉 一緒に探求し、創造してみませんか？今すぐ [|link_sf_facebook|] をクリックして参加しましょう！

.. _py_light_theremin:

7.1 ライト・テルミンの作成
====================================================

このワクワクするプロジェクトでは、Raspberry Pi Pico 2、フォトレジスタ（光センサー）、およびパッシブブザーを使用して **ライト・テルミン** を作成します。テルミンは、物理的に触れることなく演奏できるユニークな楽器で、演奏者の手の位置によって異なる音程を生成します。伝統的なテルミンを完全に再現することはできませんが、光の強さを音の周波数に変換することで、同様の機能をシミュレートできます。

**必要なもの**

このプロジェクトでは、以下のコンポーネントが必要です。

セットを購入するのが便利です。リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名称	
        - セット内容
        - リンク
    *   - Newton Lab Kit	
        - 450+
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
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 6
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 7
        - :ref:`cpn_resistor`
        - 3個（1KΩ、220Ω、10KΩ）
        - |link_resistor_buy|
    *   - 8
        - パッシブ :ref:`cpn_buzzer`
        - 1個
        - 
    *   - 9
        - :ref:`cpn_photoresistor`
        - 1個
        - |link_photoresistor_buy|


**コンセプトの理解**

* **フォトレジスタ**: 光の強さに基づいて抵抗値が変化するセンサー。光が強いと抵抗が低く、光が弱いと抵抗が高くなります。
* **パッシブブザー**: 外部信号を必要とする音を出すデバイス。PWM（パルス幅変調）を使用して周波数を制御できます。
* **トランジスタ（S8050）**: 電流を増幅するために使用し、Picoから効率よくブザーを駆動します。

フォトレジスタからの値を読み取ることで、光の強さを音の周波数にマッピングできます。つまり、手をフォトレジスタの上にかざすと、ブザーから出る音程が変化し、テルミンのように演奏できます。

**回路図**

|sch_light_theremin|

プロジェクトを始める前に、フォトレジスタの上で手を上下に振って、光強度の範囲をキャリブレーションします。GP16に接続されたLEDはデバッグの時間を示し、LEDが点灯しているときはデバッグを開始したことを、消灯しているときはデバッグが終了したことを示します。

GP15が高レベルを出力すると、S8050（NPNトランジスタ）が導通し、パッシブブザーが鳴り始めます。

光が強いと、GP28の値は小さくなり、逆に光が弱いと、値は大きくなります。
フォトレジスタの値を使って、パッシブブザーの周波数を調整することで、光感応デバイスをシミュレートできます。


**配線図**

|wiring_light_theremin|

**コードの記述**

フォトレジスタから光強度を読み取り、それを周波数にマッピングし、ブザーでその周波数を再生するMicroPythonプログラムを作成します。

.. note::

    * ``7.1_light_theremin.py`` を ``newton-lab-kit/micropython`` から開くか、コードをThonnyにコピーして、「実行」ボタンを押すか、F5キーを押して実行してください。
    * 正しいインタープリタ（MicroPython (Raspberry Pi Pico).COMxx）が選択されていることを確認してください。 


.. code-block:: python

    import machine
    import utime

    # コンポーネントの初期化
    led = machine.Pin(16, machine.Pin.OUT)  # GP16に接続されたLED
    photoresistor = machine.ADC(28)         # フォトレジスタ（GP28に接続）
    buzzer = machine.PWM(machine.Pin(15))   # GP15に接続されたブザー

    # キャリブレーション用の変数
    light_low = 65535
    light_high = 0

    # 範囲を別の範囲にマッピングする関数
    def interval_mapping(x, in_min, in_max, out_min, out_max):
        # in_minとin_maxが同じ値でないことを確認（ゼロ除算の防止）
        if in_max - in_min == 0:
            return out_min
        return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

    # ブザーで音を鳴らす関数
    def play_tone(pin, frequency):
        if frequency <= 0:
            pin.duty_u16(0)
        else:
            pin.freq(frequency)
            pin.duty_u16(32768)  # 50%のデューティサイクル

    # キャリブレーションプロセス
    def calibrate():
        global light_low, light_high
        print("Calibrating... Move your hand over the sensor.")
        led.value(1)  # LEDを点灯してキャリブレーション中であることを示す
        start_time = utime.ticks_ms()
        while utime.ticks_diff(utime.ticks_ms(), start_time) < 5000:  # 5秒間キャリブレーション
            light_value = photoresistor.read_u16()
            if light_value > light_high:
                light_high = light_value
            if light_value < light_low:
                light_low = light_value
            utime.sleep_ms(10)
        led.value(0)  # キャリブレーション後、LEDを消灯
        print("Calibration complete.")
        print("Light Low:", light_low)
        print("Light High:", light_high)

    # メイン関数
    def main():
        calibrate()
        try:
            while True:
                light_value = photoresistor.read_u16()
                # 光の値を周波数範囲にマッピング（例: 200Hz ～ 2000Hz）
                frequency = interval_mapping(light_value, light_low, light_high, 200, 2000)
                play_tone(buzzer, frequency)
                utime.sleep_ms(20)
        except KeyboardInterrupt:
            buzzer.deinit()
            print("Program stopped.")

    # メイン関数の実行
    if __name__ == "__main__":
        main()

コードが実行されると、LEDが点灯してキャリブレーション中であることを示します。

* キャリブレーション:

  * 5秒間、フォトレジスタの上で手を動かしてキャリブレーションを行います。
  * これにより、プログラムは光の範囲を把握します。

* テルミンの演奏:

  * キャリブレーションが終わると、LEDは消灯します。
  * フォトレジスタの上に手をかざすと、ブザーから音が鳴り、光強度に応じて音程が変わります。
  * 手の位置や動きで音を作り出してみましょう。


**コードの理解**

#. 初期化:

   * **LEDインジケーター**: キャリブレーション中であることを示すために使用します。
   * **フォトレジスタ**: 光強度に対応するアナログ値を読み取ります。
   * **ブザー**: PWMを使用して、異なる周波数で音を生成します。

#. キャリブレーション関数（ ``calibrate()`` ）:

   * 5秒間実行され、その間に最小値と最大値を記録します。
   * ユーザーに手を動かすよう指示し、光の範囲をキャプチャします。
   * LEDを視覚的なインジケーターとして使用します。

   .. code-block:: python

        # キャリブレーションプロセス
        def calibrate():
            global light_low, light_high
            print("Calibrating... Move your hand over the sensor.")
            led.value(1)  # LEDを点灯してキャリブレーション中であることを示す
            start_time = utime.ticks_ms()
            while utime.ticks_diff(utime.ticks_ms(), start_time) < 5000:  # 5秒間キャリブレーション
                light_value = photoresistor.read_u16()
                if light_value > light_high:
                    light_high = light_value
                if light_value < light_low:
                    light_low = light_value
                utime.sleep_ms(10)
            led.value(0)  # キャリブレーション後、LEDを消灯
            print("Calibration complete.")
            print("Light Low:", light_low)
            print("Light High:", light_high)

#. 範囲マッピング関数（ ``interval_mapping()`` ）:

   * フォトレジスタの値を、ブザー用の周波数範囲にマッピングします。
   * ゼロ除算のエラーを防止します。

   .. code-block:: python

        # 範囲を別の範囲にマッピングする関数
        def interval_mapping(x, in_min, in_max, out_min, out_max):
            # in_minとin_maxが同じ値でないことを確認（ゼロ除算の防止）
            if in_max - in_min == 0:
                return out_min
            return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

#. 音の再生（ ``play_tone()`` ）:

   * PWMを使用してブザーの周波数を設定します。
   * 周波数が0以下の場合、ブザーを停止します。

   .. code-block:: python

        # ブザーで音を鳴らす関数
        def play_tone(pin, frequency):
            if frequency <= 0:
                pin.duty_u16(0)
            else:
                pin.freq(frequency)
                pin.duty_u16(32768)  # 50%のデューティサイクル

#. メインループ:

   * フォトレジスタから光値を継続的に読み取ります。
   * この値を周波数にマッピングします。
   * 周波数に対応する音を再生します。
   * 終了時にはエラーハンドリングを行い、後片付けをします。

   .. code-block:: python

        # メイン関数
        def main():
            calibrate()
            try:
                while True:
                    light_value = photoresistor.read_u16()
                    # 光の値を周波数範囲にマッピング（例: 200Hz ～ 2000Hz）
                    frequency = interval_mapping(light_value, light_low, light_high, 200, 2000)
                    play_tone(buzzer, frequency)
                    utime.sleep_ms(20)
            except KeyboardInterrupt:
                buzzer.deinit()
                print("Program stopped.")

**さらに実験してみましょう**

* 周波数範囲を調整:

  ``interval_mapping()`` 内の値を変更して、音程範囲を広げてみましょう。例えば、200Hz ～ 2000Hzを100Hz ～ 5000Hzに変更してみてください。

* 視覚的なフィードバック:

  ピッチに応じて、追加のLEDを使用して視覚的なフィードバックを提供できます。

* センサーを追加:

  もう一つのフォトレジスタを追加して、音量や他のパラメーターを調整してみましょう。

* 音楽楽器の作成:

  他のセンサーや入力と組み合わせて、より複雑な楽器を作成できます。

**限界の理解**

* 周囲の光:

  周囲の光の変化がパフォーマンスに影響を与える可能性があります。一定の照明を保つか、必要に応じて再キャリブレーションを行ってください。

* センサーの感度:

  フォトレジスタは、急速な手の動きに対して素早く反応しない場合があります。

* 音質:

  パッシブブザーは音質に限界があります。より良い音質を求める場合は、DAC出力付きのアクティブスピーカーの使用を検討してください。

**結論**

Raspberry Pi Pico 2を使ってライト・テルミンを作成することができました！このプロジェクトは、センサーとアクチュエーターを組み合わせて、インタラクティブで楽しい実験を作成する方法を示しています。引き続き、このプロジェクトを探求して、理解と創造力を深めていきましょう。
