# Cos'é HashCat
Hashcat è uno strumento di recupero password avanzato che sfrutta la potenza di calcolo delle GPU per eseguire attacchi di: bruteforcing, combination attack, mask attack e dizionari su hash delle password. Supporta una vasta gamma di algoritmi di hashing ed è noto per la sua velocità ed efficienza.

## Come funziona?

Hashcat utilizza diverse modalità di attacco per cercare di recuperare le password originali dagli hash. Alcune delle modalità principali includono:

- Dizionario (Dictionary Attack): Utilizza un elenco di parole (dizionario) come input per tentare di trovare la corrispondenza.
- Forza Bruta (Brute-force Attack): Prova tutte le possibili combinazioni di caratteri fino a trovare la password corretta.
- Combinazione (Combination Attack): Combina due dizionari insieme.
- Maschera (Mask Attack): Simile alla forza bruta, ma limitata a un set specifico di caratteri e una lunghezza definita.

## Esempi pratici

**Crack di un hash MD5 con dizionario**

Creiamo un file contente l'hash

<5f4dcc3b5aa765d61d8327deb882cf99>
