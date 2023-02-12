
from pathlib import Path

#dictionnaire

dossiers = {
    ".mp3": "Musiques",
    ".wav": "Musiques",
    ".flac": "Musiques",
    ".avi": "Vidéos",
    ".mp4": "Vidéos",
    ".gif": "Vidéos",
    ".bmp": "Images",
    ".png": "Images",
    ".jpg": "Images",
    ".txt": "Documents",
    ".pptx": "Documents",
    ".csv": "Documents",
    ".xls": "Documents",
    ".odp": "Documents",
    ".pages": "Documents",
    "Autres": "Divers"
}

#Dossier à trier

dossier_a_trier = Path.home() / "Downloads"

#Compréhension de liste

fichiers = [f for f in dossier_a_trier.iterdir() if f.is_file()]

#boucle

for f in fichiers:
    dossier_range = dossier_a_trier / dossiers.get(f.suffix, "Autres")
    dossier_range.mkdir(exist_ok = True)
    f.rename(dossier_range / f.name)





