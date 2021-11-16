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

    def stack_top(self):
        '''
        return stack top
        '''
        if self.top != None:
            return self.top.data
        else:
            return "the list is empty"

    def stack_size(self):
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
            stack_node_list = []
            while node != None:
                stack_node_list.append(node.data)
                node = node.next

            return "\n-------\n".join(stack_node_list)
        else:
            return "the list is empty"

###################################################################################################   
       
# instantiate objects
book1 = Node("Book_01")
book2 = Node("Book_02")
book3 = Node("Book_03")
book4 = Node("Book_04")

# Instantiate stack
stack = Stack()

# stacking objects
stack.push(book1)
stack.push(book2)
stack.push(book3)
stack.push(book4)

# printing the stack
print(stack)

# printing the top of the stack
print("Top of the stack:", stack.stack_top())

# printing the stack size
print("the size of the stack:", stack.stack_size())

# removing an object
stack.pop()

print(stack)

# printing the stack size
print("the size of the stack:", stack.stack_size())