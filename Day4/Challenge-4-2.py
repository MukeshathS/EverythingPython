from statistics import mean
from decimal import Decimal

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    student_avg = {}
    stud_avg = {}
    for student, marks in student_marks.items():
        student_avg[student] = mean(marks)
        stud_avg[student] = sum(marks) / len(marks)
    query_name = input()
    # print(str(round(stud_avg[query_name],2)))
    print(Decimal(round(student_avg[query_name], 2)).quantize(Decimal('0.00')))
