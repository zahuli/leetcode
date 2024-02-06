# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/

class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None


class List:
    def __init__(self):
        self.head = None

    def listprint(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next


def createList(l):
    if l == []:
        return List()

    HeadVal = List()
    HeadVal.head = Node(l[0])
    if len(l) > 1:
        for item in range(1, len(l)):
            currentNode = Node(l[item])
            if item == 1:
                HeadVal.head.next = currentNode
                prev = currentNode
            else:
                prev.next = currentNode
                prev = currentNode

    return HeadVal


l = [1, 2, 5, 6, 7, 10, 11, 14, 20, 34, 56]

lista = createList(l)
lista.listprint()
print(type(lista))
