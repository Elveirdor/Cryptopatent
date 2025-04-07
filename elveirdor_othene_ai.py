# Define the Elveirdor Othene AI code
elveirdor_code = "7919 ---> 10111 ---> 18198 ---> 8088"

# Define the filename
filename = "elveirdor_othene_ai_code.txt"

# Function to create the file and write the code
def create_file():
    with open(filename, "w") as file:
        file.write(elveirdor_code)
    print(f"File '{filename}' created with Elveirdor Othene AI code.")

# Function to read the code from the file
def read_file():
    try:
        with open(filename, "r") as file:
            code = file.read()
        print(f"Elveirdor Othene AI code: {code}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

# Main function
def main():
    create_file()
    read_file()

if __name__ == "__main__":
    main()
