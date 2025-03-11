.. note:: 
    FacebookでSunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について熱心な仲間ともっと深く探求しましょう。

    **参加する理由は？**

    - **専門的サポート**: 当コミュニティとチームからの支援を受けて、販売後の問題や技術的な課題を解決します。
    - **学びと共有**: ヒントやチュートリアルを交換してスキルを高めましょう。
    - **独占的プレビュー**: 新製品発表やちら見せに早期アクセス。
    - **特別割引**: 最新製品の独占割引をお楽しみください。
    - **祭りプロモーションとギブアウェイ**: ギブアウェイやホリデープロモーションに参加しましょう。

    👉 私たちと一緒に探検し、創造しませんか？[|link_sf_facebook|]をクリックして今すぐ参加！

.. _cpn_led:

LED
==========

|img_led|

半導体発光ダイオードは、PN接合を介して電気エネルギーを光エネルギーに変換するコンポーネントです。波長によって、レーザーダイオード、赤外線発光ダイオード、そして一般的にLED（発光ダイオード）として知られる可視光発光ダイオードに分類されます。

ダイオードは一方向性の導電性を持ちますので、図の回路記号に示された矢印の方向でのみ電流が流れます。陽極に正の電源、陰極に負の電源を供給することでLEDは点灯します。

|img_led_symbol|

LEDには2つのピンがあります。長い方が陽極、短い方が陰極です。接続を逆にしないよう注意してください。LEDには固定の順方向電圧降下があり、そのため直接回路に接続することはできません。供給電圧がこの降下を超えるとLEDが焼損する可能性があります。赤、黄、緑色のLEDの順方向電圧は1.8V、白色のLEDは2.6Vです。ほとんどのLEDは最大20mAの電流に耐えることができるため、直列に電流制限抵抗を接続する必要があります。

抵抗値の計算式は以下の通りです：

    R = (Vsupply – VD)/I

ここで、 **R** は電流制限抵抗の抵抗値、 **Vsupply** は供給電圧、 **VD** は電圧降下、 **I** はLEDの動作電流を指します。

LEDに関する詳細な紹介はこちら： `LED - Wikipedia <https://en.wikipedia.org/wiki/Light-emitting_diode>`_。

.. **Example**

.. * :ref:`Hello, Breadboard!` (For MicroPython User)
.. * :ref:`fading_led_micropython` (For MicroPython User)
.. * :ref:`fading_led_arduino` (For C/C++(Arduino) User)
.. * :ref:`hello_led_arduino` (For C/C++(Arduino) User)


**例**

* :ref:`py_led` (MicroPythonユーザー向け)
* :ref:`py_fade` (MicroPythonユーザー向け)
* :ref:`py_alarm_lamp` (MicroPythonユーザー向け)
* :ref:`py_traffic_light` (MicroPythonユーザー向け)
* :ref:`py_reversing_aid` (MicroPythonユーザー向け)
* :ref:`ar_led` (Arduinoユーザー向け)
* :ref:`ar_fade` (Arduinoユーザー向け)
.. * :ref:`per_blink` (Piper Makeユーザー向け)
.. * :ref:`per_button` (Piper Makeユーザー向け)
.. * :ref:`per_service_bell` (Piper Makeユーザー向け)
.. * :ref:`per_reversing_system` (Piper Makeユーザー向け)
.. * :ref:`per_reaction_game` (Piper Makeユーザー向け)
