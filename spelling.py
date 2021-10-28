#testing spell creation:
import random
import json
spell_book = {}


def spellcreator(name, description):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
    spell_01 = random.sample(characters, 5)
    spell_02 = random.sample(characters, 5)
    spell = ""
    # use join() to convert to strings.
    # spell_name = "spell_" + name
    # print(spell_name)

    spell = ''.join(spell_01) + " " + ''.join(spell_02)  #  + " " + ''.join(spell_03)
    spells = spell_book.update({"name": name, "description": description, "spell": spell})

    return (spell_book)
    with open('spellbook.txt', 'a') as smells:
        json.dumps(smells.write(spell_book))

# testing
print("Make a new light spell!")
name = "Light"
description = "Casts a small amount of light around you, making it easier to see things"
spellcreator(name, description)
print(spell_book)
print("Make a fireball")
name = "Fireball"
description = "Throws a blob of molten something out of the palms of your hands like an old karate guy"
spellcreator(name, description)

with open('spellbook.txt', 'r') as smells:
    print(smells.read())
