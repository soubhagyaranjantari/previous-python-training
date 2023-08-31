from abc import ABC,abstractmethod
import random
class compan(ABC):
    def location(self,loc):
        # self.loc='USA'
        pass
    def employe(self):
        print('HELLO WORLD')
    @abstractmethod
    def employe1(self):
        pass
class company(compan):
    def employe1(self):
        A=random.randint(1,100)
        
        print(' company',A)

c=company()
if isinstance(c,company):
    c.employe1()
    c.location(3)
print(c.loc)
