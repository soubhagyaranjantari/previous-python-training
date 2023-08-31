from generalization import Student
from generalization import Employe

class goverment_services:
    """This is check for Gov. services"""
    def school(self,s):
        if isinstance(s,Student):
            print(f'{s.name} U r going to school')
        else:
            print(f'{s.name} u r a employe')
    def scolarship(self,s):
        if isinstance(s,Student):
            if s.marks>=80:
                print(f'{s.name} is Eligible For Scholarship')
            else:
                print(f'{s.name}  Not have 80% For Scholarship')
        else:
            print(f'{s.name} It is not for u')

    def tax_payment(self,e):
        if isinstance(e,Employe):
            if e.sal*12>=500000:
                print(f'{e.name} u r tax is ',e.sal*5/100)
            else:
                if e.sal<500000:
                    print(f'{e.name} u r not eligiable to pay tax')
        else:
            print(f'{e.name} u r a student')
    def Aadhar(self,obj):
        if isinstance(obj,Student) or isinstance(obj,Employe):
            print(f'{obj.name} u r eligible')
        else:
            print('Thank you')

    



