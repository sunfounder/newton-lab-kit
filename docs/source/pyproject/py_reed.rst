.. note:: 

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者と一緒にさらに深く学びましょう。

    **なぜ参加するべきか？**

    - **専門家によるサポート**: 購入後の問題や技術的な課題をコミュニティやチームからの支援で解決できます。
    - **学び・共有**: ヒントやチュートリアルを交換して、スキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先行公開情報にいち早くアクセスできます。
    - **特別割引**: 最新製品の特別割引を楽しめます。
    - **祝祭プロモーションやプレゼント**: プレゼントキャンペーンやシーズンプロモーションに参加できます。

    👉 私たちと一緒に探求し、創造してみませんか？[|link_sf_facebook|]をクリックして、今すぐ参加してください！

.. _py_reed:

2.9 磁場を感じる
===============================

このレッスンでは、Raspberry Pi Pico 2と **リードスイッチ** を使って、磁場の有無を検出する方法を学びます。リードスイッチは、磁場を利用して動作するシンプルな電気スイッチです。磁石がスイッチの近くに来ると、内部の接点が閉じ、電気回路が完成します。

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
        - :ref:`cpn_resistor`
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_reed`
        - 1
        - 

**リードスイッチの理解**

リードスイッチは、ガラスのカプセル内に封入された2本の薄い金属リードで構成されています。これらのリードは強磁性の材料でできており、わずかに離れて配置されています。磁場がない状態では、リードは離れており、スイッチは **開** いた状態です。磁石がスイッチの近くに来ると、リードが磁化され、引き寄せられて接触し、回路が閉じます。

* **磁石が近くにない場合**: スイッチは **開** いており、回路は未完成です。
* **磁石が近くにある場合**: スイッチは **閉** じており、回路は完成します。

|img_reed_sche|

**回路図**

|sch_reed|

デフォルトでは、GP14は低レベルで、磁石が近くにあると高レベルに変わります。

10KΩの抵抗は、磁石が近くにない場合でも、GP14が一定の低レベルを維持できるようにするために使用されます。

* **磁石が近くにない場合**:

  * リードスイッチは **開** いています。
  * **GP14** はプルダウン抵抗を通じて **GND** に接続されています。
  * GPIOピンは **LOW** （0）を読み取ります。

* **磁石が近くにある場合**:

  * リードスイッチは **閉** じています。
  * **GP14** はリードスイッチを通じて **3.3V** に接続されています。
  * GPIOピンは **HIGH** （1）を読み取ります。

**配線図**

|wiring_reed|

**コードの作成**

リードスイッチの近くに磁石があるかどうかを検出し、その結果を表示するMicroPythonプログラムを作成します。

.. note::

  * ``2.9_feel_the_magnetism.py`` を ``newton-lab-kit/micropython`` から開くか、コードをThonnyにコピーして、「実行」ボタンをクリックするか、F5キーを押して実行します。
  * 正しいインタプリタが選択されていることを確認してください：MicroPython（Raspberry Pi Pico）。COMxx。

.. code-block:: python

    import machine
    import utime

    # GP14を入力ピンとして初期化
    reed_switch = machine.Pin(14, machine.Pin.IN)

    while True:
        if reed_switch.value() == 1:
            print("Magnet detected!")
            utime.sleep(1)  # 複数回の検出を避けるために遅延

コードが実行されると、以下の現象が観察されます。

* **磁石が近くにない場合**: メッセージは表示されません。
* **磁石を近づけると**: コンソールに「磁石が検出されました！」と表示されます。
* **磁石を遠ざけると**: メッセージが表示されなくなります。

**コードの理解**

#. モジュールのインポート：

   * ``import machine``: ハードウェア機能にアクセスします。
   * ``import utime``: 時間関連の関数を提供します。

#. リードスイッチピンの初期化：

   * ``reed_switch = machine.Pin(14, machine.Pin.IN)``: GP14を入力ピンとして設定します。

#. メインループ：

   * ``while True``: 無限ループを開始します。
   * ``if reed_switch.value() == 1``: 磁石が近くにあるかどうかをチェック（GPIOピンがHIGHの場合）。
   * ``print("Magnet detected!")``: メッセージを表示します。
   * ``utime.sleep(1)``: 複数回の検出を避けるために遅延を追加します。

**効率的な検出のための割り込みの使用**

リードスイッチの状態をループで常にポーリングする代わりに、割り込みを使用してリードスイッチの状態変化をより効率的に検出できます。

割り込みを使用すると、リードスイッチの状態を継続的にチェックする必要がなくなり、イベントが発生したときに即座にハンドラ関数が呼び出され、反応が速くなります。

割り込みを使用した修正版コード。磁石を近づけると「磁石が検出されました！」と表示され、メインプログラムは他のタスクを実行できます。

.. code-block:: python

    import machine

    # GP14を内部プルダウン抵抗付きの入力ピンとして初期化
    reed_switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

    def magnet_detected(pin):
        print("Magnet detected!")

    # 上昇エッジ（LOWからHIGHへの遷移）で割り込みを設定
    reed_switch.irq(trigger=machine.Pin.IRQ_RISING, handler=magnet_detected)

* ``def magnet_detected(pin)``: 割り込みがトリガーされると自動的に呼び出される関数です。
    
  * ``print("Magnet detected!")``: 磁石が検出された場合にメッセージを表示します。

* ``reed_switch.irq(trigger=machine.Pin.IRQ_RISING, handler=magnet_detected)``: リードスイッチピンに割り込みを設定します。
     
  * ``trigger=machine.Pin.IRQ_RISING``: 上昇エッジ（ピンの値がLOWからHIGHに変わる時）で割り込みが発生します。
  * ``handler=magnet_detected``: 割り込みが発生したときに呼び出す関数を指定します。

**実用例**

* **セキュリティシステム**: ドアや窓が開かれたことを検出。
* **位置センサー**: 機械の動いている部品の位置を検出。
* **近接検出**: 磁石が近づいたときにイベントをトリガーします。

**さらに実験してみる**

* LEDを制御する：

  別のGPIOピン（例：GP15）にLEDを接続し、適切な抵抗を使用します。割り込みハンドラを修正して、磁石が検出されたときにLEDを点灯させます。

  .. code-block:: python

      import machine
  
      reed_switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
      led = machine.Pin(15, machine.Pin.OUT)
  
      def magnet_detected(pin):
          led.value(1)  # LEDを点灯
  
      # 上昇エッジで割り込みを設定
      reed_switch.irq(trigger=machine.Pin.IRQ_RISING, handler=magnet_detected)
  
      # メインループ
      while True:
          # 磁石がないときはLEDを消す
          if reed_switch.value() == 0:
              led.value(0)
          machine.sleep(100)

* 磁石が外れたことを検出する：

  落下エッジ（磁石が外れたとき）に対する別の割り込みを設定します。

  .. code-block:: python

    def magnet_removed(pin):
        print("Magnet removed!")

    reed_switch.irq(trigger=machine.Pin.IRQ_FALLING, handler=magnet_removed)

**結論**

Raspberry Pi Pico 2でリードスイッチを使用すると、磁場の有無を検出でき、セキュリティシステムからインタラクティブなプロジェクトまで、さまざまな応用が可能です。リードスイッチの配線方法や割り込みの利用方法を理解することで、効率的で反応の良いプログラムを作成する能力が向上します。

**参考文献**

* |link_mpython_irq|