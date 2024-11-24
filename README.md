# BitgetFutureSteuerrechner
BitgetFutureSteuerrechner ist eine Desktop-Anwendung zur Berechnung der Steuerlast für Futures-Trader. Importiere deine Handelsdaten aus einer CSV-Datei, analysiere Gewinne und Verluste, und erhalte eine präzise Steuerberechnung. Das Tool unterstützt auch den Export von Ergebnissen als PDF.


Beschreibung
Der BitgetFutureSteuerrechner ist ein Desktop-Anwendungstool, das entwickelt wurde, um Privatpersonen zu helfen, ihre steuerlichen Verpflichtungen im Zusammenhang mit Futures-Trading zu berechnen. Das Programm ermöglicht es Nutzern, ihre Handelsdaten zu importieren, Gewinne und Verluste zu analysieren und die entsprechende Steuerlast zu ermitteln. Es berücksichtigt dabei aktuelle steuerliche Regelungen und bietet eine benutzerfreundliche Oberfläche zur Eingabe von Daten und zur Darstellung der Ergebnisse.
Funktionen
CSV-Datenimport: Laden Sie Ihre Handelsdaten aus einer CSV-Datei hoch, die Informationen über realisierte Gewinne, Verluste und Gebühren enthält.
Automatische Steuerberechnung: Das Programm berechnet automatisch die steuerpflichtigen Einkünfte basierend auf den importierten Daten und den geltenden Steuervorschriften.
Währungsumrechnung: Möglichkeit zur Verwendung von Wechselkursen für USD und EUR, um die Berechnungen entsprechend der bevorzugten Währung durchzuführen.
Berücksichtigung von Verlusten: Verluste können bis zu einem Betrag von 20.000 Euro abgezogen werden, was in der Steuerberechnung berücksichtigt wird.
PDF-Export: Exportieren Sie die Berechnungsergebnisse in ein PDF-Dokument für Ihre Unterlagen.
Benutzerfreundliche GUI: Die Anwendung verwendet customtkinter für eine ansprechende Benutzeroberfläche, die einfach zu navigieren ist.
Zielgruppe
Dieses Tool richtet sich an Privatpersonen, die mit Futures handeln und ihre Steuerverpflichtungen einfach und effizient verwalten möchten. Es ist besonders nützlich für Trader, die regelmäßig Gewinne und Verluste erzielen und sicherstellen möchten, dass sie alle steuerlichen Vorteile nutzen.
Installation
Klonen Sie das Repository:
bash
git clone https://github.com/yourusername/BitgetFutureSteuerrechner.git

Installieren Sie die erforderlichen Python-Bibliotheken:
bash
pip install pandas requests matplotlib customtkinter fpdf

Führen Sie das Programm aus:
bash
python main.py

Nutzung
Starten Sie das Programm.
Klicken Sie auf "CSV-Datei laden", um Ihre Handelsdaten hochzuladen.
Passen Sie die Optionen an (z.B. Wechselkurs verwenden, Kirchensteuer einbeziehen).
Überprüfen Sie die Ergebnisse im Textfeld.
Exportieren Sie die Ergebnisse als PDF-Dokument.
