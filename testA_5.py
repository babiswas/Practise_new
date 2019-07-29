class Node:
   def __init__(self,value):
      self.value=value
      self.next=None
   def insert_end(self,value):
       test=self
       while test.next:
         test=test.next
       test.next=Node(value)
   def insert_start(self,value):
       test=Node(value)
       test.next=self
       return test
   def display(self):
       test=self
       while test:
         print(test.value)
         test=test.next

if __name__=="__main__":
   node=Node(13)
   node.insert_end(14)
   node.insert_end(16)
   node.insert_end(17)
   node.insert_end(19)
   node.insert_end(21)
   node.insert_end(32)
   node=node.insert_start(33)
   node=node.insert_start(34)
   node.display()

#The results are 
#34,33,13,14,16,17,19,21,32