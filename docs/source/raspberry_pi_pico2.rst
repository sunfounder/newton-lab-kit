.. note:: 

    こんにちは！FacebookのSunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32について、仲間と共に深く学び、探求しましょう。

    **Why Join?**

    - **専門的なサポート**：購入後の問題や技術的な課題を、コミュニティやチームのサポートを受けながら解決できます。
    - **学び＆共有**：スキル向上のためのヒントやチュートリアルを交換できます。
    - **新製品の先行情報**：新製品の発表や試作品の情報をいち早く入手できます。
    - **特別割引**：最新製品を特別価格で購入できます。
    - **イベントやプレゼント企画**：キャンペーンやプレゼント企画に参加できます。

    👉 一緒に探究し、創造しませんか？今すぐ [|link_sf_facebook|] をクリックして参加しましょう！

.. _cpn_pico_2:

Raspberry Pi Pico 2
==============================================

.. image:: img/pico-2.png
    :width: 200
    :align: center

Raspberry Pi Pico 2は、コアクロック速度の向上、メモリの倍増、より強力なArmコア、オプションのRISC-Vコア、新たなセキュリティ機能、強化されたインターフェースを備え、大幅な性能向上を実現しています。それでいて、従来のRaspberry Pi Pico 2シリーズとの互換性を維持しています。

C / C++およびPythonでプログラム可能で、詳細なドキュメントが提供されているため、エンジニアや愛好者からプロの開発者まで幅広く活用できます。

特長
--------------

* Raspberry Pi Pico 2は、低コストかつ高性能なマイコンボードで、柔軟なデジタルインターフェースを備えています。主な特長は以下の通りです：
* Raspberry Piが英国で設計したRP2350マイクロコントローラーチップ
* 最大150MHzのデュアルCortex-M33またはHazard3プロセッサ
* 520KBのSRAM、および4MBのオンボードフラッシュメモリ
* デバイスおよびホスト対応のUSB 1.1
* 低消費電力スリープおよびドーマントモード
* USBマスストレージ経由のドラッグ＆ドロッププログラミング
* 26本の多機能GPIOピン（うち3本はADCとして利用可能）
* 2x SPI、2x I2C、2x UART、3x 12-bit 500ksps アナログ-デジタルコンバーター（ADC）、24x PWMチャンネル
* 2x タイマー（4つのアラーム付き）、1x AONタイマー
* 温度センサー搭載
* 3 x プログラマブルIO（PIO）ブロック、合計12のステートマシンでカスタム周辺機能をサポート
    * 柔軟かつユーザー定義可能な高速IO
    * SDカードやVGAなどのインターフェースをエミュレート可能

Picoのピン構成
----------------

.. image:: img/pico-2-r4-pinout.svg
    :width: 800

**電源ピン**

Pico 2のピン配置は、RP2350のGPIOおよび内部回路機能を最大限に活用しながら、EMI（電磁干渉）や
信号クロストークを低減するために十分なグラウンドピンを確保するよう設計されています。
特にRP2350は40nmプロセスで製造されており、高速なデジタルIOエッジレートを持つため、この設計は
非常に重要です。

**汎用I/O**

Raspberry Pi Pico 2のGPIOは、オンボードの3.3Vレールから供給され、3.3Vに固定されています。
Pico 2は、30本のRP2350 GPIOピンのうち26本をヘッダーピンに直接出力しています。GPIO0〜GPIO22はデジタル専用であり、GPIO26〜28はデジタルGPIOまたはADC入力として利用可能（ソフトウェア設定で選択可）です。
注意点として、ADC対応のGPIO26〜29にはVDDIO（3.3V）レールへの逆ダイオードが存在するため、入力電圧はVDDIO+約300mVを超えないようにする必要があります。また、RP2350が電源オフの状態でこれらのGPIOピンに電圧を加えると、ダイオードを介してVDDIOレールに電流が漏れる可能性があります。

GPIOおよびグラウンドピンに加えて、メインの40ピンインターフェースには以下の7つのピンがあります：

  * **RUN**: RP2350のイネーブルピンで、内部プルアップ抵抗（約50kΩ）を介して3.3Vに接続されています。RP2350をリセットするには、このピンを短絡してください。
  * **ADC_VREF**: ADCの電源供給（およびリファレンス）電圧で、Pico 2では3.3Vをフィルタリングして生成されます。ADCの精度を向上させるため、外部リファレンスを使用することも可能です。
  * **AGND**: GPIO26-29用のアナロググラウンドリファレンス。このピンには、これらの信号の下に専用のアナロググラウンドプレーンが走っています。ADCを使用しない場合や、ADCの精度が重要でない場合は、このピンをデジタルグラウンドに接続しても問題ありません。
  * **3V3(O)**: RP2350とそのI/Oの主な3.3V電源で、オンボードのSMPS（スイッチング電源）によって生成されます。このピンから外部回路への電源供給も可能ですが、RP2350の負荷やVSYS電圧によって供給可能な電流が変動するため、300mA以下に抑えることが推奨されます。
  * **3V3(E)**: オンボードのSMPSイネーブルピンに接続されており、100kΩ抵抗を介してVSYSにプルアップされています。3.3Vを無効化し（RP2350の電源もオフ）、このピンを短絡することで電源を制御できます。
  * **VSYS**: メインシステムの入力電圧で、1.8V〜5.5Vの範囲で変動可能です。オンボードSMPSによって3.3Vが生成され、RP2350とそのGPIOに供給されます。
  * **VBUS**: micro-USBの入力電圧で、micro-USBポートの1ピンに接続されています。通常5Vですが、USBが接続されていない場合は0Vになります。

いくつかのRP2350 GPIOピンは内部ボード機能に使用されています：

  * **GPIO29**: ADCモード（ADC3）でVSYS/3を測定
  * **GPIO25**: ユーザーLEDに接続
  * **GPIO24**: VBUS検出用（VBUSが接続されている場合はHigh、それ以外はLow）
  * **GPIO23**: オンボードSMPS Power Saveピンを制御

Raspberry Pi Pico 2のセットアップや使用に必要なすべての情報は、 `こちら <https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html>`_ でご確認いただけます。

また、以下のリンクからも詳細な資料をダウンロードできます。

* `Raspberry Pi Pico 2 製品概要 <https://datasheets.raspberrypi.com/pico/pico-2-product-brief.pdf>`_
* `Raspberry Pi Pico 2 データシート <https://datasheets.raspberrypi.com/pico/pico-2-datasheet.pdf?_gl=1*898c50*_ga*NTA0MDU1Njg3LjE3MjUzMjY4MDE.*_ga_22FD70LWDS*MTcyNjcxMjQ2MS44LjEuMTcyNjcxMzI1NS4wLjAuMA..>`_
* `Raspberry Pi Pico 2シリーズ マイコンの始め方 <https://datasheets.raspberrypi.com/pico/getting-started-with-pico.pdf?_gl=1*1naoekg*_ga*NTA0MDU1Njg3LjE3MjUzMjY4MDE.*_ga_22FD70LWDS*MTcyNjcxMjQ2MS44LjEuMTcyNjcxMzI1NS4wLjAuMA..>`_
* `Raspberry Pi Pico 2 C/C++ SDK <https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-c-sdk.pdf>`_
* `Raspberry Pi Pico 2 MicroPython SDK <https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf>`_
* `Raspberry Pi RP2350 データシート <https://datasheets.raspberrypi.com/rp2350/rp2350-datasheet.pdf>`_
* `Raspberry Pi Pico 2 STEPファイル <https://datasheets.raspberrypi.com/pico/Pico-2-step-20240708.zip?_gl=1*1ol9494*_ga*NTA0MDU1Njg3LjE3MjUzMjY4MDE.*_ga_22FD70LWDS*MTcyNjcxMjQ2MS44LjEuMTcyNjcxMjYzMC4wLjAuMA..>`_
* `RP2350を使用したハードウェア設計 <https://datasheets.raspberrypi.com/rp2350/hardware-design-with-rp2350.pdf>`_
