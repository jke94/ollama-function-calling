import ctypes
import os
import json


class NativeEngine:
    """Wrapper class for the C++ Math Library using ctypes."""

    def __init__(self):
        """Loads the shared library based on the operating system."""
        if os.name == "nt":  # Windows
            self._lib = ctypes.CDLL("libmath_lib.dll")
        else:  # Linux/macOS
            self._lib = ctypes.CDLL("./src/cpp/lib/libmath_lib.so")

        # Define function signatures
        self._lib.add_two_numbers.argtypes = [ctypes.c_int, ctypes.c_int]
        self._lib.add_two_numbers.restype = ctypes.c_int

        self._lib.calculate_average.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int]
        self._lib.calculate_average.restype = ctypes.c_float

    def add_two_numbers(self, a: int, b: int) -> int:
        """Adds two numbers and returns the result."""
        return self._lib.add_two_numbers(a, b)

    def calculate_average(self, numbers) -> float:
        """Calculates the average of a list of numbers."""
        if isinstance(numbers, str):  # Example: '[10, 20, 30]'
            numbers = [float(num) for num in json.loads(numbers)]

        if not isinstance(numbers, list) or not all(isinstance(n, (int, float)) for n in numbers):
            raise ValueError("Input must be a list of numbers.")

        array_type = ctypes.c_float * len(numbers)  # Define array type
        return self._lib.calculate_average(array_type(*numbers), len(numbers))