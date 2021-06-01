class HashList:
    listlength = None
    hlist=[]

    def __init__(self,length):
        self.listlength = length
        self.hlist = [None]*length

    def hashfunction(self,item):
        return item% self.listlength

    def put(self,item):
        slot = self.hashfunction(item)
        counter=0

        while(self.hlist[hvalue]is not None):
            slot +=1
            slot %=self.listlength
            counter+=1

            if(counter==self.listlength):
                raise Exception("List is Full")
        self.hlist[slot]=item
  
    def contains(self,item):
        slot = self.hashfunction(item)
        counter = 0

        while(self.hlist[slot] is not None):

            if(self.hlist[slot]==item):
                return True

            else:
                slot +=1#slot 
                slot %=self.listlength #resets to remainder 
            counter+=1
# if each value equals the length of the list reset the value to zero 
            if(counter==self.listlength):
                return False
            
    def items(self):
        print(self.hlist)

h = HashList(20)
h.put(11)
h.items()
h.put(23)
h.put(1)
h.put(44)
h.put(84)
h.put(12)
h.put(0)
h.put(46)
h.put(123)
h.put(63)
h.items()
print(h.contains(123))
print(h.contains(63))
print(h.contains(100))
