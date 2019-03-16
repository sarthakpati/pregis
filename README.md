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

# Sample Data

https://github.com/uncbiag/pregis/releases/download/1.0.0/data.zip 