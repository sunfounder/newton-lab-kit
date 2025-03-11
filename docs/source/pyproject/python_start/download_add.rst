.. note::

    こんにちは、FacebookでSunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！ラズベリーパイ、アルドゥイーノ、ESP32の更なる深掘りを、同じ興味を持つ仲間たちと一緒に楽しみましょう。

    **参加する理由は？**

    - **専門家によるサポート**: コミュニティとチームからのサポートで、購入後の問題や技術的な課題を解決します。
    - **学びと共有**: スキル向上のためのヒントやチュートリアルを交換しましょう。
    - **独占的なプレビュー**: 新製品の発表や先取り情報に早期アクセスが可能です。
    - **特別割引**: 最新商品の独占割引をお楽しみいただけます。
    - **祭りプロモーションとギブアウェイ**: ギブアウェイやホリデープロモーションに参加しましょう。

    👉 私たちと一緒に探求し、創造する準備はできましたか？[|link_sf_facebook|]をクリックして今日から参加しましょう！

.. _download_upload:

1.4 コードのダウンロードとアップロード
===============================================

**コードのダウンロード**

以下のリンクから関連するコードをダウンロードしてください。


* :download:`SunFounder Newton Lab Kit Example <https://github.com/sunfounder/newton-lab-kit/archive/refs/heads/main.zip>`

* または `Newton Lab Kit - GitHub <https://github.com/sunfounder/newton-lab-kit>`_ でコードをチェックしてください。

.. _add_libraries_py:

Picoにライブラリをアップロード
----------------------------------
一部のプロジェクトでは、追加のライブラリが必要です。ここでは、まずこれらのライブラリをRaspberry Pi Pico 2にアップロードし、後で直接コードを実行できるようにします。

#. Micro USBケーブルを使用して、Raspberry Pi Pico 2をコンピューターに接続します。（ **BOOTSEL** を押さないでください。前のステップでMicroPythonファームウェアをPico 2にドラッグしたので、直接差し込んでください。）

#. Thonny IDEを開き、右下のインタープリター選択ボタンから「MicroPython (Raspberry Pi Pico).COMxx.COMxx」を選択します。

   .. image:: img/th_select_com.png

#. Thonny IDEのトップナビゲーションバーで **View** -> **Files** をクリックします。

   .. image:: img/th_open_files.png

#. 以前にダウンロードしたコードパッケージが保存されているフォルダに移動し、 ``newton-lab-kit-main/libs`` フォルダに進みます。

   .. image:: img/th_open_code.png

#. 今度は ``libs\`` フォルダ内のすべてのファイルを選択し、Raspberry Pi Pico 2にアップロードします。ファイルのアップロードにはしばらく時間がかかります。

   .. image:: img/th_upload_libs.png

#. アップロードしたファイルは ``Raspberry Pi Pico 2`` とラベル付けされたドライブ内に表示されます。

   .. image:: img/th_pico_libs.png
