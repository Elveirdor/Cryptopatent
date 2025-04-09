phrases = [
    "Supersteven@supersteven.com",
    "Supersmart@supersmart.com",
    "Busky Steven to Mandalorian",
    "Busky #",
    "Yaba enchancha Y no habla espaniol",
    "Peanut", "Tim Tebow", "Mrs Ford",
    "Nypolean dynamite",
    "Oh yeah specially con and ding",
    "Goats milk",
    "This is what dreams are made of"
]

def check_phrase(input_text):
    for phrase in phrases:
        if phrase.lower() in input_text.lower() or input_text.lower() in phrase.lower():
            return phrase
    return None

def main():
    input_text = input("Enter some text: ")
    matched_phrase = check_phrase(input_text)
    if matched_phrase:
        print(f"Matched phrase: {matched_phrase}")
    else:
        print("No match found.")

if __name__ == "__main__":
    main()
