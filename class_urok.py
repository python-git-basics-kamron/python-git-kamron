class Produkt:
    def __init__(self, title_name, price, year1,year2, country, type):
       self.title_name=title_name
       self.price=price
       self.year1=year1
       self.year2=year2
       self.country=country
       self.type=type

produkt=Produkt("kia","$30000","2024","2050","korea","car")
produkt1=Produkt("hydrolife","$1","2025","2040", "uzbekistan","water")
produkt2=Produkt("15 pro","$1500","2022","2030","canada","phone")

baza=[produkt,produkt1,produkt2]

def add_produkt(s:list):
    title_name=input("title:")
    price=input("price:")
    year1=input("year1:")
    year2=input("year2:")
    country=input("country")
    type=input("type")
    z=Produkt(title_name,price,year1,year2,country,type)

def view_produkts(s:list):
    count=0
    for i in s:
        count+=1
        print(f'{count}. title_name= {i.title_name}, price= {i.price}')

def manager(s:list):
    while True:
        kod=input("1.add \n 2.view \n 3.break")
        if kod=="1":
            add_produkt(s)
        elif kod=="2":
            view_produkts(s)
        else:
            break
manager(baza)