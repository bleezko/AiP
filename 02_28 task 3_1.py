print('Сколько слов ввести?')
n = input()
n = int(n)
s=''
if n <= 0:
    print('Ошибка!')
for a in range(n):
    a = input()
    s = s + a + ' '
print(s)