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
        smells.json.dumps(spell_book, indent = 4)

# testing
print("Make a new light spell!")
name = "Light"
description = "Casts a small amount of light around you, making it easier to see things"

with open('spellbook.txt', 'a') as smells:
    json.dump(spell_book, smells)

spellcreator(name, description)


print("Make a fireball")
name = "Fireball"
description = "Throws a blob of molten something out of the palms of your hands like an old karate guy"

spellcreator(name, description)

with open('spellbook.txt', 'a') as smells:
    json.dump(spell_book, smells)
    raise

### THIS IS HOW TO READ AND ADD TO JSON FILE with structure as spellbook.json is looking.
# code from https://www.freecodecamp.org/news/json-comment-example-how-to-comment-in-json-files/
# import json
 
 
# # function to add to JSON
# def write_json(new_data, filename='data.json'):
#     with open(filename,'r+') as file:
#           # First we load existing data into a dict.
#         file_data = json.load(file)
#         # Join new_data with file_data inside emp_details
#         file_data["emp_details"].append(new_data)
#         # Sets file's current position at offset.
#         file.seek(0)
#         # convert back to json.
#         json.dump(file_data, file, indent = 4)
 
#     # python object to be appended
# y = {"emp_name":"Nikhil",
#      "email": "nikhil@geeksforgeeks.org",
#      "job_profile": "Full Time"
#     }
     
# write_json(y)
