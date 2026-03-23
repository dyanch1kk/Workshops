class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def intersection(pA, pB):
    a, b = pA, pB
    while a != b:
        a = a.next if a else pB
        b = b.next if b else pA
    return a