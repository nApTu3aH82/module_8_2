# -*- coding: utf-8 -*-
def personal_summ(numbers):
    result = 0
    incorrect_data = 0
    for number in numbers:
        try:
            result += number
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы: {number}')
            incorrect_data += 1
    return (result, incorrect_data)


def calculate_average(numbers):
    try:
        pers_summ = personal_summ(numbers)
        count = len(numbers) - pers_summ[1]
        return pers_summ[0] / count
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return
    return pers_summ


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
