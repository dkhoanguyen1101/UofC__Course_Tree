class Node:
    def __init__(self, courseName):
        self.course = courseName
        self.child = None
        self.type = 'NODE'

    def toString(self):
        return self.course



class orNode(Node):
    def __init__(self, courseList):
        self.courses = courseList
        self.type = 'OR'

    def addItem(self, itemList):
        for item in itemList: 
            self.courses.append(item)

    def toString(self):
        toStringList = []
        for course in self.courses:
            toStringList.append(course.toString())
        return ( '(' + "+".join(toStringList) + ')' )

class andNode(Node):
    def __init__(self, courseList):
        self.courses = courseList
        self.type = 'AND'
        
    def addItem(self, itemList):
        for item in itemList:
            self.courses.append(item)

    def toString(self):
        toStringList = []
        for course in self.courses:
            toStringList.append(course.toString())
        return ( '(' + ".".join(toStringList) + ')' )

class nOfNode(Node):
    def __init__(self,number, courseList):
        self.courses = courseList
        self.num = number
        self.type = number + 'OF'
        
    def addItem(self, itemList):
        for item in itemList:
            self.courses.append(item)

    def toString(self):
        toStringList = []
        for course in self.courses:
            toStringList.append(course.toString())
        return ( self.num + '(' + "+".join(toStringList) + ')' )

class course:

    def __init__(self, node):
        self.head = node
        self.nodeList = {self.head}
        self.course = node.course

    def parse(self, node):
        toReturn = set()

        if (node.type in ['AND', 'OR', 'OF']):
            count = 0
            while (count < len(node.courses)):
                toReturn.update( self.parse(node.courses[count]))
                count += 1
        elif (node.type == 'NODE'):
            toReturn.add(node)
            if (node.child != None):
                
                toReturn.update(self.parse(node.child))

        return toReturn
    
    def setAndChild (self, l):
        self.head.child = andNode(l)


    def setOrChild (self, l):
        self.head.child = orNode(l)
        
    
    def setNofChild(self , n, l):
        self.head.child = nOfNode(n, l)
     

    def setChild(self, s):
        self.head.child = s

   



    def smallToString(self, node):
        if node.type =='NODE' and node.child != None:
            return (node.course + '->' + self.head.child.toString())
        else:
            return (node.toString)

    def largeToString(self, node):
        if node.type =='NODE' and node.child != None:
            return (node.course + '->' + self.largeToString(node.child))
        elif node.type =='NODE' and node.child == None:
            return node.course
        elif (node.type in ['AND', 'OR', 'OF']):
            count = 0
            stringList = []
            while (count < len(node.courses)):
                stringList.append( self.largeToString(node.courses[count]))
                count += 1

            if (node.type == 'AND'):
                return ( '(' + ".".join(stringList) + ')' )
            elif (node.type == 'OR'):
                return ( '(' + "+".join(stringList) + ')' )
            elif (node.type == 'OF'):
                return ( '(' + "+".join(stringList) + ')' )

    def fullString(self):
        return self.largeToString(self.head)

        

