class Employee:
    def __init__(self,name,department,salary):
        self.name=name
        self.department=department
        self.salary=salary

    def displayDetails(self):
        print("Name:",self.name,"Department:",self.department,"Salary:",self.salary,"rs.\n")
employee=[]
n=int(input("enter how many employees details you want to enter"))
for i in range(1,n+1):
    print("enter details for employee {}".format(i))
    name=input("enter a name")
    department=input("enter department")
    salary=int(input("enter a salary"))
    employee.append(Employee(name,department,salary))

for s in employee:
    s.displayDetails()


