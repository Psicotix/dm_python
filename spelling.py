"""
Used to create spells and check if spellbook.json has
already been written.
REQUIRES:
    modules: random, json, os
    files:  spellbook.json, spellbook.txt (for names),
            and spellhint.txt (for descriptions)
"""
import random
import json
import os

spell_book = {}


def spellcreator(name, description):
    """
    Creates a spell, taking name and description from elsewhere 
    and adding spell using random characters. 
    Returns: spell_book
    """
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
    """
    Used to write the spell created by spellcreator() into
    spellbook.json by default. No return, as written to file.
    """
    with open(filename,'r+') as book:
        # First we load existing data into a dict.
        spell_data = json.load(book)
        # Join new_spell with spell_data inside emp_details
        spell_data["spells"].append(new_spell)
        # Sets book's current position at offset.
        book.seek(0)
        # convert back to json.
        json.dump(spell_data, book, indent = 4)
# code from https://www.geeksforgeeks.org/append-to-json-file-using-python/



name = ""
description = ""
if os.path.getsize('spellbook.json') <= 25:
    with open('spellbook.txt', 'r') as spell_list, open('spellhint.txt', 'r') as hints:
        names_list = spell_list.readlines()
        # so we now have a dirty list.
        # print(names_list, type(names_list))
        description_list = hints.readlines()
        # we now have two lists. We want to take each element from the list.
        # print(len(names_list)) # so we have our iterable total, currently 9
        # so define a counter starting at 0
        n = 0
        while n < len(names_list):
            name = names_list[n].strip()
            description = description_list[n].strip()
            # we have to clean up the name and description to prevent newline \n to be output in the JSON

            spellcreator(name, description)  # create our unique spell
            write_book(spell_book)  # write it _all_ to the JSON file
            n += 1
else:
    print("Spell book already written! Don't bother doing it again!")
    global full_book
    full_book = os.path.getsize('spellbook.json')
    print(full_book)
