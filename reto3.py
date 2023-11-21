from urllib.request import urlopen
import re


data = urlopen("https://codember.dev/data/encryption_policies.txt")
entradas = data.read().decode("utf-8").split("\n")

invalidas = []
for entrada in entradas:    
    politica, clave = entrada.split(":")
    politica = politica.strip()
    clave = clave.strip()
    rango, letra = politica.split(" ") 
    min_rep, max_rep = rango.split("-")
    repeticiones = re.findall(letra, clave)
    
    
    if len(repeticiones) >= int(min_rep) and len(repeticiones) <= int(max_rep):
        continue
    else:
        invalidas.append(clave)
        
        
print(invalidas[41]) # repsuesta

print(invalidas[12]) # repsuesta 🔒