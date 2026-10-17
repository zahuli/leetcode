# https://leetcode.com/problems/add-two-numbers/submissions/2174459575/
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]


class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def listprint(list):
    while list is not None:
        print(list.val)
        list = list.next


def createlist(niz):
    if not niz:
        return None
    head = ListNode(niz[0])
    cur = head
    for i in range(1, len(niz)):
        cur.next = ListNode(niz[i])
        cur = cur.next  # ovo mi je falilo
    return head


def addTwoNumbers(l1, l2):
    """
    :type l1: Optional[ListNode]
    :type l2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """

    p = 0
    head = ListNode()
    cur = head
    while (l1 is not None) or (l2 is not None):
        a = (l1.val if l1 != None else 0)
        b = (l2.val if l2 != None else 0)
        cur.val = (a+b+p if (a+b+p) // 10 == 0 else (a+b+p) % 10)

        p = (1 if (a+b+p) >= 10 else 0)
        if (l1 is not None):
            l1 = l1.next

        if (l2 is not None):
            l2 = l2.next

        if (l1 != None) or (l2 != None) or p:
            cur.next = ListNode()
            cur = cur.next
            cur.val = (p if p else 0)
    return head


# niz1 = [2, 4, 3]
# niz2 = [5, 6, 4]

# niz1 = [8]
# niz2 = [7]

# niz1 = [0]
# niz2 = [0]

niz1 = [9, 9, 9, 9]
niz2 = [9, 9, 9, 9, 9, 9, 9]


# niz1 = [3, 4, 5]
# niz2 = [1, 7, 9, 8, 2]

lis1 = createlist(niz1)
lis2 = createlist(niz2)

# listprint(lis1)
# listprint(lis2)

listprint(addTwoNumbers(lis1, lis2))
