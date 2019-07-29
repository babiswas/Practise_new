class Node:
   def __init__(self,value):
      self.value=value
      self.next=None
   def insert_end(self,value):
       test=self
       while test.next:
         test=test.next
       test.next=Node(value)
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
   node.display()

        
         