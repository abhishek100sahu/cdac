class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, *args):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        if "name" in args:
            print(prefix + self.name)
        elif "designation" in args:
            print(prefix + self.designation)
        else:
            print(prefix + self.name + " (" + self.designation+ ")" )
            
        if self.children:
            for child in self.children:
                child.print_tree(*args)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        
        
def build_product_tree():
    root = TreeNode("Nilupul", "CEO")

    cto = TreeNode("Chinmay", "CTO")
    root.add_child(cto)
    ih = TreeNode("Vishwa", "Infrastructure head")
    cto.add_child(ih)
    cm = TreeNode("Dhaval", "Cloud Manager")
    am = TreeNode("Abhijeet", "App Manager")
    ih.add_child(cm)
    ih.add_child(am)
    ah = TreeNode("Aamir", "Application Head")
    cto.add_child(ah)
    
    hr = TreeNode("Gels", "HR Head")
    root.add_child(hr)
    rm = TreeNode("Peter", "Recruitment Manager")
    pm = TreeNode("Waqas", "Policy Manager")
    hr.add_child(rm)
    hr.add_child(pm)

    

    root.print_tree("name")

if __name__ == '__main__':
    build_product_tree()