import hashlib
import tkinter as tk
from tkinter import messagebox
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
    number = int(number_entry.get())
    birthdate = birthdate_entry.get()
    mother_name = mother_name_entry.get()
    mother_personality = mother_personality_entry.get()
    father_name = father_name_entry.get()
    father_personality = father_personality_entry.get()

    person = Person(number, birthdate, {"name": mother_name, "personality": mother_personality}, {"name": father_name, "personality": father_personality})
    people[number] = person
    save_people()
    messagebox.showinfo("Predictions", person.predictions)

def view_person():
    number = int(view_number_entry.get())
    if number in people:
        person = people[number]
        messagebox.showinfo("Person Information", f"Name: {person.name}\nBirthdate: {person.birthdate}\nMother's Name: {person.mother['name']}\nMother's Personality: {person.mother['personality']}\nFather's Name: {person.father['name']}\nFather's Personality: {person.father['personality']}\nPredictions: {person.predictions}")
    else:
        messagebox.showerror("Error", "Person not found.")

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

people = {}

root = tk.Tk()
root.title("Numerology and Genealogy Predictions")

create_frame = tk.Frame(root)
create_frame.pack()

tk.Label(create_frame, text="Number:").pack()
number_entry = tk.Entry(create_frame)
number_entry.pack()

tk.Label(create_frame, text="Birthdate:").pack()
birthdate_entry = tk.Entry(create_frame)
birthdate_entry.pack()

tk.Label(create_frame, text="Mother's Name:").pack()
mother_name_entry = tk.Entry(create_frame)
mother_name_entry.pack()

tk.Label(create_frame, text="Mother's Personality:").pack()
mother_personality_entry = tk.Entry(create_frame)
mother_personality_entry.pack()

tk.Label(create_frame, text="Father's Name:").pack()
father_name_entry = tk.Entry(create_frame)
father_name_entry.pack()

tk.Label(create_frame, text="Father's Personality:").pack()
father_personality_entry = tk.Entry(create_frame)
father_personality_entry.pack()

create_button = tk.Button(create_frame, text="Create Person", command=create_person)
create_button.pack()

view_frame = tk.Frame(root)
view_frame.pack()

tk.Label(view_frame, text="Number:").pack()
view_number_entry = tk.Entry(view_frame)
view_number_entry.pack()

view_button = tk.Button(view_frame, text="View Person", command=view_person)
view_button.pack()

root.mainloop()
