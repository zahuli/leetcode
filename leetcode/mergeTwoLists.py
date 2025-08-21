# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# just to build list for testing


def build_linked_list(arr):
    if not arr:  # empty array
        return None
    head = ListNode(arr[0])  # create head node
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


def mergeTwoLists(list1, list2):
    current = head = ListNode()  # dummy node
    while list1 and list2:  # it compares node values, takes lower value and moves to the next node in that list
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next  # it needs to go through merged list

    if list1 or list2:  # if the lists are empty or it went to the end of one of the lists
        current.next = list1 if list1 else list2

    return head.next


l1 = [1, 2, 4]
l2 = [1, 3, 4]
list1 = build_linked_list(l1)
list2 = build_linked_list(l2)

l3 = mergeTwoLists(list1, list2)

curr = l3
while curr:
    if curr.next:
        print(curr.val, end=" -> ")
    else:
        print(curr.val)   # last element, no arrow
    curr = curr.next
