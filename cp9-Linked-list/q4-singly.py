# find if there are any circular reff in the LL

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class SinglyLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,val,link=False):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else :
            self.tail.next = new_node
            self.tail = new_node
        if link:
            self.tail.next = self.head

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
    
    def find_circular_reff_normal(self):
        reff_set = set()
        cur = self.head

        while cur != None:
            if cur in reff_set:
                return True
            reff_set.add(cur)
            cur = cur.next
        return False
        
    def find_circular_reff_optimized(self):
       fast_pointer = slow_pointer = self.head
       while fast_pointer != None and fast_pointer.next != None:
           fast_pointer = fast_pointer.next
           fast_pointer = fast_pointer.next

           slow_pointer = slow_pointer.next
           if(slow_pointer==fast_pointer):
               return True
           return False

sll = SinglyLL()

sll.append(1)
sll.append(2)
sll.append(3)
sll.append(4)
sll.append(5)

print(sll.find_circular_reff_normal())