def full_email(people):
    result=[]
    for email,person in people:
        result.append("{} <{}>".format(person,email))
    return result

print(full_email([("first@gmail.com","first"),("second@gmail.com","second"),("third@gmail.com","third")]))
