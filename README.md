# happy-lunch-rp

[妈妈再也不用担心我吃不上午饭了](http://lunch.xiaodabao.xyz/)

## Project setup

### install python3, pip and opencv
```bash
# update raspberry pi
sudo rpi-update
# refreshing the repositories
sudo apt-get update
# its wise to keep the system up to date!
# you can skip the following line if you not
# want to update all your software
sudo apt-get upgrade
# installing python3, pip and opencv for it
# see https://www.pyimagesearch.com/2017/09/04/raspbian-stretch-install-opencv-3-python-on-your-raspberry-pi/
```

### install dependence
```bash
pip install requests
pip install schedule
```

### check if usb webcam connected
```bash
ls -ltrh /dev/video*
```

### run it
```bash
source ~/.profile
workon cv
python main.py
```
