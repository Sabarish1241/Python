#######Functions with parameters###########

# def greet(name):
#     print(f"my name is: {name}")

# greet("SSS")
# greet("SOMY")


#########Positional arguments#########

# def name(first_name, last_name):
#     print (f"my name is : {first_name} {last_name}")
# name("Saran", "Sabarish")    
# # for i in range(0-5):
# #     name("Saran", "Sabarish")

# a = float(input('First: '))
# b = float(input('Second: '))
# op = input('Operation (sum/sub/mul/div): ')

# match op:
#     case 'sum':
#         print(f'a + b = {a+b}')
#     case 'sub':
#         print(f'a - b = {a-b}')
#     case 'mul':
#         print(f'a * b = {a*b}')
#     case 'div':
#         print(f'a / b = {a/b}')
#     case _:
#         print('Invalid Operation!')


# def sum(a, b):
#     return a + b

# def sub(a, b):
#     return a - b

# def mul(a, b):
#     return a * b

# def div(a, b):
#     return a / b

# a = float(input('First: '))
# b = float(input('Second: '))
# op = input('Operation (sum/sub/mul/div): ')

# if op == 'sum':
#     print(f'a + b = {sum(a, b)}')
# elif op == 'sub':
#     print(f'a - b = {sub(a, b)}')
# elif op == 'mul':
#     print(f'a * b = {mul(a, b)}')
# elif op == 'div':
#     print(f'a / b = {div(a, b)}')
# else:
#     print('Invalid Operation!')


#############
# class computer:
#     def __init__(self,cpu,ram):
#         self.cpu = cpu
#         self.ram = ram
#     def config(self):
#         print("cpu is", self.cpu, "ram is", self.ram)
    
# com1 = computer('i5', 16)
# com2 = computer('raizon', 8)

# com1.config()
# com2.config()

def add(a, b, c):
    print(id(a), id(b), id(c))

x, y, z = 10, 15, 5
a, b, c = 5, 6, 7
add(x, y, z)
add(a,b,c)


#     r = (a+b+c)
#     return r
# #  a = float(input('a: '))
# #  b = float(input('b: '))
# #  c = input('c: ')
# # print(add())

# print (add(10, 15, 5))

# r = add(3,4,5)
# print(r)
