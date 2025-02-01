import ollama

from native_functions.basic_native_functions import add_two_numbers
from native_functions.basic_native_functions import calculate_average

from python_functions.basic_functions import calculate_conjugate_angle
from python_functions.basic_functions import subtract_two_numbers

# Dictionary with the available functions
available_functions = {
    "add_two_numbers": add_two_numbers,
    "calculate_average": calculate_average,
    "calculate_conjugate_angle": calculate_conjugate_angle,
    "subtract_two_numbers": subtract_two_numbers
}

def main(llm_request_messages:dict):

    response = ollama.chat(
        'llama3.1',
        messages=llm_request_messages,
        tools=[
            add_two_numbers,
            calculate_average,
            calculate_conjugate_angle,
            subtract_two_numbers
        ]
    )

    for tool in response.message.tool_calls or []:
        
        if function_to_call := available_functions.get(tool.function.name):
            print('Calling function:', tool.function.name)
            print('Arguments:', tool.function.arguments)

            print('Function output:', function_to_call(**tool.function.arguments))
        else:
            print('Function', tool.function.name, 'not found')
        
        print()

if __name__ == "__main__":

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

    main(llm_request_messages=client_messages)