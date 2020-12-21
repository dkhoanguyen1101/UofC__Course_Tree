from Node import *

if __name__ == '__main__':

    newCourse = course(Node('CPSC 313'))
    newCourse.setAndChild([])
    newCourse.head.child.addItem([orNode([Node('MATH 271'), Node('MATH 273')])])
    newCourse.head.child.addItem([orNode([Node('PHIL 279'), Node('PHIL 377')])])
    newCourse.head.child.addItem([orNode([Node('CPSC 219'), Node('CPSC 233'), Node('CPSC 235')])])


    # print(newCourse.smallToString(newCourse.head))
    newCourse.refresh()

    for  i in newCourse.nodeList:
        
        if i.course == 'CPSC 233':
            i.child = Node('CPSC 231')
        if i.course == 'CPSC 219':
            i.child = Node('CPSC 217')
    
    print(newCourse.fullString())
    
    # print(newCourse.allNodeToString())
