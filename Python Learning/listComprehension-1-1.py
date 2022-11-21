def simpleListComrehension(n):
    create_odd_list = [i for i in range(1, n) if i % 2 != 0]
    return create_odd_list


def ifElseListComprehension(n):
    create_odd_ello_list = \
        [i if i % 2 != 0 else "ello"
         for i in range(1, n)]
    return create_odd_ello_list


def nestedForListComprehension(n):
    the_list = [[(j, i) for j in range(5)]
                for i in n if i == "ello"]
    return the_list


if __name__ == "__main__":
    print(ifElseListComprehension(20))
    simpleListComrehension(20)
    checkList = ["yello", "ellow",
                 "lo", "yellow"]
    print(nestedForListComprehension(checkList))
    checkList = ["yello", "ellow",
                 "ello", "lo", "yellow"]
    print(nestedForListComprehension(checkList))
