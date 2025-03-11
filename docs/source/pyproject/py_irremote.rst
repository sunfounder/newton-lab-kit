.. note:: 

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Raspberry Pi、Arduino、ESP32についてもっと深く探求しましょう。

**参加する理由?**

- **専門家のサポート**: コミュニティとチームからのサポートで販売後の問題や技術的な課題を解決。
- **学びと共有**: スキル向上のためのヒントやチュートリアルを交換。
- **独占プレビュー**: 新製品の発表や先行予告をいち早く入手。
- **特別割引**: 最新製品の独占割引を楽しむ。
- **祝祭プロモーションとギブアウェイ**: ギブアウェイや休日プロモーションに参加。

👉 一緒に探求し、創造してみませんか？クリック [|link_sf_facebook|] して今すぐ参加！

.. _py_irremote:


6.4 赤外線リモコンの使用
==========================================================

このレッスンでは、Raspberry Pi Pico 2とIRレシーバーモジュールを使用して **赤外線（IR）リモコン** を使用する方法を学びます。これにより、IRリモコンからの信号を受信およびデコードすることができ、プロジェクトをワイヤレスで制御することが可能になります。

**必要なもの**

このプロジェクトには以下のコンポーネントが必要です。

キット全体を購入することは非常に便利です。こちらがリンクです：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名称	
        - このキットに含まれるアイテム
        - リンク
    *   - Newton Lab Kit	
        - 450以上
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
        - :ref:`cpn_ir_receiver`
        - 1
        - |link_receiver_buy|

**赤外線通信の理解**

赤外線通信は、赤外線光を使用してデータをワイヤレスで送信することを含みます。一般的な家庭用機器（テレビやDVDプレーヤーなど）では、操作のためにIRリモコンが使用されます。

* **IR送信機（リモコン）:** ボタンが押されると、変調された赤外線光を発します。
* **IRレシーバーモジュール:** 変調されたIR光を検出し、それをデコード可能な電気信号に変換します。

**回路図**

|sch_irrecv|

**配線図**

|wiring_irrecv|

**コードの書き方**

リモコンからのIR信号を受信してデコードするMicroPythonスクリプトを書きましょう。

.. note::

    * ``6.4_ir_remote_control.py`` を ``newton-lab-kit/micropython`` から開くか、Thonnyにコードをコピーして「実行」ボタンをクリックするか、F5キーを押します。
    * 正しいインタープリタが選択されていることを確認してください：MicroPython (Raspberry Pi Pico).COMxx。 
    * ``ir_rx`` フォルダ内のライブラリを使用する必要がありますので、Picoにアップロードされているか確認してください。詳細なチュートリアルは :ref:`add_libraries_py` を参照してください。

.. code-block:: python

    import time
    from machine import Pin
    from ir_rx.nec import NEC_8  # Adjust based on your remote's protocol
    from ir_rx.print_error import print_error

    # IRレシーバーピンを初期化
    ir_pin = Pin(17, Pin.IN)

    # 受信データを処理するコールバック関数
    def ir_callback(data, addr, ctrl):
        if data < 0:  # 繰り返しコードまたはエラー
            pass
        else:
            key = decode_key(data)
            print("Received Key:", key)

    # 受信データをキー押下にデコードする関数
    def decode_key(data):
        key_codes = {
            0x45: "POWER",
            0x46: "MODE",
            0x47: "MUTE",
            0x44: "PLAY/PAUSE",
            0x40: "BACKWARD",
            0x43: "FORWARD",
            0x07: "EQ",
            0x15: "-",
            0x09: "+",
            0xD: "U/SD",
            0x16: "0",
            0x19: "cycle",
            0xC: "1",
            0x5E: "3",
            0x18: "2",
            0x8: "4",
            0x1C: "5",
            0x5A: "6",
            0x42: "7",
            0x52: "8",
            0x4A: "9",
            0x0: "ERROR",
            # リモコンに基づいてより多くのキーコードを追加
        }
        return key_codes.get(data, "UNKNOWN")

    # IRレシーバーをインスタンス化
    ir = NEC_8(ir_pin, ir_callback)
    ir.error_function(print_error)  # オプション: エラーを出力

    try:
        while True:
            time.sleep(1)  # メインスレッドを生存させ続ける
    except KeyboardInterrupt:
        ir.close()
        print("Program terminated")

このコードを実行して赤外線リモコンのボタンを押すと、Thonny Shell（または他のシリアルモニター）に押したキーの名前が表示されます。たとえば、「PLAY」ボタンを押すと、Shellに「Received Key: PLAY」と表示されます。

**コードの理解**

#. モジュールのインポート：

   * ``ir_rx.nec.NEC_8``: 8ビットアドレス用のNECプロトコルデコーダー。
   * ``print_error``: エラーメッセージを出力する機能。

   .. code-block:: python

        import time
        from machine import Pin
        from ir_rx.nec import NEC_8
        from ir_rx.print_error import print_error

#. IRレシーバーピンの初期化：

   .. code-block:: python

        ir_pin = Pin(17, Pin.IN)

#. コールバック関数の定義：

   この関数はデータが受信されたときに自動的に呼ばれます。dataパラメータにはキーコードが含まれます。

   .. code-block:: python

        def ir_callback(data, addr, ctrl):
            if data < 0:
                pass  # 繰り返しコードを無視
            else:
                key = decode_key(data)
                print("Received Key:", key)

#. キーをデコードする関数：

   受信したキーコードを人が読めるラベルにマッピングします。

   .. code-block:: python

        def decode_key(data):
            key_codes = {
            0x45: "POWER",
            0x46: "MODE",
            0x47: "MUTE",
            0x44: "PLAY/PAUSE",
            0x40: "BACKWARD",
            0x43: "FORWARD",
            0x07: "EQ",
            0x15: "-",
            0x09: "+",
            0xD: "U/SD",
            0x16: "0",
            0x19: "cycle",
            0xC: "1",
            0x5E: "3",
            0x18: "2",
            0x8: "4",
            0x1C: "5",
            0x5A: "6",
            0x42: "7",
            0x52: "8",
            0x4A: "9",
            0x0: "ERROR",
            # リモコンに基づいてより多くのキーコードを追加
            }
            return key_codes.get(data, "UNKNOWN")

#. IRレシーバーをインスタンス化：

   コールバック関数でIRレシーバーを設定します。

   .. code-block:: python

        ir = NEC_8(ir_pin, ir_callback)
        ir.error_function(print_error)


#. メインループ：

   IR信号を聞き取るためにプログラムを実行し続けます。プログラムの終了を適切に処理します。

   .. code-block:: python

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            ir.close()
            print("Program terminated")

**応用**

* **プロジェクトをワイヤレスで制御**：IRリモコンを使用してLED、モーター、その他の周辺機器を制御します。
* **ユニバーサルリモコンデコーダーの構築**：複数のプロトコルやリモコンを処理するためにコードを拡張します。

**結論**

このレッスンでは、Raspberry Pi Pico 2を使用してIRレシーバーで赤外線リモコンの信号をデコードする方法を学びました。これにより、一般的な家庭用リモコンを使用してプロジェクトにワイヤレス制御を追加することができます。

* `Callback Function - Wikipedia <https://en.wikipedia.org/wiki/Callback_(computer_programming)>`_

