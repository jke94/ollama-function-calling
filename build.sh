#!/bin/bash


# A. Create shared library output destination folder.

mkdir -p ./src/cpp/lib

# B. Create shared library.

g++ -shared -o ./src/cpp/lib/libmath_lib.so \
    -fPIC \
    -I./src/cpp/api \
    -I./src/cpp/include \
    ./src/cpp/src/NativeFunctionsApi.cpp
