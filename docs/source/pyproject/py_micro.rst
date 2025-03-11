.. note:: 

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者とともにさらに深く学んでいきましょう。

    **参加する理由**

    - **専門家のサポート**: 購入後の問題や技術的な課題をコミュニティとチームのサポートで解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換して、スキルを高めましょう。
    - **独占プレビュー**: 新製品の発表や先行情報をいち早く入手できます。
    - **特別割引**: 最新製品に対する独占割引をお楽しみいただけます。
    - **祝祭プロモーションとギブアウェイ**: ギブアウェイや季節限定のプロモーションに参加できます。

    👉 一緒に探求し、創造してみませんか？今すぐ [|link_sf_facebook|] をクリックして参加しましょう！

.. _py_micro:

2.8 優しく押して
==========================

このレッスンでは、Raspberry Pi Pico 2を使用して **マイクロスイッチ** （別名リミットスイッチ）を使い、スイッチが押されたかリリースされたかを検出する方法を学びます。マイクロスイッチは、電子レンジのドアやプリンターのカバー、3Dプリンターのエンドストップなど、信頼性が高く、頻繁に使用できるため、さまざまなデバイスで広く使われています。

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
        - 1個（10KΩ）
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_capacitor`
        - 1個（104）
        - |link_capacitor_buy|
    *   - 7
        - :ref:`cpn_micro_switch`
        - 1個
        - 

**マイクロスイッチの理解**

マイクロスイッチには通常3つのピンがあります：

|img_micro_switch|

- **共通端子 (C)**: 中央のピン。
- **通常開端子 (NO)**: スイッチが **押された時** に共通端子に接続されます。
- **通常閉端子 (NC)**: スイッチが **押されていない時** に共通端子に接続されます。

スイッチを適切に接続することで、GPIOピンで電圧レベルを読み取ることにより、スイッチが押されたかどうかを検出できます。

**回路図**

|sch_limit_sw|

デフォルトでは、GP14は低（LOW）で、押された時にGP14は高（HIGH）になります。

10KΩの抵抗の目的は、スイッチを押したときにGP14が低い状態を維持することです。

機械式スイッチを押すと、接点がバウンスすることがあり、開閉状態が素早く繰り返し変わることがあります。GP14とGNDの間に接続されたコンデンサは、このノイズを除去するのに役立ちます。

* **スイッチが押されていない場合**：

  * **共通端子 (C)** は **NC端子** に接続され、これは **GND** に接続されます。
  * **GP14** は **LOW** （0V）を読み取ります。

* **スイッチが押された場合**：

  * **共通端子 (C)** は **NO端子** に接続され、これは **3.3V** に接続されます。
  * **GP14** は **HIGH** （3.3V）を読み取ります。

**配線図**

|wiring_limit_sw|


**コードの記述**

マイクロスイッチが押されたかどうかを検出し、その結果に応じてメッセージを表示するMicroPythonプログラムを作成します。

.. note::

  * ``2.8_micro_switch.py`` を ``newton-lab-kit/micropython`` から開くか、コードをThonnyにコピーして、「実行」ボタンを押すか、F5キーを押して実行してください。

  * 正しいインタープリタが選択されていることを確認してください：MicroPython (Raspberry Pi Pico).COMxx。

  

.. code-block:: python

    import machine
    import utime

    # GP14を入力ピンとして初期化
    switch = machine.Pin(14, machine.Pin.IN)

    while True:
        if switch.value() == 1:
            print("The switch is pressed!")
            utime.sleep(0.5)  # デバウンス遅延

コードが実行されると、次の現象が観察されます：

* **押されていない場合**: メッセージは表示されません。
* **押された場合**: スイッチを押すたびに、「スイッチが押されました！」というメッセージがコンソールに表示されます。

**コードの理解**

#. モジュールのインポート：

   * ``import machine``: ハードウェア機能にアクセスするためのモジュール。
   * ``import utime``: 時間関連の機能を使用するためのモジュール。

#. スイッチピンの初期化：

   * ``switch = machine.Pin(14, machine.Pin.IN)``: GP14を入力ピンとして設定します。

#. メインループ：

   * ``while True``: 無限ループを開始します。
   * ``if switch.value() == 1``: スイッチが押されたかどうかを確認します（GP14がHIGHを読み取ります）。
   * ``print("The switch is pressed!")``: メッセージをコンソールに出力します。
   * ``utime.sleep(0.5)``: スイッチのデバウンスを防ぐために遅延を加えます。


**代替配線：内部プルダウン抵抗を使用する方法**

配線をさらに簡素化したい場合は、内部プルダウン抵抗のみを使用することもできます。

* 回路の変更：

  * 外部の10kΩ抵抗と0.1µFコンデンサを取り外します。
  * マイクロスイッチ接続：

    * **共通端子 (C)**: GP14に接続します。
    * **通常開端子 (NO)**: 3.3Vに接続します。
    * **通常閉端子 (NC)**: 接続しません。

* 修正コード：

  .. code-block:: python

      import machine
      import utime

      # 内部プルダウン抵抗を使用してGP14を入力ピンとして初期化
      switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

      while True:
          if switch.value() == 1:
              print("The switch is pressed!")
              utime.sleep(0.5)  # デバウンス遅延
  

**実用的な応用**

* **リミット検出**: マイクロスイッチをCNCマシンや3Dプリンターのエンドストップとして使用し、移動の限界を検出します。
* **安全インターロック**: 特定の条件（例：ドアが閉まっていること）が満たされたときのみデバイスが動作するようにします。
* **ユーザー入力**: 頑丈で信頼性の高いボタンが必要なプロジェクトに組み込みます。

**さらに実験してみましょう**

* LEDを制御する：

  他のGPIOピン（例えばGP15）にLEDを接続し、スイッチが押されたときにLEDが点灯するようにコードを変更します。
  
  .. code-block:: python
    
    import machine
    import utime

    switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
    led = machine.Pin(15, machine.Pin.OUT)

    while True:
        if switch.value() == 1:
            led.value(1)  # LEDを点灯
            print("The switch is pressed!")
            utime.sleep(0.5)
        else:
            led.value(0)  # LEDを消灯

* 押された回数をカウント：

  コードを修正して、スイッチが何回押されたかをカウントします。

  * LEDを制御：

   .. code-block:: python

      import machine
      import utime

      switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
      count = 0

      while True:
          if switch.value() == 1:
              count += 1
              print("Switch pressed {} times".format(count))
              utime.sleep(0.5)

**結論**

Raspberry Pi Pico 2とマイクロスイッチを使用することで、物理的なインタラクションを確実に検出することができます。スイッチをどのように配線し、その状態をコードで読み取るかを理解することは、反応的でインタラクティブなプロジェクトを作成するために不可欠です。
