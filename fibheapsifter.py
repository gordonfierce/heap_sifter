class FibHeap(object):
    def __init__(self):
        self.root_list = []
        self.minimum = None
        self.total_nodes = 0

    class Node(object):
        def __init__(self, item):
            self.item = item
            self.parent = None
            self.children = []
            self.marked = False

        @property
        def order(self):
            return len(self.children)

        def __lt__(self, other):
            return self.item < other.item

        def __gt__(self, other):
            return self.item > other.item

        def __repr__(self):
            return self.item.__repr__()
        
        def show_tree(self):
            if self.children:
                return [self.item, [item.show_tree() for item in self.children]]
            else:
                return self.item

    def insert(self, item):
        new_item = self.Node(item)
        self.root_list.append(new_item)
        self.total_nodes += 1
        if not self.minimum:
            self.minimum = new_item
        else:
            if new_item < self.minimum:
                self.minimum = new_item

                
    def extract_minimum(self):
        item = self.minimum.item
        self.delete_min()
        self.total_nodes -= 1
        if self.root_list:
            self.minimum = min(self.root_list)
            self.consolidate()
        else:
            self.minimum = None
        return item

    
    def consolidate(self):
        possible_orders_array = [None] * self.total_nodes
        root_nodes = [node for node in self.root_list]
        for root_node in root_nodes:
            x_node = root_node
            order = x_node.order
            while possible_orders_array[order] != None:
                y_node = possible_orders_array[order]
                if  y_node < x_node:
                    x_node, y_node = y_node, x_node
                self.root_combine(x_node, y_node)
                possible_orders_array[order] = None
                order += 1
            possible_orders_array[order] = x_node
            
    def delete_min(self):
        if self.minimum.children:
            for child in self.minimum.children:
                child.parent = None
            self.root_list.extend(self.minimum.children)
        self.root_list.remove(self.minimum)

    def root_combine(self, root_a, root_b):
        # root_a should always be less than root_b
        self.root_list.remove(root_b)
        root_a.children.append(root_b)
        root_b.parent = root_a

    def decrease_key(self, node):
        if node.parent and node < node.parent:
            parent = node.parent
            self.trim_node(node)
            self.cascading_trim_node(parent)
        if node < self.minimum:
            self.minimum = node

    def trim_node(self, node):
        parent = node.parent
        parent.children.remove(node)
        node.parent = None
        node.marked = False
        

    def cascading_trim_node(self, node):
        parent = node.parent
        if parent is not None:
            if node.mark.d is False:
                node.marked = True
            else:
                self.trim_node(node)
                self.cascading_trim_node(parent)
    
    def show_heap(self):
        return [item.show_tree() for item in self.root_list]


