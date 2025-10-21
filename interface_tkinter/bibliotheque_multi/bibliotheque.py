
from livre import Livre
from film import Film
from musique import Musique
from media import Media

import sauvegarde
class Bibliotheque:
    def __init__(self):
        self.medias = []  
    
    def ajouter(self, media):
        self.medias.append(media)

    
    def rechercher(self, titre_cherche):
        resultat = []
        for media in self.medias:
           
            if titre_cherche.lower() in media.get_titre().lower():  
                resultat.append(media)  
        return resultat
    def supprimer(self, media_a_supprimer):
        if media_a_supprimer in self.medias:
            self.medias.remove(media_a_supprimer)

   
    def sauvegarder(self, fichier_json):
        sauvegarde.sauvegarder(self.medias, fichier_json)


    def charger(self, fichier_json):
      self.medias = [] 

      liste_dicts = sauvegarde.charger(fichier_json) 

      for d in liste_dicts:  
        if d["type"] == "Livre":
            livre = Livre(d["titre"], d["annee"], d["auteur"], d["nb_pages"])
            self.medias.append(livre)

        elif d["type"] == "Film":
            film = Film(d["titre"], d["annee"], d["realisateur"], d["duree"])
            self.medias.append(film)

        elif d["type"] == "Musique":
            musique = Musique(d["titre"], d["annee"], d["artiste"], d["genre"])
            
            self.medias.append(musique)  
