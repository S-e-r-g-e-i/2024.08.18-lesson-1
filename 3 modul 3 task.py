# Распаковка позиционных параметров
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
print_params(a=777)
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [33, 'Monika', [1, 2, 3]]
values_dict = {'a': 'Sasha', 'b': 9, 'c': [4, 5, 6]}

print_params(*values_list)
print_params(**values_dict)
print_params(*values_list[0:2])

values_list_2 = [[44, 56], 'Donny']
print_params(*values_list_2, 42) # работает