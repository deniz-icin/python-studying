def harf():
    harfDegeri = input("harf salla random:")
    harfDegeri = sorted(harfDegeri)
    tumHarfler =""
    for i in harfDegeri:
        if not i in tumHarfler:
         tumHarfler += i
         print("{} --> {} kez geçiyor!".format(i, harfDegeri.count(i)))
    
harf()