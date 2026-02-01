'''Track daily attendance of students.
Take 5 student names (list)
Ask each → Present or Absent
Store in dictionary → {name: status}
Count total present and absent
Save result into attendance.txt
Concepts used
list
dictionary
loop
if-else
file handling
functions'''
def take_attendance():
    lst=[]
    dic={}
    i=0
    present_count=0
    absent_count=0
    for i in range(5):
        student_name=input("Enter name of the student:")
        lst.append(student_name)
        print(lst)
        status=input("Enter present/absent:")
        dic[student_name]=status
        if status=="present":
            present_count+=1
        elif status=="absent":
            absent_count+=1
    return dic,present_count,absent_count
def save_to_file(dic):   
    with open("attendance.txt","w") as file:
        for k,v in dic.items():
            file.write(f"{k}:{v}\n")
def show_result(present,absent):
    print("No of student present:",present)
    print("No of student absent:",absent)
dic, present_count, absent_count = take_attendance()
save_to_file(dic)
show_result(present_count, absent_count)