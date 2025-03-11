.. note:: 

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者と共にさらに深く学びましょう。

    **参加する理由**

    - **専門家のサポート**: 購入後の問題や技術的な課題を、コミュニティやチームのサポートを通じて解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換し、スキルを向上させましょう。
    - **独占プレビュー**: 新製品の発表や先行情報にいち早くアクセスできます。
    - **特別割引**: 最新製品に対する独占的な割引を楽しめます。
    - **祝祭のプロモーションやギブアウェイ**: ギブアウェイや祝祭のプロモーションに参加できます。

    👉 一緒に探求し、創造しませんか？今すぐ [|link_sf_facebook|] をクリックして参加しましょう！

.. _py_pa_buz:

3.2 パッシブ・ブザーでカスタム音を再生する
===========================================================

このレッスンでは、Raspberry Pi Pico 2を使用して **パッシブ・ブザー** を操作し、さまざまな音を再生したり、簡単なメロディーを演奏する方法を学びます！アクティブ・ブザーとは異なり、パッシブ・ブザーは音を出すために変化する電気信号を必要とし、その信号の周波数を変更することで音の高さを制御できます。

**必要なもの**

このプロジェクトには、以下のコンポーネントが必要です。

全体キットを購入するのが便利です。リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名称	
        - セット内容
        - リンク
    *   - Newton Lab Kit	
        - 450+
        - |link_newton_lab_kit|

個別に購入することもできます。

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
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 1(1KΩ)
        - |link_resistor_buy|
    *   - 7
        - パッシブ :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|

**パッシブ・ブザーの仕組み**

パッシブ・ブザーは小さなスピーカーのように動作します。自分で音を出すことはなく、音を出すためには振動信号が必要です。異なる周波数の信号を供給することにより、ブザーは異なる音高を発生させることができ、これによって音符やメロディーを再生することができます。

|img_buzzer|

**回路図**

|sch_buzzer|

この回路では、パッシブ・ブザーはトランジスタ（ **S8050** NPN）を介して電力供給されます。トランジスタは電流を増幅し、Picoに直接接続した場合よりもブザーの音量を大きくします。

動作は以下の通りです：

* **GP15** が高信号を出力し、トランジスタを制御します。
* トランジスタが活性化されると、電流がブザーを通じて流れ、音を鳴らします。

**1kΩの抵抗** は、トランジスタを保護するために電流を制限します。

**配線図**

**パッシブ・ブザー** を使用していることを確認してください。正しいものかどうかは、基板が露出しているかどうかで判断できます（背面が封印されているのはアクティブ・ブザーです）。

|img_buzzer|

|wiring_buzzer|

**コードの作成**

次に、ブザーで異なる音を再生するコードを書いてみましょう。

.. note::

    * ``newton-lab-kit/micropython`` から ``3.2_custom_tone.py`` を開くか、コードをThonnyにコピーして「実行」ボタンをクリックするか、F5キーを押して実行します。
    * 正しいインタープリタ（MicroPython (Raspberry Pi Pico).COMxx）が選択されていることを確認してください。


.. code-block:: python

   import machine
   import utime

   # GP15でPWMを初期化
   buzzer = machine.PWM(machine.Pin(15))

   def play_tone(frequency, duration):
       # PWM信号の周波数を設定
       buzzer.freq(frequency)
       # デューティサイクルを50%に設定
       buzzer.duty_u16(32768)
       # 指定された期間だけ音を鳴らす
       utime.sleep_ms(duration)
       # ブザーを停止
       buzzer.duty_u16(0)

   # 音をいくつか再生
   play_tone(440, 500)  # A4音を500ms再生
   utime.sleep_ms(200)
   play_tone(494, 500)  # B4音を500ms再生
   utime.sleep_ms(200)
   play_tone(523, 500)  # C5音を500ms再生

このコードが実行されると、パッシブ・ブザーがA4音を500ms、B4音を500ms、C5音を500msの順に再生します。


**コードの説明**

#. PWMの初期化:

   * ``buzzer = machine.PWM(machine.Pin(15))``: GP15ピンでPWM（パルス幅変調）を設定し、これを使ってブザーを制御します。

#. ``play_tone`` 関数の定義:

   .. code-block:: python

      def play_tone(frequency, duration):
          buzzer.freq(frequency)
          buzzer.duty_u16(32768)
          utime.sleep_ms(duration)
          buzzer.duty_u16(0)

   * ``frequency``: 音の高さ（周波数）。周波数が高いほど高い音になります。
   * ``duration``: 音が鳴る時間（ミリ秒）。
   * ``buzzer.duty_u16(32768)``: デューティサイクルを50%に設定（65535の半分）。
   * 再生が終了したら、デューティサイクルを0にしてブザーを停止します。

#. 音符の再生:

   異なる周波数の音符を再生するために、 ``play_tone`` を呼び出します。

   .. code-block:: python

      # 音をいくつか再生
      play_tone(440, 500)  # A4音を500ms再生
      utime.sleep_ms(200)
      play_tone(494, 500)  # B4音を500ms再生
      utime.sleep_ms(200)
      play_tone(523, 500)  # C5音を500ms再生


**メロディーを演奏してみよう**

個々の音符を再生する方法を学んだので、次に簡単なメロディーを作成してみましょう！これにより、音符を順番に並べてその持続時間を調整することで、音楽を作成する方法を理解できます。

.. code-block:: python

    import machine
    import utime

    # 音符の周波数（Hz）
    NOTE_C4 = 262
    NOTE_D4 = 294
    NOTE_E4 = 330
    NOTE_F4 = 349
    NOTE_G4 = 392
    NOTE_A4 = 440
    NOTE_B4 = 494
    NOTE_C5 = 523

    melody = [
        NOTE_C4, NOTE_D4, NOTE_E4, NOTE_F4,
        NOTE_G4, NOTE_A4, NOTE_B4, NOTE_C5
    ]

    note_durations = [
        500, 500, 500, 500,
        500, 500, 500, 500
    ]

    # GP15でPWMを初期化
    buzzer = machine.PWM(machine.Pin(15))

    def play_tone(frequency, duration):
        buzzer.freq(frequency)
        buzzer.duty_u16(32768)
        utime.sleep_ms(duration)
        buzzer.duty_u16(0)
        utime.sleep_ms(50)  # 音符の間に短い間隔を置く

    for i in range(len(melody)):
        play_tone(melody[i], note_durations[i])

このコードを実行すると、ブザーはメロディーを演奏し、各音符が500ミリ秒間鳴り、音符の間には短い間隔があります。ブザーはC4（中のC）からC5（次のオクターブのC）までの昇順のスケールを演奏します。

**さらに実験してみよう**

* **自分のメロディーを作成**: メロディーと ``note_durations`` のリスト内の音符とその持続時間を変更して、自分の曲を作成しましょう。
* **テンポの調整**: ``note_durations`` の値を変更してメロディーの速さを調整します。
* **音符を追加**: 新しい音符を定義し、その周波数をメロディーに追加します。
* **音量を変更**: ``buzzer.duty_u16()`` のデューティサイクルを調整して、ブザーの音量を大きくしたり小さくしたりできます。32768は50%のデューティサイクルに相当します。

**結論**

このレッスンでは、パッシブ・ブザーを使用して音符やメロディーを再生する方法を学びました。PWM信号の周波数を制御することで、さまざまな音を作成したり、簡単な曲を演奏したりすることができます。これを活用すれば、プロジェクトに音でのフィードバックや楽しい音楽要素を加えることができます。
