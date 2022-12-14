# Проект 0. Угадай число

## Оглавление
[1. Описание проекта](https://github.com/Balzhir/sf_game_v2_08.2022/tree/main/project_0/README.md#Описание-проекта)

[2. Какой кейс решаем?](https://github.com/Balzhir/sf_game_v2_08.2022/tree/main/project_0/README.md#Какой-кейс-решаем)

[3. Краткая информация о данных](https://github.com/Balzhir/sf_game_v2_08.2022/tree/main/project_0/README.md#Краткая-информация-о-данных)

[4. Этапы работы над проектом](https://github.com/Balzhir/sf_game_v2_08.2022/tree/main/project_0/README.md#Этапы-работы-над-проектом)

[5. Результат](https://github.com/Balzhir/sf_game_v2_08.2022/tree/main/project_0/README.md#Результат)

[6. Выводы](https://github.com/Balzhir/sf_game_v2_08.2022/tree/main/project_0/README.md#Выводы)


### Описание проекта
Угадать загаданное компьютером число за минимальное число попыток.

:arrow_up: [к оглавлению](https://github.com/Balzhir/sf_game_v2_08.2022/tree/main/project_0/README.md#Оглавление)

### Какой кейс решаем?    
Нужно написать программу, которая угадывает число за минимальное число попыток.

**Условия соревнования:**  
- Компьютер загадывает целое число от 1 до 100, и нам его нужно угадать. Под «угадать» подразумевается «написать программу, которая угадывает число».
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества**     
Результаты оцениваются по среднему количеству попыток при 1000 повторений.

**Что практикуем**     
Учимся писать хороший код на python.

:arrow_up: [к оглавлению](https://github.com/Balzhir/sf_game_v2_08.2022/tree/main/project_0/README.md#Оглавление)

### Краткая информация о данных

--

:arrow_up: [к оглавлению](https://github.com/Balzhir/sf_game_v2_08.2022/tree/main/project_0/README.md#Оглавление)

### Этапы работы над проектом  
В ходе реализации проекта было опробовано два алгоритма решения данной задачи:
1. Загаданное алгоритмом число угадывает пользователь методом «горячо-холодно» ([код](https://github.com/Balzhir/sf_game_v2_08.2022/blob/main/project_0/game.py)).
2. Алгоритм сам загадывает и отгадывает число. Алгоритм угадывает число, показывая, за какое количество попыток он это сделал при данном конкретном запуске, а также показывая, за какое количество попыток он это сделал в среднем из 1000 подходов ([код](https://github.com/Balzhir/sf_game_v2_08.2022/blob/main/project_0/game_v2.py)).

:arrow_up: [к оглавлению](https://github.com/Balzhir/sf_game_v2_08.2022/tree/main/project_0/README.md#Оглавление)

### Результат

Установлено, что при использовании первого алгоритма, пользователь может легко отгадать число меньше чем за 10 попыток. Когда алгоритм сам отгадывает число, то в среднем он это делает за 101 попытку.

:arrow_up: [к оглавлению](https://github.com/Balzhir/sf_game_v2_08.2022/tree/main/project_0/README.md#Оглавление)

### Выводы

Пользователь методом «горячо-холодно» отгадывает число за меньшее количество попыток, чем это делает сам алгоритм.