#print(type('Hello world'))
# print(dir(str))
# class Character:
#     pass

# peter = Character()
# print(type(peter))

# class Character:
#     gender = ''
#     name = ''
#     height = 0
#     weight = 0
#     hands = 2


# peter = Character()
# # print(peter.name)
# # print(peter.gender)
# # print(peter.height)
# # print(peter.weight)
# # print(peter.hands)
#
# peter.name = 'Peter Parker'
# peter.gender = 'm'
# peter.weight = 70
# peter.height = 175
#
# peter.alias = 'Spider Man'
# print(peter.alias)
#
# print(peter.name)
# print(peter.gender)
# print(peter.height)
# print(peter.weight)
# print(peter.hands)

# bruce = Character()
# bruce.name = 'Bruce Wayne'
# bruce.gender = 'm'
# bruce.height = 185
# bruce.weight =85
# bruce.alias = 'Batman'

# print(bruce.name)
# print(bruce.gender)
# print(bruce.height)
# print(bruce.weight)
# print(bruce.hands)
# print(bruce.alias)

# print(bruce.__dict__)
# print(Character.__dict__)

# print(dir(peter))

# class Character:
#
#     def __init__(self, name, gender, height=0, weight=0, hands=2):
#         self.name = name
#         self.gender = gender
#         self.height = height
#         self.weight = weight
#         self.weapons = []
#         self.hands = hands
#
#     def eat(self, food):
#         self.weight += food
#
#     def do_exercise(self, hours):
#         self.weight -= hours * 0.2
#
#     def change_alias(self, new_alias):
#         print(self)
#         self.alias = new_alias
#
#     def beat_up(self, foe):
#         if not isinstance(foe, Character):
#             return
#         foe.status = 'defeated'
#         self.status = 'winner'

# bruce = Character()
# bruce.name = 'Bruce Wayne'
# bruce.gender = 'm'
# bruce.height = 185
# bruce.weight =85

# bruce.change_alias('Batman')
# print(bruce.alias)
#
# bruce.change_alias('Dark Kneight')
# print(bruce.alias)

# bruce.do_exercise(1)
# bruce.do_exercise(2)
# bruce.do_exercise(3)
# print(bruce.weight)

# bruce.eat(2)
# print(bruce.weight)

# peter = Character('Peter Parker', 'm')
# bruce = Character('Bruce Wayne', 'm')
# print(peter.gender)
# print(bruce.hands)
#
# print((peter.__dict__))
#
# peter.weapons.append('web-shooters')
# print(peter.weapons)
# print(bruce.weapons)




# num1 = 5
# num2 = 10

# print(type(num1))
# print(num1 + num2)
# print(num1.__add__(num2))


# bruce.beat_up(peter)

# print(peter.status)
# print(bruce.status)

# class Birds:
#
#     def __init__(self, name, weight=0):
#         self.name = name
#         self.weight = weight
#
#     def eat(self, food):
#         self.weight += food
#
# class Cattle:
#
#     def __init__(self, name, weight=0):
#         self.name = name
#         self.weight = weight
#
#     def eat(self, food):
#         self.weight += food

# geese = Birds('Gray', 15)
# chicken = Birds('Co_Co', 10)
# duck = Birds('Cryakva', 13)

# cow = Cattle('Manyka', 500)
# sheep = Cattle('Barashek', 100)
# goat = Cattle('Roga', 50)

# geese.eat(2)
# chicken.eat(1)
# duck.eat(1.5)

# cow.eat(30)
# sheep.eat(10)
# goat.eat(5)

# print(geese.weight)
# print(chicken.weight)
# print(duck.weight)
# print(cow.weight)
# print(sheep.weight)
# print(goat.weight)

# list = [geese, chicken, duck]
#
# for bird in list:
#     bird.eat(2)
#     print(bird.weight)


# class Person:
#
#     def __init__(self, name, gender, height=0, weight=0, hands=2):
#         self.name = name
#         self.gender = gender
#         self.height = height
#         self.weight = weight
#         self.weapons = []
#         self.hands = hands
#         self.__alias = 'No alias'
#
#     def eat(self, food):
#         self.weight += food
#
#     def do_exercise(self, hours):
#         self.weight -= hours * 0.2
#
#     def __change_alias(self, new_alias):
#         print(self)
#         self.__alias = new_alias
#
#     def beat_up(self, foe):
#         if not isinstance(foe, Character):
#             return
#         foe.status = 'defeated'
#         self.status = 'winner'
#
# peter = Person('Peter parker', 'Male', 175, 70)
# print(peter._Person__alias)
# peter._Person__change_alias('Spider Man')
# print(peter._Person__alias)



# class Human():
#     name = ''
#     gender = ''
#     height = 0
#     weight = 0
#     hands = 2
#
# class Spider():
#     gender = ''
#     height = 0
#     weight = 0
#     hands = 6
#
#     def webshoot(self):
#         print('Pew-Pew')
#
# class SpiderMan(Human, Spider):
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender

# peter_parker = SpiderMan('Peter Parker', 'Male')
# print(peter_parker.name)
# print(peter_parker.gender)
# print(peter_parker.height)
# print(peter_parker.weight)
# print(peter_parker.hands)
# peter_parker.webshoot()
#
# print(SpiderMan.mro())


# class Human():
#     def __init__(self, name, gender, height=0, weight=0, hands=2):
#         self.name = name
#         self.gender = gender
#         self.height = height
#         self.weight = weight
#         self.hands = hands
#
# class Spider():
#     def __init__(self, gender, height=0, weight=0, hands=6):
#         self.gender = gender
#         self.height = height
#         self.weight = weight
#         self.hands = hands
#
#     def webshoot(self):
#         print('Pew-Pew')
#
# class SpiderMan(Human, Spider):
#     def __init__(self, name, gender):
#         self.weapons = []
#         super().__init__(name, gender)
#
#     def attack(self):
#         if 'web' in self.weapons:
#             super().webshoot()
#         else:
#             print('No web')

# peter_parker = SpiderMan('Peter Parker', 'Male')
# peter_parker.attack()
#
# peter_parker.weapons = 'web'
# peter_parker.attack()
#
# print(SpiderMan.mro())


# class Primate:
#     def eat(self, food):
#         print(food)
#
# class Man(Primate):
#     def eat(self, food, cooked=False):
#         if cooked:
#             print('cooked', food)
#         else:
#             print(food)


# class Human():
#     def __init__(self, name, gender, height=0, weight=0, hands=2):
#         self.name = name
#         self.gender = gender
#         self.height = height
#         self.weight = weight
#         self.hands = hands
#
#     def move(self):
#         self.weight -= 0.01
#
# class Spider():
#     def __init__(self, gender, height=0, weight=0, hands=6):
#         self.gender = gender
#         self.height = height
#         self.weight = weight
#         self.hands = hands
#
#     def webshoot(self):
#         print('Pew-Pew')
#
# class SpiderMan(Human, Spider):
#     def __init__(self, name, gender):
#         self.weapons = []
#         super().__init__(name, gender)
#
#     def attack(self):
#         if 'web' in self.weapons:
#             super().webshoot()
#         else:
#             print('No web')
#
#     def move(self):
#         super().webshoot()
#         super().move()
#
#     def __lt__(self, other):
#         if not isinstance(other, SpiderMan):
#             print('Not a SpiderMan')
#         return len(self.weapons) < len(other.weapons)
#
#     def __add__(self, weapon):
#         if not isinstance(weapon, str):
#             print('Error')
#         self.weapons.append(weapon)
#
# peter_parker = SpiderMan('Peter Parker', 'Male')
# miles_morales = SpiderMan('Miles_Morales', 'Male')
# # peter_parker.weapons += 'web_shooter'
# # print(peter_parker.weapons)
# # miles_morales.weapons += 'web_shooter', 'electricity'
# # print(miles_morales.weapons)
# # print(peter_parker < miles_morales)
# # print(peter_parker > miles_morales)
#
# print(peter_parker.weapons)
# peter_parker + 'strike'
# print(peter_parker.weapons)


# f = open('text.txt')
# print(type(f))
#
# data = f.read()
# print(data)
# print(type(data))
#
# f.close()
# print(data)


# def is_closed(file_):
#     if file_.closed:
#         print('Файл закрыт')
#     else:
#         print('Файл открыт')
#
# with open('text.txt') as f:
#     # print(type(f))
#     data = f.read()
#     is_closed(f)
#     f.read()
#
# is_closed(f)
# # f.read()

# try:
#     with open('text.txt') as f:
#         data = f.read()
#         is_closed(f)
#         1/0
# except ZeroDivisionError:
#     is_closed(f)


# with open('text.txt') as f:
#     data = f.read()
#     print(type(data))
#     print(data)
#
# print(data)

# with open('text.txt') as f:
#     print(f.readline().strip())
#     print(f.readline().strip())
#     print(f.readline().strip())
#     print(f.readline().strip())
#     print(f.readline().strip())
#     print(f.readline().strip())
#     print(f.readline().strip())
#     print(f.readline() == '')
#     print(f.readline() is None)

# with open('text.txt') as f:
#     lines = f.readlines()
#     print(type(lines))
#     print(len(lines))
#     print(lines[3])

# with open('text.txt') as f:
#     for i in f:
#         print(i.strip())

# with open('text.txt') as f:
#     for idx, i in enumerate(f):
#         print(idx, i.strip())


# with open('test.txt', 'w') as f:
#     f.write('Привет!\n')
# with open('test.txt', 'a') as f:
#     f.write('Первая строка\n')
# with open('test.txt', 'a') as f:
#     f.write('Вторая\n')
# with open('test.txt', 'a') as f:
#     f.write('\n')
# with open('test.txt', 'a') as f:
#     f.write('123\n')
#
# with open('test.txt') as f:
#     print(f.read())


# with open('test.txt', 'rb') as f:
#     data = f.read()
#     print(type(data))
#     print(data)


# import os
# import time
#
# with open('test.txt', 'w') as f:
#     f.write(f'{time.time()}')
#
# with open('test.txt', 'r') as f:
#     print(f.read())
#
# print(os.getcwd())
# file_path = os.path.join(os.getcwd(), 'test.txt')
# print(file_path)


# with open('utf.txt', 'w', encoding='utf-8') as f:
#     f.write('Привет, мир!')
#
# with open('cp.txt', 'w', encoding='cp1251') as f:
#     f.write('Привет, мир!')

# with open('utf.txt', 'rb') as f:
#     print(f.read())
#
# with open('cp.txt', 'rb') as f:
#     print(f.read())

# with open('cp.txt', 'r', encoding='cp1251') as f:
#     print(f.read())

# with open('ascii.txt', 'w', encoding='ascii') as f:
#     f.write('Privet, mir!')
#
# with open('ascii.txt') as f:
#     print(f.read())


a = [1, 2, 3]
b = a
c = b
b[1] = 5
print(a, b, c)

