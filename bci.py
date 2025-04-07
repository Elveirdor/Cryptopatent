import os
import subprocess

# Define the repository URL
repo_url = "https://github.com/Elveirdor/Elveirdor-AI.git"

# Define the repository directory
repo_dir = "Elveirdor-AI"

# Clone the repository
def clone_repo():
    if os.path.exists(repo_dir):
        print(f"Repository '{repo_dir}' already exists. Skipping clone.")
    else:
        subprocess.run(["git", "clone", repo_url])

# Define the language pack
language_pack = {
    "hello": "thaiah neikil weiu",
    "goodbye": "elveirdor othene"
}

# Create a new file with the BCI code
def create_bci_code():
    bci_code = ""
    for key, value in language_pack.items():
        bci_code += f"{key}: {value}\n"
    with open("bci_code.txt", "w") as file:
        file.write(bci_code)

# Main function
def main():
    clone_repo()
    create_bci_code()

if __name__ == "__main__":
    main()
