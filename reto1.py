from urllib.request import urlopen

counts = {}

data = urlopen("https://codember.dev/data/message_01.txt")
words = data.read().decode("utf-8").split(" ")
print(words)

for word in words:
    word = word.lower()
    word = word.strip()
    word = word.replace(".", "")
    word = word.replace(",", "")
    word = word.replace("\n", "")
    counts[word] = counts.get(word, 0) + 1
    

output = ""

for key, value in counts.items():
    output += f"{key}{value}"
    
print(output)