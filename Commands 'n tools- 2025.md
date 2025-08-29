`mkpasswd` permette di generare un hash per una password
- `mkpasswd -m help` mostra la lista di algoritmi di hashing
- `mkpasswd -m sha265crypt` genera l'hash sha256 della pw chiesta in input
- `mkpasswd -m sha256crypt -S provasal` genera l'hash sha256 della pw in input con il salt

*Password Cracking e Hash Generation*
- MD5 Hash Generator
- Crack Station
- Cyber Chef

*Web Enumeration*
- OWASP TOP 10
	- Documento standard per sviluppatori sulla sicurezza web. Si tratta di una lista di rischi critici di sicurezza sulle web app.

*get DNS*

`nslookup`
- Generico `$nslookup [options] hostname [dns server]`
- `nslookup -type=A tryhackme.com 1.1.1.1`
![[Pasted image 20250829164220.png]]

`dig`
![[Dig|vedi qui]]

- DNSRecon
- DNSenum
- Fierce
- Whois
