import re

class Contact_manager:
    def init(self,name ,phone):
        self.name=name
        self.phone=phone
        self.data=[]

    def add_contact(self):
        while True:
            name = input("name: ")
            if name.isalpha():
                break
            else:
                print("Folse: ")
        while True:
            phone = input("phone: ")
            phone_regex = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
            if re.match(phone_regex, phone):
                for i in self.data:
                    if i.phone != phone:
                        pass
                    else:
                        print(f'Folse')
                        return
                break
            else:
                print(f'Folse')

        contact = Contact_manager(name,phone)
        self.data.append(contact)

    def view_contact(self):
        count = 0
        for i in self.data:
            count += 1
            print(f'{count}. name: {i.name} phone: {i.phone}')

def contact_manager(contact:Contact_manager):
    while True:
        cod_contact=input(f' 1. add contact \n 2. view contact \n 3. exit \n >>> ')
        if cod_contact=="1":
            contact.add_contact()
        elif cod_contact=="2":
            contact.view_contact()
        elif cod_contact=="3":
            break
        else:
            print(f'folse ')




class Sms_manager:
    def init(self,contact:Contact_manager):
        self.contact=contact
        self.sms_data=[]

    def add_sms(self):
        self.contact.view_contact()
        sms_id= int(input(f'choose:'))
        if sms_id-1<len(self.contact.data):
            sms=input(f'sms=')
            send_sms=[self.contact.data[sms_id-1].name,sms]
            self.sms_data.append(send_sms)
        else:
            print(f'Folse')

    def view_sms(self):
        count=0
        for item in self.sms_data:
            count+=1
            print(f'{count}. name: {item[0]} sms: {item[1]}')

    def dell_sms(self):
        self.view_sms()
        dell_id=int(input(f'delete sms='))
        if dell_id-1<len(self.sms_data):
            self.sms_data.pop(dell_id-1)
        else:
            print(f'Folse')

def sms_manager(sms:Sms_manager):
    while True:
        cod_sms= input(f' 1. add sms \n 2. view sms \n 3. del sms \n 4 exit \n ')
        if cod_sms == "1":
            sms.add_sms()
        elif cod_sms == "2":
            sms.view_sms()
        elif cod_sms == "3":
            sms.dell_sms()
        elif cod_sms=="4":
            break
        else:
            print(f'Folse')


def menu():
    contact=Contact_manager("Kamron","+998957700010")
    sms=Sms_manager(contact)
    while True:
        cod = input(f' 1. contact manager \n 2 sms manager \n 3. exit \n ')
        if cod == "1":
            contact_manager(contact)
        elif cod == "2":
            sms_manager(sms)
        elif cod=="3":
            break
        else:
            print(f'Folse')

menu()