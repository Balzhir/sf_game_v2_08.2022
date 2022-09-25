"""Игра Угадай число
Компьютер загадывает число и сам его угадывает
"""

import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count=0
    predict_number_min=1 # минимальное значение заданного интервала
    predict_number_max=101 # максимальное значение заданного интервала
    
    while True:
        count+=1
        predict_number=(predict_number_min+predict_number_max)//2 # вычисляем среднее значение между минимальным и максимальным значениями
        if number>predict_number:
            predict_number_min=predict_number # если загаданное число больше среднего значения, то минимальному значению присваиваем среднее
        elif number<predict_number:
            predict_number_max=predict_number # если загаданное число меньше среднего значения, то максимальному значению присваиваем среднее
        else:    
            break # выход из цикла, если угадали
    return(count)

print(f'Количество попыток: {random_predict()}')

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов наш алгоритм угадывает число

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score

# RUN
if __name__ == '__main__':
    score_game(random_predict)