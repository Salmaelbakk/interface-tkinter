from abc import ABC, abstractmethod 
class Media(ABC):
    def __init__(self, titre, annee):
        self._titre = titre     
        self._annee = annee

    def get_titre(self):
        return self._titre
    def get_annee(self):
        return self._annee

    def set_titre(self, titre):
        self._titre = titre
    def set_annee(self, annee):
        self._annee = annee

    @abstractmethod  
    def afficher(self):
        pass  
