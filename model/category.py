class Category:
    def __init__(self,id,name):
        self.id = id
        self.name = name

    def __str__(self):
        return self.name
    def __hash__(self):
        return hash(self.id)