import re
def repeated_word(text):
    arr = re.findall(r'[a-zA-z]*\w',text)
    
    array = []
    for i in arr:
        if i in array:
            return i
        else:
            array.append(i.lower())
    return 'There is no repeated word'


print(repeated_word("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."))
