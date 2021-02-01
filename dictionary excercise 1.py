
with open('text.txt') as file_object:
    contents = file_object.read()


textDict = {}

for c in contents.split():

    textDict[c] = contents.split().count(c)
    
    
print(textDict)