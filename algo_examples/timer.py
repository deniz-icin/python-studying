anlikSA , anlikDK = [int(anlikSA) for anlikSA in input("Anlik zamani SA:DK olarak giriniz... ").split(":")]
alarmSA , alarmDK = [int(alarmSA) for alarmSA in input("Alarm saatini SA:DK olarak giriniz... ").split(":")]

def kacDkKaldi ():

    if anlikSA > alarmSA:
        a = 24 - anlikSA
        b = 60*(a + alarmSA)
        if anlikDK < alarmDK:
            c =  alarmDK - anlikDK
            sonuc = b + c
            print("Geriye kalan dk : ", sonuc)
        elif anlikDK > alarmDK:
            c = 60 - anlikDK
            sonuc = c + alarmDK + b - 60
            print("Geriye kalan dk : ", sonuc)
        else:
            sonuc = b
            print("Geriye kalan dk : ", sonuc)

    elif anlikSA < alarmSA:
        b = 60*(alarmSA - anlikSA)
        if anlikDK < alarmDK:
            c =  alarmDK - anlikDK
            sonuc = b + c
            print("Geriye kalan dk : ", sonuc)
        elif anlikDK > alarmDK:
            c = 60 - anlikDK
            sonuc = c + alarmDK + b - 60
            print("Geriye kalan dk : ", sonuc)
        else:
            sonuc = b
            print("Geriye kalan dk : ", sonuc)

    else:
        if anlikDK < alarmDK:
            c =  alarmDK - anlikDK
            print("Geriye kalan dk : ", c)
        else:
            print("olmayacak duaya amin deme kardesim :)")

def main():
    if (24>=anlikSA>=0 and 24>=alarmSA>=0) != True or (60>=anlikDK>=0 and 60>=alarmDK>=0) != True:
        print("Saatler 0 ila 24, Dakikalar 0 ila 60 arasinda yazilmalidir.")
    else:
        return kacDkKaldi()

main()