# Installation Instructions

Have the following packages installed:

* Python including latest pip
* C++ Compiler
* CMake

## Installing Python dependencies

The instructions have been given for Anaconda; please alter as needed.

```
conda create -n pregis python=3.6.3 anaconda
conda activate pregis
# install pycuda for your platform as give in https://wiki.tiker.net/PyCuda/Installation
pip install scikit-cuda
```

## Installing NiftyReg

NiftyReg is already a sub-module in this repo and should be populated during the initial clone. If the folder is empty, update all submodules.

```bash
cd niftyreg
mkdir bin
cd bin
cmake -DCMAKE_INSTALL_PREFIX=./install -DCMAKE_BUILD_TYPE=Release ..
make install/strip -j2 # assumes you have 2 CPU threads for compilation
```

Edit the `config.json` file with the full path to `{pregis_source}/niftyreg/bin/install`

# Sample Data

https://github.com/uncbiag/pregis/releases/download/1.0.0/data.zip 