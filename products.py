class Product:
    def __init__(self,index,code,description,quantity):
        self.id = index
        self.code = code
        self.description = description
        self.quantity = quantity

    def __str__(self):
        return f"Id: {self.id}, Code: {self.code}, Description: {self.description}, Quantity: {self.quantity}"    