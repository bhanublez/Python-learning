person={"name":"bhanu","age":999}
print(person)
print(person["name"])
#key word argument passing
def func(**kwargs):
    print(kwargs)
    print(type(kwargs))
func(name="bhanu",age=999)
