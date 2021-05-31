class Deque:
    def __init__(self):
        self.items =[]
    def addFront(self,item): #0(n)
        self.items.append(item)
    def addRear(self,item): #0(1)
        self.items.insert(0,item)
        
        #remove front 
    def removeFront(self): #0(n)
        return self.items.pop()
        
        #remove rear
    def removeRear(self): #0(n)
        return self.items.pop(0)
        
        
    def isEmpty(self): #0(1)
        return self.items == []
    def size(self): #0(n)
        return len(self.items)

d = Deque()
print(d.isEmpty())
d.addFront('w')
d.addRear('z')
d.addFront('x')
d.addFront('y')
print(d.size())
print(d.removeFront())
print(d.removeRear())
print(d.isEmpty())
