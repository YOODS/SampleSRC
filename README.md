# SampleSRC

�{ Repository �́ARoVI �̋@�\���g�p����T���v���v���O�����ł��B

## �@�\

RoVI ����z�M�����摜���摜�������܂��B
- ���C�u���̎B�e�摜�̓�l��
- �P�O�b�Ԋu�łR�c�_�Q�B�e�A�B�e���ʂ̂R�c�_�Q�f�[�^�̃m�C�Y����

## �K�v�v��

RoVI �ɏ���

## �C���X�g�[��

���O�ɁAROS�ARoVI�̊����\�z���Ă��������B
�ihttps://github.com/YOODS/rovi ���Q�Ɓj

RoVI �̃\�[�X�f�B���N�g���ɁA�{ Repository �̃\�[�X�� checkout ���܂��B
~~~
cd ~/catkin_ws/src/rovi
git clone https://github.com/YOODS/SampleSRC.git
~~~

## �g����

1. RoVI �̋N��

- �J�����𑜓x SXGA ���g�p����ꍇ
~~~
roslaunch rovi ycam3sxga.launch
~~~
- �J�����𑜓x VGA ���g�p����ꍇ
~~~
roslaunch rovi ycam3vga.launch
~~~

2. Rviz �̋N��

~~~
roslaunch rovi viewer.launch
~~~

3. ��l��

~~~
roslaunch rovi rovi_bin.launch
~~~

Rviz ��ɁA���J�����̂R�̉摜��\�����܂��B
- Image(left_raw) �FRAW �摜
- Image(left_rect)�F���N�e�B�t�@�C�摜
- Image(left_bin) �F��l���摜

4. �m�C�Y����

~~~
roslaunch rovi rovi_capture.launch
~~~
Rviz �� 3DView ��ʂɕ\�����Ă��܂��B
- PointCloud(left_raw) �F �R�c�_�Q�B�e���ʁi���F�j
- PointCloud(left_test)�F�m�C�Y���������R�c�_�Q�f�[�^�i���F�j

