#singup and login program
#user defined functions

while True:
    print("1 . Signup")
    print("2 . login")
    print("3 . Exit")
    ch = int(input("Enter your choice : "))
    if ch == 1:
        name = input("enter your name  : ")
        phn = int(input("enter your phone number : "),len==10)
        mail= input("Enter your mailid : ")
        print("_____Succesfully account was created_____")