import random

word_list = ['утка', 'селезень', 'овца', 'ягненок', 'курица', 'цыплёнок', 'петух', 'кролик', 'лошадь', 'жеребёнок', 'пони',
 'поросёнок', 'свинья', 'индюк', 'корова', 'телёнок', 'коза', 'голубь', 'цесарка', 'гусь', 'осёл', 'конь', 'гусь', 'страус', 'собака',
  'кошка', 'кошка']

def print_word(word_, list_):
    for c in word_:
        if c in list_:
            print(c, end=' ')
        else:
            print('_', end=' ')
    print()

def get_word():
    return random.choice(word_list).upper()
def display_hangman(tries):
    stages = [
                '''
                _______
                |     |
                |     O
                |    \|/
                |     |
                |    / /
                _________
                
                ''',
                '''
                _______
                |     |
                |     O
                |    \|/
                |     |
                |    / 
                _________
                ''',
                '''
                _______
                |     |
                |     O
                |    \|/
                |     |
                |    
                _________
                ''',
                '''
                _______
                |     |
                |     O
                |    \|
                |     |
                |    
                _________  
                ''',
                '''
                _______
                |     |
                |     O
                |     |
                |     |
                |     
                _________
                ''',
                '''
                _______
                |     |
                |     O
                |    
                |     
                |    
                _________ 
                ''',
                '''
                _______
                |     |
                |     
                |    
                |  
                |     
                _________ 
                '''
    ]
    return stages[tries]
def play():
  a = get_word()
  print('Давайте играть в угадайку слов!')
  word_completion = ['_'] * len(a)
  guessed = False
  guessed_letters = []
  guessed_words = []
  tries = 6
  print(display_hangman(tries))
  print(*word_completion)
  while True:        
        enter_word = input('Введите одну букву или слово целиком: ').upper()
        if not enter_word.isalpha():
            print('Не вводите иных символов кроме буквы или слова')
            continue
        if enter_word in guessed_letters:
            print(f'Буква {enter_word} уже была')
            continue
        if enter_word in guessed_words:
            print(f'Слово {enter_word} уже было')
            continue
        if len(enter_word) != 1 and len(enter_word) != len(a):
            continue
        if enter_word in a:
            if len(enter_word) == 1:
                guessed_letters += enter_word
                count = -1
                for c in a:
                    count += 1
                    if c == enter_word:
                        word_completion[count] = enter_word
                print('Есть такая буква')
                print(*word_completion)
                if ''.join(word_completion) == a:
                    guessed = True
            else:
                guessed = True
        if enter_word not in a:
            if len(enter_word) == 1:
                guessed_letters += enter_word
                tries -= 1
                print(f'Нет такой буквы, количество попыток: {tries}')
                print(display_hangman(tries))
                print(*word_completion)
            else:
                guessed_words.append(enter_word)
                tries -= 1
                print(f'Слово не верно, количество попыток: {tries}')
                print(display_hangman(tries))
                print(*word_completion)
        if guessed:
            print('Поздравляем, вы угадали слово! Вы победили!')
            return
        if tries == 0:
            print(f'Загаданным, оказалось слово - {a}')
            return
def main():
    print('Добро пожаловать!')
    play()
    contin_game = input('Хотите ещё сыграть, нажмите клавишу "д", не хотите нажмите "н": ')
    while True:
        if contin_game.upper() == 'Д':
            play()
        if contin_game.upper() == 'Н':
            print('Всего хорошего, до новых встреч!')
            break
        else:
            contin_game = input('Для новой игры нажмите клавишу "д", для выхода из игры клавишу "н": ')
            continue

main()