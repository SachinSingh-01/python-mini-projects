'''Number Statistics Analyzer
Analyze a list of numbers entered by user.
Take 10 numbers into a list
Using functions find:
sum
average
even numbers
odd numbers
largest & smallest
Return results in formatted string
Concepts used
list
loops
functions
conditions
variables'''
def numbers():
    lst=[]
    even_number=[]
    odd_number=[]
    for i in range(10):
        num=int(input("Enter number:"))
        lst.append(num)
    largest=lst[0]
    smallest=lst[0]
    total=0
    for num in lst:
        total+=num
        if num%2==0:
            even_number.append(num)
        else:
            odd_number.append(num)
        if num>largest:
            largest=num
        elif num<smallest:
            smallest=num
    average=total/len(lst)
    return f"""
Sum of number:{total}
Average of number:{average}
Even numbers:{even_number}
Odd numbers:{odd_number}
Maximum number:{largest}
Minimum number:{smallest}
"""
result=numbers()
print(result)

