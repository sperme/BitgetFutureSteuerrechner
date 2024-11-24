
```markdown
# Bitget Futures Steuerrechner 🧮

Ein modernes Tool zur Berechnung von Steuerpflichten aus Futures-Trading-Daten.  
Diese Anwendung ist speziell für den deutschen Steuerkontext angepasst und bietet einfache Bedienung durch eine übersichtliche Benutzeroberfläche.

⚠️ **Hinweis:** Dieses Tool dient ausschließlich zu Test- und Informationszwecken.  
Es handelt sich nicht um eine rechtliche oder steuerliche Beratung.  
Bitte konsultieren Sie immer einen Steuerberater, um die Korrektheit der Ergebnisse zu gewährleisten. ⚠️

---

## 🚀 Funktionen

- **Automatische Steuerberechnung** gemäß den deutschen Steuerregeln für Futures-Trading.  
- **Unterstützung für verschiedene Steuerparameter:**
  - Kirchensteuer (optional einstellbar).  
  - Verlustvortrag (optional einstellbar).  
  - Wechselkursberechnung (USD/EUR).  

- **Modernes UI:** Benutzerfreundliches Design mit hilfreichen Infotexten zu jeder Funktion.  
- **PDF-Export:** Speichere Ergebnisse für deine Unterlagen.  
- **Anpassbarkeit:** Passe steuerliche Parameter flexibel an.

---
```
## 📥 Installation

1. **Clone das Repository:**
   ```bash
   git clone https://github.com/usexless/BitgetFutureSteuerrechner.git
   cd BitgetFutureSteuerrechner
   ```

2. **Installiere die benötigten Pakete:**  
   Stelle sicher, dass Python 3.8 oder höher installiert ist.
   ```bash
   pip install -r requirements.txt
   ```

3. **Starte die Anwendung:**  
   ```bash
   python app.py
   ```

---

## 🖥️ Bedienung

### 1. CSV-Datei exportieren
Um mit der Anwendung zu starten, müssen Sie zunächst Ihre Futures-Daten von Bitget als CSV-Datei exportieren.  
Folgen Sie dazu diesen Schritten:

1. Melden Sie sich auf [Bitget](https://www.bitget.com/de) an.  
2. Navigieren Sie zur Seite **Order Center** unter folgendem Link:  
   [https://www.bitget.com/de/order/mcp?tab=5](https://www.bitget.com/de/order/mcp?tab=5).  
3. Wählen Sie dort den Tab für **Futures** aus.  
4. Exportieren Sie Ihre Transaktionsdaten als CSV-Datei.

### 2. CSV-Datei in die Anwendung importieren
- Öffnen Sie die Anwendung, indem Sie die Schritte im Abschnitt **📥 Installation** ausführen.
- Klicken Sie auf **"CSV-Datei laden"** und wählen Sie die zuvor exportierte CSV-Datei aus.  
  Die Datei muss die Spalten `realized pnl` (realisierter Gewinn/Verlust) und `fees` (Gebühren) enthalten, um korrekt verarbeitet zu werden.

### 3. Steuerparameter anpassen
- Je nach Bedarf können Sie verschiedene Steueroptionen aktivieren oder deaktivieren:  
  - **Kirchensteuer**: Aktivieren, wenn Sie kirchensteuerpflichtig sind.  
  - **Verlustvortrag**: Aktivieren, um Verluste in zukünftige Steuerperioden zu übertragen.  
  - **Wechselkursberechnung**: Standardmäßig aktiviert, um USD in EUR umzurechnen. Sie können diese Option deaktivieren, wenn keine Umrechnung gewünscht ist.

### 4. Ergebnisse anzeigen und exportieren
- Die Ergebnisse werden nach dem Import der CSV-Datei automatisch berechnet und angezeigt.
- Optional können Sie die berechneten Ergebnisse als PDF exportieren, um sie zu speichern oder mit Ihrem Steuerberater zu teilen.

---

## ⚖️ Rechtlicher Hinweis

- Dieses Programm ist **keine steuerliche Beratung** und ersetzt **nicht die Überprüfung durch einen Steuerberater**.  
- Es wird keine Garantie für die Richtigkeit oder Vollständigkeit der Berechnungen übernommen.  
- Der Autor übernimmt keinerlei Haftung für Schäden oder Verluste, die durch die Nutzung dieses Tools entstehen können.  
- Die Anwendung dient ausschließlich zu **Test- und Informationszwecken**.

---

## 🛠️ Anpassungen und Weiterentwicklung

Pull-Requests und Issues sind herzlich willkommen!  
Wenn du Vorschläge oder Verbesserungen hast, erstelle gerne ein Issue oder einen PR.

---

## 📄 Lizenz

Dieses Projekt ist unter der **Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License (CC BY-NC-ND 4.0)** lizenziert. 

### Bedingungen:
- **Namensnennung**: Du musst den Urheber des Werkes nennen.
- **Nicht kommerziell**: Das Material darf nicht für kommerzielle Zwecke verwendet werden.
- **Keine Bearbeitungen**: Du darfst das Material nicht bearbeiten oder abändern.

Weitere Informationen findest du in der [LICENSE](LICENSE).

---

📧 **Kontakt:**  
Für Fragen oder Feedback besuche [mein GitHub-Profil](https://github.com/usexless).

---

Viel Erfolg mit deinem Futures-Trading! 💹
```

### Änderungen:
1. **Zeilenumbrüche**:  
   Alle Absätze sind klar getrennt, insbesondere in den Abschnitten **Funktionen** und **Rechtlicher Hinweis**, um die Lesbarkeit zu verbessern.

2. **Klare Installation**:  
   Die drei Schritte sind klar nummeriert und voneinander getrennt. Die Blöcke für Befehle sind korrekt eingerückt und voneinander abgegrenzt.

3. **Übersichtlichkeit**:  
   - Listenpunkte in Funktionen und Bedienung machen den Text einfacher lesbar.
   - Abgrenzung durch horizontale Linien (`---`).

Das sollte die Struktur und Lesbarkeit erheblich verbessern.
