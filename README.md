# Terasploit
![Framework Version](https://img.shields.io/badge/Framework_1.3.1--dev-blue) ![OS Compatibility](https://img.shields.io/badge/OS-Linux-red) ![Python Version](https://img.shields.io/badge/Python-3.11.9-green)

### Update `v1.3.1-dev`:
- [Update History](https://github.com/rupture6/terasploit-framework/blob/master/UPDATES.md)

### Available CVE Modules:
- CVE-2024-40110
- CVE-2021-36548
- CVE-2024-36598

### Tested on:
- [Kali Linux](https://www.kali.org/)
- [ParrotSec OS](https://parrotsec.org/)
- [Ubuntu](https://ubuntu.com/)
- [Debian](https://www.debian.org/)

## System Installation
```
wget https://raw.githubusercontent.com/rupture6/terasploit-framework/master/.install/tsfinstall
bash tsfinstall && rm tsfinstall
```

## Simple Installation
```
sudo apt update && sudo apt upgrade
sudo apt install wget curl git python3 python3-pip
git clone https://github.com/rupture6/terasploit-framework.git
find terasploit-framework -type f -exec chmod +x {} \;
cd terasploit-framework
./terasploit
```

## Requirements Installation
```
wget https://raw.githubusercontent.com/rupture6/terasploit-framework/master/.requirements/requirements.txt
pip3 install -r requirements.txt && rm requirements.txt
```

## License
- Terasploit Framework is released under [BSD 3-Clause License](https://github.com/rupture6/terasploit-framework/blob/master/LICENSE).

## Contribution 
- [Pull](https://github.com/rupture6/terasploit-framework/pulls) a request on this repository.
