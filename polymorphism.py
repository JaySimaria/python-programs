#polymorphism
class parrot:
    def fly(self):
        print("parrot can fly")
def swim(self):
    print("parrot can't swim")
class penguin:
    def fly(self):
        print("penguin can't fly")
def swim(self):
    print("penguin can swim")
# common interface
def flying_test(bird):
    bird.fly()
# object calling class
    blu=parrot()
    peggy=penguin()
# passing the object    
    flying_test(blu)
    flying_test(peggy)
    
