# Find sum of numbers from 0 to N.

# Using For Loop -
def findSum(n):
    addSum = 0
    for i in range(n + 1):
        addSum += i
    return addSum


# Using the formula - ((n * (n + 1)) / 2)
def findSumFormula(n):
    addSum = (n * (n + 1)) // 2
    return addSum


if __name__ == "__main__":
    getSum = 50000000
    print(findSum(getSum))
    print(findSumFormula(getSum))
