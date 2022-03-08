class Hesablama:
    def __init__(self,say1,say2):
        self.s1=say1
        self.s2=say2
        print('hesablamaya basla')    
    def toplama(self):
        return self.s1+self.s2
    def ferq(self):
        return self.s1-self.s2
    def bolme(self):
        return self.s1/self.s2
    def vurma(self):
        return self.s1*self.s2

hesablama=Hesablama(45,3)
cavab=hesablama.bolme()
print(cavab)
class Student:
  def __init__(self,ad,soyad,):
    self.firstname = ad
    self.lastname = soyad

  def printname(self):
    print(self.firstname, self.lastname)

class Muellim(Student):
  def __init__(self, ad,soyad):
    super().__init__(ad,soyad)

x = Muellim("Gulcin", "Mustafazade")
x.printname()
 #class task
   