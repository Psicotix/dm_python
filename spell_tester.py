import json
import time
import datetime

spellb = open('spellbook.json')

spell_dict= json.load(spellb)

# iterate through contents.
print(type(spell_dict))
# let's cast flutter.
a = "Flutter"
for name, description, spell in spell_dict.items():
    if name == a:
        print(spell)
    else:
        exit

time.sleep(5)

time_start = datetime.datetime.now()
spell_input = input("Type your spell now! >>> ")

spellb.close()
