.. note:: 

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者と一緒に深く学んでいきましょう。

    **参加する理由**

    - **専門家のサポート**: コミュニティやチームから、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換し、スキルを向上させましょう。
    - **独占プレビュー**: 新製品の発表や先行情報をいち早く入手できます。
    - **特別割引**: 最新製品に対する独占割引をお楽しみいただけます。
    - **祝祭プロモーションとギブアウェイ**: ギブアウェイや季節限定のプロモーションに参加できます。

    👉 一緒に探求し、創造しませんか？今すぐ [|link_sf_facebook|] をクリックして参加しましょう！

.. _py_keypad:

4.2 4x4 キーパッドの使用
=================================================

このレッスンでは、 **4x4 マトリックスキーパッド** をRaspberry Pi Pico 2に接続し、どのキーが押されたかを検出する方法を学びます。マトリックスキーパッドは、計算機、電話、販売機、セキュリティシステムなどのデバイスで、数字の入力によく使用されます。

**必要なもの**

このプロジェクトには、以下のコンポーネントが必要です。 

キットを購入するのが便利です。こちらのリンクからどうぞ：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名称	
        - キット内容
        - リンク
    *   - Newton Lab Kit	
        - 450+
        - |link_newton_lab_kit|

または、以下のリンクから個別に購入することもできます。


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
        - 4（10KΩ）
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_keypad`
        - 1
        - |link_keypad_buy|

**4x4 キーパッドの理解**

4x4 キーパッドは以下で構成されています：

* **16個のキー** が4行4列に配置されています。
* **8ピン**: 4つが行に、4つが列に接続されています。

キーを押すと、特定の行と列が接続され、その行と列の番号を基にキーを特定できます。

キーの配置は次のようになっています：

|img_keypad|

**回路図**

|sch_keypad|

マトリックスキーパッドの各列には4つのプルダウン抵抗が接続されており、キーが押されていないときは、G6〜G9のピンで安定した低レベルを取得できます。

キーパッドの行（G2〜G5）はプログラムでハイに設定され、G6〜G9のいずれかのピンがハイになると、どのキーが押されたかを特定できます。

例えば、G6がハイであれば、数字キー1が押されたことがわかります。これは、数字キー1の制御ピンがG2とG6に接続されているため、キー1が押されるとG2とG6が接続され、G6もハイになるからです。

**配線**

|wiring_keypad|

**コードの記述**

キーがどれかを検出するMicroPythonプログラムを記述します。

.. note::

    * ``4.2_4x4_keypad.py`` を ``newton-lab-kit/micropython`` から開くか、コードをThonnyにコピーして「実行」ボタンを押すか、F5キーを押してください。
    * 正しいインタープリタ（MicroPython (Raspberry Pi Pico).COMxx）が選択されていることを確認してください。

.. code-block:: python

    import machine
    import time

    # キーパッド上の文字を定義
    keys = [
        ['1', '2', '3', 'A'],
        ['4', '5', '6', 'B'],
        ['7', '8', '9', 'C'],
        ['*', '0', '#', 'D']
    ]

    # 行と列に接続されたGPIOピンを定義
    row_pins = [2, 3, 4, 5]   # GP2-GP5
    col_pins = [6, 7, 8, 9]   # GP6-GP9

    # 行ピンを出力として初期化
    rows = [machine.Pin(pin_num, machine.Pin.OUT) for pin_num in row_pins]

    # 列ピンを入力としてプルダウン抵抗付きで初期化
    cols = [machine.Pin(pin_num, machine.Pin.IN, machine.Pin.PULL_DOWN) for pin_num in col_pins]

    def scan_keypad():
        for i, row in enumerate(rows):
            # すべての行を低に設定
            for r in rows:
                r.value(0)
            # 現在の行を高に設定
            row.value(1)
            # 列で高信号を検出
            for j, col in enumerate(cols):
                if col.value() == 1:
                    # キーが検出された
                    return keys[i][j]
        return None

    last_key = None

    while True:
        key = scan_keypad()
        if key != last_key:
            if key is not None:
                print("Key pressed:", key)
            last_key = key
        time.sleep(0.1)

**コードの理解**

#. キーパッドの文字を定義

   この2Dリストは、キーパッドのレイアウトを物理的な配置に合わせて定義しています。

   .. code-block:: python

        keys = [
            ['1', '2', '3', 'A'],
            ['4', '5', '6', 'B'],
            ['7', '8', '9', 'C'],
            ['*', '0', '#', 'D']
        ]


#. ピンの初期化

   .. code-block:: python

        row_pins = [2, 3, 4, 5]   # 行用GPIOピン
        col_pins = [6, 7, 8, 9]   # 列用GPIOピン

        # 行を出力として初期化
        rows = [machine.Pin(pin_num, machine.Pin.OUT) for pin_num in row_pins]

        # 列を入力としてプルダウン抵抗付きで初期化
        cols = [machine.Pin(pin_num, machine.Pin.IN, machine.Pin.PULL_DOWN) for pin_num in col_pins]

#. キーパッドスキャン関数の定義

    この関数は、各行をハイに設定し、各列の信号をチェックして、どの行と列でキーが押されたかを特定します。

   .. code-block:: python

        def scan_keypad():
            for i, row in enumerate(rows):
                # すべての行を低に設定
                for r in rows:
                    r.value(0)
                # 現在の行を高に設定
                row.value(1)
                # 列でキーの押下を検出
                for j, col in enumerate(cols):
                    if col.value() == 1:
                        # キーが押された
                        return keys[i][j]
            return None

#. メインループでのキー押下の検出

   * このループはキーの押下を継続的にスキャンします。
   * 同じキーが複数回検出されるのを防ぐため、最後のキーと現在のキーを比較して、重複検出を防ぎます（デバウンシング）。
   * 新しいキーが検出された場合、そのキーを表示します。

   .. code-block:: python

        last_key = None

        while True:
            key = scan_keypad()
            if key != last_key:
                if key is not None:
                    print("Key pressed:", key)
                last_key = key
            time.sleep(0.1)

プログラムを実行した後、キーパッドの異なるキーを押してみてください。対応するキー文字がThonnyシェルに表示されるはずです。

**トラブルシューティングのヒント**

* キーを押しても出力がない場合：

  * すべての接続が正しいことを確認してください。
  * プルダウン抵抗が列ピンとGNDの間に正しく接続されているか確認してください。

* 不正なキーが検出された場合：

  * キー配列がキーパッドのレイアウトと一致しているか再確認してください。
  * コード内の行ピンおよび列ピンが物理的な接続と一致しているか確認してください。

* 複数のキーが検出された場合：

  複数のキーが同時に押されると、機械的なキーパッドでゴースティング（誤検出）が発生することがあります。この基本的な設定では、一度に複数のキーを押さないようにしてください。

**さらなる実験**

* **シンプルなパスワードロックを実装**: キー押下のシーケンスを保存し、設定されたパスワードと比較します。
* **LCDディスプレイを追加**: 押されたキーをLCDスクリーンに表示します。
* **電卓を作成**: キーパッドで数値を入力し、基本的な算術演算を行います。

**結論**

このレッスンでは、Raspberry Pi Pico 2で4x4マトリックスキーパッドを接続してプログラムし、キー押下を検出する方法を学びました。これにより、インタラクティブなデバイス（ロック、電卓、制御インターフェースなど）を作成するための可能性が広がります。
