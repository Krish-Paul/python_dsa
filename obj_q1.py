#create a class Employee with attributes empid,name,salary and also define methods to access properties of employees
class Employee:
    def __init__(self,empid=None,name=None,salary=None):
        self.empid=empid
        self.name=name
        self.salary=salary
    def setemp(self,empid):
        self.empid=empid
    def setname(self,name):
        self.name=name
    def setsal(self,salary):
        self.salary=salary
    def getemp(self):
        return self.empid
    def getname(self):
        return self.name
    def getsal(self):
        return self.salary
e1=Employee( )
e2=Employee(1, "Rahul", 40000)
el.setEmpid(2)
el.setName("Romesh")
el.setSalary(50000)
print(el.getemp(), el.getname(), el.getsal())
print(e2.getemp(), e2.getname(), e2.getsal())
