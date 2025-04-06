# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def createList(self, arr: list):
        head = ListNode(-1)
        curr = head
        for node in arr:
            temp = ListNode(node)
            curr.next = temp
            curr = curr.next
        
        return head.next

class DoublyListNode:
    def __init__(self, value, prev=None, next=None):
        self.val = value
        self.prev = prev
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = ListNode(-1) #dummy head node

class DoublyLinkedList:
    def __init__(self):
        self.head = DoublyListNode(-1, -1)
        self.tail = DoublyListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head