# Tensorflow

## Requirements
* Python V3 
* PIP
* virtualenv

## Installation

### MacOS
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
export PATH="/usr/local/bin:/usr/local/sbin:$PATH"
brew update
brew install python  # Python 3
sudo pip3 install -U virtualenv  # system-wide install
```

### Windows
Install the Microsoft Visual C++ 2015 Redistributable Update 3. This comes with Visual Studio 2015 but can be installed separately:

1. Go to the [Visual Studio downloads](https://visualstudio.microsoft.com/vs/older-downloads/ "Visual Studio downloads"),
2. Select Redistributables and Build Tools,
3. Download and install the Microsoft Visual C++ 2015 Redistributable Update 3
4. Make sure long paths are enabled on Windows
  1. Hit the Windows key, type gpedit.msc and press Enter.
  2. Navigate to Local Computer Policy > Computer Configuration > Administrative Templates > System > Filesystem.
  3. Double click the Enable NTFS long paths option and enable it.
5. Install Python 3 for Windows, select pip as an optional feature during install.
6. open a command prompt and run: ```pip3 install -U pip virtualenv```

## Create a Virtual Environment

### MacOS
1. In terminal switch to your home directory:
```
cd ~
```
2. In terminal run
```
virtualenv --system-site-packages -p python3 ./venv
```
2. Activate the new virtual environment
```
source ./venv/bin/activate  # sh, bash, ksh, or zsh
```

_When virtualenv is active, your shell prompt is prefixed with (venv)_

### Windows
