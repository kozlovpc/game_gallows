import random

word_list = ['Домкрат', 'Поджариться', 'Веник', 'Воззрение', 'Гусем', 'Завивка',
             'Издохнуть', 'Кончик', 'Переставить', 'Прижить', 'Раструб', 'Шкурный',
             'Взаимодействие', 'Газовик', 'Гондольер', 'Дебютировать', 'Имитация',
             'Искра', 'Нелюдим', 'Отступя', 'Тарабарский', 'Чинара']


def get_word():
    return random.choice(word_list).upper()


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
        # голова, торс, обе руки, одна нога
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
        # голова, торс, обе руки
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
        # голова, торс и одна рука
        '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
        # голова и торс
        '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
        # голова
        '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
        # начальное состояние
        '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                ''',
        '''
                   
                         
                         O
                        \\|/
                         |
                        / \\
                   
                '''
    ]
    return stages[tries]


word = get_word()


def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    tries = 6  # количество попыток
    print('Привет,давай поиграем в угадайку')
    print('У тебя есть', tries, 'попыток')
    print(display_hangman(tries))
    print('У тебя', tries, 'попыток')
    print(*word_completion, sep='')
    while not guessed:
        result = input().upper()
        if result in guessed_letters:
            print("Эта буква уже была")
        if result in '''!"№;%:?*()_-.,:;`1234567890-=+?></\~"''':
            print('\r', end='')
            print('Ошибка ввода,введите пожалуйста букву')
        elif result in word:
            print('\r', end='')
            word_completion = word_completion[:word.find(result)] + result + word_completion[word.find(result) + 1:]
            word_completion = word_completion[:word.rindex(result)] + result + word_completion[word.rindex(result) + 1:]
            if word.index(result) == len(word) - 1:
                print('\r', end='')
                word_completion = word_completion[:word.find(result)] + result + word_completion[word.find(result) + 1:]
            else:
                print('\r', end='')
                word_completion = word_completion[:word.rindex(result, 0, len(word) - 1)] + result + word_completion[
                                                                                                     word.rindex(result,
                                                                                                                 0,
                                                                                                                 len(word) - 1) + 1:len(
                                                                                                         word)]
            print(word_completion)
            guessed_letters.append(result)
        else:
            guessed_letters.append(result)
            print('\r', end='')
            tries -= 1
            print('У вас осталось', tries, 'попыток')
            if tries == 0:
                print('\r', end='')
                print(display_hangman(tries))
                print('Вы проиграли')
            else:
                print('\r', end='')
                print(display_hangman(tries))
        if word_completion == word:
            print('\r', end='')
            print('Вы выиграли,поздравляем')
            print(display_hangman(7))
            break


play(word)
