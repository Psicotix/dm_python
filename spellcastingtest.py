#testing spell creation:
import random
import time
import datetime

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
spell_01 = random.sample(characters, 5)
spell_02 = random.sample(characters, 5)

# use join() to convert to strings.
spell_fireball = ''.join(spell_01) + " " + ''.join(spell_02)  #  + " " + ''.join(spell_03)
print("Learn this spell of destructive fire splattering!\n", spell_fireball)

print("Are you ready to practice?")
time.sleep(5)

time_start = datetime.datetime.now()
spell_input = input("Type your spell now! >>> ")
time_end = datetime.datetime.now()
total_spell_time = time_end - time_start
if spell_input == spell_fireball:
    print(f"Well done!\nTotal time to cast spell was: {total_spell_time.seconds} seconds")
    if total_spell_time.seconds <= 10:
         spell_hit = 1
         print("BOOOM! Your spell hits")
    else:
        pass
else:
    print(f"""
	There's a fizzling sound, and your hand feels like it's on fire.
	You took {total_spell_time.seconds} seconds to fuck that spell up!""")
