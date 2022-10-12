def minion_game(string):
    string = string.lower()
    l = len(string)
    kevin_score = 0
    stuart_score = 0
    vowels = "aeiou"
    for _ in range(l):
        if string[_] in vowels:
            kevin_score += l-_
        else:
            stuart_score += l-_
    if stuart_score > kevin_score:
        print("Stuart",stuart_score)
    elif stuart_score < kevin_score:
        print("Kevin",kevin_score)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)