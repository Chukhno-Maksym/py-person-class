class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:

    person_list = []

    for peoples in people:
        person_list.append(Person(peoples["name"], peoples["age"]))

    for peoples in people:
        person = Person.people[peoples["name"]]
        spouse_name = peoples.get("wife") or peoples.get("husband")
        if spouse_name:
            spouse = Person.people.get(spouse_name)
            if spouse:
                if "wife" in peoples:
                    person.wife = spouse
                else:
                    person.husband = spouse

    return person_list
