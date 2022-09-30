def enBuyukAsal():

    sayi = int(input('Bir sayi giriniz = '))
    bolenSayi = 2
    list = []

    for x in range(2,sayi+1):
        if (sayi % bolenSayi == 0):
            sayi /= bolenSayi
            list.append(bolenSayi)
        else:
            bolenSayi += 1
    
    print("en buyuk asal bolen:", max(list))
    

enBuyukAsal()
