class Heart:
    def __init__(self,name,beat) -> None:
        self.name = name
        self.beat=beat
    def Analysis(self):
        if self.beat>=68 and self.beat<=74:
            print('Ok')
        else:
            print('Abnormal')
        print(f'name of patient {self.name}')
class patient:
    def __init__(self,name,age,beat,gender='male') -> None:
        self.name = name
        self.age=age
        self.beat=beat
        self.gender=gender
        self.chk_heart=Heart(self.name,self.beat)
p1=patient('anil',25,70)
p1.chk_heart.Analysis()
        