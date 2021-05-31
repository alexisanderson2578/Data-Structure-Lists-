class Node:
    def __init__(self,value):
        self.item = value
        self.nextNode = None 
        self.prevNode = None  
    def __str__(self):
        return str(self.item)
    def getValue(self):
        return self.item
    def setValue(self, value):
        self.item = value    
    def getNext(self):
        return self.nextNode
    def getPrev(self):
        return self.prevNode
    def setNext(self, node):
        self.nextNode = node
    def setPrev(self,node):
        self.prevNode = node
    
     
class Doubly_Linked_List:
    def __init__(self):
        self.head = None 
        self.tail = None
        
      
    def add(self, new):
        newnode = Node(new)
        if self.head == None:
            self.head = newnode
            self.tail = newnode
        else:
            oldnode = self.head
            oldnode.setPrev(newnode)
            newnode.setNext(oldnode)
            self.head = newnode
        
        
    def search(self,value):
        searchNode = self.head
        while (searchNode is not None):
            if (searchNode.getValue() == value):
                return True
            searchNode = searchNode.getNext()
        return False
        

    def remove(self, value):
        currentnode = self.head
        while(currentnode is not None and currentnode.getValue() != value):
            currentnode = currentnode.getNext()
        if currentnode == None:
            raise Exception('not found')
        else:
            prevnode = currentnode.getPrev()
            nextnode = currentnode.getNext()
            prevnode.setNext(nextnode)
            nextnode.setPrev(prevnode)
    
    
    def isEmpty(self):
        if self.head is None:
            return True 
        else:
            return False
    
    def size(self):
        currentNode = self.head
        count = 0
        while currentNode is not None:
            count += 1
            currentNode = currentNode.getNext()
        return count
        
        
    def append(self, value):
        newnode = Node(value)
        if self.head is None:
            self.head = newnode
            self.tail = self.head
        else:
            newnode.setPrev(self.tail)
            self.tail.setNext(newnode)
            self.tail = newnode
        
       
    def index(self,value):
        if self.head.getValue() == value:
            return 0
        cur = self.head
        index = 0
        while cur.getNext() != self.tail:
            if cur.getValue() == value:
                return index
            cur = cur.getNext()
            index += 1
        if cur.getValue() == value:
            return index
        else:
             raise Exception("not found")
        
                
    def insert(self,pos, value):
        if self.size() < pos + 1 :
             raise Exception("list too short")
        if pos == 0: 
            self.add(value)
        else: 
            currentNode = self.head
            newNode = Node(value)
            for i in range (pos):
                currentNode = currentNode.getNext()
            prevNode = currentNode.getPrev()
            prevNode.setNext(newNode)
            newNode.setNext(currentNode)
         
        
    def pop1(self):
        if self.head is None:
            raise Exception("List is empty.")
        cur = self.head
        while cur.getNext() != self.tail:
            cur = cur.getNext()
        prev = cur.getPrev()
        prev.setNext(None)
        #self.head.setPrev(prev)
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
            index = 0
            while (cur.getNext() is not None):
                if (index == pos):
                    prev = cur.getPrev()
                    prev.setNext(cur.getNext())
                    return cur.getValue()
                cur = cur.getNext()
                index += 1
            if index == pos:
                prev = cur.getPrev()
                prev.setNext(None)
                return cur.getValue()
        
        
    def printList(self):
        curNode = self.head
        while (curNode.getNext() is not None):
            print(curNode.getValue())
            curNode = curNode.getNext()
        print(curNode.getValue())
        
        
            
            
l = Doubly_Linked_List()


l.add(1)
l.add(2)
l.add(1234)
l.add(4)
l.add(9)
#l.remove(1)
#print(l.search(2))
#print(l.isEmpty())
#print(l.size())
#print(l.index(4))
#l.printList()
#print(l.insert1(2,'r'))

l.append("fgg")
print(l.pop1())
#l.pop(1)
l.printList()
#print(l.pop(3))
#l.pop(2)
