.. note:: 

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者と一緒にさらに深く学びましょう。

    **参加する理由**

    - **専門家のサポート**: 購入後の問題や技術的な課題を、コミュニティやチームのサポートを受けて解決できます。
    - **学び・共有**: ヒントやチュートリアルを交換して、スキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先行公開情報をいち早く手に入れましょう。
    - **特別割引**: 新製品に対する特別割引を楽しめます。
    - **祝祭キャンペーンやプレゼント**: プレゼントキャンペーンやシーズンプロモーションに参加できます。

    👉 一緒に探求し、創造的な活動をしてみませんか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _py_reversing_aid:

7.10 後方支援システムの構築
=============================

このプロジェクトでは、Raspberry Pi Pico 2、超音波センサー、LED、ブザーを使用して **後方支援システム** を作成します。このシステムは、実際の駐車センサーがどのように動作するかを模倣し、障害物との距離を検出して、接近に応じて音と視覚的なフィードバックを提供します。このセットアップをラジコンカーに取り付けて、ガレージにバックする体験を模倣することができます。

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
        - 450以上
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
        - 2(1KΩ, 220Ω)
        - |link_resistor_buy|
    *   - 7
        - Active :ref:`cpn_buzzer`
        - 1
        - 
    *   - 8
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 9
        - :ref:`cpn_ultrasonic`
        - 1
        - |link_ultrasonic_buy|

**部品の理解**

* **超音波センサー (HC-SR04):** 超音波を発信し、エコーが戻ってくるまでの時間を測定して、障害物までの距離を計測します。
* **ブザー:** 音でフィードバックを提供し、物体が近づくほど頻繁に鳴ります。
* **LED:** 視覚的なフィードバックを提供し、物体が近づくほど点滅が速くなります。

**回路図**

|sch_reversing_aid|

**配線図**

|wiring_reversing_aid|


**コード作成**

次のMicroPythonスクリプトを作成します：

* 超音波センサーで距離を計測する。
* 距離に応じてブザーの音の頻度やLEDの点滅速度を調整する。
* 物体が近づいたり離れたりするごとに継続的なフィードバックを提供する。

.. note::

    * ``7.10_reversing_aid.py`` を ``newton-lab-kit/micropython`` から開くか、コードをThonnyにコピーして、「実行」ボタンをクリックするか、F5キーを押して実行します。

    * 正しいインタプリタが選択されていることを確認してください：MicroPython（Raspberry Pi Pico）。COMxx。 

.. code-block:: python

    import machine
    import utime

    # ピンの設定
    trigger = machine.Pin(17, machine.Pin.OUT)
    echo = machine.Pin(16, machine.Pin.IN)
    buzzer = machine.Pin(15, machine.Pin.OUT)
    led = machine.Pin(14, machine.Pin.OUT)

    # 距離を計測する関数
    def measure_distance():
        # トリガーを低に設定
        trigger.low()
        utime.sleep_us(2)
        # トリガーに10usのパルスを送信
        trigger.high()
        utime.sleep_us(10)
        trigger.low()

        # エコーパルスの長さを測定
        while echo.value() == 0:
            signaloff = utime.ticks_us()
        while echo.value() == 1:
            signalon = utime.ticks_us()

        timepassed = utime.ticks_diff(signalon, signaloff)
        distance = (timepassed * 0.0343) / 2  # cmに変換
        return distance

    # ブザーとLEDを制御する関数
    def alert(interval):
        buzzer.high()
        led.high()
        utime.sleep(0.1)
        buzzer.low()
        led.low()
        utime.sleep(interval)

    # メインループ
    try:
        while True:
            dist = measure_distance()
            print("Distance: {:.2f} cm".format(dist))
            if dist < 0:
                print("Out of range")
                utime.sleep(1)
            elif dist <= 10:
                alert(0.2)  # 非常に近い、迅速にアラート
            elif dist <= 20:
                alert(0.5)  # 近い、適度にアラート
            elif dist <= 50:
                alert(1)    # あまり近くない、ゆっくりアラート
            else:
                alert(2)    # 遠い、まれにアラート
    except KeyboardInterrupt:
        print("Measurement stopped by User")

コードが実行されたら、超音波センサーから異なる距離で物体を配置して、ブザーの音の頻度とLEDの点滅速度の変化を観察しましょう。
コンソールには計測された距離が表示されます。

**コードの理解**

#. 距離の計測:

   * ``measure_distance()`` 関数は、TRIGピンに10マイクロ秒のパルスを送信します。
   * 次に、ECHOピンがハイになってからローになるまでの時間を測定します。
   * 超音波パルスが戻るまでの時間に基づいて、距離を計算します。

   .. code-block:: python

        def measure_distance():
            # トリガーを低に設定
            trigger.low()
            utime.sleep_us(2)
            # トリガーに10usのパルスを送信
            trigger.high()
            utime.sleep_us(10)
            trigger.low()

            # エコーパルスの長さを測定
            while echo.value() == 0:
                signaloff = utime.ticks_us()
            while echo.value() == 1:
                signalon = utime.ticks_us()

            timepassed = utime.ticks_diff(signalon, signaloff)
            distance = (timepassed * 0.0343) / 2  # cmに変換
            return distance


#. アラート関数:

   * ``alert(interval)`` 関数は、ブザーとLEDを0.1秒間オンにして、その後オフにします。
   * ``interval`` パラメータは、距離に応じてアラートの間隔を調整します。

   .. code-block:: python

        def measure_distance():
            # トリガーを低に設定
            trigger.low()
            utime.sleep_us(2)
            # トリガーに10usのパルスを送信
            trigger.high()
            utime.sleep_us(10)
            trigger.low()

            # エコーパルスの長さを測定
            while echo.value() == 0:
                signaloff = utime.ticks_us()
            while echo.value() == 1:
                signalon = utime.ticks_us()

            timepassed = utime.ticks_diff(signalon, signaloff)
            distance = (timepassed * 0.0343) / 2  # cmに変換
            return distance

#. メインループ:

   * 距離を継続的に計測します。
   * あらかじめ設定された距離の閾値に応じて、アラートの頻度を調整します。

   .. code-block:: python

        try:
            while True:
                dist = measure_distance()
                print("Distance: {:.2f} cm".format(dist))
                if dist < 0:
                    print("Out of range")
                    utime.sleep(1)
                elif dist <= 10:
                    alert(0.2)  # 非常に近い、迅速にアラート
                elif dist <= 20:
                    alert(0.5)  # 近い、適度にアラート
                elif dist <= 50:
                    alert(1)    # あまり近くない、ゆっくりアラート
                else:
                    alert(2)    # 遠い、まれにアラート
        except KeyboardInterrupt:
            print("Measurement stopped by User")
        
**安全対策**

* 電圧レベル:

  * 超音波センサーのECHOピン電圧が5Vの場合は注意してください。
  * PicoのGPIOピンを保護するために、電圧分割器やレベルシフターを使用してください。

* 電源:

  すべての部品の電流要件を満たせる電源を使用してください。

**さらに実験する**

* 視覚表示:

  LCDやOLEDディスプレイを追加して、距離を視覚的に表示できます。

* 複数のセンサー:

  複数の超音波センサーを使用して、より多くの方向をカバーできます。

* 高度なアラート:

  ブザーに異なるトーンやパターンを実装して、距離ごとに異なるアラートを出すことができます。

**結論**

Raspberry Pi Pico 2を使用して、後方支援システムを構築しました！このプロジェクトは、センサーを使ってリアルタイムのフィードバックを提供する方法を示しており、ロボティクスやオートメーションの基本的な概念を学ぶことができます。
