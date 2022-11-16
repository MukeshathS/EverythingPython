

def dot_product(a1, a2):
    n = len(a1)
    prod_sum = 0
    for i in range(n):
        prod = a1[i] * a2[i]
        prod_sum += prod
    return prod_sum


if __name__ == '__main__':
    arr1 = list(map(int, input().split(" ")))
    arr2 = list(map(int, input().split(" ")))
    result = dot_product(arr1, arr2)
    print(result)
