#---------------------
# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2)

#-----------------------
#sorting in descending order
#-----------------------

#sorted is a string which shows the values in a sequence
#reverse is a value which shows the sorted falues in reverse

# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse=True)

# Print out full_sorted
print(full_sorted)

#-----------------------
#Read inputs/pass inputs to a file
#-----------------------

# Python code to
# demonstrate readlines()
  
L = ["Geeks\n", "for\n", "Geeks\n"]
  
# writing to file
file1 = open('myfile.txt', 'w')
file1.writelines(L)
file1.close()
  
# Using readlines()
file1 = open('myfile.txt', 'r')
Lines = file1.readlines()
  
count = 0
# Strips the newline character
for line in Lines:
    count += 1
    print("Line{}: {}".format(count, line.strip()))

