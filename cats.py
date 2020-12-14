# Object Oriented Programing
class Cat:
    # CLASS ATTRIBUTE - Applies to ALL cats!
    species = 'Mammal'

    # INSTANCE ATTRIBUTES - Different for each INSTANCE of cat
    def __init__(self, name, age):
        #         ^- points back to the CLASS OF CAT
        super().__init__()
        self.name = name
        self.age = age

    #INSTANCE METHOD - Different for each INSTANCE of cat
    def description(self):
        return "{} is {} years old.".format(self.name, self.age)
#                ^----^------another way of doing string interpolation
gus = Cat("Gus", 10)
beans = Cat("Beans", 11)

print(gus.description())
print(beans.description())
