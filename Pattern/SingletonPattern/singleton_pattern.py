from abc import ABCMeta, abstractstaticmethod


class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def print_data():
        """ Implement the child class """


class PersonSingleton(IPerson):

    __instance = None

    def __init__(self, name: str, age: int):
        if PersonSingleton.__instance != None:
            raise Exception("Singleton cannot be instantiated more than once!")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance == None:
            PersonSingleton("Default Name", 0)
        return PersonSingleton.__instance

    @staticmethod
    def print_data():
        print(f"Name: {PersonSingleton.__instance.name}, Age: {PersonSingleton.__instance.age}")


# p = PersonSingleton('Sajidur', 28)
# print(p)
# p.print_data()

# p2 = PersonSingleton('Arif', 30)
