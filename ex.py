#Exercise 1: Cats
#Key Python Topics:
#Classes and objects
#Object instantiation
#Attributes
#Functions
    
class cat():
    def __init__(self,name , age):
        self.name = name
        self.age =age
cat1 = cat("sizar",3)
cat2 = cat("fena",1) 
cat3 = cat("minuch",4)   
def find_oldest_cat(cat1,cat2,cat3):
    oldest_cat = cat1
    if cat2.age > oldest_cat.age:
        oldest_cat =cat2
    if cat3.age > oldest_cat.age:
        oldest_cat=cat3
    return oldest_cat
oldest = find_oldest_cat(cat1,cat2,cat3)
print("oldest cat is "  +  oldest.name)
#Exercise 2 : Dogs
class dog():
    def __init__(self,name,height):
        self.name = name
        self.height = height
    def park(self):
        print(f"{self.name} goes woof!")
    def jump(self):
        x= self.height*2
        print(f"{self.name} jumps {x} cm high!")  
DAVID_dog= dog('linda',40)
SARAH_dog = dog('rex',55)
print(f"{DAVID_dog.name} is {DAVID_dog.height} cm ")
print(f"{SARAH_dog.name} is {SARAH_dog.height} cm")
DAVID_dog.jump()
DAVID_dog.park()
SARAH_dog.jump()
SARAH_dog.park()
if SARAH_dog.height < DAVID_dog.height:
    print(f"{DAVID_dog} is tall")
else:
    print(f"{SARAH_dog.name} is tall")
#Exercise 3 : Who’s the song producer?
class song():
    def __init__(self,lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
stairway = song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()
#Exercise 4 : Afternoon at the Zoo
class zoo():
    def __init__(self ,zoo_name ,animals):
      self.zoo_name =  zoo_name
      self.animals = []
    def add_animal(self , *new_animal):
        if new_animal not in self.animals:
           self.animals.append(new_animal)
           print(f"{new_animal} add to list")
        else :
            print(f"{new_animal} is already in the zoo" )
    def get_animals(self):
        for animal in  self.animals :
            print(animal)
    def sell_animal(self, animal_sold):
             if animal_sold in self.animals :
                 self.animals.remove(animal_sold)
                 print(f"{animal_sold} has been soold")
             else :
                 print(f"{animal_sold} not found in the zoo")
    def sort_animals(self):
        self.animals.sort()
        grouped={}
        for animal in self.animals:
            letter = animal[0].upper()
            if letter not in grouped:
                grouped[letter] = []
            grouped[letter].append(animal)

        self.groups = grouped
        return grouped

    def get_groups(self):
        if not self.groups:
            self.sort_animals()

        for letter, group in self.groups.items():
            print(f"{letter}: {group}")
brooklyn_safari = zoo("Brooklyn Safari",["Giraffe", "Bear", "Baboon", "Zebra", "Cat"])
brooklyn_safari.add_animal("Giraffe", "Bear", "Baboon", "Zebra", "Cat")
print("\nAnimals in the zoo:")
brooklyn_safari.get_animals()
print("\nSelling 'Bear'...")
brooklyn_safari.sell_animal("Bear")

print("\nAnimals after selling:")
brooklyn_safari.get_animals()

print("\nSorted and grouped animals:")
brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()
