.. note:: 
    こんにちは、FacebookでSunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、同じ情熱を持つ人々ともっと深く掘り下げましょう。

    **参加する理由は？**

    - **エキスパートサポート**: 私たちのコミュニティとチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**: スキル向上のためのヒントやチュートリアルを交換します。
    - **独占プレビュー**: 新製品の発表やちら見せに早期アクセス。
    - **特別割引**: 最新製品の独占的な割引を楽しんでください。
    - **祭りのプロモーションとギブアウェイ**: ギブアウェイや祝日のプロモーションに参加します。

    👉 私たちと一緒に探索し、創造する準備はできましたか？[|link_sf_facebook|]をクリックして今日参加しましょう！

.. _cpn_buzzer:

ブザー
=======


DC電源で駆動する統合構造の電子ブザーは、コンピューター、プリンター、コピー機、アラーム、電子玩具、自動車電子機器、電話、タイマーなどの電子製品や音声装置で広く使用されています。

ブザーはアクティブブザーとパッシブブザーの2種類に分類されます（以下の画像を参照）。ブザーをピンが上を向くようにして、緑色の基板があるものがパッシブブザー、黒いテープで封じられているものがアクティブブザーです。

|img_buzzer|

アクティブブザーとパッシブブザーの違い：

アクティブブザーは発振源を内蔵しているため、電流が流れると音が出ます。しかし、パッシブブザーにはそのような発振源がないため、DC信号では音が鳴りません。代わりに2Kから5Kの周波数の方形波を使って駆動する必要があります。複数の発振回路が内蔵されているため、アクティブブザーは通常、パッシブブザーよりも高価です。

以下はブザーの電気記号です。正極と負極の2つのピンがあり、表面に+があるものがアノード、それ以外がカソードです。

|img_buzzer_symbol|

ブザーのピンを確認できます。長い方がアノードで、短い方がカソードです。接続するときに間違えないようにしてください。そうでないとブザーは音を鳴らしません。

`Buzzer - Wikipedia <https://en.wikipedia.org/wiki/Buzzer>`_

.. 例
.. -------------------

.. :ref:`Intruder Alarm`

.. :ref:`Custom Tone`

**例**

* :ref:`py_ac_buz` (MicroPythonユーザー向け)
* :ref:`py_pa_buz` (MicroPythonユーザー向け)
* :ref:`py_light_theremin` (MicroPythonユーザー向け)
* :ref:`py_alarm_lamp` (MicroPythonユーザー向け)
* :ref:`py_music_player` (MicroPythonユーザー向け)
* :ref:`py_fruit_piano` (MicroPythonユーザー向け)
* :ref:`py_reversing_aid` (MicroPythonユーザー向け)
* :ref:`ar_ac_buz` (Arduinoユーザー向け)
* :ref:`ar_pa_buz` (Arduinoユーザー向け)
.. * :ref:`per_service_bell` (Piper Makeユーザー向け)
.. * :ref:`per_reversing_system` (Piper Makeユーザー向け)
.. * :ref:`per_reaction_game` (Piper Makeユーザー向け)
