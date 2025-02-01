# Ollama-functions-calling

Example about how to use functions callings with Ollama

- Ollama function calling example: https://ollama.com/blog/functions-as-tools

The goal is call to C++ API.

## How to run


### Ubuntu.

This example has been developed over a WSL (Windows Subsystem for Linux).

1. Create python virtual environment.

```
python3 -m venv venv
```

2. Activate python virtual environment.

```
. ./venv/bin/activate
```
3. Install **requirements.txt** packages.

```
pip3 install -r ./requirements.txt
```
4. Run example!

```
python3 ./src/python/main.py 
```

## Compile native code (C++) as shared library.

g++ -shared -o api.so -fPIC api.cpp