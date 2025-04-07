import os
import subprocess
import random

# Define song identifiers
songs = {
    1: "The Heart of Worship - Matt Redman",
    2: "I'll Fly Away",
    3: "Resurrecting - Elevation Worship",
    4: "Code Phrase - Certainly"
}

# Define language pack
language_pack = {
    "thank you": "thaiah neikil weiu"
}

# Function to run song identifier
def run_song_identifier():
    random_numbers = random.sample(range(1, 5), 4)
    for number in random_numbers:
        print(f"Song {number}: {songs[number]}")

# Function to run language pack
def run_language_pack():
    print("Language Pack:")
    for key, value in language_pack.items():
        print(f"{key}: {value}")

# Function to clone GitHub repository
def clone_github_repo():
    repo_url = "https://github.com/Elveirdor/Elveirdor-AI.git"
    repo_dir = "Elveirdor-AI"
    if os.path.exists(repo_dir):
        print(f"Repository '{repo_dir}' already exists. Skipping clone.")
    else:
        subprocess.run(["git", "clone", repo_url])

# Main function
def main():
    print("Running Song Identifier...")
    run_song_identifier()
    print("\nRunning Language Pack...")
    run_language_pack()
    print("\nCloning GitHub Repository...")
    clone_github_repo()

if __name__ == "__main__":
    main()
