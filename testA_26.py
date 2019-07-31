class Node:
   def __init__(self,value):
       self.value=value
       self.next=None
   def display(self):
       test=self
       while test:
          print(test.value)
          test=test.next
   def insert_first(self,value1):
       test=Node(value1)
       if self:
         test.next=self
       return test
   def get_node_values(self,l):
      test=self
      while test:
         l.append(test.value)
         test=test.next

def intersection_list(node1,node2):
    list1=[]
    list2=[]
    node3=None
    if node1 and node2:
       node1.get_node_values(list1)
       node2.get_node_values(list2)
       print(list1)
       print(list2)
       if len(list1)>=len(list2):
          for i in list1:
             if i in list2:
                if not node3:
                   node3=Node(i)
                   test=node3
                else:
                   test.next=Node(i)
                   test=test.next
          return node3
       else:
          for i in list2:
             if i in list1:
                if not node3:
                   node3=Node(i)
                   test=node3
                else:
                   test.next=Node(i)
                   test=test.next
          return node3

if __name__=="__main__":
   node=Node(10)
   node=node.insert_first(12)
   node=node.insert_first(14)
   node=node.insert_first(17)
   node=node.insert_first(19)
   node=node.insert_first(21)
   node=node.insert_first(23)
   node=node.insert_first(25)
   print("Displaying the first list")
   node.display()
   node1=Node(8)
   node1=node1.insert_first(12)
   node1=node1.insert_first(17)
   node1=node1.insert_first(16)
   node1=node1.insert_first(34)
   node1=node1.insert_first(19)
   node1=node1.insert_first(11)
   node1=node1.insert_first(6)
   print("Displaying the first list")
   node1.display()
   print("Displaying the common nodes")
   node3=intersection_list(node,node1)
   node3.display()
   
   
   
 

       