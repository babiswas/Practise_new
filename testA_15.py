class Node:
   def __init__(self,value):
       self.value=value
       self.next=None
   def insert_first(self,value):
       test=Node(value)
       if self:
         test.next=self
       return test
   def display(self):
       test=self
       while test:
         print(test.value)
         test=test.next
   def find_mid_element(self):
       test=self
       test1=self
       while (test1):
          test=test.next
          if not test1.next:
              test1=test1.next
          else:
              test1=test1.next.next
       print(test.value)

if __name__=="__main__":
   node=Node(12)
   node=node.insert_first(13)
   node=node.insert_first(14)
   node=node.insert_first(15)
   node=node.insert_first(16)
   node=node.insert_first(17)
   node=node.insert_first(18)
   node=node.insert_first(19)
   node.display()
   print("The mid element of the list is:")
   node.find_mid_element()
   
       