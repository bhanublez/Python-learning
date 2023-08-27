def to_second(hours,minutes,seconds):
    return hours*3600+minutes*60+seconds
print("Welcome to this converter")
cont="y"
while(cont.lower()=='y'):
    hours=int(input("Enter the number of hours: "))
    minutes=int(input("Enter the number of minutes: "))
    seconds=int(input("Enter the number of seconds: "))

    print("That is {} seconds ".format(to_second(hours,minutes,seconds)))
    cont=input("Do you want to start another staffs: [y to continue] ")
print("Good bye!")