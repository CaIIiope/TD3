from personne import *
from bibliotheque import *

class Conservateur(Personne):
    def __init__(self, nom, prenom, adr, bibliotheque):
        Personne.__init__(self, nom, prenom, adr)
        self.__bibliotheque = bibliotheque
    
    def get_bibliotheque(self) :
        return self.__bibliotheque
    
    def set_bibliotheque(self, bibliotheque) :
        self.__bibliotheque = bibliotheque

    def __str__(self):
        return Personne.__str__(self) + f'est responsable par {self.__bibliotheque.get_nom()}'