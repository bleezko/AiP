
#task 1
def f(n):
    if n % 5 == 0:
        return('Число делится на 5 без остатка')
    else:
        return('Число не делится на 5 без остатка')

print('Введите число')
n=int(input())
print(f(n))



#task 2
def g(a):
    if a==0:
        return ('ZeroDivisionError')
    else:
        d=300 / a
        return(d)

#print('Введите число')
#a=input()
#if a.isalpha():
#    print('ValueError')
#else:
#    print(g(int(a)))


#task 3
def h():
    den, mes, god = map(int, b.split('.'))
    if 1 <= den <= 31 and 1 <= mes <= 12:
        if den * mes == int(str(god)[-2:]):
            return ('True')
        else:
            return ('False')
    else:
        return ('Ошибка введённой даты')


#print('Введите дату день.месяц.год')
#b=(input())
#print(h())

#task 4
def f(bil):
    perv_pol = 0
    vtor_pol = 0
    if len(bil) % 2 == 0:
        dl=len(bil) // 2
        for i in bil[:dl]:
            perv_pol = perv_pol + int(i)
        for j in bil[dl:]:
            vtor_pol = vtor_pol + int(j)
        if perv_pol == vtor_pol:
            return ('билет счастливый')
        else:
            return('билет не счастливый')
    else:
        return('Ошибка: Количество цифр в билете должно быть чётным')

#print('Введите номер билета')
#bil=(input())
#print(f(bil))
