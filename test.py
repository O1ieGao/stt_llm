# from ollama import chat
# from ollama import ChatResponse

# response: ChatResponse = chat(model='llama3.2', messages=[
#   {
#     'role': 'user',
#     'content': 'Who are you',
#   },
# ])
# print(response['message']['content'])
# # or access fields directly from the response object
# print(response.message.content)

#TODO: Test on lower-level CPU/GPU laptop

from ollama import chat


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

while True:
    user_input = input('Chat with history: ')
    response = chat(
        'llama3.2',
    messages=messages+ [
            {'role': 'user', 'content': user_input},
        ]
    )

    # Add the response to the messages to maintain the history
    messages += [
        {'role': 'user', 'content': user_input},
        {'role': 'assistant', 'content': response.message.content},
    ]
    print(response.message.content + '\n')

'''
Input: go forward 100 centimeters
Input: go backward 100 centimeters
Input: turn left 50 degrees
Input: turn right 50 degrees
'''

# from ollama import ps, pull, chat
# from ollama import ProcessResponse

# # Ensure at least one model is loaded
# response = pull('llama3.2', stream=True)
# progress_states = set()
# for progress in response:
#   if progress.get('status') in progress_states:
#     continue
#   progress_states.add(progress.get('status'))
#   print(progress.get('status'))

# print('\n')

# print('Waiting for model to load... \n')
# chat(model='llama3.2', messages=[{'role': 'user', 'content': 'Why is the sky blue?'}])


# response: ProcessResponse = ps()
# for model in response.models:
#   print('Model: ', model.model)
#   print('  Digest: ', model.digest)
#   print('  Expires at: ', model.expires_at)
#   print('  Size: ', model.size)
#   print('  Size vram: ', model.size_vram)
#   print('  Details: ', model.details)
#   print('\n')