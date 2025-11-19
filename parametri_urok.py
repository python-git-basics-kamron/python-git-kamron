# # class Person:
# #     def __init__(self,name):
# #         print('inside')
# #         self.name=name
# #         print('initialized')
# #     def show(self):
# #         print('hello',self.name)
# #
# #     def __del__(self):
# #         print("inside")
# #         print('destroyed')
# #
# # s1=Person('ali')
# # s1.show()
# #
# # del s1
# #
#
#
# class Student:
#     def __init__(self, name, age, phone):
#         self.name=name
#         self.age=age
#         self.phone=phone
#     def __str__(self):
#         return 'student '
#     def info(self):
#         print(f'name= {self.name}, age= {self.age}, phone= {self.phone}')
#
# s1=Student('ali', 23, '12353456')
#
# def view(s:list):
#     for item in s:
#         item.info()
#

# class Car:
#     total=0
#     def __init__(self, brand,model):
#         self.brand=brand
#         self. model=model
#

# class MathUtilils:
#     @staticmethod
#     def add(a,b):
#         return a+b
#
#     @staticmethod
#     def sum(a:list):
#         return sum(a)

# test_obj= MathUtilils()
# print(MathUtilils.add(5,10))

