#file = '../data/test'
file = '../data/input'

class Node:
    def __init__(self, dataval = None):
        self.value = dataval
        self.next = None
        self.prev = None
 

with open(file) as f:
    inps = [int(line.rstrip()) for line in f.readlines()]

pos_of_zero = None
n = len(inps)


order = []
head = Node(inps[0])
if head.value == 0:
    pos_of_zero = 0
node = head

for i in range(1, len(inps)):
    curr = Node(inps[i])
    if curr.value == 0:
        pos_of_zero = i
    node.next = curr
    curr.prev = node
    order.append(curr)
    node = curr

head.prev = node
node.next = head

order = [head] + order

def move(node):
    if node.value > 0:
        moveForward(node, node.value)
    elif node.value < 0:
        moveBackwards(node, -node.value)

def moveForward(node, iters):
    for _ in range(iters):
        tmp = node.prev
        node.prev = node.next
        node.next = node.next.next
        node.prev.next = node
        node.prev.prev = tmp
        tmp.next = node.prev
        node.next.prev = node


def moveBackwards(node, iters):
    for _ in range(iters):
        tmp = node.next
        node.next = node.prev
        node.prev = node.prev.prev
        node.prev.next = node
        node.next.next = tmp
        tmp.prev = node.next


for node in order:
    move(node)

def findNumbers(node, n):
    one = 1000 - (1000 // n) * n
    two = 2000 - (2000 // n) * n
    three = 3000 - (3000 // n) * n
    a,b,c = None, None, None

    for i in range(n):
        if i == one:
            a = node.value
        if i == two:
            b = node.value
        if i == three:
            c = node.value
        node = node.next
    return a,b,c

a,b,c = findNumbers(order[pos_of_zero], n)

print(a + b + c)