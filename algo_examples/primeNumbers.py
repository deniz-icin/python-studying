sayi = int(input('Sayi giriniz = '))
asalMi = False

def asalMi():
    for i in range(2,int(sayi**0.5)+1):
        if (sayi % i) == 0:
            return asalMi and print("asal degil")
        return True and print("asal")

asalMi()