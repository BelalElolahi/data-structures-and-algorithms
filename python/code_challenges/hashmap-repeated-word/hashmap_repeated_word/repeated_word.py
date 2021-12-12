import re
def repeated_word(string):
    string=string.lower()
    string=res = re.sub(r'[^\w\s]', '', string)
    words=re.split('\s+',string)
    print(words)
    check=[]
    for word in words:
        if word in check:
            return word
        else:
            check.append(word)
    return 'no repetetion'





