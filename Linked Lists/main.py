
# Creating the Node class Data Structure
class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None


# Implementing the Linked List 
class LinkedList:
    def __init__(self):
        self.head = None
    
    def display(self):
        """ Prints the whole Linked List """
        current = self.head

        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")
    
    def insert_at_beginning(self, data):
        """ Inserts at beginning of the list """
        new_node = Node(val=data)
        new_node.next = self.head
        self.head = new_node
    
    def get_middle_element(self):
        slow = fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def remove_existing_nums(self, nums):
       
        while self.head and self.head.val in nums:
            self.head = self.head.next
        
        current = self.head
        prev = None

        while current:

            if current.val in nums:
                prev.next = current.next
            else:
                prev = current
            current = current.next

        return self.head
    
    def get_node_index(self, target):
        current = self.head
        index = 0

        while current:
            if current.val == target:
                return index
            current = current.next
            index+=1
        return -1
    
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev



if __name__ == "__main__":
    ls = LinkedList()

    ls.insert_at_beginning(1)
    ls.insert_at_beginning(2)
    ls.insert_at_beginning(3)
    ls.insert_at_beginning(4)
    ls.insert_at_beginning(5)
    ls.insert_at_beginning(6)
    ls.insert_at_beginning(7)

    ls.display()

    ls.reverse()

    ls.display()