# a = 5
# print(a)
# b = 99
# print(b + a)

# class Girl:
#     spiceis = "bird"

    #
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age
    #     self.color = 'black'
    #
    # def grow(self, heigth=1):
    #     self.heingth = heigth


# kate = Girl (heigth=170)
# kate.grow(heigth=15)
# print(kate.heigth)


# blu = Girl('nick', 10)
# woo = Girl('woo', 15)
# print(woo.color)
# print(woo.age)

class Student:

    def __init__(self, name):
        self.name = name
        self.progress = 0
        self.gladnass = 50
        self.alive = True

    def to_study(self):
        print('Time to study')
        self.progress += 0.5
        self.gladnass += 2
        pass

    def to_sleep(self):
        print('Time to study')
        self.gladnass += 5
        pass

    def to_chill(self):
        print('rest time')
        self.gladnass += 7
        self.progress += 0.2
        pass

    def is_aleve(self):
        if self.progress < -0.5:
            self.alive = False

        elif self.gladnass <= 0:
            print('Depresion')
            self.alive = False

    def end_of_day(self):
        print(f'Gladness = {self.gladnass}')
        print(f'Progres = {self.progress}')


