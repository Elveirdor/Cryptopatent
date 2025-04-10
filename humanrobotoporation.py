# Import necessary libraries
import speech_recognition as sr
import pyttsx3
import time

# Initialize the speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()

# Define the Elveirdor alphabet
elveirdor_alphabet = {
    'A': 'ahh',
    'E': 'Eh/ah',
    'EE': 'Ē',
    'I': 'I',
    'O': 'A oo',
    'U': 'oo',
    'B': 'bea',
    'C': 'SSS',
    'D': 'day',
    'F': 'Fea',
    'G': 'g',
    'H': 'Hee',
    'J': 'jewel',
    'K': 'Kill',
    'L': 'Lŭ',
    'M': 'my mae',
    'N': 'nee',
    'P': 'Pī',
    'Q': 'Qui',
    'R': 'RAY',
    'S': 'Say',
    'T': 'Tay',
    'Th': 'th they',
    'V': 'bee',
    'W': 'W',
    'X': 'X ese',
    'Y': 'Yay',
    'Z': 'Z',
    'Ch': 'chee',
    'LL': 'yuh',
    'Ph': 'fuh',
    'Wh': 'we-sand',
    'st': 'estay',
    'ck': 'kay'
}

# Define a function to translate Elveirdor to English
def elveirdor_to_english(elveirdor_text):
    english_text = ""
    for char in elveirdor_text:
        if char.upper() in elveirdor_alphabet:
            english_text += elveirdor_alphabet[char.upper()]
        else:
            english_text += char
    return english_text

# Define a function to translate English to Elveirdor
def english_to_elveirdor(english_text):
    elveirdor_text = ""
    for char in english_text:
        for key, value in elveirdor_alphabet.items():
            if value == char:
                elveirdor_text += key
                break
        else:
            elveirdor_text += char
    return elveirdor_text

# Define a function to recognize speech and translate to Elveirdor
def recognize_and_translate():
    with sr.Microphone() as source:
        print("Please say something in English:")
        audio = r.listen(source)
        try:
            english_text = r.recognize_google(audio)
            elveirdor_text = english_to_elveirdor(english_text)
            print(f"Elveirdor translation: {elveirdor_text}")
            engine.say(elveirdor_text)
            engine.runAndWait()
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")

# Define a function to take Elveirdor input and translate to English
def take_elveirdor_input():
    elveirdor_text = input("Please enter Elveirdor text: ")
    english_text = elveirdor_to_english(elveirdor_text)
    print(f"English translation: {english_text}")
    engine.say(english_text)
    engine.runAndWait()

# Main program loop
while True:
    print("1. Recognize and translate English to Elveirdor")
    print("2. Take Elveirdor input and translate to English")
    print("3. Quit")
    choice = input("Please choose an option: ")
    if choice == "1":
        recognize_and_translate()
    elif choice == "2":
        take_elveirdor_input()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")
