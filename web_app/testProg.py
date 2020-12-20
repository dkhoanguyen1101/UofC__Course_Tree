from Node import *
import csv

userCourseList = list()
allCourseList = list() 

def userOpt():
    
    opt = input('''
Choose one of these option:
0.List your course list
1.Create new course
2.Delete a course
3.Exit

input:  ''').strip()
    if(opt not in ['0', '1', '2', '3']):
        print('wrong input, please try again')
        opt = '-1'
    return int(opt)
    
    
def printuserCourseList():
    count = 0
    for i in userCourseList:
        print(count + '. ' + i.course)

def addNewCourse():
    code = input('course code: ').upper().strip()
    if not (code in allCourseList):
        raise FileExistsError('invalid course')

    course_dict = dict()

    try:
        filename = '../data/' + code + '.csv'
        csv_file = open(filename)
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                course_dict[row[0]] = [row[1].replace('$', ','), row[2].replace('$', ','), row[3].replace('$', ','), row[4].replace('$', ','), row[5].replace('$', ',')]
            line_count += 1
        # print(course_dict)
    except FileNotFoundError :
        raise FileNotFoundError('Cannot access course')
    
    num = input('enter code number: ').strip()
    
    if (num in course_dict):
        print('\nInfo\nCourse name: ' + course_dict[num][0] + '\nCourse code: ' + course_dict[num][1])
        print('Course Prerequisite: ' + course_dict[num][2] + '\nCourse Antirequisite(s): ' + course_dict[num][3] + '\n')

    
        
if __name__ == '__main__':
    try:
        csv_file = open(f'../data/courses.csv')
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                allCourseList.append(row[0])
            line_count += 1
    except FileNotFoundError:
        print('cannot access database, abort')
        exit(1)
    # print(allCourseList)

    while True:
        num = userOpt()
        if num == -1:
            pass
        elif num  == 0:
            printuserCourseList()
        elif num  == 1:
            try:
                addNewCourse()
            except FileExistsError:
                print('Invald Course Entered, Please Try Again')
            except  FileNotFoundError :
                print('Cannot access course')
        elif num == 3:
            print('Goodbye')
            exit(1)
