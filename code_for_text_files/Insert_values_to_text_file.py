# Program to show various ways to read and
# write data in a file.

file = open("sample.txt","w")
L = ["This is Sabarish \n","Sabarish works in Microsoft \n","Sabarish works in Azure DevOps core team \n"]

# \n is placed to indicate EOL (End of Line)

file.write("Hello \n")
file.writelines(L)
file.close() #to change file access modes

file = open("sample.txt",""r+)
print("Output of Read function is ")
print(file.read())
print()

#-----------------
#Replace specific string from a file
with open(FileName) as f:
    newText=f.read().replace('A', 'Orange')

with open(FileName, "w") as f:
    f.write(newText)