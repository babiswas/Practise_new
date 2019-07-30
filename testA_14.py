class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def insert_first(self, value):
        test = Node(value)
        if self:
            test.next = self
        return test

    def find_node(self, value):
        test = self
        prev = test
        while test:
            if test.value == value:
                return prev
            prev = test
            test = test.next
        return None

    def display(self):
        test = self
        while test:
            print(test.value)
            test = test.next

    def swap_node(self, value1, value2):
        test1 = self.find_node(value1)
        test2 = self.find_node(value2)
        if (test1 == None) or (test2 == None):
            return
        elif test1==test2:
            return
        elif test1.next==test2:
             temp2=test2.next
             test1.next=temp2
             temp3=temp2.next
             temp2.next=test2
             test2.next=temp3
             return self

        elif test1.value == value1 or test2.value == value2:
            if test1.value == value1:
                temp2 = test2.next
                test2.next = test1
                temp3 = test1.next
                test1.next = temp2.next
                temp2.next = temp3
                return temp2

            if test2.value == value2:
                temp1 = test1.next
                test1.next = test2
                temp3 = test2.next
                test2.next = temp1.next
                temp1.next = temp3
                return temp1

        else:
            temp1 = test1.next
            temp2 = test2.next
            test1.next = temp2
            temp3 = temp2.next
            temp2.next = temp1.next
            test2.next = temp1
            temp1.next = temp3
            return self


if __name__ == "__main__":
    node = Node(10)
    node = node.insert_first(11)
    node = node.insert_first(17)
    node = node.insert_first(19)
    node = node.insert_first(21)
    node = node.insert_first(25)
    node = node.insert_first(27)
    print("Displaying the list")
    node.display()
    print("After swapping values")
    node=node.swap_node(21,19)
    node.display()