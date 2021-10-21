def punctuation(content_clean):
    """
    Function to check if punctuation is being used in a text entry. 
    Do not use this for names unless ' is removed from check_for string.
    """
    check_for = '''!()-[]{};:'"\,\\<>./?@#$%^&*_~'''
    content = ""
    for x in content_clean:
        if x not in check_for:
            content = content + x
    return content

# testing
name = input("What's your name? >") or "no name given"
print(punctuation(name))
