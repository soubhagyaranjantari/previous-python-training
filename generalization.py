class person:
    country='India'
    nationaty='Indian'
    state='Odisha'

class Student(person):
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.gender=None
        self.marks=marks

class Employe(person):
    def __init__(self,name,sal):
        self.name=name
        self.age=None
        self.sal=sal
# ,name,age,gender,marks,
# ,name,age,gender

# s=Student(input('Enter ur name\n'),int(input('Entaer ur age\n')),input('Ur gender\n'),int(input('Enter ur Marks\n')))
# E=Student(input('Enter ur name\n'),int(input('Entaer ur age\n')),int(input('Enter ur Salary\n')))

# s=Student(int(input('Enter ur marks\n')))

# e=Employe(int(input('Enter ur Salary\n')))



        
        