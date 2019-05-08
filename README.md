# Tensorflow

## Requirements
* Python V3 
* pip
* virtualenv

## Installation
There are 3 options:

* Docker container images: https://hub.docker.com/r/tensorflow/tensorflow/  (optional)
* run Tensorflow in Google's Colaboratory: https://colab.research.google.com/notebooks/welcome.ipynb
* Install locally using pip: https://www.tensorflow.org/install/pip

### MacOS
1. install homebrew if you don't already have it installed:
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
2. setup your path:
```
export PATH="/usr/local/bin:/usr/local/sbin:$PATH"
```

3. update homebrew:
```
brew update
```

4. install python 3
```
brew install python
```

5. install virtualenv:
```
sudo pip3 install -U virtualenv
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
2. Enter and Run
```
virtualenv --system-site-packages -p python3 ./venv
```
3. Activate the new virtual environment
```
source ./venv/bin/activate  # sh, bash, ksh, or zsh
```

_When virtualenv is active, your shell prompt is prefixed with (venv)_

### Windows
1. At a command prompt, switch to your home directory. If you're at ```C:\```, then type
``` cd Users\<username>```
2. Enter and Run
```
virtualenv --system-site-packages -p python3 ./venv
```
3. Activate the new virtual environment
```
.\venv\Scripts\activate
```

## Update Virtual Environment:

### MacOS
1. In terminal:
```
pip install --upgrade pip
```

2. Run ```pip list``` to ensure everything is working correctly


### Windows
1. At a command prompt: 
```
pip install --upgrade pip
```
2. Run ```pip list``` to ensure everything is working correctly

## Install the TensorFlow pip CPU package
1. Install the package
```
pip install --upgrade tensorflow
```
2. Verify the install
```
python -c "import tensorflow as tf; tf.enable_eager_execution(); print(tf.reduce_sum(tf.random_normal([1000, 1000])))"
```

## Exiting the Virtual Environment

### MacOS
1. In terminal: ```deactivate```

### Windows
2. At a command prompt: ```deactivate```
