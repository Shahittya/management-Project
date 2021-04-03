from tech_product import Tech
class Laptop(Tech): #inherit the Tech class
    def __init__(self,name,price,weight,color,ram,cpu,storage):
        super().__init__(name,price,weight,color)
        self.ram=ram
        self.cpu=cpu
        self.storage=storage
    def set_double_price(self):
        self.price=2*self.price
    def change_specs(self,ram,storage): #if the ram(random access memory) or storage is self customized then price will be increasing linearly
        if ram>self.ram or storage>self.storage:
            self.price=self.price+1000088
        self.ram=ram
        self.storage=storage
    def __str__(self):
         return f"Name:{self.name} \n Price:{self.price}\n Weight:{self.weight}\n" \
               f"Color:{self.color}\n Ram:{self.ram}\n C.P.U:{self.cpu} Storage: {self.storage}\n"
