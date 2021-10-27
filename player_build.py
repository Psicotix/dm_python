from punction import punction
from time import sleep
from yesno import yesno

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

arms = 0
n = 0
while n == False:
    try:
        arms = int(input("Enter a number > "))
        n = 1
    except ValueError:
        print("""
        "An integer value only please, it makes it easier for me to work things out."
        """)
        n = 0


if arms == 0:
    print("""
        "Oh!" She says, looking startled. "I wasn't expecting that."
        """)

characteristics["name"] = name
characteristics["arms"] = arms
print(characteristics)


# 2 / Body height
# 3 / Body build
# 4 / Body mass
