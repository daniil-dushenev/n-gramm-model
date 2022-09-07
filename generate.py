import random
import pickle
import sys
import argparse
import numpy as np


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--prefix')
    parser.add_argument('--model', default='model/model.pickle')
    parser.add_argument('--length', default=random.randint(20, 50))
    parser.add_argument('--off_sigmoid', default=0)

    return parser


class model():
    def generate(self, model_file, word_input, count, sigm_active=True):  # count - кол-во слов для генерации
        word_input = word_input.lower()  # добавить проверку на рус. язык
        text = word_input
        word_input = word_input.split()
        input_list = word_input  # слова преобразовали в список
        word_input = word_input[-1]  # последнее введеное слово
        with open(model_file, 'rb') as file:  # выгрузили модель
            dir = pickle.load(file)
        file.close()

        for k in range(count):
            # выбираем случайно слово на основе 1 предыдущего и считаем его частоту
            try:
                dir_1 = dir['1'][word_input]
            except KeyError:
                text = f'Слова "{word_input}" мы не знаем :( \nВыберу случайное из тех, что знаю\n'
                word_input = random.choice(list(dir['1'].keys()))
                dir_1 = dir['1'][word_input]
                text += word_input
            word_list = []
            for word in dir_1:
                word_list += [word] * dir_1[word]
            word_1 = np.random.choice(word_list)
            ver_1 = dir_1[word_1] / len(word_list)
            if sigm_active:
                ver_1 = 1 / (1 + np.exp(-ver_1))  # применяем функцию сглаживания (сигмоиду), без нее часто прога выкидывает
            # 3 вариант и иногда получается просто текст из книги

            # выбираем случайно слово на основе 2 предыдущих и считаем его частоту
            word_2 = ''
            ver_2 = 0
            if str(input_list[-2:]) in dir['2']:
                dir_2 = dir['2'][str(input_list[-2:])]
                word_list = []
                for word in dir_2:
                    word_list += [word] * dir_2[word]
                word_2 = np.random.choice(word_list)
                ver_2 = dir_2[str(word_2)] / len(word_list)
                if sigm_active:
                    ver_2 = 1 / (1 + np.exp(-ver_2))  # cигмоида

            # выбираем случайно слово на основе 3 предыдущих и считаем его частоту
            word_3 = ''
            ver_3 = 0
            if str(input_list[-3:]) in dir['3']:
                dir_3 = dir['3'][str(input_list[-3:])]
                word_list = []
                for word in dir_3:
                    word_list += [word] * dir_3[word]
                word_3 = np.random.choice(word_list)
                ver_3 = dir_3[str(word_3)] / len(word_list)
                if sigm_active:
                    ver_3 = 1 / (1 + np.exp(-ver_3))  # cигмоида

            weights = [ver_1, ver_2, ver_3]
            new_word = random.choices([word_1, word_2, word_3], weights=weights, k=1)   # Выбираем самое вероятное слово
            # Часто 3 вариант имеет больший шанс, (если существует),
            # но из-за функции сглаживания разброс не сильно большой
            new_word = new_word[0]

            input_list.append(new_word)     # добавляем в список слов
            text += ' ' + new_word      # добавляем слово в вывод
            word_input = new_word   # новое слово - теперь текущее
        print(text)


parser = createParser()
args = parser.parse_args(sys.argv[1:])      # собираем параметры ввода
if args.prefix == None:
    with open(args.model, 'rb') as file:
        dir = pickle.load(file)
    file.close()
    prefix = random.choice(list(dir['1'].keys()))       # подбираем рандомное слово, если оно не задано
else:
    prefix = args.prefix

neuwork = model()
neuwork.generate(args.model, prefix, int(args.length), (False if int(args.off_sigmoid) == 1 else True))