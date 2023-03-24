# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

number_n = int(input("введите кол-во элементов первого множества n=  "))
number_m = int(input("введите кол-во элементов второго множества m=  "))


def print_number(arg):
    inp = list(input('Enter list: ').split())
    temp = list(map(int, inp))
    if len(temp) == arg:
        print(*temp)
        return temp

    else:
        print("введено неверное кол-во элементов")


n_set = print_number(number_n)
m_set = print_number(number_m)
s_set = []

s_set.extend(n_set)
s_set.extend(m_set)
s_set = set(n_set).intersection(m_set)
print(*sorted(s_set))
