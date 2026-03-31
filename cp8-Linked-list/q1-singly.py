# part - 56 - single linked list

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
    
    def insert_at(self,val,pos):
        new_node = Node(val)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return

        cur_pointer = self.head
        cur_count = 0
        while cur_pointer.next != None and cur_count < pos:
            prev_pointer = cur_pointer
            cur_pointer = cur_pointer.next
            cur_count+=1
        
        prev_pointer.next = new_node
        new_node.next = cur_pointer
        return    
    
    def delete(self,val=None):
        if val == None:
            print("value is required to delete")
            return
        is_found = False
        cur_pointer = self.head
        while is_found is False:
            if cur_pointer.val == val:
                is_found = True
                break
            prev_pointer = cur_pointer
            cur_pointer = cur_pointer.next
        prev_pointer.next = cur_pointer.next
        return
        
sll = SinglyLL()

sll.append(1)
sll.append(2)
sll.append(8)
sll.append(4)
sll.append(5)

sll.delete(8)
sll.insert_at(3,2)
sll.traverse()