import json

database_file = "database.json"
max_tries = 3

def load_data():
    try:
        with open(database_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("ошибка")
        return None

def save_data(data):
    with open(database_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def check_pin(load_data):
    for i in range(1, max_tries + 1):
        entered_pin = input("Введите PIN-код карты: ")
        if entered_pin == load_data.get('pin'):
            return True
        else:
            print(False)

    print("больше 3 попыток")
    return False

def show_menu(data):
    while True:
        print("        МЕНЮ БАНКОМАТА        ")
        print("1. Посмотреть баланс")
        print("2. Снять деньги")
        print("3. Положить деньги")
        print("4. Включить SMS")
        print("5. Выключить SMS")
        print("6. Выход")

        choice = input("Выберите операцию (1-6): ")

        if choice == '1':
            print(f" Ваш баланс: {data['balance']}")

        elif choice == '2':
            try:
                a = float(input("сумма?"))
                if a <= 0:
                    print(False)
                elif a > data['balance']:
                    print("недостаточно средств на карте")
                else:
                    data['balance'] -= a
                    save_data(data)
                    print("снято!")
            except ValueError:
                print(False)
        elif choice == '3':
            try:
                a = float(input("сумма?"))
                if a<= 0:
                    print(False)
                else:
                    data['balance'] += a
                    save_data(data)
                    print("пополнено!")
            except ValueError:
                print(False)

        elif choice == '4':
            if data.get('sms_number'):
                print("уже есть номер")
            else:
                new_number = input("номер-")
                data['sms_number'] = new_number
                save_data(data)
                print("включено")

        elif choice == '5':
            if not data.get('sms_number'):
                print("уже выключено")
            else:
                data['sms_number'] = None
                save_data(data)
                print("выключено")

        elif choice == '6':
            break

card_data = load_data()
check_pin(card_data)
show_menu(card_data)