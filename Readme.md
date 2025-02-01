# Ollama-functions-calling

Example about how to use function callings with Ollama. From a perspective to offer to the LLM a set of functions to carry out the operations acording with the user message.

The most important topic here 🚀, it´s an example to **consume C++ native** functions from an LLM model and python functions with the help of Ollama.

## How to run

This example has been developed over a WSL (Windows Subsystem for Linux), python and python virtual environment:

- WSL information:

```
(venv) javi@DESKTOP:/mnt/j/Repositories/ollama-function-calling$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 22.04.5 LTS
Release:        22.04
Codename:       jammy
(venv) javi@DESKTOP:/mnt/j/Repositories/ollama-function-calling$
```
- Python version:

```
(venv) javi@DESKTOP:/mnt/j/Repositories/ollama-function-calling$ python3 --version
Python 3.10.12
(venv) javi@DESKTOP:/mnt/j/Repositories/ollama-function-calling$

```
- Python **pip** version:

```
(venv) javi@DESKTOP:/mnt/j/Repositories/ollama-function-calling$ pip3 --version
pip 22.0.2 from /mnt/j/Repositories/ollama-function-calling/venv/lib/python3.10/site-packages/pip (python 3.10)
(venv) javi@DESKTOP:/mnt/j/Repositories/ollama-function-calling$
```
- Ollama version:

```
PS J:\Repositories\ollama-function-calling> ollama --version
ollama version is 0.5.1
PS J:\Repositories\ollama-function-calling>
```


### Ubuntu.

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
4. Build C++ native shared library

```
./build.sh
```

5. Run example!

```
python3 ./src/python/main.py 
```

## Input vs output:

- Input:

```
    client_messages = [
        {
            'role': 'user', 
            'content': 'What is the sum of 620 + 20?'
        },
        {
            'role': 'user', 
            'content': 'What is the average of the following numbers: 10, 20, 20.8 and 30?'
        },
        {
            'role': 'user', 
            'content': 'What is the average of the following numbers: 100.50, 99.50, 99.40 and 100.60?'
        },        
        {
            'role': 'user', 
            'content': 'What is 22 - 2?'
        },
        {
            'role': 'user', 
            'content': 'What is the conjugate angle of 270º?'
        },
        {
            'role': 'user', 
            'content': 'What is the conjugate angle of 350º?'
        }                    
    ]
```

- Output:

```
Calling function: add_two_numbers
Arguments: {'a': 620, 'b': 20}
Function output: 640

Calling function: calculate_average
Arguments: {'numbers': '[10, 20, 20.8, 30]'}
Function output: 20.200000762939453

Calling function: calculate_average
Arguments: {'numbers': '[100.50, 99.50, 99.40, 100.60]'}
Function output: 100.0

Calling function: subtract_two_numbers
Arguments: {'a': 22, 'b': 2}
Function output: 20

Calling function: calculate_conjugate_angle
Arguments: {'angle': 270}
Function output: 90

Calling function: calculate_conjugate_angle
Arguments: {'angle': 350}
Function output: 10
```

## Useful information

- [Ollama Python library 0.4 with function calling improvements](https://ollama.com/blog/functions-as-tools)
- [Medium: Ollama Tool Calling](https://medium.com/@danushidk507/ollama-tool-calling-8e399b2a17a8)