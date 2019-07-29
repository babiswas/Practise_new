class Node:
   def __init__(self,value):
      self.value=value
      self.next=None
   def insert_start(self,value):
      test=Node(value)
      test.next=self
      return test
   def rev_list(self):
      curr=self
      prev=None
      next=None
      while curr.next:
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
      curr.next=prev
      next=None
      prev=None
      return curr

   def display(self):
      test=self
      while test:
         print(test.value)
         test=test.next




if __name__=="__main__":
   node=Node(12)
   node=node.insert_start(13)
   node=node.insert_start(14)
   node=node.insert_start(15)
   node=node.insert_start(16)
   node=node.insert_start(18)
   node=node.insert_start(19)
   node.display()
   print("Reversing the list")
   node=node.rev_list()
   node.display()

