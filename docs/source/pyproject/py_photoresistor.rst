.. note::

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者と共にさらに深く学びましょう。

    **なぜ参加するべきか？**

    - **専門家によるサポート**: 購入後の問題や技術的な課題を、コミュニティやチームからサポートを受けて解決できます。
    - **学び・共有**: ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先行公開情報をいち早くチェックできます。
    - **特別割引**: 最新の製品に対する限定割引をお楽しみいただけます。
    - **祝祭プロモーションやプレゼント**: プレゼントキャンペーンや季節のプロモーションに参加しましょう。

    👉 私たちと一緒に探求し、創造してみませんか？[|link_sf_facebook|]をクリックして、今すぐ参加してください！

.. _py_photoresistor:

2.12 光を感じる
=====================

このレッスンでは、Raspberry Pi Pico 2を使って **フォトレジスター** （光依存抵抗器、LDR）を使い、光の強さを測定する方法を学びます。フォトレジスターは、受け取る光の量に応じて抵抗値が変化します。光が強ければ抵抗値は低くなり、これにより周囲の光の変化を検出するのに最適です。

**必要なもの**

このプロジェクトでは、以下の部品が必要です。

全ての部品を揃えたキットを購入するのが便利です。こちらのリンクからご覧ください：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - このキットの部品
        - リンク
    *   - Newton Lab Kit	
        - 450以上
        - |link_newton_lab_kit|

部品は以下のリンクから個別に購入することもできます。


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
        - 1（10KΩ）
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_photoresistor`
        - 1
        - |link_photoresistor_buy|


**回路図**

|sch_photoresistor|


この回路では、10KΩの抵抗器とフォトレジスターが直列に接続され、電圧分割回路が形成されます。GP28ピンはフォトレジスターの電圧を読み取ります。10KΩの抵抗器は、電流を制限することで保護の役割を果たします。

* **明るい光**: フォトレジスターの抵抗が減少し、その電圧とGP28の読み値が低くなります。強い光では、抵抗がほぼゼロに近づき、GP28の読み値は0に近くなります。この時、10KΩの抵抗器が保護役を果たし、3.3VとGNDが直接接続されることによる短絡を防ぎます。
* **暗闇**: フォトレジスターの抵抗が増加し、その電圧とGP28の値が上昇します。完全な暗闇では、抵抗はほぼ無限大になり（10KΩの抵抗は無視できます）、GP28の読み値は65535に近づきます。

計算式は以下の通りです。

.. code-block::

  Digital Value = (Analog Voltage/3.3V) * 65535


**配線図**

|wiring_photoresistor|

**コードの作成**

フォトレジスターからアナログ値を読み取り、それを表示するMicroPythonプログラムを作成します。

.. note::

  * ``2.12_feel_the_light.py`` ファイルを ``newton-lab-kit/micropython`` パスの下で開くか、以下のコードをThonnyにコピーして「現在のスクリプトを実行」をクリックするか、 **F5** キーを押して実行してください。
  * Thonnyの右下に「MicroPython (Raspberry Pi Pico).COMxx」のインタプリタが選択されていることを確認してください。
  * 詳細な手順については、 :ref:`open_run_code_py` を参照してください。

.. code-block:: python

    import machine
    import utime

    # GP28でADCを初期化
    photoresistor = machine.ADC(28)

    while True:
        # アナログ値（0〜65535）を読み取る
        light_value = photoresistor.read_u16()
        print("Light value:", light_value)
        utime.sleep(0.5)

コードが実行されている間、コンソールに表示される値を観察してください。

* フォトレジスターを手で覆い、暗闇をシミュレートすると、値が増加します。
* フォトレジスターに光を当てると、値が減少します。

**コードの理解**

#. モジュールのインポート：

   * ``machine``: ハードウェア関連の関数にアクセスします。
   * ``utime``: 時間関連の関数（スリープなど）を使用します。

#. ADCピンの初期化：

   * ``photoresistor = machine.ADC(28)``: GP28ピンをアナログ入力として設定し、電圧レベルを読み取ります。

#. メインループ：

   ``while True``: 無限ループを開始します。
   ``light_value = photoresistor.read_u16()``: フォトレジスターからアナログ値を読み取ります。値は0（0V）から65535（3.3V）までの範囲です。
   ``print("Light value:", light_value)``: コンソールに光の値を出力します。
   ``utime.sleep(0.5)``: 次の読み取り前に0.5秒の遅延を挟みます。


**さらなる実験**

* 読み取り値のキャリブレーション：

  アナログ値をパーセンテージや意味のあるスケールにマッピングします。

  .. code-block:: python

      import machine
      import utime

      photoresistor = machine.ADC(28)

      while True:
          light_value = photoresistor.read_u16()
          light_percentage = (light_value / 65535) * 100
          print("Light level: {:.2f}%".format(light_percentage))
          utime.sleep(0.5)

* 光の強さに基づいてLEDを制御する：

  光センサーを使用して、暗い場所ではLEDを点灯し、明るい場所ではLEDを消灯します。

  .. code-block:: python

    import machine
    import utime

    photoresistor = machine.ADC(28)
    led = machine.Pin(15, machine.Pin.OUT)

    while True:
        light_value = photoresistor.read_u16()
        if light_value > 50000:
            led.value(1)  # 暗闇でLEDを点灯
        else:
            led.value(0)  # 明るい光でLEDを消灯
        utime.sleep(0.5)

* 光をトリガーにしたアラームや通知を作成：光の強さが大きく変化した際にアクションを起こす仕組みを作成します。

**結論**

フォトレジスターをRaspberry Pi Pico 2と組み合わせて使用することで、アナログ入力を読み取り、環境光の変化に反応する方法を学びました。この知識は、自動照明システムや光を追従するロボット、または光の変化に反応するセキュリティデバイスなど、さまざまなプロジェクトに応用できます。


