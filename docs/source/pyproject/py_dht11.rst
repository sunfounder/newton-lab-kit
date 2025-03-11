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

.. _py_dht11:

6.2 DHT11を使用した温度と湿度の測定
=======================================================

このレッスンでは、Raspberry Pi Pico 2 を使用して **DHT11温度・湿度センサー** を扱う方法を学びます。  
DHT11は、周囲の温度と湿度を測定できる低コストのデジタルセンサーで、キャリブレーション済みのデジタル出力を提供します。

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
        - :ref:`cpn_dht11`
        - 1
        - |link_dht22_buy|

**DHT11センサーの概要**

DHT11は、静電容量式湿度センサーと **サーミスタ** を使用して周囲の温度と湿度を測定します。  
データピンからデジタル信号を出力し、比較的簡単に扱えますが、データを正しく取得するには適切なタイミングが必要です。

* 温度範囲: 0–50°C (±2°Cの精度)
* 湿度範囲: 20–80% RH (±5%の精度)
* サンプリングレート: 1Hz (1秒ごとに測定)

**回路図**

|sch_dht11|

**配線図**

|wiring_dht11|

**コードの記述**

MicroPythonを使用して、DHT11から温度と湿度の値を取得するプログラムを作成します。

.. note:: 

    * ``newton-lab-kit/micropython`` 内の ``6.2_temperature_humidity.py`` を開くか、コードをThonnyにコピーし、「Run」をクリックするか、F5キーを押してください。

    * インタプリタが正しく設定されていることを確認してください: MicroPython (Raspberry Pi Pico).COMxx。


    * このコードでは ``dht.py`` ライブラリを使用します。Picoにアップロードされているか確認し、詳細な手順については :ref:`add_libraries_py` を参照してください。

.. code-block:: python

   from machine import Pin
   import utime
   import dht

   # DHT11センサーを初期化
   sensor = dht.DHT11(Pin(16))

   while True:
      try:
         # 測定を実行
         sensor.measure()
         # 値を取得
         temperature = sensor.temperature()  # 摂氏温度
         humidity = sensor.humidity()        # 湿度 (%)
         # 測定結果を出力
         print("Temperature: {}°C   Humidity: {}%".format(temperature, humidity))
      except OSError as e:
         print("Failed to read sensor.")
      # 次の測定まで待機
      utime.sleep(2)

コードを実行すると、温度と湿度の測定値がThonnyのシェルに表示されます。

.. code-block::

  Temperature: 29.3°C   Humidity: 60.0%
  Temperature: 29.2°C   Humidity: 60.0%
  Temperature: 29.2°C   Humidity: 60.0%
  Temperature: 29.1°C   Humidity: 60.0%
  Temperature: 29.2°C   Humidity: 60.0%
  Temperature: 29.3°C   Humidity: 60.0%

**Understanding the Code**

#. モジュールのインポート:

   * ``machine.Pin``: GPIOピンの制御
   * ``utime``: 時間関連の関数を提供
   * ``dht``: DHTセンサーを扱うためのライブラリ

#. センサーの初期化:

   .. code-block:: python

      sensor = dht.DHT11(Pin(16))
      # GP16に接続されたDHT11センサーのインスタンスを作成

#. メインループ:

   * ``sensor.measure()``: センサーをトリガーし、測定を実行
   * ``sensor.temperature``: 摂氏温度を取得
   * ``sensor.humidity``: 湿度を取得
   * ``Exception Handling``: 読み取りエラーをキャッチし、エラーメッセージを表示
   * ``utime.sleep(2)``: 2秒ごとに測定を繰り返す

   .. code-block:: python

      while True:
         try:
            sensor.measure()
            temperature = sensor.temperature
            humidity = sensor.humidity
            print("Temperature: {}°C   Humidity: {}%".format(temperature, humidity))
         except OSError as e:
            print("Failed to read sensor.")
         utime.sleep(2)

**Experimenting Further**

* 温度を華氏に変換:

   .. code-block:: python

      temperature_f = temperature * 9 / 5 + 32
      print("Temperature: {}°F   Humidity: {}%".format(temperature_f, humidity))

* LCDディスプレイに測定結果を表示:

  PCを使わずに温度と湿度を表示できるようにLCDを追加。


* アラート機能の追加:

  設定した温度や湿度を超えた際にLEDを点灯させたり、ブザーを鳴らす機能を追加。

**Troubleshooting Tips**

* 測定値が不正確な場合:

  * センサーの接続を確認
  * 配線が緩んでいないかチェック

* センサーの読み取りに失敗する場合:

  タイミングの問題で発生することがありますが、コード内でtry-exceptを使用してエラーハンドリングを実装済み。

* プルアップ抵抗の確認:

  一部のDHTセンサーでは、VCCとデータピンの間に 4.7KΩ〜10KΩ のプルアップ抵抗が必要な場合があります。

**Conclusion**

このレッスンでは、Raspberry Pi Pico 2 を使用して DHT11温度・湿度センサー からデータを取得する方法を学びました。温湿度の測定は、気象観測、ホームオートメーション、環境モニタリングなど、多くのプロジェクトで活用できます。

* `Try Statement - Python Docs <https://docs.python.org/3/reference/compound_stmts.html?#the-try-statement>`_
