import re  #re --  regular expression
word="Simple regular expression example"
result=re.findall("gula",word)
print(result)

space=re.search("\s",word)
print("\n The first space is at:",space.start())
