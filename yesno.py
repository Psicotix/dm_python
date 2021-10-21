def yesno(answer):
    """
    Checks positive or negative answer.
    Will return "yes", "no" or "uncertain"
    """
    # Sort out inputs as answers.
    answer.lower()
    yesno = ""
    answer_no = ["non", "no", "nah", "noo", "niet", "never", "no chance",
                 "fuck off", "no fucking way", "fuck that", "no way", "not much"]
    answer_yes = ["yes", "kinda", "kind of", "a bit", "slightly", "loads",
                  "a little", "yeah", "yah", "yup", "yus", "si", "really", "ja", "of course"]

    if answer in answer_yes:
        yesno = "yes"
    elif answer in answer_no:
        yesno = "no"
    else:
        yesno = "uncertain"
    return yesno

# test
answer = input("Is it helping? ")
print(yesno(answer))
