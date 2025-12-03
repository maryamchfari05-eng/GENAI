class cat():
    def __init__(self,name,age):
        self.name=name
        self.age = age
    def meaw(self):
        print(f"{self.age} says meow!")
class siamese(cat):
    def __init__(self, name, age,colour):
         print(om)
#jjjjj
class  dog:
    def __init__(self,name,age,weight):
        self.name=name
        self.age=age
        self.weight=weight
    def  bark(self):
           return f"{self.name} is barking"     
    def run_speed(self):
            return (self.weight  / self.age)*10
    def fight(self,other_dog):
           my_power= self.run_speed()*self.weight
           other_power = other_dog.run_speed()*other_dog.weight
           if my_power > other_power:
                my_power =self.run_speed()*self.weight
                return f"{self.name} won the fight against {other_dog.name}"
           elif my_power < other_power:
                return f"{other_dog.name} won the fight against {self.name}!"
           else :
                return "it's a tie!"
dog1= dog("linda", 12, 30)
dog2=dog("rex" , 10, 15)
dog3=dog("minuch", 9, 20)
print(dog1.bark())           
print(dog1.run_speed())
print(dog1.fight(dog2))
print(dog2.bark())           
print(dog2.run_speed())
print(dog2.fight(dog2))
print(dog3.bark())           
print(dog3.run_speed())
print(dog3.fight(dog2))
#


    
        