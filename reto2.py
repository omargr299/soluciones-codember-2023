import os 

var = 0

path = os.path.join('messages','message_02.txt')

try:

    with open(path) as file:
        lines = file.readlines()
      
except:
    print("Error al leer el archivo")
    
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