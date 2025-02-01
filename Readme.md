# Ollama-functions-calling

Example about how to use functions callings with Ollama

- Ollama function calling example: https://ollama.com/blog/functions-as-tools

The goal is call to C++ API.

## How to run

```
python .\src\main.py
```

## Compile native code (C++) as shared library.

g++ -shared -o api.so -fPIC api.cpp