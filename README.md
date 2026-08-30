# PDFDarkView

<p align="center">
  <img src="https://github.com/user-attachments/assets/bc440bc9-2def-404b-ad51-142cae26dc19" alt="PDFDarkView Logo" width="260">
</p>

<p align="center">

![macOS Intel](https://img.shields.io/badge/macOS-Intel-000000?logo=apple&logoColor=white)
![macOS Apple Silicon](https://img.shields.io/badge/macOS-Apple%20Silicon-555555?logo=apple&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-64--Bit-0078D6?logo=windows&logoColor=white)
![OCR](https://img.shields.io/badge/OCR-Tesseract-blue)
![64 Sprachen](https://img.shields.io/badge/Sprachen-64-success)
![Lizenz MIT](https://img.shields.io/badge/Lizenz-MIT-green)

</p>

**PDFDarkView** ist ein kostenloser Open-Source-PDF-Viewer und PDF-Editor für **macOS und Windows** mit OCR, Barrierefreiheitsfunktionen, Text-to-Speech, Mehrsprachigkeit und umfangreichen Werkzeugen zur PDF-Bearbeitung.

Die Anwendung vereint PDF-Anzeige, Bearbeitung, OCR-Texterkennung, Dokumentkonvertierung, Barrierefreiheit und PDF-Optimierung in einer einzigen Software – sowohl für den täglichen Einsatz als auch für Nutzer mit Sehbeeinträchtigungen.

---

# Funktionen

## Kernfunktionen

| Funktion | Beschreibung |
|----------|--------------|
| PDF-Anzeige | PDF-Dokumente öffnen und komfortabel durchsuchen |
| PDF-Bearbeitung | Inhalte direkt in PDFs einfügen und bearbeiten |
| OCR-Unterstützung | Texterkennung mit Tesseract OCR |
| Volltextsuche | Dokumentinhalte schnell durchsuchen |
| Lesezeichen | Erstellen, verwalten und navigieren |
| Textfenster | Extrahierten Dokumenttext anzeigen |
| Text-to-Speech | Dokumente vorlesen lassen |
| Dark Mode & Light Mode | Angenehme Darstellung in jeder Umgebung |
| Mehrsprachige Oberfläche | Verfügbar in 64 Sprachen |
| Barrierefreiheit | Optimiert für sehbehinderte und blinde Nutzer |

---

## Bearbeitungswerkzeuge

### Elemente einfügen

- Text
- Bild
- Signatur (passwortgeschützt)
- Häkchen
- Rechteck
- Ellipse
- Linie
- Pfeil
- Seitenzahlen
- Text-Wasserzeichen
- Bild-Wasserzeichen

### Redaktion (Schwärzen)

- Schwarze Schwärzung
- Weiße Schwärzung

---

## Seitenverwaltung

- Seite drehen
- Alle Seiten drehen
- Seitenausrichtung normalisieren
- Alle Seiten normalisieren
- Seiten löschen
- Seiten extrahieren
- Seiten einfügen
- Seiten verschieben
- Seitengröße ändern
- N-Up (mehrere Seiten pro Blatt)

---

## PDF-Verarbeitung

- PDFs zusammenführen
- PDFs überlagern
- PDFs zuschneiden
- PDFs abflachen (Flatten)
- PDFs optimieren
- In PDF/A konvertieren
- Dokumente schützen

---

## Export & Konvertierung

- Apple Pages
- DOCX
- TXT
- Seiten als Bilder exportieren
- Eingebettete Bilder extrahieren

---

## Metadaten

- Metadaten anzeigen
- Metadaten bearbeiten

---

## Einstellungen

### Allgemein

- OCR-Konfiguration
- Text-to-Speech-Einstellungen
- Passwortverwaltung
- Signatureinstellungen
- Backup-Einstellungen
- Dateinamenformatierung

### Darstellung

- Dark Mode
- Farbumkehr
- Einstellbarer Graustufen-Schwellwert

### Konfiguration

- Exporteinstellungen
- Importeinstellungen
- Anwendungssprache ändern
- 64 verfügbare Sprachen

---

## Barrierefreiheit

PDFDarkView enthält zahlreiche Funktionen zur Verbesserung der Zugänglichkeit.

- Text-to-Speech
- Dark Mode
- Farbumkehr
- Einstellbarer Graustufen-Schwellwert
- Große Zoomstufen
- Vollständige Tastaturbedienung
- Mehrsprachige Benutzeroberfläche

---

# Versionsverlauf

## Version 2.4.4

### Neu

- Dateisuffixe mit optionalem Benutzernamen

### Verbesserungen

- Weitere Zeitmessungen zur Performanceanalyse

### Fehlerbehebungen

- Diverse Bugfixes

---

## Version 2.4.3

### Neu

- Neue Sprache: Esperanto

### Verbesserungen

- Drucken unter Windows nutzt jetzt die in der Windows-Anwendungsliste hinterlegte Standardanwendung

---

## Version 2.4.2

### Startzeit deutlich reduziert

Insbesondere im Netzwerk- und Citrix-Betrieb wurde die Startzeit erheblich verkürzt.

**Optimierungen**

- `shutil.which()` wird zuerst verwendet (kein Prozessstart, schneller Systemaufruf)
- Timeouts für `subprocess.run()` verhindern Blockaden von über zwei Sekunden pro Befehl
- Direkte Pfadlisten ersetzen aufwändige `subprocess`-Aufrufe
- Bundle-Pfade werden vor der Systemsuche bevorzugt
- Im Bundle-Modus entfällt die aufwändige Systemsuche vollständig
- Zeitmessungen werden im Log als **TIMING** protokolliert

---

## Version 2.4.1

### Neu

- Gerade und ungerade Seiten löschen

### Verbesserungen

- Dateisuffixe werden nun immer ersetzt
- Optionales Beibehalten wurde entfernt, um überlange Dateinamen zu verhindern
- Standard-OCR-Sprache entspricht automatisch der Sprache der Benutzeroberfläche

---

## Version 2.3.1

### Fehlerbehebungen

- Verbesserter PDF-Start per Doppelklick
- Optimiertes Logging

---

## Version 2.2.0

### Neu

- Verbesserte OCR-Erkennung
- Optimierter Dark Mode
- Updateprüfung beim Programmstart
- Automatische Erkennung der Systemsprache beim ersten Start
- Automatischer Download der Übersetzungen aus dem Repository
- Unterstützung für 64 Sprachen

### Fehlerbehebungen

- Diverse Bugfixes

---

# Unterstützte Plattformen

| Plattform | Unterstützung |
|-----------|---------------|
| macOS (Intel) | ✅ |
| macOS (Apple Silicon) | ✅ |
| Windows (64-Bit) | ✅ |

---

# macOS-Sicherheitshinweis

PDFDarkView ist derzeit nicht mit einem Apple-Developer-Zertifikat signiert.

Beim ersten Start kann macOS Gatekeeper die Ausführung blockieren.

So lässt sich die Anwendung dennoch öffnen:

1. PDFDarkView im Finder auswählen.
2. Rechtsklick (oder Ctrl-Klick).
3. **Öffnen** wählen.
4. Den Dialog erneut mit **Öffnen** bestätigen.

---

# Suchbegriffe

PDF Viewer, PDF Betrachter, PDF Reader, PDF Editor, PDF bearbeiten, PDF bearbeiten kostenlos, Open Source PDF, kostenlose PDF-Software, OCR, Texterkennung, Dokumentenerkennung, gescannte Dokumente erkennen, PDF durchsuchbar machen, PDF zusammenführen, PDF optimieren, PDF komprimieren, PDF in PDF/A umwandeln, PDF zuschneiden, PDF drehen, Seiten extrahieren, Seiten löschen, Seiten verschieben, Ankreuzen, Bilder einfügen, Formen einfügen, Text einfügen, Unterschrift einfügen, Wasserzeichen einfügen, PDF schwärzen, Dokumente anonymisieren, PDF Signatur, PDF unterschreiben, Metadaten bearbeiten, PDF vorlesen, Text-to-Speech, Barrierefreiheit, Sehbehinderung, Screenreader, Sprachausgabe, Dark Mode, Light Mode, Dunkelmodus, PDF-Software Windows, PDF-Software macOS, Tesseract OCR, GUI-Übersetzung, mehrsprachige Benutzeroberfläche.

---

# Lizenzen / Licenses

## Deutsch

PDFDarkView wird unter der MIT-Lizenz veröffentlicht.

Dieses Projekt verwendet verschiedene Open-Source-Bibliotheken und Komponenten von Drittanbietern. Diese Abhängigkeiten unterliegen weiterhin ihren jeweiligen Lizenzen und Copyright-Hinweisen.

Die MIT-Lizenz von PDFDarkView gilt ausschließlich für den ursprünglichen Quellcode dieses Projekts und ersetzt oder verändert nicht die Lizenzbedingungen der verwendeten Drittanbieter-Software.

Details zu den verwendeten Komponenten und deren jeweiligen Lizenzen befinden sich in der Datei `THIRD_PARTY_LICENSES.md`.

---

## English

PDFDarkView is released under the MIT License.

This project uses a number of third-party open-source libraries and components. These dependencies remain subject to their own licenses and copyright notices.

The MIT License of PDFDarkView applies only to the original source code of this project and does not replace or modify the license terms of any third-party software.

For details regarding third-party components and their respective licenses, please refer to the `THIRD_PARTY_LICENSES.md` file.

=====================================
# PDFDarkView

<p align="center">
  <img src="https://github.com/user-attachments/assets/bc440bc9-2def-404b-ad51-142cae26dc19" alt="PDFDarkView Logo" width="260">
</p>

<p align="center">

![Windows](https://img.shields.io/badge/Windows-64--Bit-0078D6?logo=windows&logoColor=white)
![macOS Intel](https://img.shields.io/badge/macOS-Intel-000000?logo=apple&logoColor=white)
![macOS Apple Silicon](https://img.shields.io/badge/macOS-Apple%20Silicon-555555?logo=apple&logoColor=white)
![OCR](https://img.shields.io/badge/OCR-Tesseract-blue)
![Languages](https://img.shields.io/badge/Languages-64-success)
![License](https://img.shields.io/badge/License-MIT-green)

</p>

Kostenloser Open-Source-PDF-Viewer und PDF-Editor für Windows und macOS mit OCR, Barrierefreiheit, Text-to-Speech, Dark Mode und umfangreichen Werkzeugen zur PDF-Bearbeitung.

---

# 🇩🇪 Deutsche Beschreibung

PDFDarkView ist ein kostenloser Open-Source-PDF-Viewer und PDF-Editor für Windows und macOS. Die Software ermöglicht das Anzeigen, Bearbeiten, Optimieren und Konvertieren von PDF-Dateien sowie eine leistungsstarke OCR-Texterkennung mit Tesseract OCR.

Besonders geeignet ist PDFDarkView für Anwender, die PDF-Dokumente bearbeiten, Seiten zusammenführen, Seiten extrahieren, Wasserzeichen einfügen, Dokumente schwärzen (Redaktion), PDF-Dateien optimieren oder in PDF/A umwandeln möchten.

## Funktionen

| Bereich | Funktionen |
|---------|------------|
| **PDF-Anzeige** | PDF-Dateien öffnen und anzeigen |
| **Bearbeitung** | PDF bearbeiten |
| **OCR** | Texterkennung aus gescannten Dokumenten |
| **Suche** | Durchsuchbare PDF erstellen, Volltextsuche |
| **Vorlesen** | Text-to-Speech |
| **Darstellung** | Dark Mode, Light Mode, Farbumkehr |
| **Barrierefreiheit** | Optimiert für sehbehinderte und blinde Nutzer |
| **Sprachen** | Mehrsprachige Benutzeroberfläche (64 Sprachen) |
| **PDF-Werkzeuge** | Zusammenführen, Überlagern, Zuschneiden, Optimieren |
| **Archivierung** | PDF/A erstellen |
| **Metadaten** | Anzeigen und Bearbeiten |
| **Seitenverwaltung** | Drehen, Verschieben, Löschen, Extrahieren |
| **Einfügen** | Seitenzahlen, Bilder, Text, Signaturen, Wasserzeichen |
| **Redaktion** | Dokumente schwärzen |
| **Export** | DOCX, TXT, Bilder aus PDF extrahieren, Seiten als Bilder exportieren |

---

# 🇬🇧 English Description

PDFDarkView is a free open-source PDF viewer and editor for Windows and macOS. It combines PDF viewing, editing, OCR recognition, document conversion, accessibility tools, and PDF optimization in a single application.

It is designed for both everyday PDF workflows and users with visual impairments.

---

# Features

## Core Features

| Feature | Description |
|---------|-------------|
| PDF Viewing | Open and navigate PDF documents efficiently |
| PDF Editing | Insert and modify content directly in PDFs |
| OCR Support | Text recognition powered by Tesseract OCR |
| Full-Text Search | Search document content quickly |
| Bookmarks | Create, manage, and navigate bookmarks |
| Text Panel | View and work with extracted document text |
| Text-to-Speech | Read documents aloud |
| Dark & Light Mode | Comfortable viewing in any environment |
| Multilingual UI | Available in 64 languages |
| Accessibility | Optimized for visually impaired users |

---

## Editing Tools

### Insert Elements

- Insert Text
- Insert Image
- Insert Signature (password protected)
- Insert Check Mark
- Insert Rectangle
- Insert Ellipse
- Insert Line
- Insert Arrow
- Insert Page Numbers
- Insert Text Watermark
- Insert Image Watermark

### Redaction

- Black redaction
- White redaction

---

## Page Operations

- Rotate Page
- Rotate All Pages
- Normalize Page Orientation
- Normalize All Pages
- Delete Pages
- Extract Pages
- Insert Pages
- Move Pages
- Resize Pages
- N-Up (Multiple Pages per Sheet)

---

## PDF Processing

- Merge PDFs
- Overlay PDFs
- Crop PDFs
- Flatten PDFs
- Optimize PDFs
- Convert to PDF/A
- Protect Documents

---

## Export & Conversion

- Apple Pages
- DOCX
- TXT
- Export Pages as Images
- Extract Embedded Images

---

## Metadata

- View metadata
- Edit metadata

---

## Settings

### General

- OCR configuration
- Text-to-Speech settings
- Password management
- Signature settings
- Backup settings
- Filename formatting

### Appearance

- Dark Mode
- Color Inversion
- Grayscale Threshold Adjustment

### Configuration

- Export Settings
- Import Settings
- Change Application Language
- 64 Languages Available

---

## Accessibility

PDFDarkView includes several features designed to improve accessibility.

- Text-to-Speech support
- Dark Mode
- Color inversion
- Adjustable grayscale threshold
- Large zoom options
- Full keyboard navigation support
- Multilingual interface

---

# Changelog

## Version 2.2.0

### New Features

- OCR improvements
- Better Dark Mode
- Check for Updates on start
- System-Language detection on first start
- Automatic download of translations from the repository (64 languages)

### Improvements

- Improved OCR workflow
- Enhanced Dark Mode rendering
- Better first-start experience through automatic language detection
- Automatic synchronization of available translations

### Fixes

- Various bug fixes

---

# Suchbegriffe (SEO)

PDF Viewer, PDF Betrachter, PDF Reader, PDF Editor, PDF bearbeiten, PDF bearbeiten kostenlos, Open Source PDF, kostenlose PDF-Software, OCR, Texterkennung, Dokumentenerkennung, gescannte Dokumente erkennen, PDF durchsuchbar machen, PDF zusammenführen, PDF optimieren, PDF komprimieren, PDF in PDF/A umwandeln, PDF zuschneiden, PDF drehen, Seiten extrahieren, Seiten löschen, Seiten verschieben, Ankreuzen, Bilder einfügen, Formen einfügen, Text einfügen, Unterschrift einfügen, Wasserzeichen einfügen, PDF schwärzen, Dokumente anonymisieren, PDF Signatur, PDf unterschreiben, Metadaten bearbeiten, PDF vorlesen, Text-to-Speech, Barrierefreiheit, Sehbehinderung, Screenreader, Sprachausgabe, Dark Mode, Light Mode, Dunkelmodus, PDF Software Windows, PDF Software macOS, Tesseract OCR, GUI Übersetzung, mehrsprachige Benutzeroberfläche.

---

# Supported Platforms

| Plattform | Unterstützung |
|-----------|---------------|
| Windows (64-bit) | ✅ |
| macOS (Intel) | ✅ |
| macOS (Apple Silicon) | ✅ |

---

# macOS Security Notice

PDFDarkView is currently not signed with an Apple Developer Certificate.

When launching the application for the first time, macOS Gatekeeper may block execution.

To open the application:

1. Locate PDFDarkView in Finder.
2. Right-click (Control-click) the application.
3. Select **Open**.
4. Confirm by clicking **Open** again.

---

# Licenses

## Third-Party Licenses

PDFDarkView is released under the MIT License.

This project uses a number of third-party open-source libraries and components. These dependencies remain subject to their own licenses and copyright notices.

The MIT License of PDFDarkView applies only to the original source code of this project and does not replace or modify the license terms of any third-party software.

For details regarding third-party components and their respective licenses, please refer to the `THIRD_PARTY_LICENSES.md` file.

-------------------------------------------------





## PDFDarkView

<img width="382" height="375" alt="PDFDarkView" src="https://github.com/user-attachments/assets/bc440bc9-2def-404b-ad51-142cae26dc19" />


# PDF viewer and editor with OCR, accessibility features, multilingual support, and advanced PDF processing tools.

PDFDarkView combines PDF viewing, editing, OCR recognition, document conversion, accessibility tools, and PDF optimization in a single application. It is designed for both everyday PDF workflows and users with visual impairments.

⸻

# Features

Core Features

Feature	Description
PDF Viewing	Open and navigate PDF documents efficiently
PDF Editing	Insert and modify content directly in PDFs
OCR Support	Text recognition powered by Tesseract OCR
Full-Text Search	Search document content quickly
Bookmarks	Create, manage, and navigate bookmarks
Text Panel	View and work with extracted document text
Text-to-Speech	Read documents aloud
Dark & Light Mode	Comfortable viewing in any environment
Multilingual UI	Available in 64 languages
Accessibility	Optimized for visually impaired users

⸻

Editing Tools

Insert Elements

Tool

Insert Text

Insert Image

Insert Signature (password protected)

Insert Check Mark

Insert Rectangle

Insert Ellipse

Insert Line

Insert Arrow

Insert Page Numbers

Insert Text Watermark

Insert Image Watermark

Redaction

* Black redaction
* White redaction

⸻

Page Operations

Action

Rotate Page

Rotate All Pages

Normalize Page Orientation

Normalize All Pages

Delete Pages

Extract Pages

Insert Pages

Move Pages

Resize Pages

N-Up (Multiple Pages per Sheet)

⸻

PDF Processing

Function

Merge PDFs

Overlay PDFs

Crop PDFs

Flatten PDFs

Optimize PDFs

Convert to PDF/A

Protect Documents

⸻

Export & Conversion

Export Format

Apple Pages

DOCX

TXT

Export Pages as Images

Extract Embedded Images

⸻

Metadata

* View metadata
* Edit metadata

⸻

Settings

General

* OCR configuration
* Text-to-Speech settings
* Password management
* Signature settings
* Backup settings
* Filename formatting

Appearance

* Dark Mode
* Color Inversion
* Grayscale Threshold Adjustment

Configuration

* Export Settings
* Import Settings
* Change Application Language
* 64 Languages Available

⸻

Accessibility

PDFDarkView includes several features designed to improve accessibility:

* Text-to-Speech support
* Dark Mode
* Color inversion
* Adjustable grayscale threshold
* Large zoom options
* Full keyboard navigation support
* Multilingual interface
  
⸻

New Features in version 2.2.0
• OCR improvements
• Better Dark Mode
• Check for Updates on start
• System-Language detection on first start and download of translations from repository (64 languages)
• Bug fixes

⸻

🇩🇪 Deutsche Beschreibung

PDFDarkView ist ein kostenloser Open-Source-PDF-Viewer und PDF-Editor für Windows und macOS. Die Software ermöglicht das Anzeigen, Bearbeiten, Optimieren und Konvertieren von PDF-Dateien sowie eine leistungsstarke OCR-Texterkennung mit Tesseract OCR.

Besonders geeignet ist PDFDarkView für Anwender, die PDF-Dokumente bearbeiten, Seiten zusammenführen, Seiten extrahieren, Wasserzeichen einfügen, Dokumente schwärzen (Redaktion), PDF-Dateien optimieren oder in PDF/A umwandeln möchten.

Funktionen

* PDF-Dateien öffnen und anzeigen
* PDF bearbeiten
* OCR-Texterkennung (Texterkennung aus gescannten Dokumenten)
* Durchsuchbare PDF erstellen
* Volltextsuche
* Text-to-Speech (PDF vorlesen lassen)
* Dunkelmodus (Dark Mode)
* Heller Modus
* Farbumkehr
* Barrierefreie PDF-Nutzung
* Unterstützung für sehbehinderte und blinde Nutzer
* Mehrsprachige Benutzeroberfläche (64 Sprachen)
* PDF zusammenführen
* PDF überlagern
* PDF zuschneiden
* PDF optimieren
* PDF/A erstellen
* Metadaten anzeigen und bearbeiten
* Seiten drehen, verschieben, löschen und extrahieren
* Seitenzahlen einfügen
* Bilder, Text und Signaturen einfügen
* Wasserzeichen einfügen
* Dokumente schwärzen (Redaktion)
* PDF nach DOCX exportieren
* PDF nach TXT exportieren
* Bilder aus PDF extrahieren
* PDF-Seiten als Bilder exportieren

Suchbegriffe

PDF Viewer, PDF Betrachter, PDF Reader, PDF Editor, PDF bearbeiten, PDF bearbeiten kostenlos, Open Source PDF, kostenlose PDF-Software, OCR, Texterkennung, Dokumentenerkennung, gescannte Dokumente erkennen, PDF durchsuchbar machen, PDF zusammenführen, PDF optimieren, PDF komprimieren, PDF in PDF/A umwandeln, PDF zuschneiden, PDF drehen, Seiten extrahieren, Seiten löschen, Seiten verschieben, Ankreuzen, Bilder einfügen, Formen einfügen, Text einfügen, Unterschrift einfügen, Wasserzeichen einfügen, PDF schwärzen, Dokumente anonymisieren, PDF Signatur, PDf unterschreiben, Metadaten bearbeiten, PDF vorlesen, Text-to-Speech, Barrierefreiheit, Sehbehinderung, Screenreader, Sprachausgabe, Dark Mode, Light Mode, Dunkelmodus, PDF Software Windows, PDF Software macOS, Tesseract OCR, GUI Übersetzung, mehrsprachige Benutzeroberfläche.

⸻

Licenses

Third-Party Licenses

PDFDarkView is released under the MIT License.

This project uses a number of third-party open-source libraries and components. These dependencies remain subject to their own licenses and copyright notices.

The MIT License of PDFDarkView applies only to the original source code of this project and does not replace or modify the license terms of any third-party software.

For details regarding third-party components and their respective licenses, please refer to the THIRD_PARTY_LICENSES.md file.

⸻

Supported Platforms

Platform

Windows (64-bit)

macOS (Intel)

macOS (Apple Silicon)


macOS Security Notice

PDFDarkView is currently not signed with an Apple Developer Certificate.

When launching the application for the first time, macOS Gatekeeper may block execution.

To open the application:

1. Locate PDFDarkView in Finder.
2. Right-click (Control-click) the application.
3. Select Open.
4. Confirm by clicking Open again.

