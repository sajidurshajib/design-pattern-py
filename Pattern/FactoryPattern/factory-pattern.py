from abc import ABCMeta, abstractclassmethod
from decimal import InvalidContext
from sys import argv


class IPerson(metaclass=ABCMeta):

    @abstractclassmethod
    def person_method():
        """Interface method"""


class Student(IPerson):

    def __init__(self) -> None:
        self.name = "Basic Student Name"

    def person_method(self):
        print("I'm a Student")


class Teacher(IPerson):

    def __init__(self) -> None:
        self.name = "Basic Student Name"

    def person_method(self):
        print("I'm a Teacher")


class PersonFactory:

    @staticmethod
    def build_person(person_type: int):
        if person_type == 0:
            return Student()
        if person_type == 1:
            return Teacher()
        print("Invalid person number")
        return -1


if __name__ == "__main__":
    choice = argv[1]
    person = PersonFactory.build_person(int(choice))
    person.person_method() if person != -1 else ""
