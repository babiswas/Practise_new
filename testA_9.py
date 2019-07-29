class Node:
   def __init__(self,value):
       self.value=value
       self.next=None
   def display(self):
      test=self
      while test:
         print(test.value)
         test=test.next
   def insert_start(self,value):
       test=Node(value)
       if self:
          test.next=self
       return test
   def find_intersection_point(self,node2):
       test1=self
       test2=node2
       m=[]
       while test1:
          m.append(test1)
          test1=test1.next
       while test2:
         if test2 in m:
           print("test2 is intersection point {}".format(test2.value))
           break
         else:
           test2=test2.next
       
       
   def find_node(self,value):
      test=self
      while test:
        if test.value==value:
            return test
        else:
            test=test.next
        
       

if __name__=="__main__":
   node=Node(7)
   node=node.insert_start(3)
   node=node.insert_start(6)
   node=node.insert_start(9)
   node=node.insert_start(15)
   node=node.insert_start(30)
   node1=Node(10)
   test1=node.find_node(9)
   node1.next=test1
   print("Displaying the second list")
   node1.display()
   print("Displaying the first list")
   node.display()
   print("displaying the intersection of nodes")
   node.find_intersection_point(node1)

   
   
   
       