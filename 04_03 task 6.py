def f():
    a={'Вьетнам':'Ханой', 'Таиланд':'Бангкок', 'Россия':'Москва', 'Китай':'Пекин'}
    print(a)
    print("Столица Вьетнама -", a['Вьетнам'])
    b=sorted(a)
    print(b)

def g():
    o1=['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
    o2 = ['Д', 'К', 'Л', 'М', 'П', 'У']
    o3 = ['Б', 'Г', 'Ё', 'Ь', 'Я']
    o4 = ['Й', 'Ы']
    o5 = ['Ж', 'З', 'Х', 'Ц', 'Ч']
    o8 = ['Ш', 'Э', 'Ю']
    o10 = ['Ф', 'Щ', 'Ъ']
    sum=0
    print('Введите слово')
    a=input()
    b=list(a.upper())
    for i in b:
        if i in o1:
            sum=sum+1
        if i in o2:
            sum=sum+2
        if i in o3:
            sum=sum+3
        if i in o4:
            sum=sum+4
        if i in o5:
            sum=sum+5
        if i in o8:
            sum=sum+8
        if i in o10:
            sum=sum+10
    print(sum)
g()




