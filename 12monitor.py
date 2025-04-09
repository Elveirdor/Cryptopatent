import subprocess

def detect_monitors():
    try:
        # Get the number of monitors
        num_monitors = int(subprocess.check_output(["xrandr", "--listmonitors"]).decode().splitlines()[1].split()[1])
        
        # Print the number of monitors
        print(f"Number of monitors: {num_monitors}")
        
        # Get the dimensions of each monitor
        for i in range(num_monitors):
            monitor_dimensions = subprocess.check_output(["xrandr", "--listmonitors"]).decode().splitlines()[i+2].split()[2:]
            print(f"Monitor {i+1} dimensions: {'x'.join(monitor_dimensions)}")
    
    except Exception as e:
        print(f"Error detecting monitors: {e}")

detect_monitors() 

import subprocess

def configure_monitors():
    try:
        # Set the primary monitor
        subprocess.run(["xrandr", "--output", "HDMI-1", "--primary"])
        
        # Set the secondary monitor
        subprocess.run(["xrandr", "--output", "HDMI-2", "--right-of", "HDMI-1"])
    
    except Exception as e:
        print(f"Error configuring monitors: {e}")

configure_monitors()
