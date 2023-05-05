# python_call_cpp
Example of python call cpp. <br>
CMake project name should keep same to export module name. <br>

# How to build

```
git clone https://github.com/xipingyan/python_call_cpp.git
cd python_call_cpp
python -m venv python-env
source python-env/bin/activate
pip install update --upgrade pip

mkdir build
cd build
cmake ..
make -j8

cd ../test_python
python test.py
```
