#file = '../data/test'
file = '../data/input'

class Node:
    def __init__(self, dataval = None):
        self.value = dataval
        self.next = None
        self.prev = None

dec_key = 811589153

with open(file) as f:
    inps = [int(line.rstrip()) * dec_key for line in f.readlines()]

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
        moveForward(node, node.value % (n-1))
    elif node.value < 0:
        moveBackwards(node, -node.value % (n-1))

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
        node.next.prev = node
        node.next.next = tmp
        tmp.prev = node.next

for _ in range(10):
    for node in order:
        move(node)

def findNumbers(node):
    one = 1000 - (1000 // n) * n
    two = 2000 - (2000 // n) * n
    three = 3000 - (3000 // n) * n
    a,b,c = None, None, None

    for i in range(max(one+1, two+1, three+1)):
        if i == one:
            a = node.value
        if i == two:
            b = node.value
        if i == three:
            c = node.value
        node = node.next
    return a,b,c

def findNumber(node, value):
    for i in range(n):
        if node.value == value:
            return i, True
        node = node.next
    return i, False

def findSpecificNumbers(node, a, b, c):
    one, two, three = None, None, None
    for i in range(n):
        if node.value == a:
            one = i
        if node.value == b:
            two = i
        if node.value == c:
            three = i
        if all((one, two, three)): break
        node = node.next
    return one, two, three
        

a,b,c = findNumbers(order[pos_of_zero])

print(a,b,c)
print(a + b + c)