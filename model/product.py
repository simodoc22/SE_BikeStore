class Product:
    def __init__(self,id,product_name,category_id):
        self.id = id
        self.product_name = product_name
        self.category_id = category_id

    def __str__(self):
        return str(self.product_name)

    def __hash__(self):
        return hash(self.id)