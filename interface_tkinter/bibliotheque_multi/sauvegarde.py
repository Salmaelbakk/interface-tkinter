import json
from livre import Livre
from film import Film
from musique import Musique
from media import Media

def sauvegarder(medias, fichier):
    liste = []

    for m in medias:
        d = {
            "type": type(m).__name__,
            "titre": m.get_titre(),
            "annee": m.get_annee()
        }

        if d["type"] == "Livre":
            d["auteur"] = m.get_auteur()
            d["nb_pages"] = m.get_nb_pages()
        elif d["type"] == "Film":
            d["realisateur"] = m.get_realisateur()
            d["duree"] = m.get_duree()
        elif d["type"] == "Musique":
            d["artiste"] = m.get_artiste()
            d["genre"] = m.get_genre()

        liste.append(d)

    with open(fichier, "w") as f:
        json.dump(liste, f)

def charger(fichier):
    try:
        with open(fichier, "r") as f:
            return json.load(f)
    except:
        print(f"⚠️ Erreur : Impossible de lire le fichier '{fichier}'. Il est peut-être vide ou introuvable.")
        return []
