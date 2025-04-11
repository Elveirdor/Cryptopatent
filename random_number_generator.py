import random
import time

def generate_random_number(max_value):
    return random.randint(0, max_value)

def main():
    max_value = 100
    while True:
        random_number = generate_random_number(max_value)
        print(f"Random Number: {random_number}")
        time.sleep(1)  # wait 1 second before generating next number

if __name__ == "__main__":
    main()
