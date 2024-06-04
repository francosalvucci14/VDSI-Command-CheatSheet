# Privileg Escalation Tools

## linPEAS

Tool che permette di trovare tutte le possibili vulnerabilità all'interno del sistema.

linPEAS si usa per trovare vulnerabilità in modo tale da riuscire a entrare nel sistema come utente root

Link per scaricare linPEAS.sh -> [Link](https://github.com/peass-ng/PEASS-ng/tree/master/linPEAS)

Esecuzione 

- `chmod +x linPEAS.sh`
- `./linPEAS.sh`


## GTFOBins

La bibbia della PE, in questa pagina possiamo trovare tutte le vulnerabilità note per i binari, per esempio:

- eseguiamo sudo -l e troviamo una vulnerabilità per man -> tramite GTFOBins vediamo che possiamo usare la vulnerabilità `sudo man man`, cosi facendo possiamo prendere la shell di root usando il comando linux man

Ovviamente ci sono altri esempi e altre situazioni, tipo sfruttare il caricamento di una libreria tramite variabile d'ambiente, etc..

### Mettere gli esempi più importanti


