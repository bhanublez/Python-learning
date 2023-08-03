class Apple:
    def __init__(self,color,flavor):
        self.color=color
        self.flavor=flavor
    #_str_ is a special method that returns a string representation of the object.
    def __str__(self):
        return "This apple is {} and its flavor is {}".format(self.color,self.flavor)
zuuu=Apple("red","sweet")
print(zuuu)