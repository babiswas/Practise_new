class Node:
    def __init__(self, data):
        self.value = data
        self.next = None

    def display(self):
        test = self
        while test:
            print(test.value)
            test = test.next

    def get_values(self, l):
        test = self
        while test:
            l.append(test.value)
            test = test.next

    def insert_first(self, value):
        test = Node(value)
        if self:
            test.next = self
        return test


def intersection_nodes(node1, node2):
    list1 = []
    list2 = []
    node3 = None
    node1.get_values(list1)
    node2.get_values(list2)
    if len(list1) > len(list2):
        for i, j in enumerate(list1):
            if j in list2:
                if not node3:
                    node3 = Node(j)
                    test = node3
                else:
                    test.next = Node(j)
                    test = test.next
        return node3
    else:
        for i, j in enumerate(list2):
            if j in list1:
                if not node3:
                    node3 = Node(j)
                    test = node3
                else:
                    test.next = Node(j)
                    test = test.next
        return node3


if __name__ == "__main__":
    print("The first list:")
    node = Node(10)
    node = node.insert_first(12)
    node = node.insert_first(13)
    node = node.insert_first(14)
    node = node.insert_first(15)
    node = node.insert_first(16)
    node = node.insert_first(17)
    node.display()
    print("The second list")
    node1 = Node(25)
    node1 = node1.insert_first(21)
    node1 = node1.insert_first(20)
    node1 = node1.insert_first(10)
    node1 = node1.insert_first(14)
    node1 = node1.insert_first(17)
    node1.display()
    node3 = intersection_nodes(node, node1)
    print("Displaying the list3")
    node3.display()