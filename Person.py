class Person:

    def __init__(self,name,age,gender,interest=[]):

       self.name = name 
       self.age = int(age)
       self.gender = gender
       self.interest = interest
       

       

    def hello(self):
        interest = ",".join(self.interest)
        return "Hello,my name is {} and Im a {} years old My interest are {}".format(self.name,self.age,interest)

     


teboho = Person("Teboho",24,"MALE",["being a hardarse,agile and ssd hard drives."])


print(teboho.hello())