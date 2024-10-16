class departmentA:
    def __init__(self,name,ID,bonus=90000):
        self.ID=ID
        self.name=name
        self.bonus=bonus
  
class departmentB(departmentA):
    def __init__(self, ID, name, bonus=500000):
        super().__init__(ID, name, bonus)
    

rahul=departmentA("Rahul",1234)
print(rahul.bonus)

rahul=departmentB("Rahul",2343)
print(rahul.bonus)

