from random import randint
f=3
k=0
while f>0:
    a=randint(0,100)
    b = randint(0, 100)
    c=a+b
    print(a, '+', b, '=', end=' ')
    ot=input()
    if ot == c:
        print('Правильно!')
        k+=1
    else:
        print('Ответ неверный')
        f=f-1
        print('Осталось', f, 'жизней')
if f==0:
    print('Игра окончена. Правильных ответов:', k)
