class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def insert_start(self, value):
        test = Node(value)
        if self:
            test.next = self
        return test

    def insert_end(self, value):
        test = self
        while test.next:
            test = test.next
        test.next = Node(value)

    def count(self):
        test = self
        count = 0
        while test:
            count = count + 1
            test = test.next
        return count

    def display(self):
        test = self
        while test:
            print(test.value)
            test = test.next

    def segregate_even_odd(self):
        count = 0
        test = self
        test1 = None
        test2 = None
        while test:
            count = count + 1
            temp = test
            test = test.next
            temp.next = None
            if count % 2:
                if not test1:
                    test1 = temp
                else:
                    test3=test1
                    while test3.next:
                        test3 = test3.next
                    test3.next = temp
            else:
                if not test2:
                    test2 = temp
                else:
                    test4=test2
                    while test4.next:
                        test4 = test4.next
                    test4.next = temp
        print("Odd nodes")
        test1.display()
        print("Even Nodes")
        test2.display()


if __name__ == "__main__":
    node = Node(12)
    node = node.insert_start(13)
    node = node.insert_start(15)
    node = node.insert_start(14)
    node = node.insert_start(17)
    node = node.insert_start(19)
    node = node.insert_start(21)
    node.display()
    print("The no of nodes is {0}".format(node.count()))
    node.segregate_even_odd()