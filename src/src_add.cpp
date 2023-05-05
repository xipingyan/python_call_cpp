
#include <pybind11/pybind11.h>

namespace py = pybind11;

int add(int i, int j) {
    return i + j;
}

int minus(int i, int j) {
    return i - j;
}

PYBIND11_MODULE(mylib, m) {
    m.doc() = "pybind11 example plugin"; // optional module docstring

    // Param 1: python side name of the function
    m.def("add", &add, "A function that adds two numbers");
    m.def("minus", &minus, "A function that minus two numbers");
}