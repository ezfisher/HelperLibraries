class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self, nodes = None):
        self.head = None
        if nodes is not None:
            node = Node(nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(elem)
                node = node.next
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append('None')
        return ' -> '.join(nodes)
    
    def get_nodes(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        return nodes
    
    def add_first(self, node):
        node.next = self.head
        self.head = node
    
    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node
    
    def add_after(self, target_node_data, new_node):
        if target_node_data is None:
            raise Exception("Target node must not be None")
        
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Target node not found")
    
    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("Target node must not be None")
        
        if self.head.data == target_node_data:
            return self.add_first(Node(new_node_data))
        
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node
        raise Exception("Target node not found")
    
    def remove(self, target_node_data):
        if self.head is None:
            raise Exception("Target should not be None")
        
        if self.head.data == target_node_data:
            self.head = self.head.next
            return
        
        for node in self:
            if node.data == target_node_data:
                prev_node.next = node.next
                return
            prev_node = node
        raise Exception("Target node not found")