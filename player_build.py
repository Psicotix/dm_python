from punction import punction
from time import sleep
from yesno import yesno
from random import randint

# BUILD A CHARACTER
# 1 / Hair style
characteristics = {}
print("""
    You wake up. You're on a bunk, crisp and surprisingly clean.
    The indentation your body has made suggests that you've been 
    sleeping here for a while.
    Blinking and wiping your eyes you see an old lady sitting on
    a rocking chair to your left, knitting rapidly.

    She looks up as you stir, lays the needles on her lap and
    turns to face you.""")
sleep(1.2)
print("""
        "What the hell are you?! My eyes aren't great - I can't
        tell if you're a turnip, a goat or a widow! You may even
        be a bee!" """)
sleep(1)
print("""
    Her tone is gruff, but there's a taste of sweetness there too,
    suggesting that this woman has maybe enjoyed life, or as much
    of it as she's experienced.""")
sleep(1)
print("""
        "Tell me something, so I can work out if you're a goat 
        or a bee, or maybe just an inanimate turnip getting blown
        around by a strong breeze..."
    """)
print("What do you do?")

answer_01 = punction(input("> ").lower()) or "hello"

# Clean up answer:
answer = answer_01.split()

n = 0
length = len(answer)
# print(length)
while n < length:
    for x in answer:
        if x == "hello" or x == "greeting" or x == "greet":
            print("""
        "Well, hello there!" She replies. 
                """)
            sleep(1.2)
            print("""
        "I've been waiting for you to wake up. My eyes aren't
        great you see, and you've been rolling around quite a bit. 
        I can barely see you, to be truthful."  """)
            sleep(1.2)
            print("""She rearranges herself, making herself comfortable, and asks:
        "So what's your name?"
                """)
            n = length
            # print(n)
            break
        else:
            n += 1
    else:
        print("""
        "You'll have to speak up now... I didn't hear that." """)
        sleep(1.2)
        print("""She leans forward and asks:
        "What's your name?" """)
        break

name = punction(input("> "))

print("""
    The old lady sits back with a quick "Hmph" beneath her breath.
        "You do realise you could have told me anything there and
        I'd not have known if you were telling me the truth or not?" """)
sleep(1)
print(f"""
        "Well, it'll have to do. {name} it is then. I'll just call you..."
    She pauses.""")
sleep(1)
print(f"""
        "I'll just call you {name} from now on, whether you like it or not." 

    She mumbles something under her breath that sounds a lot like "feckin' eejit".
        "OK {name}, so... how many arms do you have? Just give me a number"
    """)

arms = ""
while arms is not int:
    try:
        arms = int(input("Enter a number > "))
        break
    except ValueError:
        print("""
        "An integer value only please, you know, like numbers, 21 or something like
        that. Although if it were 21 I'm guessing you'd be very small. It just makes 
        it easier for me to work things out."
        """)
dex = 50

if arms == 0:
    print("""
        "Oh!" She exclaims, looking startled. "I wasn't expecting that. This could be
        difficult then."  """)
    dex = 10
elif arms <= 2:
    print("""
        "A fine number of arms" the old lady says, "and a very easy pattern for me to work with."
        """)
    dex = dex + randint(25,48)
elif arms <= 4:
    print("""
        "Well, that's a manageable number for us to work with," the old lady says, "Though I do
        wonder how you keep them all in check."
        """)
    dex = dex + randint(10,60)
    if dex > 100:
        dex = randint(85, 99)
elif arms <= 8:
    print("""
        "Oh my word, that's an awful number of arms... I'm surprised you fit in the bed!" 

    The old lady seems genuinely surprised, but recovers very quickly.
        """)
    dex = 30 + randint(1, 30)
else:
    print("""
        "Oh you poor thing!" exclaims the old lady. "They must be very short indeed for you to be able
        to walk around, or even just walk through doors, or around a vase without knocking it over."

        "I'll skip making you a sweater for now I think, that many sleeves would be an absolute horror."
        """)
    dex = 20 + randint(1, 20)

characteristics["name"] = name
characteristics["arms"] = arms
characteristics["dex"] = dex
print(characteristics)


# 2 / Body height
# 3 / Body build
# 4 / Body mass
