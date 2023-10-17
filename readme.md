Hier ist eine `readme.md`-Datei, die die Verwendung der Parameter in deinem Python-Skript erklärt und die Anforderungen an Python 3, Golang und Git auflistet. Es enthält auch Anweisungen zum Installieren und Verwenden des Skripts mithilfe einer `init.sh`-Datei.

# Zgrab2 Wrapper

Dieses Skript führt Scans von Domains/IPs mithilfe von Zgrab2 durch. Es unterstützt verschiedene Protokolle, darunter bacnet, banner, dnp3, fox, ftp, http, imap, ipp, modbus, mongodb, mssql, mysql, ntp, oracle, pop3, postgres, redis, siemens, smb, smtp, ssh, telnet, tls.

## Verwendung

Führe das Skript mit folgenden Parametern aus:

```bash
python3 main.py [Optionen] Ziel
```

- `Ziel` (erforderlich): Die Ziel-Domain oder -IP, die gescannt werden soll, z.B. `google.com` oder `x.x.x.x[/x]`.

### Optionen

- `-d`, `--delete`: Wenn diese Option angegeben ist, wird das Ziel gelöscht.
- `-v`, `--verbose`: Aktiviert den Verbose-Modus, um detaillierte Informationen während des Scans anzuzeigen.
- `-j`, `--json`: Gibt die Ausgabe im JSON-Format aus.

## Anforderungen

Stelle sicher, dass die folgenden Anforderungen erfüllt sind, bevor du das Skript ausführst:

- **Python 3:** Du kannst Python 3 von [python.org](https://www.python.org/downloads/) herunterladen und installieren.

- **Golang:** Installiere Golang von der offiziellen [Golang-Website](https://golang.org/doc/install).

- **Git:** Git kann von der offiziellen [Git-Website](https://git-scm.com/downloads) heruntergeladen und installiert werden.

## Installation

Du kannst die erforderlichen Abhängigkeiten und das Zgrab2-Tool automatisch installieren, indem du die `init.sh`-Datei ausführst. Diese Datei wird Zgrab2 von Git klonen und installieren. Verwende die folgenden Schritte:

1. Klone dieses Repository:

   ```bash
   git clone https://github.com/dein-benutzername/dein-repository.git
   ```

2. Navigiere in das Verzeichnis:

   ```bash
   cd zgrab2_wrapper
   ```

3. Führe die `init.sh`-Datei aus:

   ```bash
   ./init.sh
   ```

Nach der Ausführung von `init.sh` kannst du das Skript mit `./main.py` starten, wie oben beschrieben.
