class Node:
	def __init__(self,Data):
		self.data = Data
		self.next = None

class linked_list:
	def __init__(self):
		self.head = None
	def Append(self,Data):
		new_node = Node(Data)
		if not self.head:
			self.head = Node(Data)
			return
		last_node = self.head
		while last_node.next:
			last_node = last_node.next
		last_node.next = new_node
	def Display(self):
		next_node = self.head
		while next_node:
			print(next_node.data,end=" -> ")
			next_node = next_node.next
		print()

	def delete(self,key):
		current_node = self.head
		if current_node.next and current_node.data == key:
			self.head = current_node.next
		previous_node = None
		while current_node and current_node.data != key:
			previous_node = current_node
			current_node = current_node.next
		previous_node.next = current_node.next

def bubble_sort(linked_list):
    """Sorts the linked list using bubble sort."""
    if linked_list.head is None:
        return  # No need to sort an empty list

    end = None  # Track the end of the sorted portion
    while end != linked_list.head:  # Loop until the entire list is sorted
        current = linked_list.head
        while current.next != end:  # Traverse the list up to the sorted portion
            if current.data > current.next.data:
                # Swap data instead of nodes
                current.data, current.next.data = current.next.data, current.data
            current = current.next
        end = current  # Update the end to the last sorted node
linked_lists = linked_list()
linked_lists.Append(34)
linked_lists.Append(10)
linked_lists.Append(30)
linked_lists.Append(32)
linked_lists.Append(53)
linked_lists.Append(113)
linked_lists.Display()
linked_lists.delete(113)
linked_lists.Display()
linked_lists.Append(3546)
linked_lists.Display()
bubble_sort(linked_lists)
linked_lists.Display()