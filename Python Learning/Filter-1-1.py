def sampleFilter(n):
    div_by_seven_list = list(
        filter(
            lambda num: num % 7 == 0,
            [i for i in range(1, n + 1)]
        )
    )
    return div_by_seven_list


if __name__ == "__main__":
    print("Numbers divisible by 7 -",
          sampleFilter(100))









