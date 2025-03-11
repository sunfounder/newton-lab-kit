.. note::

    こんにちは、FacebookでのSunFounder Raspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！ラズベリーパイ、アルドゥイーノ、ESP32について、同じ趣味を持つ仲間たちとさらに深く探求しましょう。

    **参加する理由は？**

    - **エキスパートサポート**: コミュニティやチームからのサポートで、購入後の問題や技術的な課題を解決します。
    - **学びと共有**: スキルアップのためのヒントやチュートリアルを交換しましょう。
    - **独占プレビュー**: 新製品の発表や先取り情報に早期アクセスします。
    - **特別割引**: 最新商品の独占割引をお楽しみいただけます。
    - **祭りプロモーションとギブアウェイ**: ギブアウェイやホリデープロモーションに参加しましょう。

    👉 私たちと一緒に探求し、創造してみませんか？[|link_sf_facebook|]をクリックして今日から参加しましょう！

.. _install_micropython_on_pico:

1.3 ピコ2にマイクロパイソンをインストール
==========================================

ここでRaspberry Pi Pico 2にMicroPythonをインストールします。Thonny IDEはクリック一つで簡単にインストールできる便利な方法を提供しています。

.. note::
    Thonnyをアップグレードしたくない場合は、Raspberry Pi公式の |link_micropython_method| を使用して、 ``rp2_pico_xxxx.uf2`` ファイルをRaspberry Pi Pico2にドラッグ＆ドロップすることもできます。


#. Thonny IDEを開きます。

    .. image:: img/new/set_pico1.png

#. **BOOTSEL** ボタンを押しながら、Micro USBケーブルでPico2をコンピューターに接続します。Pico2が **RPI-RP2040** としてマスストレージデバイスとしてマウントされた後、 **BOOTSEL** ボタンを放します。

    .. image:: img/new/bootsel_onboard.png

#. 右下のインタープリタ選択ボタンをクリックし、 **Install Micropython** を選択します。

    .. note::
        Thonnyにこのオプションがない場合は、最新バージョンにアップデートしてください。

    .. image:: img/new/set_pico2.jpg

#. **Target volume** で、接続したばかりのPico2のボリュームが自動的に表示され、「Micropython variant」で **Micropython variant** を選択します。

    .. image:: img/new/set_pico3.jpg

#. **Install** ボタンをクリックし、インストールが完了するのを待ってから、このページを閉じます。

    .. image:: img/new/set_pico4.jpg


おめでとうございます、これでRaspberry Pi Pico2は使用準備が整いました。
