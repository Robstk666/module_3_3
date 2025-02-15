def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# Шаг 1: Вызовы функции с разным количеством аргументов
print("Вызовы с разными аргументами:")
print_params()  # 1 'строка' True
print_params(b=25)  # 1 25 True
print_params(c=[1, 2, 3])  # 1 'строка' [1, 2, 3]

# Шаг 2: Создание списка и словаря
values_list = [10, 'другая строка', False]
values_dict = {'a': 99, 'b': 'еще одна строка', 'c': True}

# Шаг 2: Вызов функции с распаковкой параметров
print("\nРаспаковка параметров из списка и словаря:")
print_params(*values_list)  # 10 'другая строка' False
print_params(**values_dict)  # 99 'еще одна строка' True

# Шаг 3: Распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка']

print("\nРаспаковка + отдельные параметры:")
print_params(*values_list_2, 42)  # 54.32 'Строка' 42