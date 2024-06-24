# GoBuster

Tool usato per effettuare l'enumerazione dei siti web.

Il tool ci permette di trovare tutte le sottodirectory/risorse che si trovano su un web server.

Per lanciare il comando bisogna fare

`gobuster OPTIONS`

## Enumerazione directory

Si usa il comando in questo modo

`gobuster dir -u http://<target_ip> -w <wordlist>`

Se si vogliono escludere gli status code possiamo usare il flag `-s` e darglik tutti gli status code che non vogliamo, oppure se si vuole escludere la lunghezza dobbiamo usare il flag `--exclude-length <int>`

E tante altre cose

## Enumerazione virtual host

Come le directory, con gobuster possiamo enumerare i virtual host

Per enumerare i virtual host, basta modificare l'opzione `dir` con `vhost`, e alla fine del comando scrivere `--append-domain`


