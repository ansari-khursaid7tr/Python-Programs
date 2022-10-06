import re
'''pattern = r"def$"
myString = "abcdef"'''

pattern = r"^[a-zA-Z0-9_.]+@gmail.com"
myString = "ansari.khursaid7tr@gmail.com"
print(re.match(pattern,myString))
