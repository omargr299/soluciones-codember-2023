from urllib.request import urlopen

var = 0

data = urlopen("https://codember.dev/data/message_02.txt")
lines = data.read().decode("utf-8")
print(lines)

for line in lines:
    for c in line:
        if c=="&":
            print(var,end="")
        elif c=="#":
            var+=1
        elif c=="@":
            var-=1
        elif c=="*":
            var**=2