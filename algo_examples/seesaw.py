
def tahterevalli ():
    w1 = int(input("birinci cocugun agirligi : "))
    x1 = int(input("birinci cocugun uzakligi : "))
    w2 = int(input("ikinci cocugun agirligi : "))
    x2 = 200 - x1
    print("Toplam uzunluk 200 cm oldugu icin ikinci cocugun uzakligi:" , x2)

    if (w1*x1 == w2*x2):
        print("cocuklar dengede")
    else:
        print("cocuklari yanlis oturttuk olmadi bu")

tahterevalli()