#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    newgrades = []
    for ind, grade in enumerate(grades):
        if grade > 37:
            if grade % 5 != 0:
                for itr in range(5):
                    grademultiple = grade + itr
                    # grademultiple += itr
                    if grademultiple % 5 != 0:
                        continue
                    else:
                        if (grademultiple - grade) < 3:
                            grades[ind] = grademultiple
                            # newgrades.append(grademultiple)
                        else:
                            grades[ind] = grade
                            # newgrades.append(grade)
            else:
                grades[ind] = grade
                # newgrades.append(grade)
        else:
            grades[ind] = grade
            # newgrades.append(grade)
    return grades


if __name__ == '__main__':
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    for _ in grades:
        print(_)
