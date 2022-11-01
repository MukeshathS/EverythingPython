def swap_case(s):
    res = ""
    for i in s:
        if i.isalpha():
            if i.islower():
                res += i.upper()
            else:
                res += i.lower()
        else:
            res += i
    return res


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)