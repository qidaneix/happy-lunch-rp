# happy-lunch-rp

[妈妈再也不用担心我吃不上午饭了](http://lunch.xiaodabao.xyz/)

## Project setup

### install python2.7 and pip
```bash
# refreshing the repositories
sudo apt update
# its wise to keep the system up to date!
# you can skip the following line if you not
# want to update all your software
sudo apt upgrade
# installing python 2.7 and pip for it
sudo apt install python2.7 python-pip
```

### install pipenv
```bash
sudo pip2 install pipenv
```

### install dependence
```bash
# install all packages
sudo pipenv install --two
# install all dev-packages
sudo pipenv install --two --dev
# install one package
sudo pipenv install [package_name] --two
```

### check if usb webcam connected
```bash
ls -ltrh /dev/video*
```

### run it
```bash
sudo pipenv --two run python main.py
```