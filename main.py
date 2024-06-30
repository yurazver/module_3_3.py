def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

def print_params(a, b, c):
    print(a, b, c)
values_list = [2 , 'apple', False]

print_params(*values_list)
def print_params(a, b, c):
    print(a, b, c)
values_dict = {'a':3,'b':'строка', 'c':True}
print_params(**values_dict)

def print_params(a, b, c):
    print(a, b, c)
values_list_2 = [3.14, 'Число Пи']
print_params(*values_list_2, 42)