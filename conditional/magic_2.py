#Magic ball 2
import random

messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

question=  input('What do you want to know about the future?')
print(messages[random.randint(0, len(messages) - 1)])
