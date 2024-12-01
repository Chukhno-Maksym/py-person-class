class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:

    person_list = [Person(person["name"], person["age"]) for person in people]

    for peoples in people:
        person = Person.people[peoples["name"]]
        if peoples.get("wife"):
            person.wife = Person.people[peoples["wife"]]
        elif peoples.get("husband"):
            person.husband = Person.people[peoples["husband"]]

    return person_list
