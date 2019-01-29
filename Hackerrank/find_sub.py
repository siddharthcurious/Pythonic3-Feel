import re
string = 'this is a string where the substring is is repeated this several this times this is boy'

l = re.finditer("this", string)
for e in l:
    print(e)

l = re.findall("this", string)

for e in l:
    print(e)

