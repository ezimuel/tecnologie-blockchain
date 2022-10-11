## Laboratorio di Tecnologie Blockchain

Questo repository contiene le esercitazioni svolte durante il corso di **Tecnologie Blockchain** tenuto dal docente [Enrico Zimuel](https://www.zimuel.it/) presso l'[ITS-ICT Piemonte](https://www.its-ictpiemonte.it/) di Torino.

### Markle Tree

Scrivere un programma in Python che sia in grado di leggere un insieme di file e calcolare il [Merkle tree](https://en.wikipedia.org/wiki/Merkle_tree) root utilizzando la funzione hash SHA256.

Soluzione in [merkle/merkle_tree.py](merkle/merkle_tree.py)

### Proof of Work

Scrivere un programma in Python che sia in grado di risolvere il Proof of Work (PoW) utilizzato in Bitcoin. In particolare, il programma deve accettare in input una stringa da verificare e il valore target (espresso come `2^x`). E' necessario calcolare il nonce (numerico) da aggiungere alla stringa in input affinchè `SHA256(input || nonce) < target`, dove `||` è l’operazione di concatenazione di stringhe.

Soluzione in [PoW/pow.py](PoW/pow.py)

## Generare un indirizzo Bitcoin

Scrivere un programma in Python per generare un indirizzo Bitcoin valido. Per verificare che l'indirizzo generato sia valido è possibile utilizzare [questo](https://thomas.vanhoutte.be/tools/validate-bitcoin-address.php) servizio.

Per generare un indirizzo Bitcoin è possibile leggere il seguente [post](https://medium.com/coinmonks/bitcoin-address-generation-on-python-e267df5ff3a3)

Soluzione in [indirizzo_Bitcoin/indirizzo.py](indirizzo_Bitcoin/indirizzo.py)
