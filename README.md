# VideoWallWithRaspberryPi


## Installations
### Firstly install OpenCV

```
pi@raspberrypi:~ $ sudo apt-get install build-essential cmake pkg-config
pi@raspberrypi:~ $ sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
pi@raspberrypi:~ $ sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
pi@raspberrypi:~ $ sudo apt-get install libxvidcore-dev libx264-dev
pi@raspberrypi:~ $ sudo apt-get install libgtk2.0-dev
pi@raspberrypi:~ $ sudo apt-get install libatlas-base-dev gfortran
pi@raspberrypi:~ $ cd ~
pi@raspberrypi:~ $ wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.4.0.zip                        
pi@raspberrypi:~ $ unzip opencv.zip
pi@raspberrypi:~ $ wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.4.0.zip
unzip opencv_contrib.zip
pi@raspberrypi:~ $ sudo pip install numpy
pi@raspberrypi:~ $ cd opencv-3.4.0
pi@raspberrypi:~/opencv-3.4.0 $ mkdir build
pi@raspberrypi:~/opencv-3.4.0 $ cd build/
pi@raspberrypi:~/opencv-3.4.0/build $ cmake -D CMAKE_BUILD_TYPE=RELEASE \
> -D CMAKE_INSTALL_PREFIX=/usr/local \
> -D INSTALL_PYTHON_EXAMPLES=ON \
> -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.4.0/modules/ \
> -D BUILD_EXAMPLES=ON ..
pi@raspberrypi:~/opencv-3.4.0/build $ make -j4
pi@raspberrypi:~/opencv-3.4.0/build $ sudo make install
pi@raspberrypi:~/opencv-3.4.0/build $ sudo ldconfig
```

### And then install mss library

```
pi@raspberrypi:~ $python -m pip install -U --user mss
```
