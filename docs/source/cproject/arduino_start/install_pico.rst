.. note:: 
    FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Raspberry Pi、Arduino、ESP32についての知識を深め、同じ趣味を持つ仲間と交流しましょう。

    **なぜ参加するのか？**

    - **専門的なサポート**: コミュニティとチームの支援を受けて、販売後の問題や技術的な課題を解決します。
    - **学びと共有**: ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**: 新製品の発表や先行プレビューに早期アクセスが可能です。
    - **特別な割引**: 最新製品の独占的な割引を楽しみましょう。
    - **祭りのプロモーションとギブアウェイ**: ギブアウェイや休日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造しませんか？[|link_sf_facebook|]をクリックして今すぐ参加してください！

.. _setup_pico_arduino:

1.3 Raspberry Pi Pico 2のセットアップ（重要）
==================================================

1. ボードパッケージのインストール
--------------------------------------

Raspberry Pi Pico 2をプログラムするには、Arduino IDEに適切なボードパッケージをインストールする必要があります。以下の手順に従ってセットアップを行ってください。

#. Arduino IDEを開き、 **ファイル** -> **環境設定** に移動します。

   .. image:: img/arduino_pico_file.png

#. 表示されるダイアログの「追加のボードマネージャーのURL」フィールドに、以下のURLを入力します。  
   ``https://github.com/earlephilhower/arduino-pico/releases/download/global/package_rp2040_index.json``

   .. image:: img/arduino_pico_link.png

#. **ボードマネージャー** を開き、 **pico** と検索します。  
   **INSTALL**ボタンをクリックしてインストールを開始してください。これにより、 **Raspberry Pi Pico 2/RP2040** パッケージがインストールされ、Raspberry Pi Pico 2のサポートが追加されます。

   .. image:: img/arduino_pico_install.png

#. インストール中に、特定のデバイスドライバをインストールするよう求めるポップアップが表示される場合があります。 **「Install」** を選択してください。

   .. image:: img/install_pico_sa.png

#. インストールが完了すると、正常にセットアップされたことを示す通知が表示されます。

2. ボードとポートの選択
------------------------------------------

#. **BOOTSEL** ボタンを押しながら、Raspberry Pi Pico 2をUSBポートから抜き、すぐに再接続します。

   .. image:: img/led_onboard.png
        :width: 500
        :align: center

   .. warning::    

      * このステップは特にArduino IDEを初めて使用する場合に重要です。スキップするとアップロードが失敗します。  
      * コードのアップロードが成功すると、Pico 2はコンピュータによって認識されます。以降のアップロードでは、ボタンを押さずにPico 2を接続するだけで大丈夫です。

#. **ツール** -> **ボード** -> **Raspberry Pi Pico 2/RP2040** -> **Raspberry Pi Pico 2** を選択します。

   .. image:: img/arduino_pico_board.png
      :width: 800
      :align: center

#. 次に、正しいポートを選択するために、 **ツール** -> **ポート** -> **UF2 Board** を選択します。

   .. note::    
     * 初回接続時や **BOOTSEL** ボタンを押している場合は **UF2 Board** を選択してください。  
     * コードのアップロードが成功すると、Pico 2はコンピュータに認識されます。以降は、対応する **COMxx (Raspberry Pi Pico 2)** を選択してください。

   .. image:: img/arduino_pico_port.png


3. コードのアップロード
--------------------------

Raspberry Pi Pico 2にコードをアップロードする手順を説明します。

#. 既存の ``.ino`` ファイルを開くか、デフォルトで表示される空のスケッチを使用します。その後、 **Upload** ボタンをクリックします。

   .. image:: img/install_pico_upload.png

#. アップロードが完了すると、確認のメッセージが表示されます。

   .. image:: img/install_pico_upload_done.png

#. コンピュータがPico 2を正常に認識していることを確認してください。

   .. image:: img/arduino_pico_port_com.png

#. Arduino 2.0では、ボードとポートの設定を簡単に行えるクイックセレクト機能が追加されました。

   .. image:: img/install_pico_select.png
