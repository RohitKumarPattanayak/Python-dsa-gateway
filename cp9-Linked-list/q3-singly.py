# reverse the LL 

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class SinglyLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else :
            self.tail.next = new_node
            self.tail = new_node

    def traverse(self):
        cur_pointer = self.head
        if cur_pointer == None:
            print('sl is empty')
            return
        while cur_pointer.next is not None:
            print(cur_pointer.val)
            cur_pointer = cur_pointer.next
        print(cur_pointer.val)
        return
    
    def reverse_stack_based(self):
        stackLL = []
        cur_pointer = self.head
        while cur_pointer != None:
            stackLL.append(cur_pointer.val)
            cur_pointer = cur_pointer.next

        cur_pointer = self.head
        while cur_pointer != None:
            cur_pointer.val = stackLL.pop()
            cur_pointer = cur_pointer.next
        return
        
    def reverse_iterative_mode(self):
        prev = None
        cur = front = self.head
        while front!=None:
            front  = cur.next
            cur.next = prev

            prev = cur     
            cur = front       
        self.head = prev
        return
# 1 -> None
sll = SinglyLL()

sll.append(1)
sll.append(2)
sll.append(3)
sll.append(4)
sll.append(5)

sll.reverse_iterative_mode()
sll.traverse()