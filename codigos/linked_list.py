class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    

class LinkedList:

    def __init__(self) -> None:
        self.head = None

    def add_node_start_list(self, data) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def add_node_end_list(self, data) -> None:
        new_node = Node(data)

        # Check if the list is empty
        if self.head == None:
            new_node.next = self.head
            self.head = new_node
        else:
            previous_node = self.head
            # Until it finds the last element of the list
            while previous_node.next != None:
                previous_node = previous_node.next
            
            previous_node.next = new_node
            new_node.next = None
    
    def add_node_after_target_node(self, data, target_node) -> None:
        '''
        insert a node after the target node
        '''
        new_node = Node(data)
        node = self.head
        find = False

        while node != None:
            if node.data == target_node:
                new_node.next = node.next
                node.next = new_node
                find = True
                break

            node = node.next

        if not find:
            print ("Target Node: {} not found".format(target_node))


    def remove_node(self, data) -> None:

        node = self.head
        find = False

        # Checks if the first node is the element sought
        if node.data == data:
            self.head = node.next
        else:
            previous_node = node
            node = node.next

        while node != None:
            if node.data == data:   
                previous_node.next = node.next
                find = True
                break
            else:
                previous_node = node
                node = node.next

        if not find:
            print("O nó não foi encontrado")


    
    def __str__(self) -> str:
        list_nodes = []
        node = self.head
        while node is not None:
            list_nodes.append(node.data)
            node = node.next
        list_nodes.append("None")

        return " --> ".join(list_nodes)

##########################################################################################

# Exemplo de uso

# Lista de atividades
# 1 Ir ao banco
# 2 Fazer compras
# 3 Levar carro na oficina
# 4 Estudar matemática

# Instanciando a lista encadeada
Linked_List = LinkedList()

# Adicionando tarefas em ordem de prioridades
Linked_List.add_node_end_list('Ir ao banco')
Linked_List.add_node_end_list('Fazer compras')
Linked_List.add_node_end_list('Levar carro na oficina')
Linked_List.add_node_end_list('Estudar matemática')

# Impressão da lista
print(Linked_List)

# Remover uma tarefa
Linked_List.remove_node('Levar carro na oficina')

# Impressão da lista
print(Linked_List)

# Adicionando uma nova atividade no início da lista
Linked_List.add_node_start_list('Planejamento semanal')

# Impressão da lista
print(Linked_List)

# Adicionando atividade em algum lugar definido na lista
Linked_List.add_node_after_target_node('Aula de programação', "Planejamento semanal")

# Impressão da lista
print(Linked_List)