if __name__ == '__main__':
    N = int(input())
    lst = []
    for _ in range(N):
        command = input().split()
        if command[0] == "insert":
            lst.insert(int(command[1]), command[2])
            lst = list(map(int, lst))
        elif command[0] == "print":
            print(list(map(int, lst)))
        elif command[0] == "remove":
            lst.remove(int(command[1]))
        elif command[0] == "append":
            lst.append(int(command[1]))
        elif command[0] == "sort":
            lst = sorted(lst)
        elif command[0] == "pop":
            lst.pop()
        elif command[0] == "reverse":
            lst = lst[::-1]
