n=5
while n>0:
    n=n-1
    a=input()
    if 'ф' in a or 'Ф' in a:
        print('Ого! Это редкое слово!')
    else:
        print('Эх, это не очень редкое слово...')