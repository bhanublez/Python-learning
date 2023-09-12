class Student:
    def putdata(self,name,enr_no,age,branch,semester):
        self.name=name
        self.enr_no=enr_no
        self.age=age
        self.branch=branch
        self.semester=semester

    def getData(self):
        print("Name is {}, enrollment no is {}, age is {}, branch is {} and semester is {} ".format(self.name, self.enr_no, self.age, self.branch, self.branch))
        # print("Hello")
        # return 0

#Example
s1=Student()
s1.putdata("Bhanu","0187",21,"Cse",5)
s1.getData()