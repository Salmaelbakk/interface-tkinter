from media import Media

class Film(Media):
    def __init__(self, titre, annee, realisateur, duree):
        super().__init__(titre, annee)
        self._realisateur = realisateur
        self._duree = duree

    def get_realisateur(self):
        return self._realisateur

    def get_duree(self):
        return self._duree

    def afficher(self):
        return f"Film : {self.get_titre()} ({self.get_annee()}) - Réalisateur : {self.get_realisateur()} - Durée : {self.get_duree()} min"
