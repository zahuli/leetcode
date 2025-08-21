# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/

# recursion

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
    if not list1:
        return list2
    if not list2:
        return list1

    if list1.val < list2.val:
        list1.next = mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoLists(list1, list2.next)
        return list2


l1 = [1, 2, 4, 5, 8, 11]
l2 = [1, 3, 4, 7, 8, 9, 12, 14, 15]
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
