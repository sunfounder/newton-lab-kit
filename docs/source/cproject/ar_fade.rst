.. note::

    こんにちは！SunFounder Raspberry Pi & Arduino & ESP32 愛好者コミュニティ（Facebook）へようこそ！  
    Raspberry Pi、Arduino、ESP32 の知識を深め、仲間とともにものづくりを楽しみましょう。

    **なぜ参加するのか？**

    - **専門的なサポート**：購入後の問題や技術的な課題を、コミュニティメンバーやチームがサポート。  
    - **学びと共有**：ヒントやチュートリアルを交換し、スキルを向上。  
    - **最新情報の先行公開**：新製品の発表やプレビューをいち早くチェック。  
    - **特別割引**：最新製品を会員限定の特別価格で購入可能。  
    - **イベント & プレゼント企画**：プレゼントキャンペーンや季節ごとのプロモーションに参加可能。  

    👉 一緒にものづくりを楽しみませんか？[|link_sf_facebook|] をクリックして、今すぐ参加！  

.. _ar_fade:

2.3 LED の明るさを調整する (フェード)
============================================

このレッスンでは、パルス幅変調（PWM） を使用して、Raspberry Pi Pico 2 で LED の明るさを制御する方法を学びます。 PWM は、LED やモーターなどのデバイスをさまざまな強度で制御するために広く使われる基本的な技術です。

**PWM とは？**

**パルス幅変調（PWM：Pulse Width Modulation）** とは、電力を高周波で ON/OFF することで、デバイスに供給する電力量を調整する方法です。 ON の時間が長いほど、デバイスが受け取る電力は多くなります。

|img_pwm_duty_cycle|

* **デューティサイクル**: 信号が ON である割合（%）。100% なら常に ON、0% なら常に OFF。  
* **周波数**: 1 秒間に信号が ON/OFF を繰り返す回数。

デューティサイクルを調整することで、デジタル信号を使用しながらアナログ出力のような制御を実現できます。 例えば、LED を高速で点滅させると、人間の目には明るさが変化しているように見えます。

**PWM の活用例**

* **LED の明るさ調整**: 滑らかに明るさを変える。  
* **モーターの速度制御**: DC モーターの回転数を調整する。  
* **省エネルギー**: 可変抵抗を使うよりも熱損失が少なく、効率的に電力を制御できる。  

**Raspberry Pi Pico 2 の PWM 機能**

Raspberry Pi Pico 2 はすべての GPIO ピンで PWM をサポートしています。 しかし、実際には 8 つの PWM スライス（PWM0～PWM7）を持ち、それぞれ A/B の 2 チャンネルを使用できるため、 最大16 個の独立した PWM 出力が利用可能です。

|pin_pwm|

.. note::
     同じ PWM スライスを共有するピン（例: GP0 と GP16）は、異なるデューティサイクルを設定できますが、 **異なる周波数には設定できません** 。


**必要なもの**

このプロジェクトでは、以下のコンポーネントが必要です。

すべて揃ったキットを購入すると便利です。リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名称  
        - キットに含まれるアイテム  
        - リンク  
    *   - Newton Lab Kit  
        - 450点以上  
        - |link_newton_lab_kit|  

個別に購入する場合は、以下のリンクからどうぞ。

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
        - Micro USB ケーブル  
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
        - 1 (220Ω)  
        - |link_resistor_buy|  
    *   - 6  
        - :ref:`cpn_led`  
        - 1  
        - |link_led_buy|  

**回路図**

|sch_led|

**配線図**

|wiring_led|

**コードの記述**

.. note::

   * ``2.3_fading_led.ino`` を ``newton-lab-kit/arduino/2.3_fading_led`` から開くことができます。  
   * または、このコードを **Arduino IDE** にコピーしてください。  
   * **Raspberry Pi Pico 2** ボードを選択し、適切なポートを設定して「Upload」をクリックしてください。  

.. code-block:: Arduino

    const int ledPin = 15; // LED を接続する GPIO ピン

    void setup() {
      pinMode(ledPin, OUTPUT); // GPIO ピンを出力として設定
    }

    void loop() {
      // 明るさを徐々に上げる
      for (int value = 0; value <= 255; value += 5) {
        analogWrite(ledPin, value); // 明るさを設定
        delay(30);                  // 30 ミリ秒待機
      }
      // 明るさを徐々に下げる
      for (int value = 255; value >= 0; value -= 5) {
        analogWrite(ledPin, value);
        delay(30);
      }
    }

コードをアップロードすると、LED の明るさが徐々に上がり、また徐々に暗くなる「フェード効果」が確認できます。

**コードの解説**

#. LED ピンの定義

   ``ledPin`` という定数を定義し、GPIO 15 に接続された LED を制御。

   .. code-block:: Arduino

        const int ledPin = 15;

#. ピンの初期設定

   ``setup()`` 関数で ``ledPin`` を 出力モード に設定。

   .. code-block:: Arduino

        void setup() {
          pinMode(ledPin, OUTPUT);
        }

#. ループ関数

    ``loop()`` 関数は繰り返し実行されます。  
    ここでは 2 つの ``for`` ループを使用しています。

     * 明るさを上げる: ``value = 0`` から 5 ずつ増加し、255 になるまで繰り返す。  
     * 明るさを下げる: ``value = 255`` から 5 ずつ減少し、0 になるまで繰り返す。  

   * ``analogWrite()`` 関数は、指定したピンに PWM 信号を出力します。 0（常時 OFF）～255（常時 ON）の範囲で値を指定し、256 段階の明るさを制御できます。  
   * ``delay(30);`` を追加することでループの実行を遅らせ、明るさの変化を人間の目で滑らかに感じられるようにします。

   .. code-block:: Arduino

        void loop() {
          // 明るさを上げる
          for (int value = 0; value <= 255; value += 5) {
            analogWrite(ledPin, value);
            delay(30);
          }
          // 明るさを下げる
          for (int value = 255; value >= 0; value -= 5) {
            analogWrite(ledPin, value);
            delay(30);
          }
        }

**追加のヒント**

* **実験してみよう**: 増加・減少のステップ幅やdelayの時間を変更し、フェードの速度がどう変わるか試してみましょう。  
* **PWM の制限を理解する**: Pico のすべての GPIO ピンは PWM をサポートしていますが、同じ PWM スライスを共有するピンは異なる周波数を設定できません（デューティサイクルは個別に設定可能）。  
* **安全対策**: LED に過電流が流れると故障する可能性があるため、必ず適切な抵抗を使用してください。  

**まとめ**

PWM を使用して、Raspberry Pi Pico 2 でLED のフェード（明るさの変化）を実現できました。  
このプロジェクトでは、デジタル信号を用いてアナログ動作をシミュレートする方法を学びました。  
これは、マイコンや電子回路設計における基本的な概念の 1 つであり、LED 制御だけでなく、モーターや音の出力制御など幅広い用途に応用できます。
