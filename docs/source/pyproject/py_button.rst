.. note:: 

    こんにちは！SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！  
    Facebookコミュニティで、Raspberry Pi、Arduino、ESP32について深く学び、愛好者と交流しましょう。

    **なぜ参加するべきか？**

    - **専門的なサポート**: 購入後の問題や技術的な課題を、コミュニティやサポートチームと一緒に解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換し、スキルを向上させましょう。
    - **最新情報の先行公開**: 新製品の発表やプレビューにいち早くアクセスできます。
    - **特別割引**: 最新製品を特別価格で購入できます。
    - **イベントやプレゼント企画**: さまざまなキャンペーンやプレゼント企画に参加できます。

    👉 さあ、一緒に学び、創造しましょう！[|link_sf_facebook|] をクリックして、今すぐ参加！

.. _py_button:

2.5 ボタン入力の読み取り
=============================

このレッスンでは、Raspberry Pi Pico 2 を使用してプッシュボタンの入力を読み取る方法を学びます。  
これまで、GPIOピンは主にLEDの点灯などの出力に使用してきましたが、今回はGPIOピンを入力として設定し、ボタンが押されたことを検出します。  
これは、インタラクティブなプロジェクトを作成する上での基本スキルとなります。


**必要なもの**

このプロジェクトでは、以下のコンポーネントを使用します。

すべての部品が揃った便利なキットはこちら：

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
        - :ref:`cpn_resistor`
        - 1 (10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_button`
        - 1
        - |link_button_buy|


**回路図**

|sch_button|

ボタンの片方のピンを3.3Vに接続し、もう片方のピンをGP14に接続すると、ボタンが押されたときにGP14はHIGHになります。しかし、ボタンが押されていない場合、GP14は浮いた状態（不安定な状態）になり、HIGHまたはLOWのどちらにもなり得ます。ボタンが押されていないときにGP14を安定してLOWにするためには、10KΩのプルダウン抵抗を介してGNDに接続する必要があります。

* **ボタン未押下**: GP14はGNDに接続され、 **LOW (0)** を読み取る。  
* **ボタン押下時**: GP14は3.3Vに接続され、 **HIGH (1)** を読み取る。

**配線図**

4ピンのボタンは "H" の形をしており、左右の2ピンずつが内部で接続されています。 

ボタンを押すと、中央のギャップをまたいで2つの独立した行が接続されます。

|wiring_button|


**コードの記述**

ボタンが押されたときにメッセージを出力するシンプルなプログラムを書いてみましょう。

.. note::

  * ``2.5_read_button_value.py`` を ``newton-lab-kit/micropython`` から開くか、Thonnyにコードをコピーし、「Run」をクリックするか、F5キーを押してください。
  * インタプリタがMicroPython (Raspberry Pi Pico) COMxxに設定されていることを確認してください。

.. code-block:: python

    import machine
    import utime

    # GP14を入力ピンとして初期化
    button = machine.Pin(14, machine.Pin.IN)

    while True:
        if button.value() == 1:
            print("Button pressed!")
            utime.sleep(0.2)  # デバウンス処理

コードを実行すると、以下の動作が確認できます：

* **ボタン未押下**: 何も表示されない。  
* **ボタン押下**: "ボタンが押されました！" のメッセージが表示される。



**コードの解説**

#. モジュールのインポート:

   * ``machine``: ハードウェア制御のための機能を提供。
   * ``utime``: 時間関連の関数（遅延処理など）を提供。

#. ボタンピンの設定:

   * ``button = machine.Pin(14, machine.Pin.IN)``: GPIO 14を入力ピンとして初期化。

#. メインループ:

* ``while True``: 無限ループを作成します。  
   * ``if button.value() == 1``: ボタンが押されているかを確認します。  
   * ``button.value()`` が1を返すとき、ピンがHIGH（ボタンが押された状態）になっています。  
   * ``print("Button pressed!")``: コンソールにメッセージを表示します。  
   * ``utime.sleep(0.2)``: ボタンのデバウンス処理として200ミリ秒待機します。  

**別の配線方法: プルアップ抵抗を使用する**

ボタンの配線はプルアップ抵抗を使用して設定することもできます。

#. 10KΩ抵抗をGP14と3.3Vの間に接続すると、ボタンが押されていないときにGP14がHIGH (1)になります。

    |sch_button_pullup|

    |wiring_button_pullup|

   * **ボタン未押下**: GP14は3.3Vに接続され、HIGH (1)を読み取る。  
   * **ボタン押下**: GP14はGNDに接続され、LOW (0)を読み取る。  

#. プルアップ設定に対応するコード

   .. code-block:: python
   
       import machine
       import utime
   
       # GP14を入力ピンとして初期化
       button = machine.Pin(14, machine.Pin.IN)
   
       while True:
           if button.value() == 0:
               print("Button pressed!")
               utime.sleep(0.2)

**Using Internal Pull-Up/Pull-Down Resistors** 

Raspberry Pi Pico 2 では、内部プルアップ抵抗やプルダウン抵抗を有効にすることができ、外部抵抗を使用せずに回路を構成できます。

内部抵抗を利用することで、配線が簡単になり、ブレッドボード上の外部抵抗を減らすことでスペースを節約できます。

* 内部プルダウン抵抗を有効にする:

  .. code-block:: python
  
      import machine
      import utime
  
      # GP14を内部プルダウン抵抗付きの入力ピンとして初期化
      button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
  
      while True:
          if button.value() == 1:
              print("Button pressed!")
              utime.sleep(0.2)

* 内部プルアップ抵抗を有効にする:

  .. code-block:: python

    import machine
    import utime

    # GP14を内部プルアップ抵抗付きの入力ピンとして初期化
    button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)

    while True:
        if button.value() == 0:
            print("Button pressed!")
            utime.sleep(0.2)

**Experimenting Further**

* **複数のボタンを接続**: 複数のGPIOピンにボタンを接続し、コードを変更して複数の入力を処理できるようにする。
* **LED制御**: ボタンの入力とLEDの出力を組み合わせ、ボタンが押されたときにLEDの状態を切り替える。

.. code-block:: python

    import machine
    import utime

    button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
    led = machine.Pin(15, machine.Pin.OUT)
    led_state = False

    while True:
        if button.value() == 1:
            led_state = not led_state  # LEDの状態をトグル
            led.value(led_state)
            utime.sleep(0.2)

**Conclusion**

マイコンプログラミングにおいて、ボタンの入力を読み取ることは基本的なスキルです。  
これにより、プロジェクトをインタラクティブにし、ユーザーの入力に応じて動作させることができます。  
プルアップ抵抗とプルダウン抵抗の使い方を理解することで、安定した入力信号を取得し、信頼性の高いシステムを構築できます。
