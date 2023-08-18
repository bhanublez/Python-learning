#Decorative Function
def decor(hello):
    def inner(situation):
        if(situation=="Yes"):
            situation="Yes do"
            return hello(situation)
        else:
            return hello(situation)
    return inner


def hello(situation):
    print("Need Help",situation)
hello("No")
    
