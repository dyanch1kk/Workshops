from intersection import Node, intersection

# A = [4,1,8,4,5]
# B = [5,6,1,8,4,5]

com = Node(1)
com.next = Node(8)
com.next.next = Node(4)
com.next.next.next = Node(5)

pA = Node(4)
pA.next = com

pB = Node(5)
pB.next = Node(6)
pB.next.next = com

result = intersection(pA, pB)
print(result.val)  