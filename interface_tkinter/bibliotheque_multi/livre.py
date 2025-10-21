from media import Media  
class Livre(Media):
    def __init__(self, titre, annee, auteur, nb_pages):
        super().__init__(titre, annee)
        self._auteur = auteur
        self._nb_pages = nb_pages
    def get_auteur(self):
        return self._auteur
    def get_nb_pages(self):
        return self._nb_pages

    def afficher(self):
        return f"Livre : {self.get_titre()} ({self.get_annee()}) - Auteur : {self.get_auteur()} - Pages : {self.get_nb_pages()}"
