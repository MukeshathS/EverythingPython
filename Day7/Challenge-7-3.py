if __name__ == '__main__':
    s = input()
    alnum = False
    alpha = False
    digit = False
    lower = False
    upper = False
    for t in s:
        if t.isalnum() and alnum == False:
            print(t.isalnum())
            alnum = True
        if t.isalpha() and alpha == False:
            print(t.isalpha())
            alpha = True
        if t.isdigit() and digit == False:
            print(t.isdigit())
            digit = True
        if t.islower() and lower == False:
            print(t.islower())
            lower = True
        if t.isupper() and upper == False:
            print(t.isupper())
            upper = True
