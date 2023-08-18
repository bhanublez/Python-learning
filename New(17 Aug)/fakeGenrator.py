# fake data generation
import random,time
names=['rahul','vasu','gaurang','divyanshu','ayush']
subjects=['hidni','english','maths','science']
def peop_list(num):
    result=[]
for i in range(num):
    person={'id':i,'name':random.choice(names),'subjects':random.choice(subjects)}
result.append(person)
def peop_gen(num):
    for i in range(num):
        person={'id':i,'name':random.choice(names),'subjects':random.choice(subjects)}
        yield(person)

t1=time.clock()
peop_list(100)
t2=time.clock()
print("time take by normal:",t2-t1)
t3=time.clock()
peop_gen(100)
t4=time.clock()
print("time take by gen:",t4-t3)