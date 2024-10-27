def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(a=100, b='bass', c=True)
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(b='BigBoss', c=(100-1==99))


values_list = [99, 'Бууза', [1, 10, 100]]
values_dict = {'a': [1, 2, 3], 'b': 'Хемультан-это суп!', 'c': 99}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
