from Node import *
import csv

userCourseList = list()
allCourseList = list() 

def userOpt():
    
    opt = input('''
Choose one of these option:
0.List your course list
1.Create new course
2.Edit a course
3.Delete a course
4.Exit

input:  ''').strip()
    if(opt not in ['0', '1', '2', '3', '4']):
        print('wrong input, please try again')
        opt = '-1'
    return int(opt)
    
    
def printuserCourseList():
    if userCourseList:
        count = 0
        for i in userCourseList:
            print(str(count) + '. ' + i.course)
            count += 1
        return count

    else:
        print('There is no course to be printed')
        return 0

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
        print('Course Prerequisite: ' + course_dict[num][2] + '\nCourse Antirequisite(s): ' + course_dict[num][3] + '\ncourse added\n')
    else:
        raise FileExistsError('invalid course')

    
    userCourseList.append(course(Node(course_dict[num][1])))

def deleteCourse():
    num  = printuserCourseList()
    if num == 0:
        print('There is no course to be deleted')
        return

    opt = int()
    try:
        opt = int(input('enter the number of the course to be deleted: '))
    except ValueError:
        print('invalid input for number')
        return
    
    try:
        courseDelete = userCourseList[opt].course
        userCourseList.pop(opt)
        print(f"course {courseDelete} deleted")
    except IndexError:
        print('the index is not in range')
        return

def editCourse():
    num  = printuserCourseList()
    if num == 0:
        print('There is no course to be edited')
        return

    opt = int()
    try:
        opt = int(input('enter the number of the course to be edited: '))
    except ValueError:
        print('invalid input for number')
        return
    
    if (opt >= len(userCourseList)):
        print('wrong input for option')
        return
    

    

    courseToEdit = userCourseList[opt]

    print(courseToEdit.fullString())
        
    if courseToEdit.nodeList:
        count = 0
        for i in courseToEdit.nodeList:
            print(str(count) + '. ' + i.toString())
            count += 1
    pass

    
    
        
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

    newCourse = course(Node('CPSC 313'))
    newCourse.setAndChild([])
    newCourse.head.child.addItem([orNode([Node('MATH 271'), Node('MATH 273')])])
    newCourse.head.child.addItem([orNode([Node('PHIL 279'), Node('PHIL 377')])])
    newCourse.head.child.addItem([orNode([Node('CPSC 219'), Node('CPSC 233'), Node('CPSC 235')])])

    userCourseList.append(newCourse)
    # print(newCourse.smallToString(newCourse.head))
    # newCourse.nodeList = newCourse.parse(newCourse.head)

    newCourse.refresh()

    for  i in newCourse.nodeList:
        if i.course == 'CPSC 233':
            i.child = Node('CPSC 231')
        if i.course == 'CPSC 219':
            i.child = Node('CPSC 217')
    newCourse.refresh()

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
        elif num == 2:
            editCourse()
        elif num == 3:
            deleteCourse()
        elif num == 4:
            print('Goodbye')
            exit(1)
