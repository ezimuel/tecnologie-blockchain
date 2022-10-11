# Esercizio sui Merkle tree
#
# Scrivere un programma in Python che sia in grado di leggere un insieme di
# file e calcolare il  Merkle tree root utilizzando la funzione hash SHA256.
# Nel caso in cui il numero dei nodi (file) sia dispari è necessario duplicare
# l'ultimo nodo per rendere il numero degli elementi pari
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
            content = hashes[i] + (hashes[i+1] if i+1 < len(hashes) else hashes[i])
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