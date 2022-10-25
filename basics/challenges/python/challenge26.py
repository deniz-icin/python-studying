
def main():
    fine = 0
    d1, m1, y1 = [int(d1) for d1 in input().split(" ")] #returned date
    d2, m2, y2 = [int(d2) for d2 in input().split(" ")] #due date
    if y2 >= y1:
        if m2 >= m1:
            if d2 >= d1:
                print(fine)
            else:
                hackos = 15
                delay = d1 - d2
                print(hackos * delay)
        else:
            hackos = 500
            delay = m1 - m2
            print(hackos * delay)
    else:
        hackos = 10000
        print(hackos)
        
main()