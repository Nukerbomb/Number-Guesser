def vsmisli(s,n):
    my_string = ''.join(map(str, s))
    my_number = int(my_string)
    if my_number>1 and my_number<=n:
        return True
    else:
        return False

def is_valid(text,n):
    if text.isdigit()==True and vsmisli(text,n) == True:
        return True
    else:
        return False

def is_valid_int(number,n):
    if number == int(number) and number <= n:
        return True
    else:
        return False

import random



print("Добро пожаловать в числовую угадайку")
print("До какого числа рандомим, друг мой?")
n = int(input())

Chislo = random.randint(1,n)
s = input()

counter = 0


my_string = ''.join(map(str, s))
my_number = int(my_string)
while my_number != Chislo:

    if my_number < Chislo:
        if is_valid_int(my_number,n) == False:
            print('А может быть все-таки введем целое число от 1 до',n,"?")
            my_number = int(input())
        else:
            counter += 1
            print('Ваше число меньше загаданного, попробуйте еще разок')
            my_number = int(input())

    if my_number > Chislo:
        if is_valid_int(my_number,n) == False:
            print('А может быть все-таки введем целое число от 1 до',n,"?")
            my_number = int(input())
        else:
            counter += 1
            print('Ваше число больше загаданного, попробуйте еще разок')
            my_number = int(input())
    if my_number == Chislo:
        print('Вы угадали, поздравляем!',"вот, кстати, сколько вам понадобилось попыток:", counter)
        print("Ну что?)) снова в бой? д = да, н = нет")
        answer = input()
        if answer == "д":
            Chislo = random.randint(1,n)
        else: break
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')