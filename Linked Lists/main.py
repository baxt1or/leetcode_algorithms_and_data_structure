class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return
        
        last = self.head

        while last.next:
            last = last.next
        last.next = new_node
        

    def print_values(self):
        current = self.head

        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")
    
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
    def remove_dupl(self):
        current = self.head

        while current is not None and current.next is not None:
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next
        
        return self.head

if __name__ == "__main__":
    ls = LinkedList()

    ls.append(12)
    ls.append(54)
   

    ls.print_values()

    