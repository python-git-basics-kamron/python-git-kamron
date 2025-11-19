class Produkt:
    def __init__(self, title, price, year):
        self.title=title
        self.price=price
        self.year=year
        self.type=''

class Shop:
    def __init__(self, title,phone):
        self.title=title
        self.phone=phone
        self.baza=[]
        self.water=[]
        self.food=[]
        self.sneak=[]

    def add_water(self):
        title=input('title')
        price=int(input('price'))
        year=int(input("year"))
        p1=Produkt(title,price,year)
        p1.type='water'
        self.baza.append(p1)

    def add_food(self):
        title = input('title')
        price = int(input('price'))
        year = int(input("year"))
        p1 = Produkt(title, price, year)
        p1.type='food'
        self.baza.append(p1)

    def add_sneak(self):
        title = input('title')
        price = int(input('price'))
        year = int(input("year"))
        p1 = Produkt(title, price, year)
        p1.type='sneak'
        self.baza.append(p1)

    def view_water(self):
        for item in self.water:
            print(f'title= {item.title} price= {item.price}')


    def view_food(self):
        for item in self.food:
            print(f'title= {item.title} price= {item.price}')

    def view_sneak(self):
        for item in self.sneak:
            print(f'title= {item.title} price= {item.price}')

    def view_all(self):
        for item in self.baza:
            print(f'title= {item.title}, price= {item.price}')

    def update(self):
        print('Удалить:\n 1. water\n 2. food \n 3. sneak')
        choice = input('Ваш выбор: ').strip()

        if choice == '1':
            title = input('Введите название воды (water) для удаления: ')
            self.remove_product(title, product_type='water')

        elif choice == '2':
            title = input('Введите название еды (food) для удаления: ')
            self.remove_product(title, product_type='food')

        elif choice == '3':
            title = input('Введите название снека (sneak) для удаления: ')
            self.remove_product(title, product_type='sneak')

        else:
            print(False)




    def manager(self):
        while True:
            kod=input("1.add water\n 2.add food \n 3.add sneak\n 4.view water\n 5.view food\n 6.view sneak\n 7.view all\n")