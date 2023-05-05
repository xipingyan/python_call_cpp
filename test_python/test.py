import sys
sys.path.append("../build/")
sys.path.append("/home/xiping/mygithub/python_call_cpp/python-env/lib/python3.8/site-packages/")

# import importlib
# importlib.reload(mylib)

from mylib import add



print(add(1, 2))