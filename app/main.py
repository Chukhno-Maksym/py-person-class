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
        if "wife" in peoples and peoples["wife"]:
            person.wife = Person.people.get(peoples["wife"])
        elif "husband" in peoples and peoples["husband"]:
            person.husband = Person.people.get(peoples["husband"])

    return person_list
