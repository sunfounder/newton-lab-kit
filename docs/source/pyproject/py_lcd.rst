.. note:: 

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者と一緒に深く学んでいきましょう。

    **参加する理由**

    - **専門家のサポート**: コミュニティやチームから、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換し、スキルを向上させましょう。
    - **独占プレビュー**: 新製品の発表や先行情報をいち早く入手できます。
    - **特別割引**: 最新製品に対する独占割引をお楽しみいただけます。
    - **祝祭プロモーションとギブアウェイ**: ギブアウェイや季節限定のプロモーションに参加できます。

    👉 一緒に探求し、創造しませんか？今すぐ [|link_sf_facebook|] をクリックして参加しましょう！

.. _py_lcd:

3.4 液晶ディスプレイ (LCD1602)
================================

このレッスンでは、 **1602 LCD** をRaspberry Pi Pico 2に接続し、テキストを表示する方法を学びます。LCD1602は、16文字を2行に表示できるキャラクターベースの液晶ディスプレイで、メッセージ、センサーデータ、ステータス更新などの情報を表示するプロジェクトに最適です。

LCDをマイコンに直接接続する場合、複数のGPIOピンを使用する必要があり、プロジェクトの機能に制限を与える可能性があります。この問題を解決するために、 **I2Cインターフェース** を搭載したLCD1602モジュールを使用できます。I2Cプロトコルでは、データ線が2本（SDAおよびSCL）だけで、LCDを2本のGPIOピンで制御でき、他のピンをセンサーやデバイスに利用できるようになります。

**Raspberry Pi Pico 2でのI2Cの理解**

Raspberry Pi Pico 2は、複数のGPIOピンを使ったI2C通信をサポートしており、プロジェクトに柔軟性を提供します。Pico 2には、I2C0およびI2C1の2つのI2Cバスがあり、それぞれ複数のピンセットにマッピングできます。

以下は、Pico 2でI2C対応のピンの一覧です：

|pin_i2c|

I2C0またはI2C1のいずれかに対応するSDAおよびSCLのピンペアを選択できます。この柔軟性により、プロジェクト内で他の周辺機器とのピン競合を避けることができます。

**必要なもの**

このプロジェクトに必要なコンポーネントは以下の通りです。

キット全体を購入するのが便利です。こちらのリンクをご覧ください：

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
        - :ref:`cpn_i2c_lcd`
        - 1
        - |link_i2clcd1602_buy|

**回路図**

|sch_lcd_ar|

**配線図**

|wiring_lcd_ar|

**コードの記述**

LCD1602にメッセージを表示するためのMicroPythonプログラムを記述しましょう。

.. note::

   * ``3.4_liquid_crystal_display.py`` を ``newton-lab-kit/micropython`` から開くか、コードをThonnyにコピーして「実行」ボタンを押すか、F5キーを押してください。
   * 正しいインタープリタ（MicroPython (Raspberry Pi Pico).COMxx）が選択されていることを確認してください。
   * このコードでは、 ``lcd1602.py`` ライブラリを使用します。このライブラリがPicoにアップロードされていることを確認してください。詳細なチュートリアルについては、 :ref:`add_libraries_py` をご覧ください。

.. code-block:: python

   from machine import I2C, Pin
   from lcd1602 import LCD
   import utime

   # I2C通信を初期化（I2C0）
   i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)

   # LCDオブジェクトを作成
   lcd = LCD(i2c)

   # 最初のメッセージを表示
   lcd.clear()
   lcd.message("Hello, World!")
   utime.sleep(2)

   # 2行目に移動して別のメッセージを表示
   lcd.write(0, 1,"LCD1602 with I2C")  # 列0、行1
   utime.sleep(5)

   # ディスプレイをクリア
   lcd.clear()

コードを実行すると、次のように表示されます：

* LCDの1行目に「Hello, World!」が表示されます。
* 2秒後、2行目に「LCD1602 with I2C」が表示されます。
* さらに5秒後、表示がクリアされます。

**コードの理解**

#. モジュールのインポート：

   * ``machine``: ハードウェアにアクセスするためのモジュール。
   * ``lcd1602``: LCDを制御するためのカスタムライブラリ。
   * ``utime``: 遅延などの時間関連の関数。

#. I2C通信の初期化：

   .. code-block:: python
   
      i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)
   
   * ``I2C(0, ...)``: I2C0バスを使用。
   * ``sda=Pin(4)``: GP4をSDAに設定。
   * ``scl=Pin(5)``: GP5をSCLに設定。
   * ``freq=400000``: I2Cの周波数を400kHzに設定。

#. LCDオブジェクトの作成：

   * ``lcd = LCD(i2c)``: I2Cオブジェクトを渡してLCDクラスのインスタンスを作成。

#. メッセージの表示：

   * ``lcd.clear()``: 既存のテキストをクリアします。
   * ``lcd.message("Hello, World!")``: LCDに「Hello, World!」の文字列を表示します。
   * ``utime.sleep(2)``: 次のコマンドが実行される前に2秒待機。

#. カーソルを移動してさらにテキストを表示：

   * ``lcd.write(0, 1,"LCD1602 with I2C")``: 2行目の1列目にカーソルを移動し、文字列を表示。

#. 最終的な遅延とクリア：

   * ``utime.sleep(5)``: 5秒待機
   * ``lcd.clear()``: ディスプレイをクリア。

**さらなる実験**

* **カスタムメッセージの表示**: ``lcd.message()`` 内の文字列を変更して、自分のメッセージを表示してみましょう。
* **行の切り替え**: LCD1602には2行あるため、 ``(0, 1, message[i:i+16])`` を使用して2行目にカーソルを移動できます。
* **スクロールテキストの作成**: ループ内でディスプレイを更新することでスクロール効果を作成できます。

  .. code-block:: python

      from machine import I2C, Pin
      from lcd1602 import LCD
      import utime

      # I2C通信を初期化（I2C0）
      i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)

      # LCDオブジェクトを作成
      lcd = LCD(i2c)

      message = "Scrolling Text Demo "
      lcd.clear()
      while True:
         for i in range(len(message)):
            lcd.write(0, 0, message[i:i+16])  # 16文字ごとに表示
            utime.sleep(0.3)

**トラブルシューティングのヒント**

* 不正な文字や表示されない場合：

  * 配線が正しいか、特にSDAとSCLの接続を確認してください。
  * lcd1602ライブラリ内のI2CアドレスがLCDのアドレスと一致していることを確認してください。デフォルトでは、0x27または0x3Fであることが多いです。

* コントラストの調整：

  一部のLCDモジュールにはコントラスト調整用のポテンショメータがあります。画面に何も表示されない場合は、それを調整してみてください。

* 電源供給：

  LCDが適切な電源を受けていることを確認してください。5Vを使用している場合は、PicoのVSYSピン（USB経由で給電している場合）や外部5V電源に接続してください。

* I2Cアドレスの理解

  LCDにテキストが表示されない場合、異なるI2Cアドレスを使用している可能性があります。I2Cバス上のデバイスをスキャンできます：

  .. code-block:: python
  
      from machine import I2C, Pin
      i2c = I2C(0, sda=Pin(4), scl=Pin(5))
      devices = i2c.scan()

      # I2Cアドレスを16進数形式で表示
      print("I2C addresses found:", [hex(device) for device in devices])

  これにより、I2Cバスに接続されたデバイスのアドレスが表示されます。lcd1602.pyライブラリやコード内で正しいアドレスを使用するように更新してください。

**結論**

I2Cインターフェースを使用して、Raspberry Pi Pico 2でLCD1602ディスプレイを制御する方法を習得しました！この技術により、プロジェクトに視覚的な出力を追加でき、インタラクティブで情報量の多いものにすることができます。
