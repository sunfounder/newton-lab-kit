.. note::

    こんにちは！SunFounderのRaspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者と一緒にさらに深く学びましょう。

    **参加する理由**

    - **専門的サポート**：販売後の問題や技術的な課題をコミュニティとチームからのサポートで解決できます。
    - **学びと共有**：スキル向上のためのヒントやチュートリアルを交換しましょう。
    - **独占プレビュー**：新製品の発表や先行情報をいち早くゲット！
    - **特別割引**：最新製品をお得に購入できます。
    - **キャンペーン＆プレゼント**：プレゼント企画や季節限定のプロモーションに参加できます。

    👉 一緒に探索してクリエイションしませんか？[|link_sf_facebook|]をクリックして、今すぐ参加しよう！

.. _py_slide:

2.7 左右切替
============================

このレッスンでは、Raspberry Pi Pico 2を使用して **スライドスイッチ** の位置（左または右）を検出し、それに基づいて動作を行う方法を学びます。スライドスイッチは、位置に応じて共通ピン（中央ピン）と外側の2つのピンのいずれかを接続するシンプルな機械的デバイスです。

**必要なもの**

このプロジェクトでは、以下のコンポーネントが必要です。

便利なキットを購入することをお勧めします。こちらから購入できます：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名称
        - キット内容
        - リンク
    *   - ニュートンラボキット
        - 450+
        - |link_newton_lab_kit|


また、以下のリンクから個別に購入することもできます。

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
        - マイクロUSBケーブル
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
        - :ref:`cpn_capacitor`
        - 1（104）
        - |link_capacitor_buy|
    *   - 7
        - :ref:`cpn_slide_switch`
        - 1
        - 

**スライドスイッチの理解**

|img_slide|

スライドスイッチには3つのピンがあります：

- **ピン1**：スイッチを一方向（例：左）に切り替えた時に接続されます
- **ピン2**：共通ピン（中央ピン）
- **ピン3**：スイッチを反対方向（例：右）に切り替えた時に接続されます

共通ピンの電圧を読み取ることで、スイッチの位置を判別できます。

**回路図**

|sch_slide|

スライドスイッチを右または左に切り替えると、GP14には異なるレベルが表示されます。

10KΩの抵抗は、スイッチを切り替える際にGP14を低電圧に保つ役割を果たします（スイッチが極端に左または右に切り替わらないようにします）。

スイッチを切り替えると、機械的接点により急速なノイズ信号「バウンス」が発生することがあります。GP14とGNDの間に接続されたコンデンサがこれらの急激な変動をフィルタリングし、よりクリーンな信号を提供します。

* 右にスイッチを切り替えた場合：

  * ピン2（GP14）はピン1を通じて **3.3V** に接続されます。
  * GPIOピンは **HIGH** （1）を読み取ります。

* 左にスイッチを切り替えた場合：

  * ピン2（GP14）はピン3を通じて **GND** に接続されます。
  * GPIOピンは **LOW** （0）を読み取ります。

* 中間位置のスイッチ：

  * ピン2（GP14）は **3.3V** にも **GND** にも接続されていません。
  * プルダウン抵抗がGPIOピンを **LOW** （0）に保ちます。
  * コンデンサはスイッチバウンス（機械的動作によるノイズ）を低減します。


**配線**

|wiring_slide|                                                                                                                                                                                                  



**コードの作成**

スライドスイッチの位置を検出し、その結果に基づいてメッセージを表示するMicroPythonプログラムを作成します。

.. note::

  * ``2.7_slide_switch.py`` を ``newton-lab-kit/micropython`` から開くか、コードをThonnyにコピーして、「Run」をクリックするかF5を押してください。

  * 正しいインタプリタが選択されていることを確認してください：MicroPython（Raspberry Pi Pico）。COMxx。

  

.. code-block:: python

  import machine
  import utime

  # GP14を入力として初期化
  slide_switch = machine.Pin(14, machine.Pin.IN)

  while True:
      switch_state = slide_switch.value()
      if switch_state == 1:
          print("Switch is toggled to the LEFT!")
      else:
          print("Switch is toggled to the RIGHT!")
      utime.sleep(0.5)

コードが実行されると、次の現象が観察されます：

* **右に切り替えた場合**：コンソールに「スイッチは右に切り替えられました！」と表示されます。
* **左に切り替えた場合**：コンソールに「スイッチは左に切り替えられました！」と表示されます。


**コードの理解**

#. モジュールのインポート：

   * ``import machine``：ハードウェア機能にアクセスします。
   * ``import utime``：時間に関連する関数を使用します。

#. スライドスイッチピンの初期化：

   * ``slide_switch = machine.Pin(14, machine.Pin.IN)``：GP14を入力ピンとして設定します。

#. メインループ：

   * ``while True``：スイッチの状態を継続的にチェックする無限ループを作成します。
   * ``switch_state = slide_switch.value()``：スイッチの現在の状態を読み取ります。
   * ``if switch_state == 1``：GPIOピンがHIGH（スイッチが左に切り替えられた場合）であることを確認します。
   * ``print("Switch is toggled to the RIGHT!")``：メッセージを表示します。
   * ``else``：GPIOピンがLOW（スイッチが右または中間にある場合）である場合。
   * ``print("Switch is toggled to the LEFT!")``：メッセージを表示します。
   * ``utime.sleep(0.5)``：スイッチのデバウンスを防ぎ、コンソールが溢れないように短い遅延を追加します。


**代替案：内部プルダウン抵抗の使用**

Raspberry Pi Pico 2では、内部プルダウン抵抗を有効にすることができ、外部抵抗が不要になります。

* 回路の変更：

  外部の10 kΩ抵抗と0.1 µFコンデンサを取り外します。

* 修正されたコード：

  .. code-block:: python

    import machine
    import utime

    # GP14を内部プルダウン抵抗付きで入力として初期化
    slide_switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

    while True:
        switch_state = slide_switch.value()
        if switch_state == 1:
            print("Switch is toggled to the LEFT!")
        else:
            print("Switch is toggled to the RIGHT!")
        utime.sleep(0.5)
  
**実用的な応用例**

* **モード選択**：プログラム内で異なるモード間でスイッチを切り替えます。
* **電源制御**：回路の特定部分の電源を制御します。
* **ユーザー入力**：プロジェクトにシンプルなユーザー制御を提供します。

**さらなる実験**

* LEDインジケーターを追加：

  適切な抵抗を介して別のGPIOピン（例：GP15）にLEDを接続します。スイッチの位置に基づいてLEDをオンまたはオフにするコードを修正します。

  .. code-block:: python

    import machine
    import utime

    slide_switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
    led = machine.Pin(15, machine.Pin.OUT)

    while True:
        if slide_switch.value() == 1:
            led.value(1)  # LEDを点灯
        else:
            led.value(0)  # LEDを消灯
        utime.sleep(0.1)

* 中間位置の検出：

  スイッチが中間位置（左でも右でもない）にあるときを検出するために、配線とコードを修正し、3つの状態すべてを読み取れるようにします。

**結論**

Raspberry Pi Pico 2とスライドスイッチを使用することで、物理的な入力コントロールをプロジェクトに追加できます。スイッチの状態を読み取り、スイッチバウンスのような潜在的な問題を処理する方法を理解することにより、よりインタラクティブでユーザーフレンドリーなアプリケーションを作成できます。
