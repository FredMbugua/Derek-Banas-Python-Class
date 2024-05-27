class Person:
    def __init__(self, name="nameless", age=0):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    def details(self):
        print("Name is {}, {} years old and".format(self.name, self.age), end=" ")


class Adult(Person):
    def __init__(self, name, age, profession):
        Person.__init__(self, name, age)
        self.profession = profession

    def detail(self):
        Person.details(self)
        print("works as {}".format(self.profession))

    @property
    def profession(self):
        return self.__profession

    @profession.setter
    def profession(self, value):
        self.__profession = value


class Child(Person):
    def __init__(self, name, age, school):
        Person.__init__(self, name, age)
        self.school = school

    @property
    def school(self):
        return self.__school

    @school.setter
    def school(self,value):
        self.__school = value

    def detail(self):
        Person.details(self)
        print("studies in {}".format(self.school))


def main():
    a = Adult("Amos", 28,  "ICT officer")
    b = Adult("Rhema",  24,  "Human Resource Officer")
    c = Child("Benny", 10, "Eldoret Union Primary School")
    d = Child("Nami", 13, "Precious Blood Riruta")
    people = [a, b, c, d]
    for person in people:
        person.detail()


main()
