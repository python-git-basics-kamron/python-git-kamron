tovari = {
    "12345": {
        "title": "15 pro",
        "price": "1500$",
        "year": "2024",
        "type": "phone"
    },
    "123456789": {
        "title": "samsung",
        "price": "1000$",
        "year": "2025",
        "type": "televizor"
    },
    "987654321": {
        "title": "mac",
        "price": "500$",
        "year": "2023",
        "type": "kompyuter"
    },
}

def add_product(d, product_type):
    product_id = input(f"Введите ID для нового {product_type}: ")
    title = input("Введите название: ")
    price = input("Введите цену: ")
    year = input("Введите год: ")
    new_product = {
        "title": title,
        "price": price,
        "year": year,
        "type": product_type
    }
    d[product_id] = new_product

def view_by_type(d, product_type):
    for k, v in d.items():
        if v["type"] == product_type:
            print(f'ID: {k}, title: {v["title"]}, price: {v["price"]}, year: {v["year"]}')

def view_all(d):
    for k, v in d.items():
        print(f'ID: {k}, title: {v["title"]}, price: {v["price"]}, year: {v["year"]}, type: {v["type"]}')

def magazin_manager(d):
    while True:
        kod = input(
            "1. Добавить телефон\n"
            "2. Добавить телевизор\n"
            "3. Добавить компьютер\n"
            "4. Посмотреть телефоны\n"
            "5. Посмотреть телевизоры\n"
            "6. Посмотреть компьютеры\n"
            "7. Посмотреть все товары\n"
        )
        if kod == "1":
            add_product(d, "phone")
        elif kod == "2":
            add_product(d, "televizor")
        elif kod == "3":
            add_product(d, "kompyuter")
        elif kod == "4":
            view_by_type(d, "phone")
        elif kod == "5":
            view_by_type(d, "televizor")
        elif kod == "6":
            view_by_type(d, "kompyuter")
        elif kod == "7":
            view_all(d)
        else: break

magazin_manager(tovari)