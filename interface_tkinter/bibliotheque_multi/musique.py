
from media import Media

class Musique(Media):
    def __init__(self, titre, annee, artiste, genre):
        super().__init__(titre, annee)   
        self._artiste = artiste          
        self._genre = genre               
    def get_artiste(self):
        return self._artiste
    def get_genre(self):
        return self._genre
    def afficher(self):
        return f"Musique : {self.get_titre()} ({self.get_annee()}) - Artiste : {self.get_artiste()} - Genre : {self.get_genre()}"
