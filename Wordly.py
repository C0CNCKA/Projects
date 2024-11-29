import requests
import sys

def getword(l):
    word = requests.get(f"https://random-word-api.herokuapp.com/word?length={l}")
    if word.status_code == 200:
        print(str(word.json())[2:][:l]) #<- загаданное слово
        return str(word.json())[2:][:l]
        
    else:
        return word.status_code
def getword_ru(l):
    word = open('russian_nouns.txt', 'r')
    return word

def game():
    l = int(input('Word length: '))
    word = getword(l)
    if word.isdigit():
        return word
    att = 0
    while att < 5:
        guess = input()[:l]
        att += 1
        if len(guess) == l and guess != word:
            for i in range(0, l):
                if guess[i] == word[i]:
                    print(f'\033[38;5;120m{guess[i]}\033[0m', end='')
                elif guess[i] in word:
                    print(f'\033[38;5;185m{guess[i]}\033[0m', end='')
                else:
                    print(f'\033[38;5;8n{guess[i]}\033[0m', end='')
            print('\033[0m')
        elif len(guess) == l and guess == word:
            return 0
        else:
            print('Incorrect word length.')
            att -= 1
    return 1

streak = 0
while(True):
    e = game()
    #print(e)
    if e == 0:
        print('\033[38;5;120mYou win!\033[0m')
        if streak > 0:
            print(f'\033[38;5;54mYour winstreak: {streak + 1}\033[0m')
        streak +=1
    elif e == 1:
        print('\033[38;5;124mYou lose.\033[0m')
        if streak > 1:
            print(f'\033[38;5;54mYou lost your winstreak :C\033[0m')
        streak = 0
    else:
        print(f'Can\'t get word. ({e})')
