class Tech:
    discount=0.5
    total_products=0
    def __init__(self,name,price,weight,color): #instance variable
        self.name=name
        self.price=price
        self.weight=weight
        self.color=color
        Tech.total_products+=1
    #defining methods
    def apply_discount(self):
        self.price=int(self.price-self.price*Tech.discount)
    def calculate_shipping_price(self,rate):
        return f"Shipping cost will be {self.weight*rate}"
    @classmethod
    def get_total_products(cls):
        return "Total products "+str(cls.total_products)
