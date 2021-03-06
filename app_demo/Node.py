class Node:
    def __init__(self, courseName):
        self.course = courseName
        self.child = None
        self.type = 'NODE'

    def setChild(self, node):
        self.child = node


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
    

    
    def refresh(self):
        self.nodeList = self.parse(self.head)

    

    
    def setAndChild (self,node, l):
        
        node.setChild(andNode(l))
        self.refresh()


    def setOrChild (self,node, l):
        node.setChild(orNode(l))
        self.refresh()
        
    
    def setNofChild(self , node, n, l):
        node.setChild(nOfNode(n, l))
        self.refresh()
     

    def setChild(self,node, s): 
        node.setChild(s)
        self.refresh()

    def smallToString(self, node):
        self.refresh()
        if node.type =='NODE' and node.child != None:
            return (node.course + '->' + node.child.toString())
        else:
            return (node.toString())
    

    def largeToString(self, node):
        self.refresh()
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
        self.refresh()
        return self.largeToString(self.head)
    
    def allNodeToString(self):
        self.refresh()
        toReturn = list()
        for i in self.nodeList:
            toReturn.append(i.toString())
        return toReturn
    
    def allNodeSmallToString(self):
        self.refresh()
        toReturn = list()
        for i in self.nodeList:
            toReturn.append(self.smallToString(i))
        return toReturn
    
    def findNode(self, aString):
        self.refresh()
        for i in self.nodeList:
            if i.course == aString:
                return i
        return None


        

