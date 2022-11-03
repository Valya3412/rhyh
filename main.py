# class Human:
#     heigth = 170
#     setiety = 10

# class Student(Human):
#     setiety = 10

# class Worker(Human):
#     pass
#
# nick = Student()
# anna = Worker()
# print(nick.setiety)
# print(anna.setiety)

# class Grandparen:
#     heigth = 170
#     gladness = 100
#     age = 60
#
# class Parent(Grandparen):
#     age = 40

# class Child(Parent):
#     heigth = 50
#     def __init__(self):
#         print(self.heigth)
#         print(self.gladness)
#         print(self.age)
#
# nick = Child()

# class Class1:
#     var = 20
#     def __init__(self):
#         self.var = 10


# class Class2(Class1):
#     def __init__(self):
#         print(self.var)
#         super().__init__()
#         print(self.var)
#
# hello_world = Class2

# class Grandparent:
#     def about(self):
#         print('I am GrandParent')
#     def about_muself(self)):
#         print('I am GramdParent'

# try:
#     print('Start code')
#     print(10/0)
#     print('No errors')
# except ZeroDivisionError:
#     print('error!because hare is division zero')
# except NameError:
#     print("We have an error")
#
# print('code after capsul')
#
# def checker(var_1):
#     if type(var_1)!= str:
#         raise TypeError(f'Sorry, we cant work with {type(var_1)}')

# class Grandparent:
#
#     def about(self):
#         print("I am GrandParent")
#
#     def about_myself(self):
#         print("I am Grandparent")
#
#
# class Parent(Grandparent):
#
#     def about_myself(self):
#         print("I am Parent")
#
#
# class Child(Parent):
#
#     def __init__(self):
#         super().about()
#
#         super().about_myself()
#
#
# nick = Child()

# class BuildingEror(Exception):
#
#     def __str__(self):
#
#         return f"With so much material the house cannot be built!"
#
#
#
# def check_material(amount_of_material,limit_value):
#
#     if amount_of_material > limit_value:
#
#         return "enough material"
#
#     else:
#
#         raise BuildingEror(amount_of_material)
#
#
#
# # materials = 123
#
# check_material(123, 300)



class BuildingEror(Exception):

    def __str__(self):

        return f"With so much material the house cannot be built!"



def check_material(amount_of_material,limit_value):

    if amount_of_material > limit_value:

        return "enough material"

    else:

        raise BuildingEror(amount_of_material)



# materials = 123

check_material(123, 300)























