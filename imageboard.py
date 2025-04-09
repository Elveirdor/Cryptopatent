import hashlib
import json

name_map = {
    1: "Sonja", 2: "Sherman", 3: "Lauren", 4: "Dennis", 5: "Aaron",
    6: "Morgan", 7: "Dawson", 8: "John", 9: "Tim", 10: "Chris",
    11: "Richard", 12: "Tim", 13: "Ray"
}

class Person:
    def __init__(self, number, birthdate, mother, father):
        self.name = name_map[number]
        self.birthdate = birthdate
        self.mother = mother
        self.father = father
        self.predictions = self.generate_predictions()

    def generate_predictions(self):
        if self.mother["personality"] == "nurturing":
            return f"{self.name} will have a happy life."
        elif self.father["personality"] == "adventurous":
            return f"{self.name} will have an exciting life."
        else:
            return f"{self.name} will have a balanced life."

def create_person():
    number = int(input("Enter number: "))
    birthdate = input("Enter birthdate: ")
    mother_name = input("Enter mother's name: ")
    mother_personality = input("Enter mother's personality: ")
    father_name = input("Enter father's name: ")
    father_personality = input("Enter father's personality: ")

    person = Person(number, birthdate, {"name": mother_name, "personality": mother_personality}, {"name": father_name, "personality": father_personality})
    people[number] = person
    save_people()
    print(person.predictions)

def view_person():
    number = int(input("Enter number: "))
    if number in people:
        person = people[number]
        print(f"Name: {person.name}")
        print(f"Birthdate: {person.birthdate}")
        print(f"Mother's Name: {person.mother['name']}")
        print(f"Mother's Personality: {person.mother['personality']}")
        print(f"Father's Name: {person.father['name']}")
        print(f"Father's Personality: {person.father['personality']}")
        print(f"Predictions: {person.predictions}")
    else:
        print("Person not found.")

def save_people():
    people_data = []
    for person in people.values():
        people_data.append({
            "number": list(name_map.keys())[list(name_map.values()).index(person.name)],
            "birthdate": person.birthdate,
            "mother": person.mother,
            "father": person.father
        })
    with open("people.json", "w") as file:
        json.dump(people_data, file)

def load_people():
    try:
        with open("people.json", "r") as file:
            people_data = json.load(file)
            for person_data in people_data:
                person = Person(person_data["number"], person_data["birthdate"], person_data["mother"], person_data["father"])
                people[person_data["number"]] = person
    except FileNotFoundError:
        pass

people = {}
load_people()

while True:
    print("\n1. Create Person")
    print("2. View Person")
    print("3. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        create_person()
    elif choice == "2":
        view_person()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")
