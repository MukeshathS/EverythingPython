def iteratorSample():
    even_list = [i for i in range(2, 31) if i % 2 == 0]
    even_iter = iter(even_list)
    print("Printing from an Iterator.")
    for i in range(3):
        even_num = next(even_iter, "End of list.")
        print(even_num)
    print("I changed my mind. Printing the rest too.")
    for even_num in even_iter:
        print(even_num)


if __name__ == "__main__":
    iteratorSample()








