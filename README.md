# SampleSRC

本 Repository は、RoVI の機能を使用するサンプルプログラムです。

## 機能

RoVI から配信される画像を画像処理します。
- ライブ中の撮影画像の二値化
- １０秒間隔で３Ｄ点群撮影、撮影結果の３Ｄ点群データのノイズ除去

## 必要要件

RoVI に準拠

## インストール

事前に、ROS、RoVIの環境を構築してください。
（https://github.com/YOODS/rovi を参照）

RoVI のソースディレクトリに、本 Repository のソースを checkout します。
~~~
cd ~/catkin_ws/src/rovi
git clone https://github.com/YOODS/SampleSRC.git
~~~

## 使い方

1. RoVI の起動

- カメラ解像度 SXGA を使用する場合
~~~
roslaunch rovi ycam3sxga.launch
~~~
- カメラ解像度 VGA を使用する場合
~~~
roslaunch rovi ycam3vga.launch
~~~

2. Rviz の起動

~~~
roslaunch rovi viewer.launch
~~~

3. 二値化

~~~
roslaunch rovi rovi_bin.launch
~~~

Rviz 上に、左カメラの３つの画像を表示します。
- Image(left_raw) ：RAW 画像
- Image(left_rect)：レクティファイ画像
- Image(left_bin) ：二値化画像

4. ノイズ除去

~~~
roslaunch rovi rovi_capture.launch
~~~
Rviz の 3DView 画面に表示しています。
- PointCloud(left_raw) ： ３Ｄ点群撮影結果（白色）
- PointCloud(left_test)：ノイズ除去した３Ｄ点群データ（水色）

