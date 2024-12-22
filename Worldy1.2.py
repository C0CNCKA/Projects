import requests

def getword(l):
    word = requests.get(f"https://random-word-api.herokuapp.com/word?length={l}")
    if word.status_code == 200:
        #print(str(word.json())[2:][:l]) #<- загаданное слово
        word = str(word.json())[2:][:l]
        #return to_dict(word) #Возврат слова списком
        return word #Возврат слова строкой

def to_dict(w):
    a = []
    for i in range(len(w)):
        a.append({w[i]:None})
    return a

def settings():
    global c
    global length
    print('\033[FSettings:            ')

    while True:
        print(f'Enter new word length:   \033[38;5;8m({length})\033[0m', end='\b\b\b\b\b')
        try:
            length = int(input())   
        except ValueError:
            print('Wrong input.')
            continue
        break

    while True:
        print(f'Enter new attempts count:   \033[38;5;8m({c})\033[0m', end='\b\b\b\b\b')
        try:
            c = int(input())
        except ValueError:
            print('Wrong input.')
            continue
        break
    print('Game starts.')       

def game(length, c):
    att = 0
    #word = [{'c':None}, {'h':None}, {'e':None}, {'e':None}, {'s':None}, {'e':None}] #getword(len)
    global word
    word = getword(length) #'cheese'
    #print(word) #Вывод загаданного слова
    
    while att < c:
        count = {}
        guess = input()[:length]
        guessD = to_dict(guess)

        if guess == '/q': #Обработка выхода из игры
            return 0
        elif guess == '/s': #Обработка настроек
            return 3
        for i in range(len(word)):
            count[word[i]] = word.count(word[i])

        while len(guessD) < length:
            guessD.append({'_':None})
            guess = guess + '_'

        if guess == word:

            print(f'\033[F\033[38;5;120m{guess}\033[0m')
            return 1
        else:
            for i in range(len(guess)):
                if guess[i] not in word or count[guess[i]] == 0:
                    guessD[i][guess[i]] = 'wrong'
                elif guess[i] == word[i]:
                    guessD[i][guess[i]] = 'right'
                    count[guess[i]] -= 1
                elif guess[i] in word:
                    guessD[i][guess[i]] = 'place'
                    count[guess[i]] -= 1
        att += 1
        
        for i in range(length):
            if i == 0:
                print('\033[F',end = '')
            match guessD[i][guess[i]]:
                case 'right':
                    print(f'\033[38;5;120m{guess[i]}\033[0m',end = '')
                case 'place':
                    print(f'\033[38;5;185m{guess[i]}\033[0m',end = '')
                case 'wrong':
                    print(f'\033[38;5;8m{guess[i]}\033[0m',end = '')
        print()
    return 2

print('Enter "/q" to exit, "/s" for settings.')
streak = 0
c = 5 #Кол-во попыток
length = 5 #Длина слова
inp = input('Enter word length: ')
if inp == '/s':
    settings()
elif inp == '/q':
    exit()
else:
    try:
        length = int(inp)
    except ValueError:print('Wrong length.')
    print('\033[FWord length:',length,'        ')

while True:
    match game(length, c):
        case 0:
            break
        case 1:
            print('\033[38;5;120mYou Win!\033[0m')
            if streak > 0:
                print(f'\033[38;5;54mYour winstreak: {streak + 1}\033[0m')
            streak +=1
        case 2:
            print('\033[38;5;124mYou lose.\033[0m\nWord was: ' + word)
            if streak > 1:
                print(f'\033[38;5;54mYou lost your winstreak :C\033[0m')
            streak = 0
        case 3:
            settings()