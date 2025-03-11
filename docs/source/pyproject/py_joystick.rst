.. note:: 

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Raspberry Pi、Arduino、ESP32についてさらに深く学び、他の愛好者と共に探求しましょう。

**参加する理由**

- **専門家のサポート**: コミュニティとチームからのサポートを受けて、購入後の問題や技術的な課題を解決できます。
- **学びと共有**: ヒントやチュートリアルを交換し、スキルを向上させましょう。
- **独占プレビュー**: 新製品の発表や先行情報をいち早くゲット。
- **特別割引**: 最新製品に対する独占割引を楽しめます。
- **祝祭プロモーションとギブアウェイ**: ギブアウェイや季節限定のプロモーションに参加しましょう。

👉 一緒に探求し、創造しませんか？今すぐ [|link_sf_facebook|] をクリックして参加しましょう！

.. _py_joystick:

4.1 ジョイスティックからの値の読み取り
======================================

このレッスンでは、Raspberry Pi Pico 2を使用して **ジョイスティック** を使い、アナログ値の読み取りとボタンの押下を検出する方法を学びます。ジョイスティックは、2軸（X軸、Y軸）の移動を制御できる一般的な入力デバイスで、ボタンが押されるとZ軸（スイッチ）が作動します。

**必要なもの**

このプロジェクトには、以下のコンポーネントが必要です。

全てのコンポーネントがセットになったキットを購入するのが便利です。こちらのリンクからどうぞ：

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
        - 1（10KΩ）
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_joystick`
        - 1
        - 

**ジョイスティックの理解**

一般的なジョイスティックモジュールは、直交する2つのポテンショメーターで構成されています：

* **X軸ポテンショメーター**: 左右の移動を測定します。
* **Y軸ポテンショメーター**: 上下の移動を測定します。
* **Z軸（スイッチ）**: ジョイスティックを押し込むと作動するデジタルボタンです。

X軸およびY軸のアナログ値を読み取ることで、ジョイスティックの位置を把握できます。Z軸のボタンは、ジョイスティックが押されているかどうかを検出するために使用します。

**回路図**

|sch_joystick|

SWピンは10KΩのプルアップ抵抗に接続されています。これにより、ジョイスティックが押されていないときにSWピン（Z軸）で安定したハイレベルを取得できます。そうでない場合、SWはサスペンド状態となり、出力値が0または1の間で不安定になることがあります。

**配線図**

|wiring_joystick|

**コードの記述**

ジョイスティックのX軸、Y軸の位置を読み取り、ボタンの押下を検出するMicroPythonプログラムを記述します。

.. note::

    * ``4.1_toggle_the_joystick.py`` を ``newton-lab-kit/micropython`` から開くか、コードをThonnyにコピーして「実行」ボタンを押すか、F5キーを押してください。
    * 正しいインタープリタ（MicroPython (Raspberry Pi Pico).COMxx）が選択されていることを確認してください。

.. code-block:: python

    import machine
    import utime

    # X軸およびY軸用のADCを初期化
    x_adc = machine.ADC(27)  # GP27
    y_adc = machine.ADC(26)  # GP26

    # スイッチ用のデジタル入力を初期化
    z_button = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_UP)

    while True:
        # アナログ値を読み取る（0-65535）
        x_value = x_adc.read_u16()
        y_value = y_adc.read_u16()
        
        # ボタンの状態を読み取る（0または1）
        z_state = z_button.value()
        
        # 値を表示
        print("X:", x_value, "Y:", y_value, "Button:", z_state)
        
        # 出力を読みやすくするために少し遅延を挿入
        utime.sleep(0.2)


**コードの理解**

#. モジュールのインポート：

   * ``machine``: ハードウェア関連の機能にアクセスするためのモジュール。
   * ``utime``: 時間関連の関数を提供するモジュールで、遅延を扱います。

#. ADC入力の初期化：

   GP27およびGP26のピンにアナログ-デジタル変換（ADC）を設定し、ジョイスティックのX軸とY軸の位置を読み取ります。

   .. code-block:: python

      x_adc = machine.ADC(27)  # X軸はGP27に接続
      y_adc = machine.ADC(26)  # Y軸はGP26に接続

#. デジタル入力の初期化：

   * GP22をデジタル入力として設定し、ジョイスティックのボタン（Z軸）のために内部プルアップ抵抗を使用します。
   * ``machine.Pin.PULL_UP`` によって、押されていないときはピンがハイ（1）になり、押されるとロー（0）になります。

   .. code-block:: python

      z_button = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_UP)

#. メインループでの値の読み取り：

   * アナログ値の読み取り: ``read_u16()`` によって16ビットの値（0〜65535）を取得し、電圧レベルを表します。
   * 値の表示: X軸、Y軸の位置とボタンの状態をコンソールに表示します。

   .. code-block:: python

      while True:
          x_value = x_adc.read_u16()
          y_value = y_adc.read_u16()
          z_state = z_button.value()
          
          print("X:", x_value, "Y:", y_value, "Button:", z_state)
          
          utime.sleep(0.2)

プログラムを実行後、ThonnyのShellまたはREPLウィンドウを開きます。

* X、Y、ボタンの値が表示されるはずです。
* ジョイスティックを動かし、ボタンを押して値が変化する様子を確認してください。

**値の解釈**

* XおよびYの値：

  * 範囲は0から65535までです。
  * 中央位置: 約32768。
  * 左端または上端: 0に近い。
  * 右端または下端: 65535に近い。

* ボタンの状態：

  * 押されていない: 1。
  * 押された: 0。

**さらなる実験**

* 値の正規化：

  生のADC値を-100から100の範囲に変換して、より解釈しやすくします。

  .. code-block:: python

    import machine
    import utime

    # X軸およびY軸用のADCを初期化
    x_adc = machine.ADC(27)  # GP27
    y_adc = machine.ADC(26)  # GP26

    # スイッチ用のデジタル入力を初期化
    z_button = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_UP)

    # ADC値を-100から100の範囲に正規化する関数
    def normalize(value):
        return int((value - 32768) / 327.68)

    while True:
        # アナログ値を読み取る（0-65535）
        x_value = x_adc.read_u16()
        y_value = y_adc.read_u16()
        
        # ボタンの状態を読み取る（0または1）
        z_state = z_button.value()
        
        # 正規化した値を-100から100に変換
        x_normalized = normalize(x_value)
        y_normalized = normalize(y_value)
        
        # 正規化された値を表示
        print("X:", x_normalized, "Y:", y_normalized, "Button:", z_state)
        
        # 出力を読みやすくするために少し遅延を挿入
        utime.sleep(0.2)

* 出力の制御：

  ジョイスティックの入力を使用して、LED、サーボ、またはモーターを制御できます。例えば、X軸の値に基づいてオブジェクトを左右に動かすことができます。

* ゲームコントローラーの作成：

  ジョイスティックの入力を組み合わせて、シンプルなゲームやグラフィカルな出力を制御できます。

**結論**

このレッスンでは、Raspberry Pi Pico 2を使用してジョイスティックからアナログおよびデジタル入力を読み取る方法を学びました。この知識を活用して、ロボット、ゲーム、リモコンなどのインタラクティブなアプリケーションにジョイスティックを組み込むことができます。
