import tty
import termios
import sys

typed_text = ""

# Get the current terminal settings
fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)

try:
    # Turn off echoing and buffering
    tty.setraw(sys.stdin.fileno())

    while True:
        key = sys.stdin.read(1)
        typed_text += key
        for letter in "abcdefghijklmnopqrstuvwxyz":
            if letter in typed_text:
                print(f"Letter '{letter}' detected!")
                typed_text = typed_text.replace(letter, "")
        if key == "\x1b":  # Esc key
            break
finally:
    # Restore the original terminal settings
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
