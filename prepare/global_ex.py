
sesli_harfler = 'aeıioöuü'
sayaç = 0

kelime = input('Bir kelime girin: ')

def seslidir(harf):
    return harf in sesli_harfler

def artır():
    global sayaç
    for harf in kelime:
        if seslidir(harf):
            sayaç += 1
    return sayaç

mesaj = '{} kelimesinde {} sesli harf var.'
print(mesaj.format(kelime, artır()))


# global üzerinden sayaç değişkenini değiştirdiğimiz için fonksiyonumuzda kullanmamız gerekir.
# kelime değişkenimiz de global üzerinden geliyor ancak kendisini değiştirmeye çalışmıyoruz,sadece kullanıyoruz.
# sadece kullandığımız için global üzerinden çağırmamıza gerek kalmıyor.