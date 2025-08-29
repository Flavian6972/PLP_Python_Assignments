# Q1 : Designing your own class
class moviesList:
    def __init__(self, movieName, genre, availability):
        self.movieName = movieName
        self.genre = genre
        self.availability = availability
    def info(self):
        print(f"Hi there! Here are details about the movie you selected:\nMovie Title :{self.movieName}\nGenre: {self.genre}\n"
              f"Availability: {self.availability} ")
        
movie1 = moviesList('Night Agent', 'Action Thriller', 'Netflix')
movie1.info()

# Q2: Polymorphism Challenge
class cow:
    def make_sound(self):
        print('Cow: mooo!mooo!') 

class dog:
    def make_sound(self):
        print('Dog: woof!woof!')   

class cat:
    def make_sound(self):
        print('Cat: meow! meow!')  

class duck:
    def make_sound(self):
        print('Duck: quack!quack!')

animal1 = cow() 
animal2 = cat()  
animal3 = duck()
animal4 = dog()                 
animal1.make_sound()
animal2.make_sound()
animal3.make_sound()
animal4.make_sound()