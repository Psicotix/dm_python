#test:
answer = input("input some text> ").lower()

answer_no = ["fuck off", "no fucking way", "fuck that", "not much",
             "no feckin way", "no chance", "never", "never going to work"]

#     # Now let's split those lists
#testing yes
yesno = "yes"
n = 0
an = len(answer_no)
if len(answer_no) >= 1:
    an = an - 1
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
                yesno = "no"
                n = len(answer_no)
                if yesno == "no":
                    break
                else:
                    n+=1
                    break
            elif None:
                n += 1
        else:
            n += 1
            # pass
        break
print(yesno)
