def task1():
    from PIL import Image
    filename = "picture.jpg"
    with Image.open(filename) as img:
        img.load()
    img.show()
    print(img.size)
    print(img.format)
    print(img.mode)
task1()

def task2():
    from PIL import Image
    filename = "picture.jpg"
    with Image.open(filename) as img:
        img.load()
    img1=img.reduce(3)
    img2=img.transpose(Image.FLIP_LEFT_RIGHT)
    img3=img.transpose(Image.FLIP_TOP_BOTTOM)
    img1.save("picture0_33.jpg")
    img2.save("picture_horiz.jpg")
    img3.save("picture_vert.jpg")
task2()

def task3():
    from PIL import Image
    images = ["1.jpg", "2.jpg", "3.jpg", "4.jpeg", "5.jpg"]
    for img in images:
        image = Image.open(img)
        smooth_img = img.filter(ImageFilter.SMOOTH)
        imgcont.save('picture/' + str(img))
task3()

def task4():
    from PIL import Image
    filename = "picture.jpg"
    with Image.open(filename) as img:
        img.load()
    img_new=img.reduce(10)
    img_fil = img_new.convert("L")
    edges = img_fil.filter(ImageFilter.FIND_EDGES)
    img.paste(edges)
    img.show()
task4()
