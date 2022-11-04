# Python Program to find the L.C.M. of two input number

def compute_hcf(x, y):
    while y != 0:
        x, y = y, x % y
    return x


def compute_lcm1(x, y):
    # choose the greater number
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1
    return lcm


def compute_lcm2(x, y):
    lcm = (x * y)//compute_hcf(x, y)
    return lcm


if __name__ == '__main__':
    num1 = int(input())
    num2 = int(input())
    print(num1, num2)
    # compute_lcm(num1, num2)
    print("The H.C.F. is", compute_hcf(num1, num2))
    print("The L.C.M. is", compute_lcm1(num1, num2))
    print("The L.C.M. is", compute_lcm2(num1, num2))
