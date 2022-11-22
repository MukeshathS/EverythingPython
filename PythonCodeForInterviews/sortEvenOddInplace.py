def sortInPlace(inarray):
    left = 0
    right = len(inarray) - 1
    while left < right:
        while left < right and inarray[right] % 2 == 0:
            right -= 1
        if inarray[left] % 2 == 0:
            inarray[left], inarray[right] = inarray[right], inarray[left]
        left += 1
    return inarray


if __name__ == "__main__":
    array = [3, 2, 8, 4, 5, 1, 7, 6, 16, 19, 26]
    print(array)
    print(sortInPlace(array))
