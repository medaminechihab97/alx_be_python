class Product:
    def __init__(self, name , price , quantity) :
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_value(self):
        print(f"The totale value of {self.name} available in the stock is {self.price * self.quantity}")


product1 = Product("adidas" , 250 , 20)
product2 = Product("nike" , 160 , 60)
product1.calculate_value()
product2.calculate_value()
