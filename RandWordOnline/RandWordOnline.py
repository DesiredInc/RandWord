# import random
# FILE = "words.txt"
# def choose_word():
#     i = int(input('How many words do you want?:'))
#     with open(FILE) as f:
#         words = f.readlines()
#         for i in range(i):
#             print(random.choice(words).strip())
# choose_word()

from random import choice
import requests

URL = "https://www.mit.edu/~ecprice/wordlist.10000"

def collect_data():
    return list(map(lambda x: x.strip(), requests.get(URL).text.splitlines()))

def main():
    # Collecting data
    print("Collecting data... ", end='')
    data = collect_data()
    print("OK")

    # Prompt count
    count = int(input("How many words?: "))

    # Choice
    for _ in range(count):
        word = choice(data)
        print(word)

if __name__ == '__main__':
    main()