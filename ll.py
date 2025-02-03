class LinkedList:

    def __init__(self, val, next=None, prev=None) -> None:
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self) -> str:
        return str(self.val)



head = tail = LinkedList(10)
a = LinkedList(11)
b = LinkedList(12)
c = LinkedList(13)

head.next = a
a.next = b
b.next = c


def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr))
        curr = curr.next
    print('->'.join(elements))


display(head)


# def insert_at_beginning(head, tail, val):
#     newnode = LinkedList(val, next=head)
#     head.prev = newnode
#     return newnode, tail


# head, tail = insert_at_beginning(head, tail, 9)
# head, tail = insert_at_beginning(head, tail, 8)
# head, tail = insert_at_beginning(head, tail, 7)

# print('==== LinkedList After inserting at beginning =====')
# display(head)


# def insert_at_end(head, tail, val):
#     new_node = LinkedList(val, prev=tail)
#     tail.next = new_node
#     return head, new_node


# head, tail = insert_at_end(head, tail, 11)
# head, tail = insert_at_end(head, tail, 12)
# head, tail = insert_at_end(head, tail, 13)
# head, tail = insert_at_end(head, tail, 14)
# head, tail = insert_at_end(head, tail, 15)

# print('==== LinkedList After inserting at End =====')
# display(head)


# def search(head, val):
#     curr = head
#     while curr:
#         if curr.val == val:
#             return True
#         curr = curr.next

#     return False
# print(search(head, 16))


# def iterate_till_value(head,value):
#     curr = head
#     val = value
#     l = []
#     while curr:
#         if curr.val <= val:
#             l.append(str(curr))
#         curr = curr.next
#     print('->'.join(l))
# iterate_till_value(head,value=12)


# display(head)


# def insert(after,val):
#     new_node = LinkedList(val)
#     after = new_node.prev
#     return after,new_node

# insert(11,200)
# display(head)

