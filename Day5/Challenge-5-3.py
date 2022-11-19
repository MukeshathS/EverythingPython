
def compute_hcf(x, y):
    if y == 0:
        return x
    return compute_hcf(y, x % y)


def compute_lcm(x, y):
    lcm = (x * y)//compute_hcf(x, y)
    return lcm


if __name__ == '__main__':
    num1, den1 = map(int, input().split("/"))
    num2, den2 = map(int, input().split("/"))

    lcm = compute_lcm(den1, den2)

    num3 = (num1 * (lcm/den1)) + (num2 * (lcm/den2))
    den3 = lcm

    hcf = compute_hcf(num3, den3)
    print("hcf", hcf)

    num3 = int(num3/hcf)
    den3 = int(den3 / hcf)

    print(str(num3) + '/' + str(den3))

    # if den1 == lcm:
    #     num2 = num2 * (lcm // den2)
    # elif den2 == lcm:
    #     num1 = num1 * (lcm // den1)
    # else:
    #     num1 = num1 * (lcm // den1)
    #     num2 = num2 * (lcm // den2)
    # num3 = num1 + num2











