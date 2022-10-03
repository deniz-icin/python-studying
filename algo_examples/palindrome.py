girdi = input("Bir kelime giriniz:")

def palindrome():
    if girdi == girdi[::-1]:
        print("Girdiğiniz kelime bir palindrome'dur.")
    else:
        print("Girdiğiniz kelime bir palindrome değildir.")

palindrome()