import re
txt ="The rain in Spain"
# x = re.search("^The.*Spain$" ,txt)
x=re.findall("spain$",txt)
if x:
    print("match")
else:
    print("no match")

