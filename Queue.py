class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self,item): #0(1)
        self.items.append(item)
    def dequeue(self): #0(n)
        return self.items.pop(0)
    def isEmpty(self):  #0(1)
        return self.items == []
    def size(self): #0(n)
        return len(self.items)
    
q = Queue()
print(q.isEmpty())
q.enqueue('yes')
q.enqueue('no')
q.enqueue('ok')
print(q.isEmpty())
print(q.size())
