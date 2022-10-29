def checksum(a, array):
    for ind, i in enumerate(array):
        c = a - i
        if c in array[ind+1:]:
            return True
    return False


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    k = int(input().strip())
    print(checksum(k, arr))
