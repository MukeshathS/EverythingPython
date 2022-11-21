def sampleMap(n):
    div_by_seven_list = list(
        map(
            lambda num: num % 7 == 0,
            [i for i in range(1, n + 1)]
        )
    )
    count_seven = div_by_seven_list.count(True)
    return count_seven


if __name__ == "__main__":
    print("Count of numbers divisible by 7 -",
          sampleMap(100))









