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
    # print(spell_book)


def write_book(new_spell, filename='spellbook.json'):
    with open(filename,'r+') as book:
        # First we load existing data into a dict.
        spell_data = json.load(book)
        # Join new_spell with spell_data inside emp_details
        spell_data["spells"].append(new_spell)
        # Sets book's current position at offset.
        book.seek(0)
        # convert back to json.
        json.dump(spell_data, book, indent = 4)


# testing 
name = ""
description = ""
with open('spellbook.txt', 'r') as spell_list, open('spellhint.txt', 'r') as hints:
        for index, line in enumerate(spell_list):
            name = line.strip()
            description = hints[index]
            print(name, description)
# BROKEN
        # for script in hints:
        #     description = script.strip()
        #     print(description)
        # print(name, description)


# print("Make a new spell: ")
# name = input("What's the spell called? ")
# description = input("Describe the spell: ")
# spellcreator(name, description)

# write_book(spell_book)
# code from https://www.geeksforgeeks.org/append-to-json-file-using-python/
