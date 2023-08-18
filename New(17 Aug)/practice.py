#WAP to tio genrater fake data from the available data 
import random,time
name=["anmol","Ravi","Konsa","Haona"]
subject=["Hindi"]

## Normal function
def fake(n):
    result=[]
    for i in range(n):
        person={'id':i,'name':random.choice(name),'subject':random.choice(subject)}
        result.append(person)
    return result

