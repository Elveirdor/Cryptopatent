import random

class TeleportationGame:
    def __init__(self):
        self.position = 0
        self.score = 0
        self.story = {
            "goal": "Reach the other side of the walkway",
            "main_character": "Echo",
            "impact_character": "The Architect",
            "problem": "Malfunctioning teleportation device"
        }
        self.y_table = {
            "obstacle_chance": 0.2,
            "pit_chance": 0.4,
            "wall_chance": 0.6,
            "teleport_distance": 10
        }

    def teleport(self):
        new_position = self.position + random.randint(-self.y_table["teleport_distance"], self.y_table["teleport_distance"])
        print(f"Current position: {self.position}")
        print(f"New position: {new_position}")
        self.position = new_position

    def check_obstacles(self):
        obstacle_chance = random.random()
        if obstacle_chance < self.y_table["obstacle_chance"]:
            print("Hit the right wall!")
            self.position += 5
        elif obstacle_chance < self.y_table["pit_chance"]:
            print("Encountered a pit!")
            self.position -= 5
        elif obstacle_chance < self.y_table["wall_chance"]:
            print("Hit the left wall!")
            self.position -= 5

    def update_score(self):
        self.score += 1
        print(f"Score: {self.score}")

    def play_game(self):
        print("Welcome to the Teleportation Game!")
        print(self.story["goal"])
        print(f"Main Character: {self.story['main_character']}")
        print(f"Impact Character: {self.story['impact_character']}")
        print(f"Problem: {self.story['problem']}")

        while True:
            user_input = input("Press 't' to teleport, 'q' to quit: ")
            if user_input.lower() == 't':
                self.teleport()
                self.check_obstacles()
                self.update_score()
            elif user_input.lower() == 'q':
                print("Game over!")
                break
            else:
                print("Invalid input. Please try again.")

if __name__ == "__main__":
    game = TeleportationGame()
    game.play_game()
