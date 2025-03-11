.. note::

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！ラズベリーパイ、アルドゥイーノ、ESP32について、同じ趣味を持つ人々とさらに深く探求しましょう。

    **参加する理由は？**

    - **専門家によるサポート**: コミュニティとチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学びと共有**: 技術を磨くためのヒントやチュートリアルを交換しましょう。
    - **独占プレビュー**: 新製品の発表やちら見せに早期アクセスが可能です。
    - **特別割引**: 最新製品を特別割引価格でお楽しみください。
    - **祝祭プロモーションとギブアウェイ**: ギブアウェイや休日のプロモーションに参加しましょう。

    👉 私たちと一緒に探求し、創造しませんか？[|link_sf_facebook|]をクリックして今すぐ参加！

.. _ar_pa_buz:

3.2 パッシブブザーでカスタムトーンを再生する
================================================

このレッスンでは、Raspberry Pi Pico 2を使用して、異なるトーンや簡単なメロディーを演奏する方法を学びます。アクティブブザーとは異なり、パッシブブザーは音を出すために変化する電気信号が必要です。これにより、信号の周波数を変更することで音の高さを制御できます。

**必要なもの**

このプロジェクトには、以下のコンポーネントが必要です。

全てのキットを購入するのが便利ですが、こちらがリンクです：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - このキットのアイテム
        - リンク
    *   - Newton Lab Kit
        - 450以上
        - |link_newton_lab_kit|

個別に購入することもできます。以下のリンクからどうぞ。


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
        - Passive :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|

**パッシブブザーの仕組み**

パッシブブザーは小さなスピーカーのように機能します。自ら音を発することはありません。代わりに、振動する信号が必要です。異なる周波数の信号を提供することにより、ブザーを使って異なるピッチの音を出し、音符やメロディーを演奏することができます。

|img_buzzer|

**回路図**

|sch_buzzer|

この回路では、パッシブブザーはトランジスタ（ **S8050** NPN）を通して電力を供給されます。トランジスタは電流を増幅し、Picoに直接接続されている場合よりも大きな音を出します。

以下のように動作します：

* **GP15** は高い信号を出力してトランジスタを制御します。
* トランジスタが動作すると、ブザーを通して電流が流れ、ビープ音が鳴ります。

トランジスタを保護するために **1kΩの抵抗** が使用されます。

**配線図**

**パッシブブザー** を使用していることを確認してください。裸のPCBが見えるものが正しいものです（密閉された背面のアクティブブザーとは異なります）。

|img_buzzer|

|wiring_buzzer|

**コードの書き方**


.. note::

   * ファイル ``3.2_custom_tone.ino`` を ``newton-lab-kit/arduino/3.2_custom_tone`` から開くことができます。
   * あるいは、このコードを **Arduino IDE** にコピーしてください。
   * **Raspberry Pi Pico 2** ボードと正しいポートを選択し、「Upload」をクリックします。

.. code-block:: arduino

    const int buzzerPin = 15;  // トランジスタのベースに接続されたGPIOピン

    void setup() {
      pinMode(buzzerPin, OUTPUT);
    }

    void loop() {
      // 440 Hz（A4音）のトーンを1秒間再生
      tone(buzzerPin, 440, 1000);
      delay(1000);  // トーンの終了を待つ
      // 再度演奏する前に1秒間待つ
      delay(1000);
    }

コードは440 Hzのトーン（標準的なA音）を1秒間再生し、1秒間待って繰り返します。

* ``tone(pin, frequency, duration)``:

  * ``pin``: トランジスタを通じてブザーに接続されたGPIOピン。
  * ``frequency``: トーンの周波数をヘルツ（Hz）で。
  * ``duration (optional)``: トーンを再生する持続時間をミリ秒で。


**メロディを演奏する**

コードを拡張して、定義された音符とそれに対応する周波数で単純なメロディを演奏しましょう。

* 配列 ``melody[]`` は演奏する音符の順序を保持します。
* 配列 ``noteDurations[]`` は各音符の持続時間を定義します。4の持続時間は四分音符を表します。
* ``for`` ループはメロディ内の各音符を反復処理します。

  * ミリ秒単位で音符の持続時間を計算します。
  * ``tone()`` を使用して各音符を演奏します。
  * ``delay()`` を使用して音符間の休止を取ります。
  * 次の音符に移る前に ``noTone()`` を呼び出してトーンを停止します。

.. code-block:: arduino

        // ブザーピンを定義
        const int buzzerPin = 15;

        // 音符の周波数を定義
        #define NOTE_C4  262
        #define NOTE_D4  294
        #define NOTE_E4  330
        #define NOTE_F4  349
        #define NOTE_G4  392
        #define NOTE_A4  440
        #define NOTE_B4  494
        #define NOTE_C5  523

        // メロディの音符
        int melody[] = {
          NOTE_C4, NOTE_D4, NOTE_E4, NOTE_F4,
          NOTE_G4, NOTE_A4, NOTE_B4, NOTE_C5
        };

        // ノートの長さ：4 = 四分音符、8 = 八分音符など
        int noteDurations[] = {
          4, 4, 4, 4,
          4, 4, 4, 4
        };

        void setup() {
          pinMode(buzzerPin, OUTPUT);
        }

        void loop() {
          // メロディのノートを反復処理
          for (int thisNote = 0; thisNote < 8; thisNote++) {
            int noteDuration = 1000 / noteDurations[thisNote];
            tone(buzzerPin, melody[thisNote], noteDuration);
            // ノート間の一時停止
            int pauseBetweenNotes = noteDuration * 1.30;
            delay(pauseBetweenNotes);
            // トーンを停止
            noTone(buzzerPin);
          }
          // メロディを繰り返す前に遅延
          delay(2000);
        }

コードをアップロードした後、ブザーがメロディを演奏するのが聞こえるはずです。音が小さい場合は、すべての接続が確実であることを確認してください。パッシブブザーは非常に大きな音を出すことはありません。

**さらに学ぶ**

* 独自のメロディを作成する：

  ``melody[]`` および ``noteDurations[]`` 配列を変更して、独自のメロディを作成できます。

* ``pitches.h`` ライブラリの使用：

  多くの音符の定義が含まれている ``pitches.h`` というライブラリファイルを便宜上含めることができます。
  ``pitches.h`` というファイルを作成し、スケッチに含めてください。
  
  .. code-block:: arduino

    #include "pitches.h"

**さらなる探求**

* 自作の曲を作る：

  新しいノートのシーケンスと持続時間を定義して、自分だけの曲を作成してみてください。

* インタラクティブ音楽：

  ボタンやセンサーを追加して、メロディの再生を制御します。

* 視覚フィードバック：

  ノートが演奏されるのに合わせてLEDを光らせることで統合します。

**まとめ**

このレッスンでは、Raspberry Pi Picoを使用してパッシブブザーで異なるトーンやメロディを再生する方法を学びました。ブザーに送信される信号の周波数を制御することにより、さまざまなピッチを生成し、プロジェクトに音楽を作成することができます。
