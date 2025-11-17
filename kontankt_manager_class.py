class Kontakt:
    def __init__(self, name,phone,email,age):
       self.name=name
       self.phone=phone
       self.email=email
       self.age=age

kontakt=Kontakt('bob','+998112223344','qwerty@gmail.com','23')
kontakt2=Kontakt('max','+998998887766','asdfgh@gmail.com','18')
kontakt3=Kontakt('robert','+998119992288','qwertyuiop@gmail.com','39')

baza=[kontakt,kontakt2,kontakt3]

def view_kontakts(s:list):
    count=0
    for item in s:
        count+=1
        print(f'{count}. name= {item.name}, phone= {item.phone}, email= {item.email}, age= {item.age}')
# view_kontakts(baza)

def add_kontakt(s:list):
    name=input("name:")
    phone=input("phone:")
    email=input("email:")
    age=input("age:")
    a=Kontakt(name,phone,email,age)
# add_kontakt(baza)

def kontakt_manager(s:list):
    while True:
        kod=input("1.add \n 2.view \n 3.break")
        if kod=="1":
            add_kontakt(s)
        elif kod=="2":
            view_kontakts(s)
        else:
            break
kontakt_manager(baza)
