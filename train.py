import re
import pickle
import os
import sys
import argparse


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir', default='texts')
    parser.add_argument('--model', default='model/model.pickle')

    return parser


class model():
    def fit(self, input_dir, input_model):
        file_list = os.listdir(input_dir)
        try:
            with open(input_model, 'rb') as file:
                try:
                    model_dir = pickle.load(file)
                except EOFError:
                    model_dir = {'1': {}, '2': {}, '3': {}}
                file.close()
        except:
            file = open(input_model, 'w+')
            file.close()
            model_dir = {'1': {}, '2': {}, '3': {}}

        dir_1 = model_dir['1']      # словарь с 1 словом перед генерируемым
        dir_2 = model_dir['2']      # словарь с 2 словами перед генерируемым
        dir_3 = model_dir['3']      # словарь с 3 словами перед генерируемым

        for text_input in file_list:
            file = open(f'{input_dir}/{text_input}', 'r').read()
            text = re.sub("[^а-я]", ' ', file.lower())
            text_list = text.split()  # Список слов без лишних символов в нижнем регистре

            for i in range(3, len(text_list)):
                word = text_list[i]  # текущее слово
                word_1 = text_list[i - 1]  # предыдущее слово
                word_2 = text_list[i - 2]  # перед предыдущим
                word_3 = text_list[i - 3]

                #   для 1 слова перед текущим
                if word_1 not in dir_1:  # Если предыдущего слова нет в словаре, добавляем
                    dir_1[word_1] = {word: 1}
                if word not in dir_1[word_1]:  # Если текущего слова нет в словаре предыдщего слова,
                    # добавляем и ставим количество 1
                    dir_1[word_1][word] = 1
                else:
                    dir_1[word_1][word] += 1  # Если такое слово уже попадалось, увеличиваем количество в словаре

                #   для 2 слов перед текущим
                word_1_2 = str([word_2, word_1])
                if word_1_2 not in dir_2:  # Все то же самое, что и для 1 слова, только в словаре хранятся 2 слова
                    dir_2[word_1_2] = {word: 1}
                if word not in dir_2[word_1_2]:
                    dir_2[word_1_2][word] = 1
                else:
                    dir_2[word_1_2][word] += 1

                #   для 3 слов перед текущим
                word_1_2_3 = str([word_3, word_2, word_1])
                if word_1_2_3 not in dir_3:  # Все то же самое, что и для 1 слова, только в словаре хранятся 3 слова
                    dir_3[word_1_2_3] = {word: 1}
                if word not in dir_3[word_1_2_3]:
                    dir_3[word_1_2_3][word] = 1
                else:
                    dir_3[word_1_2_3][word] += 1

        model_dir['1'] = dir_1
        model_dir['2'] = dir_2
        model_dir['3'] = dir_3

        with open(input_model, 'wb') as file:  # Загружаем все в модель
            pickle.dump(model_dir, file)
        file.close()


parser = createParser()
args = parser.parse_args(sys.argv[1:])      # собираем параметры ввода

neuwork = model()
neuwork.fit(args.input_dir, args.model)
print('Модель успешно обучена!')