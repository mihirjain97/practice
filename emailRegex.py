import re

text = "my EMail addreSS: 19/09/20 Hello.world1997@gmail.com . Some more Random Text . WorldHello-1999@yahoo.com"

# pattern = re.compile("[a-zA-Z0-9|()\-\_\:\.]+@[a-zA-Z0-9]+\.[a-zA-Z]+")
pattern = re.compile("[a-zA-Z0-9/ /: /. /@ /-]+")
result = pattern.findall(text)
print(result)
