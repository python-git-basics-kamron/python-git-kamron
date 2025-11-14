kontakts={
    "+998950001000":{
        "name":"max",
        "phone":"+998950001000",
        "age":25,
        "email":"freoiwnm@frbv"
    },
    "+998117770007":{
        "name": "sam",
        "phone": "+998117770007",
        "age": 23,
        "email": "hgvthn@dgfvb"
    }
}
a=r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
b=r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
def add_kontakt(d:dict):
    name=input("name:")
    phone=input("phone:")
    age=input("age:")
    email=input("email:")
    import re
    if not re.match(a, phone):
        print("не правильный номер телефона")
    if not re.match(b, email):
        print("не правильный email")
    else:
        print("все правильно")
    s={
        phone:{
            "name": name,
            "phone": phone,
            "age": age,
            "email": email}
    }
    d.update(s)
def view_kontakts(d:dict):
    for k,v in d.items():
        print(f'id.{k}. name {v["name"]} phone {v["phone"]} age {v["age"]} email {v["email"]}')

def kontakt_maneger (d:dict):
    while True:
        kod=input(" 1.view kontakts \n 2.add kontakt \n 3.break")
        if kod=="1":
            view_kontakts(d)
        elif kod=="2":
            add_kontakt(d)
        else:break
kontakt_maneger(kontakts)