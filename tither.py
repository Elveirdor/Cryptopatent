class Tither:
    def __init__(self):
        self.members = {}
        self.tithes = {}

    def add_member(self, name, email):
        self.members[name] = email
        self.tithes[name] = 0

    def remove_member(self, name):
        if name in self.members:
            del self.members[name]
            del self.tithes[name]
        else:
            print("Member not found.")

    def record_tithe(self, name, amount):
        if name in self.members:
            self.tithes[name] += amount
        else:
            print("Member not found.")

    def view_tithes(self):
        for name, amount in self.tithes.items():
            print(f"{name}: ${amount}")

    def send_notification(self, name):
        if name in self.members:
            email = self.members[name]
            print(f"Sending notification to {email}...")
        else:
            print("Member not found.")

def main():
    tither = Tither()

    while True:
        print("1. Add member")
        print("2. Remove member")
        print("3. Record tithe")
        print("4. View tithes")
        print("5. Send notification")
        print("6. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter member name: ")
            email = input("Enter member email: ")
            tither.add_member(name, email)
        elif choice == "2":
            name = input("Enter member name: ")
            tither.remove_member(name)
        elif choice == "3":
            name = input("Enter member name: ")
            amount = float(input("Enter tithe amount: "))
            tither.record_tithe(name, amount)
        elif choice == "4":
            tither.view_tithes()
        elif choice == "5":
            name = input("Enter member name: ")
            tither.send_notification(name)
        elif choice == "6":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
