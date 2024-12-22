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

def game():
    c = 6 #Кол-во попыток
    att = 0
    #word = [{'c':None}, {'h':None}, {'e':None}, {'e':None}, {'s':None}, {'e':None}] #getword(len)
    word = getword(length) #'cheese'
    #print(word) #Вывод загаданного слова
    
    while att < c:
        count = {}
        guess = input()[:length]
        guessD = to_dict(guess)

        if guess == 'q': #Обработка выхода из игры
            return 0
        
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

print('Press "q" to exit.')
streak = 0
length = int(input('Введите длинну слова: '))


while True:
    match game():
        case 0:
            pass
        case 1:
            print('\033[38;5;120mYou Win!\033[0m')
            if streak > 0:
                print(f'\033[38;5;54mYour winstreak: {streak + 1}\033[0m')
            streak +=1
        case 2:
            print('\033[38;5;124mYou lose.\033[0m')
            if streak > 1:
                print(f'\033[38;5;54mYou lost your winstreak :C\033[0m')
            streak = 0