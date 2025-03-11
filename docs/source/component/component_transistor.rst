.. note:: 
    FacebookでSunFounder Raspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Raspberry Pi、Arduino、ESP32についての知識を深め、同じ趣味を持つ仲間と交流しましょう。

    **なぜ参加するのか？**

    - **専門的なサポート**: 私たちのコミュニティとチームからの支援で、販売後の問題や技術的な課題を解決します。
    - **学びと共有**: ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**: 新製品の発表や先行プレビューに早期アクセスが可能です。
    - **特別な割引**: 最新製品の独占的な割引を楽しむことができます。
    - **祭りのプロモーションとギブアウェイ**: ギブアウェイや休日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造しませんか？[|link_sf_facebook|]をクリックして今すぐ参加してください！

.. _cpn_transistor:

トランジスタ
===============

|img_NPN&PNP|

トランジスタは、電流で電流を制御する半導体デバイスです。弱い信号を大きな振幅の信号に増幅する機能を持ち、非接触スイッチとしても使用されます。

トランジスタはP型とN型の半導体から成る三層構造で、内部に三つの領域を形成します。中間の薄い部分がベース領域で、他の二つの領域はN型またはP型で、主なキャリアが多い小さい領域がエミッタ領域、もう一つがコレクタ領域です。この構成により、トランジスタは増幅器として機能します。
これら三つの領域からそれぞれベース(b)、エミッタ(e)、コレクタ(c)の三つの端子が生成されます。二つのP-N接合、すなわちエミッタ接合とコレクタ接合を形成します。トランジスタ回路記号の矢印の方向はエミッタ接合の方向を示しています。

* `P–N junction - Wikipedia <https://en.wikipedia.org/wiki/P-n_junction>`_

半導体のタイプに基づいて、トランジスタはNPNとPNPの二つのグループに分けられます。略称から、前者は二つのN型半導体と一つのP型で構成され、後者はその逆であることが分かります。下記の図を参照してください。

.. note::
    s8550はPNPトランジスタで、s8050はNPNトランジスタです。非常に似ていますので、ラベルを注意深く確認する必要があります。

|img_transistor_symbol|

NPNトランジスタに高レベル信号が通過すると、エネルギーが供給されます。しかし、PNPトランジスタは低レベル信号で制御する必要があります。両タイプのトランジスタは、この実験のように非接触スイッチで頻繁に使用されます。

* `S8050トランジスタデータシート <https://components101.com/asset/sites/default/files/component_datasheet/S8050%20Transistor%20Datasheet.pdf>`
* `S8550トランジスタデータシート <https://www.mouser.com/datasheet/2/149/SS8550-118608.pdf>`

ラベル面を前にしてピンを下に向けると、左から右にエミッタ(e)、ベース(b)、コレクタ(c)のピンがあります。

.. note::
    * ベースはより大きな電気供給のためのゲート制御装置です。
    * NPNトランジスタでは、コレクタがより大きな電気供給であり、エミッタはその供給の出口ですが、PNPトランジスタはその逆です。


.. Example
.. -------------------

.. :ref:`二つのトランジスタの種類`

**例**

* :ref:`py_transistor` (MicroPythonユーザー用)
* :ref:`py_relay` (MicroPythonユーザー用)
* :ref:`py_ac_buz` (MicroPythonユーザー用)
* :ref:`py_pa_buz` (MicroPythonユーザー用)
* :ref:`py_light_theremin` (MicroPythonユーザー用)
* :ref:`py_alarm_lamp` (MicroPythonユーザー用)
* :ref:`py_music_player` (MicroPythonユーザー用)
* :ref:`py_fruit_piano` (MicroPythonユーザー用)
* :ref:`py_reversing_aid` (MicroPythonユーザー用)
* :ref:`ar_ac_buz` (Arduinoユーザー用)
* :ref:`ar_pa_buz` (Arduinoユーザー用)
* :ref:`ar_transistor` (Arduinoユーザー用)
* :ref:`ar_relay` (Arduinoユーザー用)
.. * :ref:`per_service_bell` (For Piper Make User)
.. * :ref:`per_reversing_system` (For Piper Make User)
.. * :ref:`per_reaction_game` (For Piper Make User)