.. note:: 

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32をさらに深く学び、仲間と共に楽しんでください。

    **なぜ参加するのか？**

    - **専門家によるサポート**：販売後の問題や技術的な課題をコミュニティやチームのサポートで解決できます。
    - **学びと共有**：スキル向上のためのヒントやチュートリアルを交換しましょう。
    - **限定プレビュー**：新製品の発表や先行情報をいち早く手に入れましょう。
    - **特別割引**：最新の製品に対する限定割引をお楽しみいただけます。
    - **お祭りプロモーションやプレゼントキャンペーン**：プレゼントやキャンペーンに参加できます。

    👉 一緒に探索し、創造していきませんか？ [|link_sf_facebook|] をクリックして今すぐ参加しましょう！

.. _py_tilt:

2.6 傾きセンサー
=======================

このレッスンでは、Raspberry Pi Pico 2を使用して、 **傾きスイッチ** を使い、向きの変化を検出する方法を学びます。傾きスイッチは、垂直か傾いているかを感知する単純なデバイスで、動き検出、向きの感知、位置に基づくトリガーとして役立ちます。

**必要なもの**

このプロジェクトには、以下のコンポーネントが必要です。 

一式で購入するのが便利です。こちらのリンクをご確認ください：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - キット内アイテム
        - リンク
    *   - Newton Lab Kit	
        - 450+
        - |link_newton_lab_kit|


個別に購入したい場合は、以下のリンクから購入できます。


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
        - 1（10KΩ）
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_tilt`
        - 1
        - 

**回路図**

|sch_tilt|

* **直立時（スイッチ閉）**：

  * 傾きスイッチが **3.3V** を **GP14** に直接接続します。
  * GPIOピンは **HIGH** （1）を読み取ります。

* **傾いた時（スイッチ開）**：

  * 傾きスイッチが **3.3V** を **GP14** から切り離します。
  * プルダウン抵抗が **GP14** を **GND** に引き下げます。
  * GPIOピンは **LOW** （0）を読み取ります。

**配線**

|wiring_tilt|

**コードを書く**

傾きスイッチの状態を検出し、スイッチが傾いた際にメッセージを表示する簡単なMicroPythonプログラムを作成します。

.. note::

    * ``2.6_tilt_switch.py`` を ``newton-lab-kit/micropython`` から開くか、コードをThonnyにコピーして、「実行」ボタンを押すか、F5キーを押して実行してください。
    * 適切なインタープリターが選択されていることを確認してください：MicroPython（Raspberry Pi Pico）。COMxx。

.. code-block:: python

    import machine
    import utime

    # GP14を入力ピンとして初期化
    tilt_switch = machine.Pin(14, machine.Pin.IN)

    while True:
        if tilt_switch.value() == 0:
            print("Tilt detected!")
            utime.sleep(1)  # 複数回検出を防ぐために1秒間の遅延を追加

コードを実行すると、以下の現象が観察できます：

* 傾きスイッチを直立させておくと、メッセージは表示されません。
* ブレッドボードやスイッチを傾けると、「傾き検出！」と表示されます。

**コードの理解**

#. モジュールのインポート：

   * ``import machine``: ハードウェアコンポーネントへのアクセスを提供します。
   * ``import utime``: 時間に関連する関数を使用できます。

#. 傾きスイッチのピンの初期化：

   * ``tilt_switch = machine.Pin(14, machine.Pin.IN)``: GP14を入力ピンとして設定します。

#. メインループ：

   * ``while True``: 傾きスイッチの状態を常にチェックする無限ループを作成します。
   * ``if tilt_switch.value() == 0``: GPIOピンがLOW（0）を読み取っている場合、スイッチが傾いていることを示します。
   * ``print("Tilt detected!")``: 傾きが検出された際にメッセージを表示します。
   * ``utime.sleep(1)``: スイッチのチャタリングを防ぐため、1秒間の遅延を追加します。

**内部プルダウン抵抗を使用した代替配線**

Raspberry Pi Pico 2では、内部プルアップまたはプルダウン抵抗を有効にすることで、外部抵抗を使用せずに済みます。

.. code-block:: python

    import machine
    import utime

    # GP14を内部プルダウン抵抗付きの入力ピンとして初期化
    tilt_switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

    while True:
        if tilt_switch.value() == 1:
            print("Tilt detected!")
            utime.sleep(1)

内部プルダウン抵抗（ ``machine.Pin.PULL_DOWN`` ）を有効にすることで、GPIOピンは電圧がかかっていないときにデフォルトでLOWになります。
傾きスイッチが直立していると（閉じていると）、3.3VをGP14に接続し、ピンはHIGH（1）を読み取ります。

**実践的な応用**

* **向き検出**：デバイスが直立しているか、傾いているかを判定できます。
* **動き検出によるイベント発生**：動きが検出されたときにアラームや通知、アクションを起動できます。
* **インタラクティブプロジェクト**：傾きに反応するゲームやインタラクションを制御するための入力として使用できます。

**さらに実験してみよう**

* LEDインジケーターを追加：

別のGPIOピン（例：GP15）にLEDを接続し、適切な抵抗を挟んで、傾きが検出された際にLEDを点灯させるコードを変更しましょう。

.. code-block:: python

    import machine
    import utime

    tilt_switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
    led = machine.Pin(15, machine.Pin.OUT)

    while True:
        if tilt_switch.value() == 1:
            print("Tilt detected!")
            led.value(1)  # LEDを点灯
            utime.sleep(1)
        else:
            led.value(0)  # LEDを消灯

* 他のセンサーとの組み合わせ：

  傾きスイッチを他のセンサー（例：ボタンや光センサー）と組み合わせて、より複雑なインタラクションを実現しましょう。

**結論**

傾きスイッチをRaspberry Pi Pico 2のプロジェクトに組み込むことで、向きや動きに基づいた新たなインタラクションを追加できます。傾きスイッチのようなデジタル入力センサーを読み取る方法を理解することで、動的で反応的な電子機器を作成する能力が広がります。
