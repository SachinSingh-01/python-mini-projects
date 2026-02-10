'''Employee management system.
Requirements
Menu:
1 Add employee
2 View employees
3 Search employee
4 Delete employee
5 Save to file
6 Exit
Rules:
Store employees → {id: (name, salary)}
Use tuple for employee info
Use match-case
Use functions
Save/load from file
Concepts used
dict
tuple
list
match-case
functions
file handling
loops
This is interview-style real problem.'''
dic={}
def add_employee():
    Employee_ID=int(input("Enter employee ID:"))
    Employee_Name=input("Enter the name of the employee:")
    Employee_Salary=int(input("Enter the salary of employee:"))
    if Employee_ID in dic:
        print("Employee ID already exists")
    else:
        dic[Employee_ID] = (Employee_Name, Employee_Salary)


def display_employee():
    if not dic:
        print("No employees found")
    else:
        for emp_id, info in dic.items():
            name, salary = info
            print(f"ID: {emp_id}, Name: {name}, Salary: {salary}")



def search_employee():
    search_Id=int(input("Enter employee ID:"))
    if search_Id in dic:
        name, salary = dic[search_Id]
        print(f"ID: {search_Id}, Name: {name}, Salary: {salary}")

    else:
        print("Wrong ID")

def delete_employee():
    remove_id=int(input("Enter employee ID to remove:"))
    if remove_id in dic:
        dic.pop(remove_id)
        print("Delete successfully")
    else:
        print("Wrong Id")

def save_file():
    with open("employee_data.txt", "w") as file:
        for emp_id, info in dic.items():
            name, salary = info
            file.write(f"ID: {emp_id}, Name: {name}, Salary: {salary}\n")
    print("Employee data saved successfully.")

while True:
    print("1. To add employee")
    print("\n2. Display info")
    print("\n3. Search employee")
    print("\n4. Delete employee")
    print("\n5. Save file")
    print("6. Exit")
    choice=int(input("Enter the number from (1-6):"))
    match choice:
        case 1:
            add_employee()
        case 2:
            display_employee()
        case 3:
            search_employee()
        case 4:
            delete_employee()
        case 5:
            save_file()
        case 6:
            print("You exit")
            break
        case _:
            print("Invalid number")