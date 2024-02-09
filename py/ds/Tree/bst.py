class BinarySearchTree:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, child):
        # We've to simply return if data is already present in the tree
        if child.data == self.data:
            return

        if child.data < self.data:
            # Add to the left child

            # Call the function untill we reach to the left child
            if self.left:
                self.left.add_child(child)
            else:
                self.left = child
        else:
            # Add to the right child

            # Call the function untill we reach to the left child
            if self.right:
                self.right.add_child(child)
            else:
                self.right = child

    def in_order_traversal(self):
        elements = []
        # left
        if self.left:
            elements += self.left.in_order_traversal()
        # root

        elements.append(self.data)

        # right
        if self.right:
            elements += self.right.in_order_traversal()

        return elements


    def pre_order_traversal(self):
        # root
        elements = [self.data]
        
        # left
        if self.left:
            elements += self.left.in_order_traversal()
        

        # right
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []
        
        # left
        if self.left:
            elements += self.left.in_order_traversal()
        

        # right
        if self.right:
            elements += self.right.in_order_traversal()
            
        # root
        elements.append(self.data)

        return elements
    
    def search(self, value):
        # root
        if self.data == value:
            return True
        # left
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        # right
        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def calculate_sum(self):
        # recursively call left node
        if self.left:
            left_sum = self.left.calculate_sum()
        # no left Node
        else:
            left_sum = 0
        
        # recursively call left node
        if self.right:
            right_sum = self.right.calculate_sum()
        # no right Node
        else:
            right_sum = 0

        # whatever 
        return self.data + left_sum + right_sum


    def delete(self, value):
        # recursively call left node
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
                
        # recursively call right node
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        
        else:
            # deleting leaf Node
            if self.left is None and self.right is None:
                return None
            # deleting Node having single child
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            
            # deleting Node having two child
            
            # finding minimum value for right subtree / maximum value for left
            min_val = self.right.find_min()
            # replacing data with minimum value found
            self.data = min_val
            # 
            self.right = self.right.delete(min_val)
            print("replacing: ", self.right.in_order_traversal())
            
        return self


def build_tree(elements):
    print("Building tree with these elements:", elements)
    root = BinarySearchTree(elements[0])

    for i in range(1, len(elements)):
        root.add_child(BinarySearchTree(elements[i]))

    return root


if __name__ == "__main__":
    # countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    # country_tree = build_tree(countries)

    # print("Country: ", country_tree.in_order_traversal())
    # print("UK is in the list? ", country_tree.search("UK"))
    # print("Sweden is in the list? ", country_tree.search("Sweden"))

    # print(country_tree.find_min())
    # print(country_tree.find_max())

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    # print(numbers_tree.calculate_sum())
    print(numbers_tree.in_order_traversal())
    print("after: ",numbers_tree.delete(20).in_order_traversal())
    print(numbers_tree.in_order_traversal())
    # print(numbers_tree.pre_order_traversal())
    # print(numbers_tree.post_order_traversal())
