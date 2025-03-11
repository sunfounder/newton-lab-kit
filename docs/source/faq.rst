.. note::

    こんにちは！SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community（Facebook）へようこそ！Raspberry Pi、Arduino、ESP32について、愛好者と共により深く学びましょう。

    **なぜ参加するべきか？**

    - **専門的なサポート**：購入後の問題や技術的な課題を、コミュニティやチームのサポートを受けながら解決できます。
    - **学び＆共有**：スキル向上のためのヒントやチュートリアルを交換できます。
    - **新製品の先行情報**：新製品の発表や試作品の情報をいち早く入手できます。
    - **特別割引**：最新製品を特別価格で購入できます。
    - **イベントやプレゼント企画**：キャンペーンやプレゼント企画に参加できます。

    👉 一緒に探究し、創造しませんか？今すぐ [|link_sf_facebook|] をクリックして参加しましょう！

FAQ
=========

Arduino
---------------------

#. Arduino IDEでコードのアップロードが失敗する場合？
    * Arduino IDEがPicoを正しく認識しているか確認してください。ポートは COMXX (Raspberry Pi Pico 2) である必要があります。詳細な手順については :ref:`setup_pico_arduino` を参照してください。
    * ボード（Raspberry Pi Pico 2）およびポート（COMXX (Raspberry Pi Pico 2)）が正しく選択されているか確認してください。
    * コードが正しく、適切なボードとポートを選択しているにもかかわらずアップロードに失敗する場合、 **Upload** アイコンを再度クリックし、進行状況が「Upload...」と表示されたらUSBケーブルを抜き、 **BOOTSEL** ボタンを押しながら再度接続すると、コードが正常にアップロードされます。

MicroPython
------------------

#. コードを開いて実行する方法は？
    詳細なチュートリアルについては :ref:`open_run_code_py` を参照してください。

#. Raspberry Pi Pico 2 にライブラリをアップロードする方法は？
    詳細なチュートリアルについては :ref:`add_libraries_py` を参照してください。

#. Thonny IDEにMicroPython（Raspberry Pi Pico）インタープリターオプションが表示されない？
    * USBケーブルでPicoが正しくPCに接続されているか確認してください。
    * MicroPythonがPicoにインストールされているか確認してください（ :ref:`install_micropython_on_pico` を参照）。
    * Raspberry Pi Pico 2 のインタープリターは、Thonnyのバージョン3.3.3以上でのみ利用可能です。古いバージョンを使用している場合はアップデートしてください（ :ref:`thonny_ide` を参照）。
    * Micro USBケーブルを何度か抜き差ししてみてください。

#. Thonny IDEでPicoのコードを開けない、または保存できない？
    * USBケーブルでPicoがPCに接続されているか確認してください。
    * インタープリターとして **MicroPython (Raspberry Pi Pico).COMxx** を選択しているか確認してください。

#. Raspberry Pi Pico 2 はThonnyとArduinoを同時に使用できますか？
    いいえ、それぞれ異なる操作が必要です。

    * 先にArduinoで使用していた場合、Thonny IDEで使用するには :ref:`install_micropython_on_pico` を実行してください。
    * 先にThonnyで使用していた場合、Arduino IDEで使用するには :ref:`setup_pico_arduino` を実行してください。

#. Windows 7のPCでPicoが認識されない場合？
    * USB CDCドライバーを以下のリンクからダウンロードしてください：http://aem-origin.microchip.com/en-us/mindi-sw-library?swsearch=Atmel%2520USB%2520CDC%2520Virtual%2520COM%2520Driver
    * ダウンロードした ``amtel_devices_cdc.inf`` を ``pico-serial`` フォルダに解凍してください。
    * ``amtel_devices_cdc.inf`` を ``pico-serial.inf`` にリネームしてください。
    * テキストエディタ（メモ帳など）で ``pico-serial.inf`` を開いて、以下のセクションを修正してください：

    .. code-block::

        [DeviceList]
        %PI_CDC_PICO%=DriverInstall, USB\VID_2E8A&PID_0005&MI_00

        [DeviceList.NTAMD64]
        %PI_CDC_PICO%=DriverInstall, USB\VID_2E8A&PID_0005&MI_00

        [DeviceList.NTIA64]
        %PI_CDC_PICO%=DriverInstall, USB\VID_2E8A&PID_0005&MI_00

        [DeviceList.NT]
        %PI_CDC_PICO%=DriverInstall, USB\VID_2E8A&PID_0005&MI_00

        [Strings]
        Manufacturer = "ATMEL, Inc."
        PI_CDC_PICO = "Pi Pico Serial Port"
        Serial.SvcDesc = "Pi Pico Serial Driver"

    #. 編集が完了したら、ファイル名をpico-serial.infのまま保存してください。
    #. PCのデバイスマネージャーを開き、「ポート（COMとLPT）」内の「CDC Device」を探してください。黄色い警告マークが表示されていることがあります。
    #. 「CDC Device」を右クリックし、「ドライバーの更新」または「ドライバーのインストール」を選択し、作成したファイルを指定してインストールしてください。

.. Piper Make
.. ------------------

.. #. Piper MakeでPicoをセットアップする方法？
..     詳細なチュートリアルについては :ref:`per_setup_pico` を参照してください。

.. #. コードをダウンロードまたはインポートする方法？
..     詳細なチュートリアルについては :ref:`per_save_import` を参照してください。

.. #. Picoに接続する方法？
..     詳細なチュートリアルについては :ref:`connect_pico_per` を参照してください。
