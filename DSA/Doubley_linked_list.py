class Node:
	def __init__(self,data):
		self.previous = None
		self.data = data
		self.next = None


class Doublie_Linked_list:

	def __init__(self):
		self.head = None

	def append(self,data):

		new_node = Node(data)
		if not self.head:
			self.head = new_node
			return

		current_node = self.head
		while current_node.next:
			current_node = current_node.next

		current_node.next = new_node
		new_node.previous = current_node

	def display(self):
		current_node = self.head

		while current_node:
			print(current_node.data,end=" <-> ")
			current_node = current_node.next
		print()

	def delete(self,data):
		if self.head.data == data:
			self.head = self.head.next
			if self.head:
				self.head.previous = None
			return
		current_node = self.head
		prevoius_node = None
		while current_node.next and current_node.data != data:
			prevoius_node = current_node
			current_node = current_node.next
		prevoius_node.next = current_node.next
		if current_node.next:
			current_node.next.previous = prevoius_node
	def display_backward(self):
		current_node = self.head
		if not current_node:
			print("List is empty.")
			return

		while current_node.next:
			current_node = current_node.next

		while current_node:
			print(current_node.data, end=" <-> ")
			current_node = current_node.previous
		print("None")

	def insert(self,key,value):
		count = 0
		new_node = Node(value)
		current_node = self.head
		previous_node = Node
		if count == key:
			new_node.next = self.head
			self.head.previous = new_node
			self.head = new_node
			return
		while current_node.next and count !=key:
			previous_node = current_node
			current_node = current_node.next
			count = count+1
		if not current_node.next:
			current_node.next = new_node
			new_node.previous = current_node
		else:
			previous_node.next = new_node
			current_node.previous = new_node
			new_node.next = current_node
			new_node.previous = previous_node



DLL = Doublie_Linked_list()
DLL.append(23)
DLL.append(45)
DLL.append(48)
DLL.append(87)
DLL.append(76)
DLL.append(56)
DLL.append(67)
DLL.display()
DLL.insert(8,96)
DLL.display_backward()