from abc import ABCMeta, abstractstaticmethod


class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def person_method():
        """ Interface Method """


class Person(IPerson):

    def person_method(self):
        print("I am a Person!")


class ProxyPerson():

    def __init__(self) -> None:
        self.person = Person()

    def person_method(self):
        print("I'm the proxy functionality!")
        self.person.person_method()


# demo
p1 = Person()
p1.person_method()

# actual demo
p2 = ProxyPerson()
p2.person_method()
