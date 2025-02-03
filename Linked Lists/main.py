
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



if __name__ == "__main__":
    ls = LinkedList()

    ls.insert_at_beginning(12)
    ls.insert_at_beginning(54)
    ls.insert_at_beginning(76)

    ls.display()

    print(ls.get_middle_element().val)