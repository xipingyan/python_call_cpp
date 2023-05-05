cmake_minimum_required(VERSION 3.10)

project(mylib)
set(CMAKE_CXX_STANDARD 17)
# set(PYBIND11_PYTHON_VERSION 3.8)
set(CMAKE_CXX_FLAGS "-Wall -Wextra -fPIC")

set(PYBIND11_INSTALL_DIR "${CMAKE_SOURCE_DIR}/python-env/lib/python3.8/site-packages/pybind11/share/cmake/pybind11/")
IF(NOT EXISTS ${PYBIND11_INSTALL_DIR})
    message(FATAL "PYBIND11_INSTALL_DIR: ${PYBIND11_INSTALL_DIR} does not exist")
ELSE()
    message(STATUS "PYBIND11_INSTALL_DIR: ${PYBIND11_INSTALL_DIR}")
    set(CMAKE_PREFIX_PATH "${PYBIND11_INSTALL_DIR};${CMAKE_PREFIX_PATH}")
    find_package(pybind11 REQUIRED)
ENDIF()

# # Create an extension module
# add_library(mylib MODULE main.cpp)
# 

# find_package(pybind11 REQUIRED)
# find_package(Eigen3 REQUIRED)

pybind11_add_module(${PROJECT_NAME} src/src_add.cpp)

target_compile_definitions(${PROJECT_NAME} PRIVATE VERSION_INFO=${EXAMPLE_VERSION_INFO})
target_include_directories(${PROJECT_NAME} PRIVATE ${PYBIND11_INCLUDE_DIRS})
# target_link_libraries(${PROJECT_NAME} PRIVATE Eigen3::Eigen)
# target_link_libraries(${PROJECT_NAME} PUBLIC pybind11::module)

# # Or embed the Python interpreter into an executable
# add_executable(myexe main.cpp)
# target_link_libraries(myexe PUBLIC pybind11::embed)
