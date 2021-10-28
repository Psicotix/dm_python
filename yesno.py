"""
Check whether an answer is positive, negative or just indifferent.
"""
def yesno(answer):
    answer_no = ["fuck off", "no sirree", "no sirree", "no fucking way", "fuck that", "not much",
                 "no feckin way", "no chance", "never", "never going to work", "not likely", "unlikely",
                 "na", "nah", "not much good", "a bit shit", "a bit useless", "nope", "niet"]
    answer_yes = ["yes", "kinda", "kind of", "a bit", "a tiny bit", "a little bit", "a small", "slightly", "loads",
                  "a little", "yeah", "yah", "yup", "yus", "si", "really", "ja", "of course", "very much so",
                  "yes siree", "yes sirree", "fuck yeah"]
    ans_status = ""
    an = len(answer_no)
    n = 0
    # n should remain 0 or iteration until next item in list is checked.
    for x in answer_no:
        # while comes after for so that we iterate correctly, else for will always just check index[0]
        while n < an:
            # p is probably a string at this point already.
            test_negative = x
            test_negative = test_negative.split()
            test_answer = answer.split()
            if all(x in test_negative for x in test_answer):
                if True:
                    ans_status = "no"
                    n = len(answer_no)
                    if ans_status == "no":
                        break
                    else:
                        n += 1
                        break
            else:
                n += 1
                # pass
            break
    an = len(answer_yes)
    # if len(answer_yes) >= 1:
    #     an = an - 1
    n = 0
    for z in answer_yes:
        # while comes after for so that we iterate correctly, else for will always just check index[0]
        while n < an:
            # p is probably a string at this point already.
            test_positive = z
            test_positive = test_positive.split()
            test_answer = answer.split()
            if all(z in test_positive for z in test_answer):
                if True:
                    ans_status = "yes"
                    n = len(answer_yes)
                    if ans_status == "yes":
                        break
                    else:
                        n += 1
                        break
            else:
                n += 1
                # pass
            break

        if not ans_status:
            # print("WTF?")
            print()
            ans_status = "uncertain"

    return ans_status


# testing lines
# f = input("input some text> ").lower()
# print(yesno(f))
