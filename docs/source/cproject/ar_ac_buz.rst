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

.. _ar_ac_buz:

3.1 ブザーを鳴らそう！
==========================

このレッスンでは、Raspberry Pi Pico 2 を使用して **ブザー** を鳴らす方法を学びます。  
ブザーは LED と同様にデジタル出力デバイスであり、制御が非常に簡単です。  
今回は、 **アクティブブザー** を使用します。このブザーは信号を受け取るだけで音を発するため、複雑な周波数制御が不要です。

**アクティブブザーとは？**

**アクティブブザー** は内部に発振回路を持っており、信号を送るだけで音を鳴らせます。  
一方で **パッシブブザー** は、外部からの信号（周波数制御）が必要となります。

|img_buzzer|


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
        - :ref:`cpn_transistor`  
        - 1 (S8050)  
        - |link_transistor_buy|  
    *   - 6  
        - :ref:`cpn_resistor`  
        - 1 (1KΩ)  
        - |link_resistor_buy|  
    *   - 7  
        - アクティブ :ref:`cpn_buzzer`  
        - 1  
        -  


**回路図**

|sch_buzzer|

この回路では、ブザーは **S8050** NPN トランジスタを介して駆動されます。  
トランジスタは電流を増幅するため、Pico に直接接続するよりも大きな音を出すことができます。

動作の仕組み：

* **GP15** が HIGH を出力すると、トランジスタが ON になり、ブザーに電流が流れて音が鳴る。
* **1kΩ 抵抗** はトランジスタの保護のために使用。

**配線図**

必ず **アクティブブザー** を使用してください。  
アクティブブザーは底面が密閉されているのに対し、パッシブブザーは基板が露出しています。

|img_buzzer|

|wiring_beep|


**コードの記述**


.. note::

   * ``3.1_beep.ino`` を ``newton-lab-kit/arduino/3.1_beep`` から開くことができます。  
   * または、このコードを **Arduino IDE** にコピーしてください。  
   * **Raspberry Pi Pico 2** ボードを選択し、適切なポートを設定して「Upload」をクリックしてください。  

.. code-block:: Arduino

    const int buzzerPin = 15;  // トランジスタのベースに接続する GPIO ピン

    void setup() {
      pinMode(buzzerPin, OUTPUT);
    }

    void loop() {
      digitalWrite(buzzerPin, HIGH);  // ブザーを ON
      delay(1000);                    // 1秒間待機
      digitalWrite(buzzerPin, LOW);   // ブザーを OFF
      delay(1000);                    // 1秒間待機
    }

コードをアップロードすると：

* ブザーが 1 秒間鳴り、その後 1 秒間無音 を繰り返します。  
* ブザーが鳴らない場合は、配線を確認し、アクティブブザー を使用していることを確認してください。

**コードの解説**

#. ブザーピンの定義  

   GPIO 15 を buzzerPin として定義し、トランジスタを介してブザーを制御します。

   .. code-block:: Arduino

        const int buzzerPin = 15;  // GPIO 15 をブザー制御ピンとして設定

#. ピンモードの設定  

   buzzerPin を出力モードに設定。

   .. code-block:: Arduino

        void setup() {
          pinMode(buzzerPin, OUTPUT);
        }

#. ブザーの制御 ``loop()`` 関数が繰り返し実行され、ブザーを 1 秒ごとに ON/OFF します。

   * ``digitalWrite(buzzerPin, HIGH)`` → トランジスタを ON にし、ブザーが鳴る
   * ``delay(1000)`` → 1 秒間待機
   * ``digitalWrite(buzzerPin, LOW)`` → トランジスタを OFF にし、ブザーが止まる

   .. code-block:: Arduino

        void loop() {
          digitalWrite(buzzerPin, HIGH);  // ブザーを ON
          delay(1000);                    // 1秒間待機
          digitalWrite(buzzerPin, LOW);   // ブザーを OFF
          delay(1000);                    // 1秒間待機
        }
  

**さらなる応用**

* ビープ音の長さを変える

  * ``delay()`` の値を変更することで、ブザーの ON/OFF の時間を調整可能。  
  * 短くしたり長くしたりして、さまざまな音のパターンを試してみましょう。

* パターンを作成する

  * ``loop()`` 関数内のタイミングを調整し、より複雑な音のパターンを作成。  
  * 例えば、モールス信号の SOS (・・・---・・・) を再現することもできます。

* パッシブブザーを使用する

  * パッシブブザーを使用し、 ``tone()`` 関数で異なる周波数の音を生成可能。  
  * ただし、パッシブブザーの場合は配線とコードの記述方法が異なる点に注意してください。

**まとめ**

このレッスンでは、 **Raspberry Pi Pico とトランジスタを使用してアクティブブザーを鳴らす方法** を学びました。  
GPIO ピンでトランジスタを制御することで、安全にブザーを ON/OFF でき、Pico の GPIO ピンに過負荷をかけることなく動作させることが可能です。  
この基本的な仕組みを応用すれば、より複雑なサウンドを作成したり、アラームや通知音、インタラクティブなプロジェクトに活用できます。
