class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    

class Stack():
    def __init__(self) -> None:
        self.top = None
        self.size = 0

    def push(self, node):
        '''
        add a node to the stack
        '''
        node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        '''
        remove a node from the stack
        '''
        if self.size > 0:
            node = self.top
            self.top = node.next
            self.size -= 1
        else:
            print("the list is empty")

    def size_stack(self):
        '''
        return stack size
        '''
        return self.size
    
    def __str__(self) -> str:
        '''
        returns a string with data about object
        '''
        if self.top != None:
            node = self.top
            list_node_stack = []
            while node != None:
                list_node_stack.append(node.data)
                node = node.next

        return "\n-------\n".join(list_node_stack)
       
# Instaciar nós
node1 = Node("Book_01")
node2 = Node("Book_02")
node3 = Node("Book_03")
node4 = Node("Book_04")

# Instaciar Pilha
stack = Stack()

# Empilhando nós
stack.push(node1)
stack.push(node2)
stack.push(node3)
stack.push(node4)

# Imprimindo a pilha
print(stack)

print()

# Imprimindo o tamanho da lista
print("the size of the stack:", stack.size_stack())

print()

# Removendo um objeto
stack.pop()
print(stack)

print()

# Imprimindo o tamanho da lista
print("the size of the stack:", stack.size_stack())