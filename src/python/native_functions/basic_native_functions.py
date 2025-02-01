import ctypes
import os
import json

# Cargar la librería C++ (ajusta el nombre según tu sistema)
if os.name == "nt":  # Windows
    lib = ctypes.CDLL("libmath_lib.dll")
else:  # Linux/macOS
    lib = ctypes.CDLL("./src/cpp/lib/libmath_lib.so")

# Definir los tipos de las funciones
lib.add_two_numbers.argtypes = [ctypes.c_int, ctypes.c_int]
lib.add_two_numbers.restype = ctypes.c_int

lib.calcular_media.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int]
lib.calcular_media.restype = ctypes.c_float

def add_two_numbers(a: int, b: int) -> int:
    """
    Add two numbers

    Args:
        a (int): The first integer number
        b (int): The second integer number

    Returns:
        int: The sum of the two numbers
    """

    return lib.add_two_numbers(a, b)

def calculate_average(numbers) -> float:
    """
    Calculate average of number integer list

    Args:
        numbers: List of integers numbers

    Returns:
        float: The average of number integers numbers list
    """

    if isinstance(numbers, str): # Example:  "[10, 20, 30]"
        
        list_of_numbers = [float(num) for num in json.loads(numbers)]

        # Define de array type and call to the function.
        array_type = ctypes.c_float * len(list_of_numbers) 
        return lib.calcular_media(array_type(*list_of_numbers), len(list_of_numbers))
    
    else:

        # Define de array type and call to the function.
        array_type = ctypes.c_float * len(numbers)
        return lib.calcular_media(array_type(*numbers), len(numbers))       
