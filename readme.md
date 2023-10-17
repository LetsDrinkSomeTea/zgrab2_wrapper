# Zgrab2 Wrapper

Dieses Skript führt Scans von Domains/IPs mithilfe von Zgrab2 durch. Es unterstützt verschiedene Protokolle,
darunter bacnet, banner, dnp3, fox, ftp, http, imap, ipp, modbus, mongodb, mssql, mysql, ntp, oracle, pop3,
postgres, redis, siemens, smb, smtp, ssh, telnet, tls. <br><br>
Das Skript erstellt automatisch einen Ordner mit dem Namen der Ziel-Domain/IP und speichert die Ergebnisse bzw. Logs von Zgrab2, 
zusätzlich werden die Ergebnisse zusammengefasst ausgegeben. 

## Verwendung

Führe das Skript mit folgenden Parametern aus:

```bash
python3 main.py [Optionen] Ziel
```

- `Ziel` (erforderlich): Die Ziel-Domain oder -IP, die gescannt werden soll, z.B. `google.com` oder `x.x.x.x[/x]`.

### Optionen

- `-d`, `--delete`: Wenn diese Option angegeben ist, werden die Log-Dateien gelöscht.
- `-v`, `--verbose`: Aktiviert den Verbose-Modus, um detaillierte Informationen während des Scans anzuzeigen.
- `-j`, `--json`: Gibt die Ausgabe im JSON-Format aus.

## Anforderungen

Stelle sicher, dass die folgenden Anforderungen erfüllt sind, bevor du das Skript ausführst:

- **Python 3:** Du kannst Python 3 von [python.org](https://www.python.org/downloads/) herunterladen und installieren.<br>
Oder ```apt install python3``` verwenden

- **Golang:** Installiere Golang von der offiziellen [Golang-Website](https://golang.org/doc/install).<br>
Oder ```apt install golang-go``` verwenden

- **Git:** Git kann von der offiziellen [Git-Website](https://git-scm.com/downloads) heruntergeladen und installiert werden.<br>
Oder ```apt install git``` verwenden

## Installation

Du kannst die erforderlichen Abhängigkeiten und das Zgrab2-Tool automatisch installieren, indem du die `init.sh`-Datei ausführst. Diese Datei wird Zgrab2 von Git klonen und installieren. Verwende die folgenden Schritte:

1. Klone dieses Repository:

   ```bash
   git clone https://github.com/LetsDrinkSomeTea/zgrap2_wrapper
   ```

2. Navigiere in das Verzeichnis:

   ```bash
   cd zgrab2_wrapper
   ```

3. Führe die `init.sh`-Datei aus:

   ```bash
   ./init.sh
   ```
   (Ggf. muss die Datei vorher noch ausführbar gemacht werden: ```chmod a+x init.sh```)

Nach der Ausführung von `init.sh` kannst du das Skript mit `./main.py` starten, wie oben beschrieben.
