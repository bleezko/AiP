def task1 ():
with open('D:\UserFolders\Desktop\"products.json"') as f:
    products = json.load(f)
for product in products['product']:
    print(f"Название: {product['name']}")
    print(f"Цена: {product['price']}")
    print(f"Вес: {product['weight']}")
    if product['available']:
        print("В наличии")
    else:
        print("Нет в наличии!")
    print()
task1()

def task2 ():
    with open('C:\Рабочий стол\"product.json"') as f:
        products = json.load(f)
    for product in products['product']:
        print(f"Название: {product['name']}")
        print(f"Цена: {product['price']}")
        print(f"Вес: {product['weight']}")
        if product['available']:
            print("В наличии")
        else:
            print("Нет в наличии!")
        print()
    newname = input("Введите название продукта: ")
    newprice = input("Введите цену продукта: ")
    newavailable = input("Введите наличие продукта (True/False): ")
    newweight = input("Введите вес продукта: ")
    products['products'].append({
        "name": newname,
        "price": newprice,
        "available": newavailable,
        "weight": newweight
    })
    with open('products.json', 'w') as f:
        json.dump(products, f)
    with open('products.json') as f:
        products = json.load(f)
    for product in products['products']:
        print(f"Название: {product['name']}")
        print(f"Цена: {product['price']}")
        print(f"Вес: {product['weight']}")
        if product['available']:
            print("В наличии")
        else:
            print("Нет в наличии!")
        print()
task2()

def task3() :
    with open('en-ru.txt', 'r') as f:
        lines = f.readlines()
    dict = {}
    for line in lines:
        eng, ru = line.strip().split(' - ')
        eng = en.strip()
        ru = ru.strip()
        dict[ruslovo] = eng
    sorteddict = sorted(dict.items())
    with open('ru-en.txt', 'w') as f:
        for ru, eng in sorteddict:
            f.write(f"{ru} – {eng}\n")
