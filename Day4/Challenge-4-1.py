
def stud_grades(name, score):
    return [name, score]


if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append(stud_grades(name, score))

    students_n = dict(students)
    second_lowest = sorted(list(set([students_n[i] for i in students_n])), reverse=True)[-2]
    sec_low_students = []
    for i, j in students_n.items():
        if j == second_lowest:
            sec_low_students.append(i)

    for n in sorted(sec_low_students):
        print(n)
