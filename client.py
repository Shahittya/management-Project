from mobile_tech import Mobile
from laptop_tech import Laptop
from tech_product import Tech
from sales_person import SalesPerson
from datetime import  date

phone_1=Mobile("iphone_11",60000,500,"Black",'1920-1080',10)
phone_2=Mobile("iphone_12",70000,400,"Grey",'1920-1080',20)
phone_3=Mobile("iphone_13",80000,300,"Silver",'1920-1080',30)

laptop_1=Laptop("Asus g14",130000,1.6,"Black",16,'i-3',200)
laptop_2=Laptop("Asus g19",170000,1.1,"White",86,'i-5',100)
print(laptop_1)
print(phone_1)

#applying the discount
phone_1.apply_discount()
print(phone_1)

#total number of products
print(Tech.get_total_products())

#shipping cost
print(laptop_2.calculate_shipping_price(10))
print(" ")
#double price of the laptop
print(laptop_1.price)
laptop_1.set_double_price()
print(laptop_1.price)
sales_person_1=SalesPerson('Majed',"Ali",40000,date(2020,1,5))
#changing thespecsc
print(laptop_2)
laptop_2.change_specs(3000,1000)
print(laptop_2)

#adding the products
sales_person_1.sell_products(laptop_1)
sales_person_1.sell_products(laptop_2)
sales_person_1.sell_products(phone_1)
sales_person_1.sell_products(phone_2)
print(sales_person_1.total_product_sold())
#dispalysales
sales_person_1.display_sells()

#commision
print(sales_person_1.calculate_commision(0.2))

sales_person_1.sort_by_price()
sales_person_1.display_sells()
