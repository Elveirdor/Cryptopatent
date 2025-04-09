phrases = [
    "Supersteven@supersteven.com",
    "Supersmart@supersmart.com",
    "Busky Steven",
    "Mandalorian Busky",
    "Busky #",
    "Yaba enchancha",
    "Y no habla espaniol",
    "Peanut Tim Tebow",
    "Mrs Ford",
    "Nypolean dynamite",
    "Oh yeah specially con and ding",
    "Goats milk",
    "This is what dreams are made of"
]
def check_phrase(input_text):
    for phrase in phrases:
        if phrase.lower() in input_text.lower():
            return phrase
    return None
