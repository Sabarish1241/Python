# square = []
# for i in range(10):
#   square.append(i**2)
# print(square)


# import string

# def print_alphanumeric():
#     # Print all lowercase letters
#     for letter in string.ascii_lowercase:
#         print(letter, end=",")
    
#     # Print all uppercase letters
#     for letter in string.ascii_uppercase:
#         print(letter, end=",")
    
#     # Print all digits from 0 to 9
#     for digit in string.digits:
#         print(digit, end=",")

# # Call the function
# print_alphanumeric()

###function enumerate ######

players = ["Sabarish", "Muni", "Ravi"]
for i, player in enumerate(players):
    print(f"{i}:{player}")


#####function zip#######

scores = [100, 200, 300]
players = ["SSS", "Ravi", "Muni"]

for score,player in zip(scores,players):
    print(f"{player} score is {score}")

#####Iter#########

list = [1, 2, 3, 4, 5]
sample = iter(list)

print("value of 1st iter")
for i in range(0, 3):
  print(next(sample))

print("value of 2nd iter")
for z in range(0,2):
   print(next(sample))