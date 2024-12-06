from ollama import chat
from vosk_audio import Vosk

# audio format: PCM 16khz 16bit mono
vosk = Vosk(audio_path='')
results = vosk.parse()
user_input = ''
for result in results:
    user_input += f' {result} '

messages = [
    {
        'role': 'user',
        'content': 'Your task is to parse the input to extract the direction and distance/angle,and convert it into the specific output format: [f/b/l/r, number].\
            f=forward, b=backward, l=left, r=right. The number is in centimeters for forward or backward and in degrees for left or right. Your output must strictly \
            follow this format and contain no extra text or explanation. This is not a code generation task.\
            Example Inputs and outputs: \
            1. Input: "go forward 50 centimeters" -> Output: [f,50].\
            2. Input: "turn right 20 degrees" -> Output: [r,20].\
            3. Input: "go backward 50 centimeters" -> Output: [b,50].\
            4. Input: "turn left 20 degrees" -> Output: [l,20].\
            Do you understand?',
    },
    {
        'role': 'user',
        'content': 'Generate answer 3 times and pick the one you think is correct. Do you understand?'
    }
]

response = chat(
        'llama3.2',
        messages=messages+ [
                {'role': 'user', 'content': user_input},
        ]
    )
print(response.message.content)

# while True:
#     user_input = input('Chat with history: ')
#     response = chat(
#         'llama3.2',
#         messages=messages+ [
#                 {'role': 'user', 'content': user_input},
#         ]
#     )

#     # Add the response to the messages to maintain the history
#     messages += [
#         {'role': 'user', 'content': user_input},
#         {'role': 'assistant', 'content': response.message.content},
#     ]
#     print(response.message.content + '\n')

'''
Input: go forward 100 centimeters
Input: go backward 100 centimeters
Input: turn left 50 degrees
Input: turn right 50 degrees
'''