'''Mini Chat Logger
Save chat messages.
Requirements
User enters messages repeatedly
Type "exit" to stop
Store all messages in list
Write all messages into chatlog.txt
Read file and display again
Concepts used
list
loop
strings
file handling
functions
'''
message=[]
def text_message():
    while True:
        text=input("Enter the text:")
        if text=="exit":
            print("You stop")
            break
        message.append(text)
def save_message():
    with open("chatlog.txt","a") as file:
        for meg in message:
            file.write(meg +"\n")
def show_result():
    with open("chatlog.txt","r") as file:
        print("chat log \n")
        print(file.read())
text_message()
save_message()
show_result()

# service_ikjy30a