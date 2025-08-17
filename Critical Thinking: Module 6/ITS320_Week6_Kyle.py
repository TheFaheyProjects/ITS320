#Kyle Fahey
#ITS320-1
#Critical Thinking: Module 6

#Animal Shelter Management System

#Importing Abstract Method
import __main__
from abc import ABC, abstractmethod

#Animal Class
class AnimalInformation(ABC):
    def __init__(self, animalName, animalAge, animalSpecies):
        self.__name = animalName 
        self._age = animalAge
        self.species = animalSpecies
        
    def displayAnimalInformation(self):
        print(f"\nName: {self.__name}, Age: {self._age}, Species: {self.species}")
        
    def updateAge(self, newAge):
        if newAge >= 0:
            self._age = newAge
        else:
            print("The Animals Age cannot be negative. Please enter the correct age.")
            
    def getName(self):
        return self.__name
    
    @abstractmethod
    def speak(self):
        pass

#Dog Class
class Dog(AnimalInformation):
    def __init__(self, animalName, animalAge, dogBreed):
        super().__init__(animalName, animalAge, "Dog")
        self.dogBreed = dogBreed
        
    def speak(self):
        print("Woof!")
        
    def bark(self):
        print(f"{self.dogBreed} Barks!")

#Cat Class
class Cat(AnimalInformation):
    def __init__(self, animalName, animalAge, catColor):
        super().__init__(animalName, animalAge, "Cat")
        self.catColor = catColor 
         
    def speak(self):
        print("Meow!")
        
    def meow(self):
        print(f"The {self.catColor} cat Meeoowwwws!")
        
#Animal Shelter Class
class AnimalShelter(ABC):
    #Adding an Animal
    @abstractmethod
    def addAnimal(self, animal):
        pass
    
    #Removing an Animal
    @abstractmethod
    def removeAnimal(self, name):
        pass
    
    #Displaying all the Animals
    @abstractmethod
    def displayAllAnimals(self):
        pass
    
#Shelter Class
class Shelter(AnimalShelter):
    def __init__(self):
        self.animals = []
        
    #Add Animal
    def addAnimal(self, animal):
        self.animals.append(animal)
        print(f"{animal.species} has been added to the Shelter Successfully!")
        
    #Removing Animal
    def removeAnimal(self, name):
        for animal in self.animals:
            if animal.getName() == name:
                self.animals.remove(animal)
                print(f"{name} has been removed from the Shelter Successfully!")
                return
        print(f"\nNo Animal has been found with the following name: {name}")
    
    #Displaying All Animals
    def displayAllAnimals(self):
        if not self.animals:
            print("\nThere are currently no Animals in the Shelter.")
        else:
            for animal in self.animals:
                animal.displayAnimalInformation()
                animal.speak()
                if isinstance(animal, Dog):
                    animal.bark()
                elif isinstance(animal, Cat):
                    animal.meow()
                
#Main Menu Implementation
def mainMenu():
    #Building the Shelter from the Shelter Class
    shelter = Shelter()
    
    while True:
        print("\n--- Animal Shelter Management System ---")
        print("1. Add An Animal")
        print("2. Remove An Animal")
        print("3. Display All The Animals")
        print("4. Exit The Program")
        
        #User Input for Menu Choice
        userMenuInput = input("\nPlease select an option, 1-4: ")
        
        #Option 1 | Add Animal
        if userMenuInput == "1":
            typeOfAnimal = input("\nPlease enter the type of Animal. Dog or Cat: ").strip().lower()
            name = input("\nPlease enter the name: ")
            age = input("\nPlease enter the age: ")
            
            #Adding Dog
            if typeOfAnimal == "dog":
                dogBreed = input("\nPlease enter the Breed of the Dog: ")
                dog = Dog(name, age, dogBreed)
                shelter.addAnimal(dog)
                
            #Adding Cat
            elif typeOfAnimal == "cat":
                catColor = input("\nPlease enter the Color of the Cat: ")
                cat = Cat(name, age, catColor)
                shelter.addAnimal(cat)
            else:
                print("\nThe Shelter Only Accepts Cats and Dogs! Check Back Later.")
        
        #Option 2 | Remove Animal
        elif userMenuInput == "2":
            name = input("\nPlease enter the name of the Animal you want to remove from the Shelter: ")
            shelter.removeAnimal(name)
            
        #Option 3 | Display All Animals
        elif userMenuInput == "3":
            shelter.displayAllAnimals()
        
        #Option 4 | Exit the Program
        elif userMenuInput == "4":
            print("\nThank you for using the Animal Shelter Management System! See You Next Time!")
            break
        
        #Handling Invalid Menu Option
        else:
            print("\nInvalid Menu Option. Please choose between 1 and 4.")

#Running the Program
if __name__ == "__main__":
    mainMenu()
            
    
    
