# happy-lunch-rp
快乐午餐——树莓派

## bash used
1. install python2.7 and pip
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

2. install pipenv
```bash
sudo pip2 install pipenv
```

3. install dependence
```bash
# install all
sudo pipenv --two install
# install one
sudo pipenv --two install [package_name]
```

4. run it
```bash
pipenv --two run python main.py
```