'''Duplicate Remover Tool
What to build
Clean duplicate data.
Take 15 numbers
Store in list
Remove duplicates using set
Sort result
Save cleaned list to file
Concepts used
list
set
file handling
sort()
loops'''
numbers=[]
for i in range(15):
    num=int(input("Enter numbers:"))
    numbers.append(num)
numbers=list(set(numbers))
numbers.sort()
print("Remove duplicate and sorted:",numbers)
with open("duplicate_remover.txt","a") as file:
    file.write(str(numbers))
