class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches

    def is_leaf(self):
        return not self.branches

    def print_tree(self, indent=0):
        print("  " * indent + str(self.label))
        for b in self.branches:
            Tree.print_tree(b, indent + 1)
