import os 

counts = {}

path= os.path.join('messages','message_01.txt')

with open(path) as file:
    text = file.readlines()
    words = text[0].split()
    for word in words:
        word = word.lower()
        counts[word] = counts.get(word, 0) + 1
    

output = ""

for key, value in counts.items():
    output += f"{key}{value}"
    
print(output)