from native_functions.native_engine import NativeEngine

native_engine_instance = NativeEngine()

def add_two_numbers(a: int, b: int) -> int:
    """
    Add two numbers

    Args:
        a (int): The first integer number
        b (int): The second integer number

    Returns:
        int: The sum of the two numbers
    """

    return native_engine_instance.add_two_numbers(a, b)

def calculate_average(numbers) -> float:
    """
    Calculate average of number integer list

    Args:
        numbers: List of integers numbers

    Returns:
        float: The average of number integers numbers list
    """

    return native_engine_instance.calculate_average(numbers=numbers)   
