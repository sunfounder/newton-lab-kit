.. note:: 

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者と一緒にさらに深く学びましょう。

    **参加する理由**

    - **専門家のサポート**: 購入後の問題や技術的な課題をコミュニティとチームのサポートで解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換して、スキルを向上させましょう。
    - **独占プレビュー**: 新製品の発表や先行情報をいち早く入手できます。
    - **特別割引**: 最新製品に対する独占割引を楽しめます。
    - **祝祭プロモーションとギブアウェイ**: ギブアウェイや季節限定のプロモーションに参加できます。

    👉 一緒に探求し、創造しませんか？今すぐ [|link_sf_facebook|] をクリックして参加しましょう！

.. _py_mpu6050:

6.3 MPU-6050からのデータ読み取り
===================================

このレッスンでは、 **MPU-6050** 6軸モーションセンサーをRaspberry Pi Pico 2に接続する方法を学びます。MPU-6050は、3軸ジャイロスコープと3軸加速度計を組み合わせたセンサーで、I2C通信プロトコルを介して生データを提供します。

**必要なもの**

このプロジェクトには、以下のコンポーネントが必要です。

セットで購入するのが便利です。リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名称	
        - セット内容
        - リンク
    *   - Newton Lab Kit	
        - 450+
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
        - :ref:`cpn_mpu6050`
        - 1
        - 

**MPU-6050センサーの理解**

**MPU-6050**センサーは、モーション追跡や方向検出を必要とするプロジェクト、例えばドローン、ロボティクス、ゲームデバイスなどで広く使用されています。

* **加速度計**: X、Y、Z軸に沿った加速度を測定します。これには重力加速度も含まれており、センサーの傾きや方向を確認できます。
* **ジャイロスコープ**: X、Y、Z軸周りの回転速度を測定し、センサーがどれだけ速く回転しているかの情報を提供します。

**回路図**

|sch_mpu6050_ar|

**配線図**

|wiring_mpu6050_ar|

**コードの記述**

MPU-6050センサーから加速度計とジャイロスコープのデータを読み取るMicroPythonスクリプトを書いてみましょう。

.. note::

    * ``6.3_6axis_motion_tracking.py`` を ``newton-lab-kit/micropython`` から開くか、コードをThonnyにコピーして「実行」ボタンをクリックするか、F5キーを押して実行します。
    * 正しいインタープリタ（MicroPython (Raspberry Pi Pico).COMxx）が選択されていることを確認してください。 
     
    * ここでは ``imu.py`` と ``vector3d.py`` を使用します。Picoにアップロードされているか確認し、詳細なチュートリアルについては :ref:`add_libraries_py` をご参照ください。

.. code-block:: python

   from machine import I2C, Pin
   import utime
   from imu import MPU6050

   # I2Cインターフェースの初期化（SDAはGP4、SCLはGP5）
   i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)

   # MPU-6050センサーの初期化
   mpu = MPU6050(i2c)

   def read_accelerometer():
      """Reads accelerometer data and returns it as a tuple (x, y, z)."""
      accel = mpu.accel
      return accel.x, accel.y, accel.z

   def read_gyroscope():
      """Reads gyroscope data and returns it as a tuple (x, y, z)."""
      gyro = mpu.gyro
      return gyro.x, gyro.y, gyro.z

   def main():
      """Main loop to read and print sensor data."""
      while True:
         # 加速度計データの読み取り
         ax, ay, az = read_accelerometer()
         print("Accelerometer (g) - X: {:.3f}, Y: {:.3f}, Z: {:.3f}".format(ax, ay, az))
         
         # 視認性のために一時停止
         utime.sleep(0.5)
         
         # ジャイロスコープデータの読み取り
         gx, gy, gz = read_gyroscope()
         print("Gyroscope (°/s) - X: {:.3f}, Y: {:.3f}, Z: {:.3f}".format(gx, gy, gz))
         
         # 次のデータセットの前に一時停止
         utime.sleep(0.5)

   # メイン関数の実行
   if __name__ == "__main__":
      main()


このスクリプトは、加速度計とジャイロスコープの読み取りを0.5秒ごとに交互に表示します。

* 加速度計の出力:

  .. code-block::

     Accelerometer (g) - X: 0.000, Y: 0.000, Z: 1.000

  静止している場合、X軸とY軸の値は0 g近く、Z軸は重力の影響で約1 gになります。

* ジャイロスコープの出力:

  .. code-block::

     Gyroscope (°/s) - X: 0.000, Y: 0.000, Z: 0.000

  静止している場合、ジャイロスコープの値はすべての軸で0 °/s近くになります。
  センサーを回転させると、これらの値が変化し、角速度を反映します。

**コードの理解**


#. インポートとセットアップ:

   * ``machine.I2C と machine.Pin``: ハードウェアインターフェース用
   * ``utime``: 時間関連の関数
   * ``MPU6050``: imu.pyライブラリからのセンサークラス

#. I2Cの初期化:

   GP4（SDA）とGP5（SCL）を使用してI2Cバス0をセットアップし、通信速度を400kHzに設定します。

   .. code-block:: python

      i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)


#. センサーの初期化:

   I2Cインターフェースを使用してMPU-6050センサーのインスタンスを作成します。

   .. code-block:: python

      mpu = MPU6050(i2c)

#. 加速度計データの読み取り:

   加速度計のデータを取得し、X、Y、Zの値を返します。

   .. code-block:: python

      def read_accelerometer():
         accel = mpu.accel
         return accel.x, accel.y, accel.z


#. ジャイロスコープデータの読み取り:

   ジャイロスコープのデータを取得し、X、Y、Zの値を返します。

   .. code-block:: python

      def read_gyroscope():
         gyro = mpu.gyro
         return gyro.x, gyro.y, gyro.z


#. メインループ:

   * 加速度計データを読み取り、表示します。
   * 0.5秒待機します。
   * ジャイロスコープデータを読み取り、表示します。
   * さらに0.5秒待機してから繰り返します。

   .. code-block:: python

      def main():
         while True:
            # 加速度計データを読み取って表示
            ax, ay, az = read_accelerometer()
            print("Accelerometer (g) - X: {:.3f}, Y: {:.3f}, Z: {:.3f}".format(ax, ay, az))
            
            utime.sleep(0.5)
            
            # ジャイロスコープデータを読み取って表示
            gx, gy, gz = read_gyroscope()
            print("Gyroscope (°/s) - X: {:.3f}, Y: {:.3f}, Z: {:.3f}".format(gx, gy, gz))
            
            utime.sleep(0.5)


#. プログラムのエントリーポイント:



   スクリプトが直接実行されるときに ``main()`` が呼び出されることを保証します。

   .. code-block:: python

      if __name__ == "__main__":
         main()

**さらなる実験**


* **センサーの1つに集中**: 加速度計かジャイロスコープのデータのみに集中するには、もう一方のセンサーに関連するprint文をコメントアウトします。
* **データの視覚化**: リアルタイムでセンサーデータをプロットするツールやソフトウェアを使用して、データを視覚化しましょう。
* **方向の計算**: 加速度計データを使ってピッチやロールを計算するアルゴリズムを実装しましょう。
* **モーション検出**: 特定の動きの閾値を超えたときにアクションを実行するプログラムを作成します。

**センサーデータの理解**

* 加速度計:

  * 加速度（g単位）を測定します。
  * 傾き、方向、直線運動の検出に役立ちます。

* ジャイロスコープ:

  * 回転速度（°/s単位）を測定します。
  * 回転や角運動の検出に役立ちます。

**トラブルシューティングのヒント**

* 出力がない、またはエラーが発生した場合:

  * 配線接続、特にSDAおよびSCLラインを確認してください。
  * センサーが正しく電源が供給されているか確認してください。

* 静的な読み取り:

  * センサーを動かしても読み取った値が変化しない場合は、接続が緩んでいないか確認してください。
  * 正しいI2Cアドレスが使用されているか確認してください。

* 一貫性のないデータ:

  * 環境の振動がセンサーデータに影響を与える場合があります。
  * センサーを安定した表面に置いてテストしてください。

**結論**

このレッスンでは、MPU-6050加速度計およびジャイロスコープセンサーをRaspberry Pi Pico 2に接続する方法を学びました。生のセンサーデータを読み取ることで、モーション検出、方向追跡など、多くの応用を探索できます。
