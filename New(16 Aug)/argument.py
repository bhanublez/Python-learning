# Keyword Arguments
def wish(name,msg):
    print(f"Hello {name} {msg}")
wish("Raj",msg="Good Morning")

#Positional Arguments
def wish(name,msg):
    print(f"Hello {name} {msg}")
wish("Raj","Good Morning")

#Default Arguments
def wish(name,msg="Good Morning"):
    print(f"Hello {name} {msg}")