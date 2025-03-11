.. note:: 

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者と一緒に深く学びましょう。

    **参加する理由**

    - **専門家のサポート**: 購入後の問題や技術的な課題をコミュニティとチームのサポートで解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換して、スキルを向上させましょう。
    - **独占プレビュー**: 新製品の発表や先行情報をいち早く入手できます。
    - **特別割引**: 最新製品に対する独占割引を楽しめます。
    - **祝祭プロモーションとギブアウェイ**: ギブアウェイや季節限定のプロモーションに参加できます。

    👉 一緒に探求し、創造しませんか？今すぐ [|link_sf_facebook|] をクリックして参加しましょう！

.. _py_motor:

3.5 小型ファン（DCモーター）の制御
======================================

このレッスンでは、 **DCモーター** （小型ファンのようなもの）をRaspberry Pi Pico 2と **L293Dモータードライバ** を使用して制御する方法を学びます。L293Dを使用すると、モーターの回転方向を制御できます—時計回りと反時計回りの両方です。DCモーターはPicoが直接供給できる電流以上を必要とするため、外部電源を使用してモーターに安全に電力を供給します。

**必要なもの**

このプロジェクトでは、以下のコンポーネントが必要です。

セットを購入するのが便利です。リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名称	
        - セット内容
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
        - :ref:`cpn_l293d`
        - 1
        - 
    *   - 6
        - :ref:`cpn_motor`
        - 1
        - |link_motor_buy| 
    *   - 7
        - :ref:`cpn_power_module`
        - 1
        -  
    *   - 8
        - 9V電池
        - 1
        - 

**回路図**

|sch_motor|


L293Dはモータードライバーチップで、ENはL293Dが動作するために5Vに接続されています。1Aと2AはそれぞれGP15とGP14に接続されており、1Yと2Yはモーターの両端に接続されています。

Y（出力）はA（入力）と同相なので、GP15とGP14に異なるレベルを与えると、モーターの回転方向を変更できます。

**配線図**

|wiring_motor|

この回路では、ボタンがRUNピンに接続されていることがわかります。これは、モーターが高電流で動作するため、Picoがコンピュータから切断される可能性があり、ボタンを押すことで（Picoの **RUN** ピンに低レベルが入力され）リセットする必要があるからです。

DCモーターは高電流を必要とするため、ここでは安全のために電源モジュールを使用してモーターに電力を供給します。

**コードの記述**

モーターを制御するためのMicroPythonプログラムを作成しましょう。

.. note::

    * ``3.5_small_fan.py`` を ``newton-lab-kit/micropython`` から開くか、コードをThonnyにコピーして、「実行」ボタンを押すか、F5キーを押して実行します。
    
    * 正しいインタープリタ（MicroPython (Raspberry Pi Pico).COMxx）が選択されていることを確認してください。 

.. code-block:: python

    import machine
    import utime

    # 制御用ピンの定義
    motor_in1 = machine.Pin(14, machine.Pin.OUT)
    motor_in2 = machine.Pin(15, machine.Pin.OUT)

    def rotate_clockwise():
        motor_in1.high()
        motor_in2.low()

    def rotate_counterclockwise():
        motor_in1.low()
        motor_in2.high()

    def stop_motor():
        motor_in1.low()
        motor_in2.low()

    while True:
        rotate_clockwise()
        utime.sleep(1)
        stop_motor()
        utime.sleep(1)
        rotate_counterclockwise()
        utime.sleep(1)
        stop_motor()
        utime.sleep(1)

コードが実行されると、モーターは1秒間時計回りに回転し、その後1秒間停止し、次に1秒間反時計回りに回転し、再度1秒間停止するというループを繰り返します。

**コードの理解**

#. ピンの初期化:

   ``motor_in1`` と ``motor_in2`` は、それぞれGP14とGP15に接続され、モーターの回転方向を制御します。

   .. code-block:: python

      motor_in1 = machine.Pin(14, machine.Pin.OUT)
      motor_in2 = machine.Pin(15, machine.Pin.OUT)

#. 関数の定義:

   * ``rotate_clockwise()``: ``motor_in1`` をHighに、 ``motor_in2`` をLowに設定してモーターを時計回りに回転させます。
   * ``rotate_counterclockwise()``: ``motor_in1`` をLowに、 ``motor_in2`` をHighに設定して反時計回りに回転させます。
   * ``stop_motor()``: ``motor_in1`` と ``motor_in2`` の両方をLowに設定してモーターを停止させます。

#. メインループ:

   モーターは時計回りに回転し、停止し、反時計回りに回転し、再度停止します。それぞれ1秒間ずつ繰り返されます。

   .. code-block:: python

      while True:
          rotate_clockwise()
          utime.sleep(1)
          stop_motor()
          utime.sleep(1)
          rotate_counterclockwise()
          utime.sleep(1)
          stop_motor()
          utime.sleep(1)

**トラブルシューティングのヒント**

* プログラム停止後もモーターが回転し続ける:

  プログラムを停止してもモーターが回転し続ける場合、Picoをリセットする必要があります。RUNピンをGNDに一時的に接続することで、Picoをリセットできます。

  |wiring_run_reset|

* Picoが切断される、または応答しなくなる:

  モーターが過剰な電流を引き込んでいる可能性があり、電圧の変動を引き起こしているかもしれません。モーターには別の電源を使用し、すべてのグラウンドが接続されていることを確認してください。

**結論**

このレッスンでは、L293DモータードライバとRaspberry Pi Pico 2を使用してDCモーターを制御する方法を学びました。これでモーターの回転方向を制御できるようになり、小型ファンやモーター駆動のデバイスなど、さまざまなプロジェクトを作成できます。

**次のステップ**

* **速度制御**: PWM（パルス幅変調）を使用してモーターの速度を制御する方法を試してみましょう。EN1ピンをPWM対応のGPIOピンに接続します。
* **複数モーターの制御**: L293Dの他のチャンネルを使用して、追加のモーターを制御します。
* **センサー統合**: センサーを組み合わせて、入力（例えば、温度や光）に基づいてモーターを制御します。
