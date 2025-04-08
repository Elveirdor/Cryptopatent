import random
from git import Repo
import os

# Define the repository URL and the local directory path
repo_url = 'https://github.com/Elveirdor/Elveirdor-AI.git'
repo_path = '/data/data/com.termux/files/home/my_stock_exchange/Elveirdor-AI'

# Check if the directory already exists
if os.path.exists(repo_path):
    # If it exists, delete it
    import shutil
    shutil.rmtree(repo_path)

# Clone the repository to the local directory
repo = Repo.clone_from(repo_url, repo_path)

# Generate a random number
random_number = random.randint(1, 100)

# Create a file with the random number
with open(repo_path + '/random_number.txt', 'w') as f:
    f.write(str(random_number))

# Add the file to the index
repo.git.add('random_number.txt')

# Commit changes
repo.git.commit('-m', f'Random number: {random_number}')

# Push changes to the remote repository
repo.git.push('origin', 'main')
