import random

answers = [
    "It is certain", "It is decidedly so", "Without a doubt", 
    "Yes definitely", "You may rely on it", "As I see it yes", 
    "Most likely", "Outlook good", "Yes", "Signs point to yes", 
    "Reply hazy try again", "Ask again later", "Better not tell you now", 
    "Cannot predict now", "Concentrate and ask again", 
    "Don't count on it", "My reply is no", "My sources say no", 
    "Outlook not so good", "Very doubtful"
]

def get_answer(answers):
    return random.choice(answers)

print("Hello world, i am a magic ball and i know the answer to any of your questions!")
name = input("What is your name?: ")

while True:
    input(f"Your question, {name.title()}?: ")
    print(get_answer(answers))

    que = input(f"Do you have another question, {name.title()}?: ")

    w = ["yes", "ja", "да", "lf"]

    if que.lower() in w:
        continue
    else:
        break

print("Bye-bye")