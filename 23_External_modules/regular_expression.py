import re

text = "one two three and to the four Snoop Doggy Dogg and Dr. Dre is at the door"

match = re.search("Dogg",text)

if match:
    print("match found")
    print("start index",match.start())
    print("end index",match.end())

matches = re.findall("the",text,re.IGNORECASE) # case insensitive

print("matches:",len(matches))

new_text = re.sub("Dogg","Cat",text)

print("New text:",new_text)

