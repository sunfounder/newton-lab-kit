.. note:: 

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、仲間たちとさらに深く学びましょう。

    **参加する理由は？**

    - **専門家のサポート**：販売後の問題や技術的な課題を、コミュニティやチームからのサポートで解決できます。
    - **学び・共有**：ヒントやチュートリアルを交換して、スキルを向上させましょう。
    - **限定プレビュー**：新製品の発表や先行情報をいち早くゲット。
    - **特別割引**：最新製品の特別割引を楽しめます。
    - **イベントプロモーションとプレゼント**：プレゼント企画やホリデープロモーションに参加しましょう。

    👉 一緒に探求して創造しませんか？[|link_sf_facebook|]をクリックして、今すぐ参加！

.. _py_ultrasonic:

6.1 超音波センサーを使った距離の測定
================================================

このレッスンでは、Raspberry Pi Pico 2を使用して、 **超音波センサーモジュール** を使った距離の測定方法を学びます。超音波センサーは、ロボット工学や自動化システムで物体検出や距離測定に広く使用されています。

**必要なもの**

このプロジェクトで必要なコンポーネントは以下の通りです。

一式を購入するのが便利です。リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - このキットのアイテム
        - リンク
    *   - Newton Lab Kit	
        - 450+
        - |link_newton_lab_kit|

個別に購入することもできます。以下のリンクからどうぞ。

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
        - :ref:`cpn_ultrasonic`
        - 1
        - |link_ultrasonic_buy|

**超音波センサーの理解**

超音波センサーは、 **Trig** ピンから短い超音波パルスを発信し、 **Echo** ピンでそのエコーを受信することで動作します。エコーが返ってくるまでの時間を測定することで、音速を使って物体までの距離を計算できます。

|ultrasonic_prin|

* **トリガーパルス**：Trigピンに10マイクロ秒の高いパルスを送信し、測定を開始します。
* **超音波バースト**：センサーは40 kHzで8サイクルの超音波バーストを発信します。
* **エコー受信**：Echoピンが高くなり、エコーが返ってくるまでその状態が続きます。
* **時間測定**：Echoピンが高い状態でいる時間を測定し、その時間を使って距離を計算します。

**回路図**

|sch_ultrasonic|

**配線図**

|wiring_ultrasonic|


**コードの作成**

超音波センサーを使用して距離を測定するためのMicroPythonプログラムを作成しましょう。

.. note::

    * ``6.1_measuring_distance.py`` を ``newton-lab-kit/micropython`` から開くか、コードをThonnyにコピーして「実行」をクリックするか、F5を押してください。
    * 正しいインタープリタを選択していることを確認してください：MicroPython（Raspberry Pi Pico）。COMxx。

.. code-block:: python

    import machine
    import utime

    # センサーに接続されたピンを定義
    TRIG = machine.Pin(17, machine.Pin.OUT)
    ECHO = machine.Pin(16, machine.Pin.IN)

    def measure_distance():
        # トリガーピンを低くしておく
        TRIG.low()
        utime.sleep_us(2)
        # 測定を開始するために10µsのパルスを送信
        TRIG.high()
        utime.sleep_us(10)
        TRIG.low()
        
        # Echoピンが高くなるのを待機（エコーパルスの開始）
        while ECHO.value() == 0:
            pass
        start_time = utime.ticks_us()
        
        # Echoピンが低くなるのを待機（エコーパルスの終了）
        while ECHO.value() == 1:
            pass
        end_time = utime.ticks_us()
        
        # エコーパルスの時間を計算
        duration = utime.ticks_diff(end_time, start_time)
        
        # 距離を計算（音速は34300 cm/s）
        distance = (duration * 0.0343) / 2
        return distance

    while True:
        dist = measure_distance()
        print("Distance: {:.2f} cm".format(dist))
        utime.sleep(0.5)

コードが実行されると、Thonny Shellにセンチメートル単位で距離の測定値が表示されます。物体をセンサーに近づけたり離したりして、読み取り値が変わるのを確認できます。

**コードの理解**

#. 必要なモジュールをインポートし、トリガーピンとエコーピンを設定：

   .. code-block:: python
   
       import machine
       import utime
   
       TRIG = machine.Pin(17, machine.Pin.OUT)
       ECHO = machine.Pin(16, machine.Pin.IN)


#. 距離の測定：

   * トリガーパルスを送信して測定を開始します。
   * エコーの応答を待ちます。
   * エコーパルスの時間を計算します。
   * 音速を使って距離を計算します。

   .. code-block:: python

       def measure_distance():
           # トリガーを低くしておく
           TRIG.low()
           utime.sleep_us(2)
           # 10µsのパルスをトリガー
           TRIG.high()
           utime.sleep_us(10)
           TRIG.low()
           
           # エコーの開始を待つ
           while ECHO.value() == 0:
               pass
           start_time = utime.ticks_us()
           
           # エコーの終了を待つ
           while ECHO.value() == 1:
               pass
           end_time = utime.ticks_us()
           
           # 時間を計算
           duration = utime.ticks_diff(end_time, start_time)
           # 距離を計算
           distance = (duration * 0.0343) / 2
           return distance


#. メインループ：

   * 距離を継続的に測定し、表示します。
   * 測定の間に0.5秒の間隔を置きます。

   .. code-block:: python
   
       while True:
           dist = measure_distance()
           print("Distance: {:.2f} cm".format(dist))
           utime.sleep(0.5)

**制限事項の理解**


* ブロッキングコード：

  * エコーを待つためのwhileループは、他のコードの実行をブロックすることがあります。
  * より高度なアプリケーションでは、割り込みや非同期プログラミングを使用して、ブロックを避けることを検討してください。

* 測定範囲：

  * HC-SR04センサーは通常、2 cmから400 cmの範囲で動作します。
  * 2 cm未満または400 cm以上の物体は、正確に検出できないことがあります。

* 環境要因：

  * 温度や湿度は音速に影響を与えることがあります。
  * 精密な測定を行う場合は、周囲の条件に応じて音速を調整してください。

**結論**

あなたはRaspberry Pi Pico 2
