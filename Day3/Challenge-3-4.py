
def easy1(n):
    for i in range(n):
        print(i**2)


def easy2(n):
    s = ""
    for i in range(1, n+1):
        s += str(i)
    print(s)


if __name__ == '__main__':
    n = int(input())
    easy1(n)
    easy2(n)

# easy3
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sortarr = sorted(list(set(arr)))
    print(sortarr[-2])

# easy4
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    lst = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                lst.append([i, j, k])
    print(lst)
    # Or
    print([[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n])

# easy5
if __name__ == '__main__':
    ar = list(map(int, input().rstrip().split()))
    print(sum(ar))
