class Person:

    def __init__(self, name="nameless", height=0, age=0):
        self.name = name
        self.height = height
        self.age = age

    @property
    def name(self):
        print("Retrieving data: 32%")
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def height(self):
        print("Retrieving data: 64%")
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def age(self):
        print("Retrieving data: 100%")
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    def details(self):
        print(f"Confirm that your Name is {self.name} "
              f"height is {self.height} "
              f"age is {self.age}")


def main():
    person = Person()

    name = input("Enter you Name\n")
    height = input("Enter your Height\n")
    age = input("Enter your Age\n")

    person.name = name
    person.age = age
    person.height = height

    person.details()


main()