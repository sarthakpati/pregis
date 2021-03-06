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
pip install scikit-cuda simpleitk
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

Edit the `config.json` file with the full path to `${pregis_source}/niftyreg/bin/install`

# Sample Data

```bash
cd ${pregis_source}
wget https://github.com/uncbiag/pregis/releases/download/1.0.0/data.zip 
unzip data.zip
rm -rf data.zip
```

# Usage

The main entry point of the code is `${pregis_source}/main_code/pregis.py`.

The CPU/GPU toggle is handled by the command line parameter **-p**.

User needs to use the -a for the post-resection image

# To Do

* Change temporary writing directory from `${pregis_source}/tmp_res/` to a temporary directory in the user's home directory.
* NiftyReg installation location should not be getting picked up from a config file; instead, it should be getting picked up directly from the environment variables. This ensures a seamless interface for the user.
* C++ Conversion
  * [Xu] Provide pseudo-code to Sarthak
  * [Sarthak] After Xu provides pseudo-code, check which decompositions are available on the GPU via OpenCV
