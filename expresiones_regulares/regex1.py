import re


text = "The quick brunc dog"

x =  re.search("^The.*dog$", text)

if x:
    print("si")
else:
    print("no")