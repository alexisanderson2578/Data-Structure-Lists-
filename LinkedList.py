class Node:
    def __init__(self,value):
        self.item = value
        self.nextNode = None 
        
    def getValue(self):
        return self.item
    
    def setValue(self, value):
        self.item = value
        
    def getNext(self):
        return self.nextNode
    
    def setNext(self, node):
        self.nextNode = node

class Linked_List:
    def __init__(self):
        self.head = None 
        
    def add(self, new):
        newnode = Node(new)
        newnode.setNext(self.head)
        self.head = newnode 
        
    def search(self,value):
        currentnode = self.head
        find = False
        while currentnode is not None and not find:
            if currentnode.getValue() == value:
                find = True
            else:
                currentnode = currentnode.getNext()
        return find


    
    def remove(self,value):
        currentnode = self.head
        prev = None
        find = False
        if currentnode is None:
            raise Execption("Empty list")
        while not find:
            if currentnode.getValue() == value:
                find = True
            else:
                prev = currentnode
                currentnode = currentnode.getNext()
        if prev is None:
            self.head = currentnode.getNext()
        else:
            prev.setNext(currentnode.getNext())    
    
    
    def isEmpty(self):
        if self.head is None:
            return True 
        else:
            return False
    
    def size(self):
        currentnode = self.head
        count = 0
        while currentnode is not None:
            count += 1
            currentnode = currentnode.getNext()
        return count
        
        
    def append(self, value):
        newnode = Node(value)
        if self.head is None:
            self.head.setValue(value)
        else:
            addEnd = self.head
            while(addEnd.nextNode is not None):
                addEnd = addEnd.getNext()
            addEnd.nextNode = newnode
    

        
    def index(self,value):
        if self.head.getValue() == value:
            return 0
        cur = self.head
        index = 0
        while cur.getNext() is not None:
            if cur.getValue() == value:
                return index
            cur = cur.getNext()
            index += 1
        if cur.getValue() == value:
            return index
        
    def insert(self,pos, value):
        if self.size() < pos +1 :
             raise Exception("list too short")
        if pos == 0: 
            self.add(value)
        else: 
            currentNode = self.head
            newNode = Node(value)
            for i in range (pos):
                prevNode = currentNode
                currentNode = currentNode.getNext()
            prevNode.nextNode = newNode
            newNode.nextNode = currentNode
         
    def pop1(self):
        if self.head is None:
            raise Exception("List is empty.")
        cur = self.head
        prev = cur
        while cur.getNext() is not None:
            prev = cur
            cur = cur.getNext()
        prev.next = None
        return cur.getValue()
           
    def pop(self, pos):
        if self.size() < pos + 1:
            raise Exception("Cannot pop from position that does not exist.")
        if pos == 0:
            value = self.head.getValue()
            self.head = self.head.getNext()
            return value
        else:
            cur = self.head
            prev = cur
            index = 0
            while (cur.getNext() is not None):
                if (index == pos):
                    prev.setNext(cur.getNext())
                    return cur.getValue()
                prev = cur
                cur = cur.getNext()
                index += 1
            if index == pos:
                prev.setNext(None)
                return cur.getValue()
        
    def printList(self):
        curNode = self.head
        while (curNode.getNext() is not None):
            print(curNode.getValue())
            curNode = curNode.getNext()
        print(curNode.getValue())
    
    
l = Linked_List()

l.add(1)
l.add(2)
l.add(1234)
l.add(4)
#l.remove(1)
#print(l.search(2))
#print(l.isEmpty())
#print(l.size())
#print(l.index(4))
#l.printList()
#print(l.insert(2,'r'))

#l.append("fgg")
print(l.pop1())
#l.pop(1)
#l.printList()
#print(l.pop(3))
#l.pop(2)
