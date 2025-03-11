.. note:: 

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者と一緒に深く学んでいきましょう。

    **参加する理由**

    - **専門家のサポート**: コミュニティやチームから、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換し、スキルを向上させましょう。
    - **独占プレビュー**: 新製品の発表や先行情報をいち早く入手できます。
    - **特別割引**: 最新製品に対する独占割引をお楽しみいただけます。
    - **祝祭プロモーションとギブアウェイ**: ギブアウェイや季節限定のプロモーションに参加できます。

    👉 一緒に探求し、創造しませんか？今すぐ [|link_sf_facebook|] をクリックして参加しましょう！

.. _py_led_bar:

2.2 レベルを表示する
=============================

このレッスンでは、Raspberry Pi Pico 2を使用してLEDバーグラフを制御する方法を学びます。LEDバーグラフは、10個のLEDが並んだもので、通常は音量や信号強度、その他の測定値などのレベルを表示するために使用されます。LEDを順番に点灯させて、レベル表示のエフェクトを作成します。

|img_led_bar_pin|


**必要なもの**

このプロジェクトには、以下のコンポーネントが必要です。

セットを購入するのが便利です。リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名称	
        - キット内容
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
        - :ref:`cpn_resistor`
        - 10個（220Ω）
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led_bar`
        - 1
        - 

**回路図**

|sch_ledbar|

このプロジェクトでは、LEDバーグラフの10個のLEDそれぞれがRaspberry Pi Pico 2に接続されています。LEDのアノード（正端子）はGPIOピンのGP6からGP15に接続され、カソード（負端子）は220Ωの抵抗を通してGND（グラウンド）ピンに接続されます。

**配線図**

|wiring_ledbar|

**コードの記述**

.. note::

  * ``2.2_display_the_level.py`` ファイルを ``newton-lab-kit/micropython`` パスから開くか、以下のコードをThonnyにコピーして「実行」ボタンを押すか、 **F5** キーを押して実行してください。
  * Thonnyの右下にある「MicroPython (Raspberry Pi Pico).COMxx」インタープリタが選択されていることを確認してください。

.. code-block:: python

  import machine
  import utime

  # LEDに接続されているGPIOピンを定義
  pins = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
  leds = []

  # 各ピンを出力として初期化し、ledsリストに格納
  for pin_number in pins:
      led = machine.Pin(pin_number, machine.Pin.OUT)
      leds.append(led)

  while True:
      # LEDを1つずつ点灯させてレベルの上昇をシミュレート
      for led in leds:
          led.value(1)  # LEDを点灯
          utime.sleep(0.2)
      # LEDを1つずつ消灯させてレベルの下降をシミュレート
      for led in leds:
          led.value(0)  # LEDを消灯
          utime.sleep(0.2)

プログラムを実行すると、LEDバーグラフのLEDが最初から最後まで順番に点灯し、レベルが上昇するエフェクトが作成されます。その後、LEDは1つずつ消灯し、レベルが下降するエフェクトがシミュレートされます。

**コードの理解**

このプロジェクトでは、MicroPythonでリストとループを使用して複数のLEDを制御しており、コードが効率的で読みやすくなっています。

コードの重要な部分を分解してみましょう：

1. モジュールのインポート：

   * ``import machine``: Raspberry Pi Pico 2のハードウェア機能にアクセスするためのモジュール。
   * ``import utime``: 遅延などの時間関連の関数を使用するためのモジュール。

2. ピンの定義とLEDの初期化：

   * ``pins`` リストにLEDに接続されているGPIOピン番号を格納し、空のリスト ``leds`` を作成してLEDオブジェクトを格納します。

     .. code-block:: python

      # LEDに接続されているGPIOピンを定義
      pins = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
      leds = []
     
   * ``for`` ループを使って、各ピン番号に対して出力ピンを設定し、対応する ``Pin`` オブジェクトを ``leds`` リストに追加します。
     
     .. code-block:: python

        for pin_number in pins:
            led = machine.Pin(pin_number, machine.Pin.OUT)
            leds.append(led)
     
3. レベル表示エフェクトの作成：

   * ``while True:`` ループは無限に実行されます。
   * レベルの上昇：

     * ``for`` ループを使って ``leds`` リスト内の各 ``led`` に対して処理を行います。
     * ``led.value(1)`` でLEDを点灯させます。
     * ``utime.sleep(0.2)`` で次のLEDを点灯させる前に200msの遅延を加えます。
     
     .. code-block:: python

        for led in leds:
            led.value(1)
            utime.sleep(0.2)
     
   * レベルの下降：

     * 別の ``for`` ループを使って、各LEDを1つずつ消灯します。
     * ``led.value(0)`` でLEDを消灯させます。

     .. code-block:: python

        for led in leds:
            led.value(0)
            utime.sleep(0.2)

**さらに実験してみましょう**

コードを使って、以下のように実験をしてみましょう：

* 速度を変更する：

  * ``utime.sleep(0.2)`` の遅延時間を調整することで、LEDの点灯速度を速くしたり遅くしたりできます。

* 順番を逆にする：

  * ``reversed(leds)`` を使って、LEDの順番を逆にできます。

    .. code-block:: python

        for led in reversed(leds):
            led.value(1)
            utime.sleep(0.2)
    
* ピンポンエフェクトを作成する：

  * LEDを左から右へ、そして右から左へ点灯させるエフェクトを作成します。

    .. code-block:: python

        while True:
            for led in leds:
                led.value(1)
                utime.sleep(0.1)
            for led in reversed(leds):
                led.value(0)
                utime.sleep(0.1)

**結論**

各LEDを個別に制御することによって、Raspberry Pi Pico 2を使用してシンプルで効果的なレベル表示を作成しました。このプロジェクトは、Pythonのリストとループを活用し、複数の出力を効率的に管理する方法を示しています。

複数のGPIOピンを使いこなし、リストやループといったプログラミング構造を使うことは、アニメーション作成、複数のセンサー制御、インタラクティブなデバイス作成など、より複雑なプロジェクトに必要不可欠です。

**参考文献**

* |link_python_for|
* |link_python_list|
