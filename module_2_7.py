def print_params(a=1, b='строка', c=True):
    print(a, b, c)
print_params()
def print_params(a=1, b='строка', c=True):
    print(a, c)
print_params()
def print_params(a=1, b='строка', c=True):
    print()
print_params()
def print_params(a=1, b='строка', c=True):
    print(a, b, c)
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = [1.25, 'мальчик', 25]
values_dict = {'a':32, 'b':'вот, пожалуйста', 'c':False}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [52.32, 'Строка']
print_params(*values_list_2)

