# Esercizio sul PoW
#
# Scrivere un programma in Python che sia in grado di risolvere il
# PoW utilizzato in Bitcoin. In particolare, il programma deve accettare in 
# input una stringa da verificare e il valore target (espresso come 2^x)
# E' necessario calcolare il nonce (numerico) da aggiungere alla stringa
# in input per ottenere SHA256(input || nonce) < target, 
# dove || è l’operazione di concatenazione di stringhe.
#
# Laboratorio di Tecnologie Blockchain - Docente: Enrico Zimuel
# ITS ICT Piemonte (https://www.its-ictpiemonte.it/)
from hashlib import sha256

print('Inserire il valore di target sotto forma di 2^x')

base = 2
x = int(input('Inserire il valore dell\'esponente (x): '))
target = pow(2, x)

input = input('Inserire la string in input: ')

nonce = -1
while True:
    nonce += 1
    hash = sha256(f'{input}{nonce}'.encode('utf-8')).hexdigest()
    if int(hash, 16) < target:
        break

print(f'Il valore del nonce è: {nonce}')
print(f'SHA256("{input}{nonce}") < 2^{x}')