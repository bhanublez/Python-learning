import struct
print(dir())   # show the names in the module namespace  

print(dir(struct))   # show the names in the struct module 




class Shape:
    def __dir__(self):
        return ['area', 'perimeter', 'location']
s = Shape()
print(dir(s))