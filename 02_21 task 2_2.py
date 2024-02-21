print('введите номер места')
num=input()
num=int(num)
if num%2==1:
    if num%5==0:
        print('боковое нижнее')
    else:
        print('в купе нижнее')
else:
    if num%6==0:
        print('боковое верхнее')
    else:
        print('в купе верхнее')
if num>100:
    print('не существует номера места')