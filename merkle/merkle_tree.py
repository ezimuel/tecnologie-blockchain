# Esercizio sui Merkle tree
#
# Scrivere un programma in Python che sia in grado di leggere un insieme di
# file e calcolare il  Merkle tree root utilizzando la funzione hash SHA256.
#
# Laboratorio di Tecnologie Blockchain - Docente: Enrico Zimuel
# ITS ICT Piemonte (https://www.its-ictpiemonte.it/)

from hashlib import sha256
from os import listdir
import os.path

# Calcola il merkle tree root partendo da un array di hash
def merkle(hashes):
    while len(hashes) > 1:
        next_hashes = []
        for i in range(0, len(hashes), 2):
            content = hashes[i] + hashes[i+1] 
            next_hashes.append(sha256(content.encode('utf-8')).hexdigest())
        hashes = next_hashes
    return hashes[0]

# Prendo tutti i file nella cartella tranne lo script in python
script_dir = os.path.dirname(__file__)
files = [f for f in listdir(script_dir) if f != os.path.basename(__file__)]

# Ordino i file per nome
files.sort()
print("File in input del Merkle Tree:")
print(files)

n = len(files)
# Verifico che il numero dei file sia una potenza di 2
# Utilizzo un metodo basato sui numeri binari. Una potenza di 2 espressa
# in notazione binaria ha sempre un unico 1 seguito da 0. Ad esempio 8 è 1000.
# Sottraendo 1 a una potenza di 2 si ottiene un'inversione dei bit. L'1 diventa 0
# e tutti gli altri 0 diventano 1. Quindi 8-1=7 è 0111. Se faccio l'AND tra 8 e 7
# avrò come risultano zero, poichè i bit sono tutti diversi tra loro. Quindi
# posso verificare che un numero n è potenza di 2 se n AND n-1 è uguale a 0.
if not(n & (n-1) == 0 and n != 0):
    print("Errore: il numero di file deve essere una potenza di 2")
    exit(1)

# Calcolo i valori SHA256 di ogni file
hashes = []
for f in files:
    with open(f, 'r') as file:
        file_content = file.read()
    hashes.append(sha256(file_content.encode('utf-8')).hexdigest())

print("\nSHA256 dei file:")
print(hashes)

# Calcolo il merkle tree root e lo stampo
print("\nMerkle tree root: " + merkle(hashes))