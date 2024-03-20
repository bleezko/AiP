
#task 1
def F(n):
    if n % 5 == 0:
        return('Число делится на 5 без остатка')
    else:
        return('Число не делится на 5 без остатка')

#print('Введите число')
#n=input()
#n=int(n)
#print(F(n))



#task 2
def G(a):
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
#    print(G(int(a)))


#task 3
def H():
    den, mes, god=map(int, b.split('.'))
    if 1<=den<=31 and 1<=mes<=12:
        if den*mes==int(str(god)[-2:]):
            return ('True')
        else:
            return ('False')
    else:
        return ('Ошибка введённой даты')


#print('Введите дату день.месяц.год')
#b=(input())
#print(H())

#task 3
def J(l):
    if len(l)%2==0:
        dl=len(l)//2
        pe=(sum(int(i)) for i in l[:dl])
        vt=(sum(int(i)) for i in l[dl:])
        if pe==vt:
            return('билет счастливый')
        else:
            return ('билет не счастливый')
    else:
        print('Ошибка: Количество цифр в билете должно быть чётным')





print('Введите номер билета')
l=(input())
