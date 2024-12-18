print ('1.Функция с параметрами по умолчанию:')
print()

def print_params(a = 1, b = 'строка', c = True):
    print (a, b, c)
print_params() # вывод функции без аргументов
print_params(7, ',банан', False)
print_params(5, 'None')
print_params(False)
print_params(a='банан', b='яблоко', c='апельсин')
print_params(b='слон', c='конь')
print_params(b = 25) #g
print_params(c = [1,2,3])
print('__________________')
print('2.Распаковка параметров:')
print()

values_list = [1, 'строка', True]
values_dict = {'a':7 , 'b':'банан', 'c': False }

print_params(*values_list)
print_params(**values_dict)

print('____________________')
print('3.Распаковка + отдельные параметры:')
print()

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)
print('____________________')
print()

def append_to_list(item, list_my=None):
    if list_my is None:
        list_my = []
        list_my.append(item)

        print(list_my)
append_to_list(1,2) #не выводит ибо list_my не None
append_to_list([1,2]) #добавляет список в списокa

