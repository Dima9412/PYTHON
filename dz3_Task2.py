"""
Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.
"""

"""
При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения `list_1` и `k`

При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения `list_1` и `k` для проверки
"""

list_1 = [1, 2, 3, 4, 5]
k = 6

# Введите ваше решение ниже
#решение 1
def find_closest(list_1, k):
    minDiff = float('inf')
    closest = None
    for x in list_1:
        diff = abs(x - k)
        if diff < minDiff:
            minDiff = diff
            closest = x
    return closest


result = find_closest(list_1, k)
print(result)

#решение 2
m = abs(k - list_1[0])  # модуль числа
number = list_1[0]
for i in range(1, len(list_1)):
    if m > abs(list_1[i] - k):
        m = abs(list_1[i] - k)
        number = list_1[i]
print(number)
