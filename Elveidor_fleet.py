import hashlib
import json

# Define a name map for Person class
name_map = {
    1: "Sonja", 2: "Sherman", 3: "Lauren", 4: "Dennis", 5: "Aaron",
    6: "Morgan", 7: "Dawson", 8: "John", 9: "Tim", 10: "Chris",
    11: "Richard", 12: "Tim", 13: "Ray"
}

# Define a Person class
class Person:
    def __init__(self, number, birthdate, mother, father):
        """
        Initialize a Person object.
        """
        self.name = name_map[number]
        self.birthdate = birthdate
        self.mother = mother
        self.father = father
        self.predictions = self.generate_predictions()

    def generate_predictions(self):
        """
        Generate predictions for the person based on their parents.
        """
        if self.mother["personality"] == "nurturing":
            return f"{self.name} will have a happy life."
        elif self.father["personality"] == "adventurous":
            return f"{self.name} will have an exciting life."
        else:
            return f"{self.name} will have a balanced life."

# Define a Ship class
class Ship:
    def __init__(self, name, ship_id, online_id, material_id, specifications):
        """
        Initialize a Ship object.
        """
        self.name = name
        self.ship_id = ship_id
        self.online_id = online_id
        self.material_id = material_id
        self.specifications = specifications

# Define a Fleet class
class Fleet:
    def __init__(self, name):
        """
        Initialize a Fleet object.
        """
        self.name = name
        self.ships = []

    def add_ship(self, ship):
        """
        Add a ship to the fleet.
        """
        self.ships.append(ship)

    def teleport(self, destination):
        """
        Teleport the fleet to a destination.
        """
        print(f"Teleporting {self.name} fleet to {destination}...")

# Define an ElveirdorFleet class
class ElveirdorFleet(Fleet):
    def __init__(self):
        """
        Initialize an ElveirdorFleet object.
        """
        super().__init__("Elveirdor")

    def regime(self):
        """
        Print the Elveirdor Fleet's regime.
        """
        print("Elveirdor Fleet Regime:")
        print("Explore galaxy, defend against threats, engage in trade.")

# Create ships
elveirdor = Ship("Elveirdor", "75298484751231232975", "2975848475@123123@2975", "29758484751231232975", {
    "shape": "Flat on top and bottom",
    "glass_squares": "Slightly stretched out glass squares"
})

comb = Ship("Comb", "75298484751231232975", "2975848475@123123@2975", "29758484751231232975", {
    "shape": "Flat on top and bottom",
    "captains_window": "Facing the sun with thick glass"
})

juan_60s = Ship("Juan 60's", "75298484751231232975", "2975848475@123123@2975", "29758484751231232975", {
    "shape": "Similar to Comb ship",
    "cuts": "Cuts from outside to inside"
})

sonic = Ship("Sonic", "75298484751231232975", "2975848475@123123@2975", "29758484751231232975", {
    "shape": "Similar to Speedway big gulp cup",
    "rotating_floorboards": "Inside that align with doorways"
})

# Create fleet
elveirdor_fleet = ElveirdorFleet()
elveirdor_fleet.add_ship(elveirdor)
elveirdor_fleet.add_ship(comb)
elveirdor_fleet.add_ship(juan_60s)
elveirdor_fleet.add_ship(sonic)

# Print fleet information
print("Elveirdor Fleet:")
for ship in elveirdor_fleet.ships:
    print(f"Ship: {ship.name}")
    print(f"Ship ID: {ship.ship_id}")
    print(f"Specifications: {ship.specifications}")

# Print link to documentation
print("For more information, see:")
print("https://docs.google.com/document/d/1_X6m8KDTGvHMg9gA2TGkVDO2jdcQBnx4IuijKR5nBNM/edit?usp=drivesdk")
