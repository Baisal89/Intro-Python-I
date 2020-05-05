# def func(a):
#     print(f'1: {a}')
#     a[0] = 99
#     print(f'2: {a}')
# a = [0,1,2,3,4]

# func(a)

# print(a)

# def func2(x):
#     x += 5
# a = 12
# func2(a)

# print(a)

# for i in range(20):
#     print(i)

# a = [1,2,3,4,5]

# for i in a:
#     print(i)

# f = open("foo.txt", "rb")

# for i in f:
#     print(i)


#OOP
#examples

class Animal:
    
    def __init__(self):
        print("constructor called!")
        self.leg_count = 4


cat = Animal() #contstruct a new Animal, Instatiate a new Animal
dog = Animal() #contstruct a new Animal
rabbit = Animal()  #contstruct a new Animal
#^^
#objects

# "cat" is an instancce of an Animal
#"cat" is na Animal

print(f"cat's leg count: {cat.leg_count}")

cat.leg_count = 3

print(f"dog's leg count: {cat.leg_count}")
print(f"rabbit's leg count: {cat.leg_count}")