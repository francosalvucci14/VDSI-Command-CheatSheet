`dig` sta per **Domain Information Groper** ed è un tool da riga di comando presente in Kali Linux (e in generale nelle distro Linux) che serve per interrogare i **server DNS**.  
Con `dig` puoi ottenere informazioni su:

- la risoluzione di un dominio → indirizzo IP associato
    
- record specifici (A, AAAA, MX, NS, TXT, ecc.)
    
- il percorso di risoluzione DNS
    
- testare configurazioni DNS
    
- fare query dirette a un DNS specifico (utile in penetration testing per vedere se un server è mal configurato o permette trasferimenti di zona)
    

---

## 🛠 Sintassi base

`dig [@dns_server] hostname [record-type] [options]`

```bash
dig [opzioni] [nome-dominio] [tipo-record]
```

### Esempi pratici:

1. **Risoluzione base di un dominio**
    

```bash
dig example.com
```

→ mostra i record di tipo `A` (indirizzo IPv4) per `example.com`.

---

2. **Query di un record specifico**
    

```bash
dig example.com MX
```

→ ottieni i mail server associati (`MX`).

```bash
dig example.com TXT
```

→ mostra i record `TXT` (spesso usati per SPF, DKIM, verifiche Google/Microsoft).

---

3. **Specificare un server DNS da interrogare**
    

```bash
dig @8.8.8.8 example.com
```

→ chiede la risoluzione a Google DNS (8.8.8.8).

---

4. **Ottieni solo la risposta (senza sezioni extra)**
    

```bash
dig +short example.com
```

→ output pulito, solo l’IP.

---

5. **Trace (risoluzione passo per passo)**
    

```bash
dig +trace example.com
```

→ mostra come il DNS viene risolto partendo dai root server fino all’autorità finale.

---

6. **Reverse lookup (IP → dominio)**
    

```bash
dig -x 93.184.216.34
```

→ cerca il dominio associato all’IP.

---

7. **Zone transfer (in contesto di test in laboratorio)**
    

```bash
dig @ns1.example.com example.com AXFR
```

→ tenta un trasferimento di zona. Se il server DNS è mal configurato e permette questa query, puoi ottenere l’intero contenuto della zona DNS (nomi host, sottodomini, ecc.), informazione molto sensibile.  
⚠️ Questo lo puoi fare solo nei laboratori o su domini autorizzati!

---

## 📌 Struttura tipica dell’output

Eseguendo ad esempio:

```bash
dig example.com
```

vedrai sezioni come:

- **; <<>> DiG 9.16.1 <<>> example.com** → intestazione
    
- **;; QUESTION SECTION:** → la query che hai fatto
    
- **;; ANSWER SECTION:** → la risposta vera e propria (record DNS trovati)
    
- **;; AUTHORITY SECTION:** → i nameserver autoritativi
    
- **;; ADDITIONAL SECTION:** → info aggiuntive (spesso IP dei nameserver)
    
- **Query time, SERVER, WHEN, MSG SIZE** → statistiche della query
