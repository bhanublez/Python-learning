class employee:
    def __init__(self,ei,n,s):
        self.employee_id=ei
        self.name=n
        self.salary=s
    
    def show_emp(self):
        print("Employee id {} emp name {} and his/her salary {} ".format(self.employee_id,self.name,self.salary))



list=[]
list.append(employee(1001,"Ravi",500))
list.append(employee(1002,"Davi",1500))
list.append(employee(1003,"Ravi",5100))

#Sorting list according to name
list.sort(key=lambda x: x.name)

# for element in list:
#     # print("Employee id {} , employee name {} and employee salary {}".format(element.employee_id,element.name,element.salary))
#     element.show_emp()


#Sorting list according to name
list.sort(key=lambda x: x.salary,reverse=True)

for element in list:
    element.show_emp()

 
