'''Simple bus booking system.
Requirements
Seats 1-10 stored in list
Menu:
1 Book seat
2 Cancel seat
3 Show seats
4 Exit
Use match-cas
Prevent double booking
Concepts used
list
match-case
loops
conditions
functions'''
seat=[]
def book_seat():
    book=int(input("Enter the seat number from 1-10 to book seat: "))
    if book<1 or book>10:
        print("Invalid Seat")
    elif book in seat:
        print("Your seat is booked")
    else:
        seat.append(book)
        print("your seat is booked successfully")
def cancel_seat():
    cancel=int(input("Enter the seat number to cancel you booked seat: "))
    if cancel<1 or cancel>10:
        print("Invalid Seat")
    elif cancel not in seat:
        print("Seat not booked")
    else:
        seat.remove(cancel)
        print("Your seat has cancelled successfully")
def show_seat():
    print("Booked seat:",seat)
while True:
    print("1.Book Seat")
    print("\n2.Cancel Seat")
    print("\n3.Show Seats")
    print("\n4.To exit")
    choice=int(input("Enter number from (1-4) to check result: "))
    match choice:
        case 1:
            book_seat()
        case 2:
            cancel_seat()
        case 3:
            show_seat()
        case 4:
            print("You exit")
            break
            