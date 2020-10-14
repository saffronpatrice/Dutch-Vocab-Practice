from random import choice

dutch = {}
english_keys = []
# {key is english: value is dutch}

words = open("A2 Vocab.txt")

for line in words:
    x = line.rstrip().split(";")
    key = x[0]
    value = x[1]
    dutch[key] = value
    english_keys.append(key)

while True:
    english_key = choice(english_keys)
    answer = input("Translate: " + english_key + "\n")
    dutch_value = dutch[english_key]

    if answer == dutch_value:
        print("Goed antwoord!")
    else:
        print("Sorry! The correct answer is: " + dutch_value + ".")
    print("")