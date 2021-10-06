# BUILD A CHARACTER
# 1 / Hair style

# define Yes and No possible answers
answer_no = ["non", "no", "nah", "noo", "niet", "never", "no chance", "fuck off", "no fucking way", "fuck that",]
answer_yes = ["yes", "kinda", "a bit", "slightly", "loads", "yeah", "yah", "yup", "yus", "si", "really"]
answer_indecisive = ["maybe", "mebbe", "not sure"]
# define punctuation to take it out
punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

print("You wake up. You're on a bunk, crisp and surprisingly clean. "
      "The indentation your body has made suggests that you've been sleeping here for a while"
      "Blinking you see an old lady who seems to be looking at you.")
print("Do you look closer at her?")
punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
answer_01 = input("> ").lower() or "yes"

# Clean up answer:
clean = ""
for letter in answer_01:
    if letter not in punctuation:
        clean = clean + letter
answer_01 = clean
print(answer_01)

answer_positive = any(x in answer_01 for x in answer_yes)
if answer_positive:
      print("Hello")
else:
      print("Goodbye")

# 2 / Body height
# 3 / Body build
# 4 / Body mass
