import random
import string

if __name__ == "__main__":
    c1 = string.ascii_lowercase
    #print(c1)
    c2 = string.ascii_uppercase
    #print(c2)
    c3 = string.digits
    #print(c3)
    c4 = string.punctuation
    #print(c4)
    pass_len = int(input("provide length of the password: "))
    
    c = []
    c.extend(list(c1))
    c.extend(list(c2))
    c.extend(list(c3))
    c.extend(list(c4))
    #print(c)
    random.shuffle(c)
    #print(c)
    print("".join(c[0:pass_len]))