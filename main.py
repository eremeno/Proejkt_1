"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Oleg Eremenko
email: eremenko.oleg26@gmail.com
"""
# Kód:

# Seznam textů
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

# Registrovaní uživatelé
users  = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# Přihlášení
username = input("username: ")
password = input("password: ")

if users.get(username) != password:
    print("unregistered user, terminating the program..")
    exit()

print("-" * 40)
print(f"Welcome to the app, {username}")
print(f"We have {len(TEXTS)} texts to be analyzed.")
print("-" * 40)

# Výběr textu
selection = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")
print("-" * 40)

if not selection.isdigit() or not (1 <= int(selection) <= len(TEXTS)):
    print("Invalid selection, terminating the program..")
    exit()

text = TEXTS[int(selection) - 1]
words = text.split()

# Odstranění interpunkce a prázdných znaků
cleaned_words = [word.strip(".,:;!?()") for word in words]

# Statistiky
num_words = len(cleaned_words)
titlecase_words = sum(1 for word in cleaned_words if word.istitle())
uppercase_words = sum(1 for word in cleaned_words if word.isupper())
lowercase_words = sum(1 for word in cleaned_words if word.islower())
numeric_strings = [int(word) for word in cleaned_words if word.isdigit()]
sum_numbers = sum(numeric_strings)

# Výpis výsledků
print(f"There are {num_words} words in the selected text.")
print(f"There are {titlecase_words} titlecase words.")
print(f"There are {uppercase_words} uppercase words.")
print(f"There are {lowercase_words} lowercase words.")
print(f"There are {len(numeric_strings)} numeric strings.")
print(f"The sum of all the numbers {sum_numbers}")
print("-" * 40)
print(f"{'LEN':>3}| {'OCCURENCES':<28}|NR.")
print("-" * 40)

# Histogram podle délky slov
lengths = {}
for word in cleaned_words:
    lengths[len(word)] = lengths.get(len(word), 0) + 1

for length in sorted(lengths):
    stars = '*' * lengths[length]
    print(f"{length:>3}| {stars:<28}|{lengths[length]}")
