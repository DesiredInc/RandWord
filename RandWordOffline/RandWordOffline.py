import random
FILE = "words.txt"
def choose_word():
    i = int(input('How many words do you want?:'))
    with open(FILE) as f:
        words = f.readlines()
        for i in range(i):
            print(random.choice(words).strip())
choose_word()