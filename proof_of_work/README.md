## Consegna


- Scrivere un programma in qualsiasi linguaggio che sia 
  in grado di calcolare il nonce di un blocco utilizzando l’algoritmo PoW presentato nelle slide precedenti.
- In particolare, questo programma deve accettare in 
  input una stringa da verificare e il valore target
- Il nonce dovrà essere un valore tale che:
SHA256(input || nonce) < target
dove || è l’operazione di concatenazione di stringhe.
 