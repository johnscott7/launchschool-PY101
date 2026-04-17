class Tree:
    def __init__(self):
        self.type = "Generic Tree"

class Pine(Tree):
    def __init__(self):
        super().__init__()
        self.type = "Pine Tree"

# When an instance of Pine is created,
# what value will its type attribute have? Why?

# It should have the type "Pine Tree" as that should
# overwrite the value initialized from the 
# inherited Tree class.