#testing spell creation:
import random
import time
import datetime 

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
spell_01 = random.sample(characters, 5)
spell_02 = random.sample(characters, 5)
# spell_03 = random.sample(characters, 5)
# use join() to convert to strings.
spell_1 = ''.join(spell_01) + " " + ''.join(spell_02)  #  + " " + ''.join(spell_03)
print("Learn this spell of spelling!\n", spell_1)

print("Are you ready to practice?")
time.sleep(5)

time_start = datetime.datetime.now()
spell_input = input("Type your spell now! >>> ")
time_end = datetime.datetime.now()
total_spell_time = time_end - time_start
if spell_input == spell_1:
    print(f"Well done!\nTotal time to cast spell was: {total_spell_time.seconds} seconds")
    if total_spell_time.seconds <= 10:
        print("woot")
    else:
        pass
else:
    print(f"You took {total_spell_time.seconds} seconds to fuck that spell up!")
