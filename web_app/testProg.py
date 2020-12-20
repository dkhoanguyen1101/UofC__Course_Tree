from Node import *
import csv

userCourseList = list()
allCourseList = list() 

def userOpt():
    # author: Khoa Nguyen
    
    opt = input('''
Choose one of these option:
0.List your course list
1.Create new course
2.Delete a course
3.Exit

input:  ''')
    if(opt not in ['0', '1', '2', '3']):
        print('wrong input, please try again')
        opt = '-1'
    return int(opt)
    
    
def printuserCourseList():
    count = 0
    for i in userCourseList:
        print(count + '. ' + i.course)

def addNewCourse():
    code = input('course code: ').upper()
    if not (code in allCourseList):
        raise FileExistsError('invalid course')

    try:
        filename = code + '.csv'


if __name__ == '__main__':

    csv_file = open('../data/courses.csv')
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count != 0:
            allCourseList.append(row[0])
        line_count += 1

    # print(allCourseList)

    while True:
        num = userOpt()
        if num == -1:
            pass
            print(num)
        elif num  == 0:
            printuserCourseList()
        elif num  == 1:
            try:
                addNewCourse()
            except FileExistsError:
                print('Invald Course Entered, Please Try Again')

        elif num == 3:
            print('Goodbye')
            exit(1)
