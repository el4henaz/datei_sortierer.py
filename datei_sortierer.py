# Datei-Sortierer: Ein Skript zur Automatisierung der Dateiverwaltung
# Fokus: System-Automatisierung und Dateisystem-Operationen

import os
import shutil

def ordner_struktur_erstellen(ziel_pfad):
    """Erstellt die notwendigen Unterordner, falls sie nicht existieren."""
    kategorien = ['Bilder', 'Dokumente', 'Videos', 'Sonstiges']
    for kategorie in kategorien:
        ordner_pfad = os.path.join(ziel_pfad, kategorie)
        if not os.path.exists(ordner_pfad):
            os.makedirs(ordner_pfad)

def dateien_sortieren(ziel_pfad):
    """Sortiert die Dateien in die entsprechenden Ordner basierend auf ihrer Endung."""
    dokumente_ext = ['.pdf', '.docx', '.txt', '.xlsx']
    bilder_ext = ['.jpg', '.jpeg', '.png', '.gif']
    videos_ext = ['.mp4', '.mkv', '.avi']

    # Liste aller Dateien im Zielordner abrufen
    dateien = [d for d in os.listdir(ziel_pfad) if os.path.isfile(os.path.join(ziel_pfad, d))]

    if not dateien:
        print("Keine Dateien zum Sortieren gefunden.")
        return

    for datei in dateien:
        datei_pfad = os.path.join(ziel_pfad, datei)
        endung = os.path.splitext(datei)[1].lower()

        # Zielordner bestimmen
        if endung in dokumente_ext:
            ziel_ordner = 'Dokumente'
        elif endung in bilder_ext:
            ziel_ordner = 'Bilder'
        elif endung in videos_ext:
            ziel_ordner = 'Videos'
        else:
            ziel_ordner = 'Sonstiges'

        # Datei an den neuen Ort verschieben
        neues_ziel = os.path.join(ziel_pfad, ziel_ordner, datei)
        shutil.move(datei_pfad, neues_ziel)
        print(f"Verschoben: {datei} -> {ziel_ordner}")

def hauptprogramm():
    print("\n--- AUTOMATISCHER DATEI-SORTIERER ---")
    print("Beispiel für einen Pfad: C:/Users/Name/Downloads (Windows) oder /Users/Name/Downloads (Mac)")
    
    ziel_ordner = input("Bitte geben Sie den absoluten Pfad des zu sortierenden Ordners ein: ")

    if os.path.exists(ziel_ordner):
        ordner_struktur_erstellen(ziel_ordner)
        dateien_sortieren(ziel_ordner)
        print("\nErfolg: Alle Dateien wurden erfolgreich sortiert!")
    else:
        print("Fehler: Der angegebene Pfad existiert nicht. Bitte überprüfen Sie die Eingabe.")

if __name__ == "__main__":
    hauptprogramm()