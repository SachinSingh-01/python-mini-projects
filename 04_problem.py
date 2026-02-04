'''Mini report card for one student.
Take 5 subject marks (list)
Store subjects + marks in dictionary
Calculate total, percentage
Assign grade using function
Print formatted report
list
dictionary
functions
calculations
string formatting'''
subjects = ["Math", "English", "Science", 'Computer', 'Hindi']
lst=[]
dic={}
total=0
for i in range(5):
    marks=int(input(f"Marks in {subjects[i]}: "))
    lst.append(marks)
    dic[subjects[i]]=marks
    total+=marks
percentage = (total / 500) * 100
print("Dictionary:\n",dic)
print("Total marks: ",total)
print("Percentage: ",percentage)
def grade(p):
    if p>=90:
        print("Grade:A")
    elif p>=70:
        print("Grade:B")
    elif p>=50:
        print("Grade:C")
    else:
        print("Grade:D")
grade(percentage)