from urllib.request import urlopen

data = urlopen("https://codember.dev/data/files_quarantine.txt")
files = data.read().decode("utf-8").split("\n")
true_files = []

for file in files:
    left,right = file.split("-")
    
    counts = {}
    for c in left:
        counts[c] = counts.get(c,0) + 1
    
    once_letters = [c for c in counts if counts[c] == 1]
    ouput = "".join(once_letters)
    
    if ouput == right:
        true_files.append(right)
        
print(true_files[32])



