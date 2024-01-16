def main(students):
    #choice = input().split(' ')
    choice = ["A:", "3"]
    print(choice)
    if choice[0] == "S:" or choice[0] == "Student:":
        if len(choice) > 2 and (choice[2] == "B" or choice[2] == "Bus"): 
            student_bus(students, choice[1])

        else:
            student(students, choice[1])
    if choice[0] == "T:" or choice[0] == "Teacher:":
        teacher(students, choice[1])
    if choice[0] == "G:" or choice[0] == "Grade:":
        if len(choice) > 2: 
            if choice[2] == "H" or choice[2] == "High":
                grade_high(students, choice[1])
            else: grade_low(students, choice[1])
        else: grade(students, choice[1])
    if choice[0] == "B:" or choice[0] == "Bus:":
        bus(students, choice[1])
    if choice[0] == "A:" or choice[0] == "Average:":
        average(students, choice[1])
    return 0


def student(students, name):
    lookup = {}
    for student in students: 
        lookup.setdefault(student[0], []).append(student[1:])
    if not lookup.get(name): 
        print("")
        return 0
    for student in lookup.get(name):
        student = student[:3] + student[5:]
        print(name + ',' + ','.join(student))
    return 0

def student_bus(students, name): 
    lookup = {}
    for student in students: 
        lookup.setdefault(student[0], []).append(student[1:])
    if lookup.get(name) != None: 
        for student in lookup.get(name):
            student = [student[0]] + [student[3]]
            print(name + ',' + ','.join(student))
    else: print(" ")
    return 0

def teacher(students, name):
    lookup = {}
    for teacher in students:
        lookup.setdefault(teacher[6], []).append(teacher[:2])
    if lookup.get(name) != None:
        for student in lookup.get(name):
            student = student[0] + ", " + student[1]
            print(student)
    else: print(" ")
    return 0

def grade(students, number): 
    lookup = {}
    for grade in students:
        lookup.setdefault(grade[2], []).append(grade[:2])
    if lookup.get(number) != None:
        for student in lookup.get(number):
            student = student[0] + ", " + student[1]
            print(student)
    else: print(" ")
    return 0

def grade_high(students, number): # make it so students w/ same high GPA are all printed
    lookup = {}
    for grade in students:
        lookup.setdefault(grade[2], []).append(grade[:2] + grade[5:] + [grade[4]])
    if lookup.get(number) != None:
        high = lookup.get(number)[0]
        for student in lookup.get(number):
            if student[2] > high[2]:
                high = student
        print(", ".join(high))
    else: print(" ")
    return 0

def grade_low(students, number): # make it so students w/ same low GPA are all printed
    lookup = {}
    for grade in students:
        lookup.setdefault(grade[2], []).append(grade[:2] + grade[5:] + [grade[4]])
    if lookup.get(number) != None:
        low = lookup.get(number)[0]
        for student in lookup.get(number):
            if student[2] < low[2]:
                low = student
        print(", ".join(low))
    else: print(" ")
    return 0

def bus(students, number):
    lookup = {}
    for bus in students:
        lookup.setdefault(bus[4], []).append(bus[:4])
    if lookup.get(number) != None:
        for student in lookup.get(number):
            print(', '.join(student))
    else: print(" ")
    return 0

def average(students, number):
    lookup = {}
    total = 0
    amount = 0
    for grade in students:
        lookup.setdefault(grade[2], []).append(grade[5])
    if lookup.get(number) != None:
        for student in lookup.get(number):
            amount += 1
            total += float(student)
        print(number, ', ', round(total/amount, 2))
    else: print(" ")
    return 0

def info(students):
    return 0


if __name__ == "__main__":
    with open("students.txt") as file: 
        lines = [line.strip().split(',') for line in file]
        # for loop to go through lines and error check format
       #print(lines)
    
    main(lines)


