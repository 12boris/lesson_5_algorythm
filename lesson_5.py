"""1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
(за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести
наименования предприятий, чья прибыль ниже среднего."""

how_much_company = int(input('введите количество предприятий: '))
company = {

}
avg_sl = {

}

for i in range(how_much_company):
    company_name = input(f'\nвведите наименование {i + 1} компании: ')
    company[company_name] = []

    for ii in range(4):
        quarter = float(input(f'прибыль за {ii + 1} квартал: '))
        company[company_name].append(quarter)

    sum = 0
    for i in company[company_name]:
        sum += i

    avg_sl[company_name] = sum/4

profit_sum = 0

for i in avg_sl.values():
    profit_sum += i

profit_avg = profit_sum / how_much_company

min_profit = []
max_profit = []

for i in avg_sl.values():
    if i > profit_avg:
        max_profit.append(i)

    elif i < profit_avg:
        min_profit.append(i)

print(f'\nсредняя прибыль состовляет {profit_avg}. прибыль ниже среднего: {[i for i in min_profit]}'
      f',прибыль выше среднего: {[i for i in max_profit]}')

print('\nкомпании и их прибыль:')
for i in company.items():
    print(*i)

print('\nкомпании и их средняя прибыль прибыль:')
for i in avg_sl.items():
    print(*i)


"""2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и 
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]."""

from collections import deque


def sum_hex(x, y):
    nums = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    result = deque()
    transfer = 0

    if len(y) > len(x):
        x, y = deque(y), deque(x)

    else:
        x, y = deque(x), deque(y)

    while x:

        if y:
            res = nums[x.pop()] + nums[y.pop()] + transfer

        else:
            res = nums[x.pop()] + transfer

        transfer = 0

        if res < 16:
            result.appendleft(nums[res])

        else:
            result.appendleft(nums[res - 16])
            transfer = 1

    if transfer:
        result.appendleft('1')

    return list(result)


def mult_hex(x, y):
    nums = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    result = deque()
    queue = deque([deque() for _ in range(len(y))])

    x, y = x.copy(), deque(y)

    for i in range(len(y)):
        m = nums[y.pop()]

        for j in range(len(x) - 1, -1, -1):
            queue[i].appendleft(m * nums[x[j]])

        for _ in range(i):
            queue[i].append(0)

    transfer = 0

    for _ in range(len(queue[-1])):
        res = transfer

        for i in range(len(queue)):
            if queue[i]:
                res += queue[i].pop()

        if res < 16:
            result.appendleft(nums[res])

        else:
            result.appendleft(nums[res % 16])
            transfer = res // 16

    if transfer:
            result.appendleft(nums[transfer])

    return list(result)


a = list(input('Введите 1 шестнадцатиричное число: ').upper())
b = list(input('Введите 2 шестнадцатиричное число: ').upper())

print(*a, '+', *b, '=', *sum_hex(a, b))

print(*a, '*', *b, '=', *mult_hex(a, b))