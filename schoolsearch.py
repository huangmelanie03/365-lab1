def main(students):
    while True:
        print("What search would you like to make? ")
        choice = input().split(' ')
        if choice[0] == "S:" or choice[0] == "Student:":
            if len(choice) > 2 and (choice[2] == "B" or choice[2] == "Bus"): 
                student_bus(students, choice[1])
            else:
                student(students, choice[1])
        elif choice[0] == "T:" or choice[0] == "Teacher:":
            teacher(students, choice[1])
        elif choice[0] == "G:" or choice[0] == "Grade:":
            if len(choice) > 2: 
                if choice[2] == "H" or choice[2] == "High":
                    grade_high(students, choice[1])
                else: grade_low(students, choice[1])
            else: grade(students, choice[1])
        elif choice[0] == "B:" or choice[0] == "Bus:":
            bus(students, choice[1])
        elif choice[0] == "A:" or choice[0] == "Average:":
            average(students, choice[1])
        elif choice[0] == "I" or choice[0] == "Info":
            info(students)
        elif choice[0] == "Q" or choice[0] == "Quit":
            exit()
        else: 
            print("Search option not recognized")
        print("")


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
            print(name + ', ' + ', '.join(student))
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
        highs = []
        for student in lookup.get(number):
            if student[2] > high[2]:
                high = student
        highs.append(high)
        for student in lookup.get(number):
            if student[0] != high[0] and student[2] == high[2]:
                highs.append(student)
        for student in highs:
            print(", ".join(student))
    else: print(" ")
    return 0

def grade_low(students, number): # make it so students w/ same low GPA are all printed
    lookup = {}
    for grade in students:
        lookup.setdefault(grade[2], []).append(grade[:2] + grade[5:] + [grade[4]])
    if lookup.get(number) != None:
        low = lookup.get(number)[0]
        lows = []
        for student in lookup.get(number):
            if student[2] < low[2]:
                low = student
        lows.append(low)
        for student in lookup.get(number):
            if student[0] != low[0] and student[2] == low[2]:
                lows.append(student)
        for student in lows:
            print(", ".join(student))
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
        print(str(number) + ', ' + str(round(total/amount, 2)))
    else: print(" ")
    return 0

def info(students):
    # dictionary with grade as key
    lookup = {}
    for grade in students:
        lookup.setdefault(grade[2], []).append(grade)
    # create list of tuples with grade # and # of students in grade
    info = []
    for grade in lookup.keys():
        number = 0
        for student in lookup.get(grade): 
            number += 1
        info.append((grade, number))
    # sort list by second value
    info = sorted(info, key=lambda x:int(x[0]))
    # print list
    for grade in info: 
        print(str(grade[0]) + ": " + str(grade[1]))
    return 0

def is_float(string):
    try:
        test1 = int(string)
        return False
    except ValueError: 
        try: 
            test = float(string)
            return True
        except ValueError: 
            return False

if __name__ == "__main__":
    with open("students.txt") as file: 
        lines = [line.strip().split(',') for line in file]
        for line in lines:
            if len(line) == 8:
                last_name, first_name, grade_num, classroom, bus_route, gpa, t_last_name, t_first_name = line
                if (grade_num.isdigit() == False) or int(grade_num) < 0 or int(grade_num) > 6:
                    print("wrong grade")
                    exit()
                if (classroom.isdigit() == False):
                    print("wrong classroom")
                    exit()
                if (bus_route.isdigit() == False):
                    print("wrong bus")
                    exit()
                if (is_float(gpa) == False) or float(gpa) < 0 or float(gpa) > 6:
                    print("wrong gpa")
                    exit()
                main(lines)
            else: 
                print("error with file")
                exit()



