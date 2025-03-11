.. note:: 

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Raspberry Pi、Arduino、ESP32についてもっと深く探求しましょう。

**参加する理由?**

- **専門家のサポート**: コミュニティとチームからのサポートで販売後の問題や技術的な課題を解決。
- **学びと共有**: スキル向上のためのヒントやチュートリアルを交換。
- **独占プレビュー**: 新製品の発表や先行予告をいち早く入手。
- **特別割引**: 最新製品の独占割引を楽しむ。
- **祝祭プロモーションとギブアウェイ**: ギブアウェイや休日プロモーションに参加。

👉 一緒に探求し、創造してみませんか？クリック [|link_sf_facebook|] して今すぐ参加！

.. _py_bubble_level:

7.12 デジタル水準器の作成
==========================================

このプロジェクトでは、Raspberry Pi Pico 2、MPU6050加速度計・ジャイロスコープモジュール、そして2つの74HC595シフトレジスタによって制御される8x8 LEDマトリックスディスプレイを使用して、 **デジタル水準器** を作成します。このデバイスは伝統的な水準器と同様に機能し、表面の傾きを示します。MPU6050を傾けると、マトリックス上のLEDで表された「バブル」が移動し、表面の水平を視覚的に確認できます。

**必要なもの**

このプロジェクトには以下のコンポーネントが必要です。

キット全体を購入することは非常に便利です。こちらがリンクです：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名称	
        - このキットに含まれるアイテム
        - リンク
    *   - Newton Lab Kit	
        - 450以上
        - |link_newton_lab_kit|

以下のリンクから個別に購入することもできます。


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
        - :ref:`cpn_dot_matrix`
        - 1
        - 
    *   - 6
        - :ref:`cpn_74hc595`
        - 2
        - |link_74hc595_buy|
    *   - 7
        - :ref:`cpn_mpu6050`
        - 1
        - 

**コンポーネントの理解**

* **MPU6050加速度計とジャイロスコープ**: X、Y、Zの三軸に沿って加速度と角速度のデータを提供し、これを使用して傾斜角を計算します。
* **8x8 LEDマトリックスディスプレイ**: 8行と8列に配列されたLEDで、個々のLEDを制御することによってパターンや画像を表示できます。
* **74HC595シフトレジスタ**: PicoのGPIOピンよりも少ないピンを使用して複数の出力（この場合はLEDマトリックスの行と列）を制御することができます。

**回路図**

|sch_bubble_level|

MPU6050は各方向の加速度値を取得し、姿勢角を計算します。

その結果、プログラムは2つの74HC595チップからのデータに基づいてドットマトリックス上に2x2のドットを描画します。

姿勢角が変化すると、プログラムは74HC595チップに異なるデータを送信し、ドットの位置が変わり、バブル効果が生まれます。

**配線**

|wiring_digital_bubble_level| 


**コードの書き方**

MicroPythonスクリプトを書いて、以下の操作を行います：

* MPU6050から加速度データを読み取る。
* X軸およびY軸に沿った傾斜角を計算する。
* 傾斜角を8x8 LEDマトリックス上の位置にマッピングする。
* 傾斜に応じて移動する「バブル」（2x2ピクセルの表現）を表示する。

.. note::

    * ``7.12_digital_bubble_level.py`` を ``newton-lab-kit/micropython`` から開くか、Thonnyにコードをコピーして「実行」ボタンをクリックするか、F5キーを押します。
    * 正しいインタープリタが選択されていることを確認してください：MicroPython (Raspberry Pi Pico).COMxx。 
    * ``imu.py`` および ``vector3d.py`` がPicoにアップロードされていることを確認してください。詳細なチュートリアルは :ref:`add_libraries_py` を参照してください。

.. code-block:: python

    import machine
    from machine import I2C, Pin
    import time
    import math
    from imu import MPU6050
    
    # MPU6050センサーとのI2C通信を初期化
    i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)
    mpu = MPU6050(i2c)
    
    # 2点間の距離を計算する関数
    def dist(a, b):
        return math.sqrt((a * a) + (b * b))
    
    # Y軸周りの回転を計算する関数
    def get_y_rotation(x, y, z):
        radians = math.atan2(x, dist(y, z))
        return -math.degrees(radians)
    
    # X軸周りの回転を計算する関数
    def get_x_rotation(x, y, z):
        radians = math.atan2(y, dist(x, z))
        return math.degrees(radians)
    
    # MPU6050センサーから現在の角度を取得する関数
    def get_angle():
        y_angle = get_y_rotation(mpu.accel.x, mpu.accel.y, mpu.accel.z)
        x_angle = get_x_rotation(mpu.accel.x, mpu.accel.y, mpu.accel.z)
        return x_angle, y_angle
    
    # LEDマトリックスを制御するためのシフトレジスタピンを初期化
    sdi = machine.Pin(18, machine.Pin.OUT)
    rclk = machine.Pin(19, machine.Pin.OUT)
    srclk = machine.Pin(20, machine.Pin.OUT)
    
    # シフトレジスタにデータを入力する関数
    def hc595_in(dat):
        for bit in range(7, -1, -1):
            srclk.low()
            time.sleep_us(30)
            sdi.value(1 & (dat >> bit))
            time.sleep_us(30)
            srclk.high()
    
    # シフトレジスタからLEDマトリックスへデータを出力する関数
    def hc595_out():
        rclk.high()
        time.sleep_us(200)
        rclk.low()
    
    # LEDマトリックス上にグリフ（8x8マトリックス）を表示する関数
    def display(glyph):
        for i in range(0, 8):
            hc595_in(glyph[i])
            hc595_in(0x80 >> i)
            hc595_out()
    
    # 2DマトリックスをLEDマトリックスに表示できるグリフに変換する関数
    def matrix_2_glyph(matrix):
        glyph = [0 for i in range(8)]
        for i in range(8):
            for j in range(8):
                glyph[i] += matrix[i][j] << j
        return glyph
    
    # 指定された最小値と最大値の間で値を制限する関数
    def clamp_number(val, min_val, max_val):
        return min_val if val < min_val else max_val if val > max_val else val
    
    # ある範囲から別の範囲へ値をマッピングする関数
    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    
    # MPU6050の読み取りに基づいてマトリックス内のバブルの位置を計算する関数
    sensitivity = 4  # バブルの動きの感度
    matrix_range = 7  # マトリックスのサイズは8x8なので範囲は0-7
    point_range = matrix_range - 1  # バブルの位置は0-6の間であるべきなので範囲を調整
    
    # センサーデータに基づいてバブルの位置を計算する関数
    def bubble_position():
        y, x = get_angle()  # 現在の回転角度を取得
        x = int(clamp_number(interval_mapping(x, 90, -90, 0 - sensitivity, point_range + sensitivity), 0, point_range))
        y = int(clamp_number(interval_mapping(y, -90, 90, point_range + sensitivity, 0 - sensitivity), 0, point_range))
        return [x, y]
    
    # マトリックスにバブル（2x2のLEDをオフにすることによって表現）を落とす関数
    def drop_bubble(matrix, bubble):
        matrix[bubble[0]][bubble[1]] = 0
        matrix[bubble[0] + 1][bubble[1]] = 0
        matrix[bubble[0]][bubble[1] + 1] = 0
        matrix[bubble[0] + 1][bubble[1] + 1] = 0
        return matrix
    
    # メインループ
    while True:
        matrix = [[1 for i in range(8)] for j in range(8)]  # 全てのLEDをオンにする空のマトリックスを作成
        bubble = bubble_position()  # センサーデータに基づいて現在のバブルの位置を取得
        matrix = drop_bubble(matrix, bubble)  # マトリックスにバブルを落とす
        display(matrix_2_glyph(matrix))  # LEDグリッド上にマトリックスを表示
        time.sleep(0.1)  # 更新を遅らせるために小さな遅延を追加

コードが実行されると、セットアップを平らな面に置いてください。
バブル（2x2ピクセルの領域）はLEDマトリックスの中心に表示されるはずです。
ブレッドボードまたはMPU6050モジュールを傾けてください。
LEDマトリックス上でバブルが傾斜の方向に動くのを観察し、実際の水準器をシミュレートします。

**コードの理解**

このコードはMPU6050加速度計およびジャイロスコープセンサーからのデータを読み取り、デバイスの傾斜を判定し、8x8 LEDマトリックス上に「バブル」を表示して、デジタル水準器をシミュレートします。

#. インポートと初期化:

   * ``machine``: マイクロコントローラーのハードウェアコンポーネントへのアクセス。
   * ``I2C`` , ``Pin``: I2C通信とGPIOピンの操作用。
   * ``time``: 遅延のためのタイミング機能。
   * ``math``: 計算用の数学関数。
   * ``MPU6050`` from ``imu``: MPU6050センサーとのインタフェース用ライブラリ。

#. I2Cの初期化:

   * バス1でSDAをピン6、SCLをピン7に設定してI2C通信を設定。
   * データ転送の速度を高めるために周波数を400kHzに設定。
   * MPU6050センサーとやり取りするための ``mpu`` オブジェクトを作成。

#. 数学関数:

   * ``dist(a, b)`` 関数:

     * 二つの値の間のユークリッド距離を計算。
     * 角度計算の大きさの成分を算出するために使用。

   * ``get_y_rotation(x, y, z)``:
     
     * Y軸周りの回転を度単位で計算。
     * xとyとzの距離のアークタンジェントを計算する ``math.atan2`` を使用。
     * 望ましい方向に合わせるために結果を符号反転。

   * ``get_x_rotation(x, y, z)``:

     * X軸周りの回転を度単位で計算。
     * ``get_y_rotation`` と似ていますが、yとxとzの距離のアークタンジェントを計算します。

   * ``get_angle()``:

     * MPU6050センサーから現在の加速度データを取得。
     * 加速度計データを使用してXおよびYの回転角を計算。

#. シフトレジスタ関数:

   * ピン定義:

     * ``sdi``: シフトレジスタのシリアルデータ入力ピン（ピン18）。
     * ``rclk``: シフトレジスタのレジスタクロック（ラッチ）ピン（ピン19）。
     * ``srclk``: シフトレジスタのシフトレジスタクロックピン（ピン20）。

   * ``hc595_in(dat)`` 関数:

     * 8ビットデータバイトをシフトレジスタにシフトします。
     * MSBからLSBまで各ビットを反復します。
     * ``srclk`` と ``sdi`` を制御してデータビットをクロックインします。

   * ``hc595_out()``:

     * シフトレジスタの出力ピンにシフトされたデータをラッチします。
     * データをシフトレジスタからストレージレジスタに転送するために ``rclk`` ピンを切り替えます。

#. LEDマトリックスディスプレイ関数:

   * ``display(glyph)`` 関数:

     * LEDマトリックス上に8x8のグリフを表示します。
     * グリフの各行を反復します。
     * 行データと対応する列セレクタをシフトします。
     * ``hc595_out()`` を呼び出してディスプレイを更新します。

   * ``matrix_2_glyph(matrix)`` 関数:

     * 0と1の8x8 2Dマトリックスを8バイトのグリフに変換します。
     * グリフ内の各バイトはLEDマトリックスの行を表します。
     * 各バイト内のビットはその行のLEDに対応します。

#. ユーティリティ関数:

   * ``clamp_number(val, min_val, max_val)`` 関数:

     * ``val`` が指定された ``min_val`` および ``max_val`` の範囲内に留まることを保証します。
     * バブルがLEDマトリックスの境界外に移動するのを防ぎます。

   * ``interval_mapping(x, in_min, in_max, out_min, out_max)`` 関数:

     * 数値 ``x`` を一つの数値範囲から別の範囲にマッピングします。
     * 角度測定をマトリックス位置に変換するために使用します。

#. バブル位置計算:

   * 感度設定:

     * ``sensitivity = 4``: バブルが傾斜の変化に反応する度合いを決定します。
     * ``matrix_range = 7``: 8x8マトリックスの最大インデックス（0から7）。
     * ``point_range = matrix_range - 1``: バブルが範囲内に留まるように調整された範囲（0から6）。

   * ``bubble_position()`` 関数:

     * 現在のXおよびYの回転角度を取得します。
     * 角度を ``interval_mapping`` を使用してLEDマトリックス上の位置にマッピングします。
     * 位置がマトリックス内に留まるように位置を制限します。

#. バブル表示関数:

   * ``drop_bubble(matrix, bubble)`` 関数:

     * LEDマトリックスを修正して、与えられた位置にバブルを表現します。
     * バブルの座標で中心に2x2ブロックのLEDをオフにします。
     * バブルが動く視覚効果を作り出すためにマトリックスを更新します。

#. メインループ

   * センサー入力に基づいてディスプレイを更新するために継続的に実行されます。
   * すべてのLEDがオンになっている新鮮な8x8マトリックスを初期化します（値 ``1`` ）。
   * ``bubble_position()`` から現在のバブル位置を取得します。
   * ``drop_bubble()`` を使用してバブルの新しい位置を反映するためにマトリックスを更新します。
   * ``matrix_2_glyph()`` を使用してマトリックスをグリフに変換します。
   * ``display()`` を使用してLEDマトリックスにグリフを表示します。
   * 更新率を制御するために0.1秒間待ちます。

**トラブルシューティング**

* LEDマトリックスが正しく表示されない：

  * シフトレジスタとLEDマトリックス間のすべての配線接続を確認します。
  * シフトレジスタがPicoに正しく接続されていることを確認します。
  * LEDマトリックスの共通アノードまたはカソードの設定がコードのロジックと一致しているか確認します。

* バブルの動きが正しくない：

  * MPU6050が正しく接続され、機能していることを確認します。
  * MPU6050が正しく向きを向けているか確認します。

* プログラムエラー：

  * ``imu.py`` および ``vector3d.py`` が正しくアップロードされていることを確認します。
  * コードのタイプミスやインデントのエラーをチェックします。

**さらなる実験**

* 感度の調整：

  角度を位置にマッピングすることでバブルの動きの感度を変更します。

* 表示の向上：

  * バブルのサイズや形を変更します。
  * トレイルや異なるパターンなどの視覚効果を追加します。

* キャリブレーション：

  デバイスを不均等な面に置いたときにゼロポイントを設定するためのキャリブレーションルーチンを実装します。

* 代替ディスプレイ：

  視覚的なバブルに加えて、数値の角度値を表示するためにOLEDまたはLCDディスプレイを使用します。

**結論**

あなたはRaspberry Pi Pico 2を使用してデジタル水準器を成功裏に構築しました！このプロジェクトは、加速度データを使用して方向と傾斜を視覚化する方法と、シフトレジスタを使用してLEDマトリックスディスプレイを制御する方法を示しています。

このプロジェクトをさらに拡張して新しい機能を追加するか、より大きなシステムに統合してください。
