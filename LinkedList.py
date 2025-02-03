class Node:
    def __init__(self,val,next=None) -> None:
        self.val = val
        self.next = next


class Linkedlist:
    def __init__(self) -> None:
        self.head = None
        self.n = 0

    ## constant time -> O(1)
    def __len__(self) -> int:
        return self.n

    ## constant time -> O(1)
    def insert_head(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.n += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.n += 1

    ## Linear time -> O(n)
    def insert_tail(self,value):
        curr = self.head
        if self.head == None:
            self.head = new_node
            self.n += 1
            return
        new_node = Node(value)
        while curr.next:
            curr = curr.next
        
        curr.next = new_node
        self.n += 1

    ## Linear time -> O(n)
    def insert(self,after,value):
        curr = self.head
        new_node = Node(value)
        while curr:
            if curr.val == after:
                break
            curr = curr.next
        if curr:
            new_node.next = curr.next
            curr.next =  new_node
            self.n += 1

    ## constant time O(1)
    def clear(self):
        self.head = None
        self.n = 0

    ## Constant time O(1)
    def delete_head(self):
        if self.head == None:
            return 'Empty LinkeList'
        self.head = self.head.next
        self.head -= 1

    ## Linear time -> O(n)
    def pop(self):
        curr = self.head
        if self.head == None:
            return 'Empty LinkeList'
        
        while curr.next:
            curr = curr.next
        
        curr.next = None
    ## Linear time -> O(n)
    def remove(self,value):
        curr = self.head
        while curr.next:
            if curr.next.val == value:
                break
            curr = curr.next
        if curr.next == None:
            return 'Item not Found'
        else:
            curr.next = curr.next.next
        
        self.n -= 1

    ## Linear time -> O(n)
    def search(self,value):
        curr = self.head
        pos = 0
        while curr:
            if curr.val == value:
                return pos
            curr = curr.next
            pos += 1

        return 'item not found'
    
    ## Linear time -> O(n)
    def search_by_index(self,index):
        curr = self.head
        pos = 0
        while curr:
            if pos == index:
                return curr.val
            curr = curr.next
            pos += 1
    
    
    def __str__(self) -> str:
        curr = self.head
        elements = []
        while curr:
            elements.append(str(curr.val))
            curr = curr.next
        return str('->'.join(elements))

if __name__ == '__main__':

    L = Linkedlist()
    L.insert_head(100)
    L.insert_tail(101)
    L.insert_head(99)
    L.insert_tail(102)
    print(L)
    L.insert(101,1000)

    print(len(L))
    print(L)
    L.remove(1000)
    print(L)
    print(len(L))
    print(L.search(100))
    