import ollama

from python_functions.basic_functions import add_two_numbers
from python_functions.basic_functions import subtract_two_numbers

client_messages = [
    {
        'role': 'user', 
        'content': 'What is 221 + 2?'
    },
    {
        'role': 'user', 
        'content': 'What is 22 - 2?'
    } 
]

available_functions = {
  'add_two_numbers': add_two_numbers,
  'subtract_two_numbers': subtract_two_numbers,
}

response = ollama.chat(
    'llama3.1',
    messages=client_messages,
    tools=[
        add_two_numbers,
        subtract_two_numbers
    ]
)

for tool in response.message.tool_calls or []:
    function_to_call = available_functions.get(tool.function.name)
    if function_to_call:
        print('Function output:', function_to_call(**tool.function.arguments))
    else:
        print('Function not found:', tool.function.name)