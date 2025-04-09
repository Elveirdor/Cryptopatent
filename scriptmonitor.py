import os
import subprocess
import sqlite3

# Get the current working directory
current_dir = os.getcwd()

# Create a database to store information about monitored scripts
conn = sqlite3.connect('monitored_scripts.db')
cursor = conn.cursor()

# Create a table to store script information
cursor.execute('''
    CREATE TABLE IF NOT EXISTS scripts (
        id INTEGER PRIMARY KEY,
        script_name TEXT,
        random_number_generator TEXT,
        tip TEXT
    );
''')

# Insert script information into the table
scripts = [
    ('script1.py', 'random.randint(1, 10)', 'Tip 1'),
    ('script2.py', 'random.uniform(1, 10)', 'Tip 2'),
]

cursor.executemany('INSERT INTO scripts VALUES (NULL, ?, ?, ?)', scripts)

# Commit changes and close the connection
conn.commit()
conn.close()

# Define a function to monitor script execution
def monitor_script_execution(script_name):
    # Construct the full path to the script
    script_path = os.path.join(current_dir, script_name)

    # Check if the script exists
    if not os.path.exists(script_path):
        print(f"Script '{script_name}' not found in directory '{current_dir}'.")
        return

    # Run the script and capture the output
    try:
        output = subprocess.check_output(['python', script_path])
    except subprocess.CalledProcessError as e:
        print(f"Error running script '{script_name}': {e}")
        return

    # Check if the output contains a random number
    if b'random' in output:
        # Connect to the database
        conn = sqlite3.connect('monitored_scripts.db')
        cursor = conn.cursor()

        # Retrieve the script information from the database
        cursor.execute('SELECT * FROM scripts WHERE script_name = ?', (script_name,))
        script_info = cursor.fetchone()

        # If a match is found, generate a new tip to the police
        if script_info:
            tip = script_info[3]
            print(f'Generating tip to the police: {tip}')

            # Send the tip to the police (e.g., via email or API)
            # ...

# Monitor script execution
scripts_to_monitor = ['script1.py', 'script2.py']
for script_name in scripts_to_monitor:
    monitor_script_execution(script_name)
