def iterableSample():
    even_list = [i for i in range(2, 31) if i % 2 == 0]
    print("This list is an Iterable - ", even_list)
    print("Printing all numbers from an Iterable.")
    for even_num in even_list:
        print(even_num)


if __name__ == "__main__":
    iterableSample()
