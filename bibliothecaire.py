from personne import *

class Bibliothecaire(Personne) :
  def __init__(self, nom, prenom, adr, numero) :
    Personne.__init__(self, nom, prenom, adr)
    self.__numero = numero

  def __str__(self) :
    return Personne.__str__(self) + f", {self.__numero}"

  def get_numero(self) :
    return self.__numero

  def set_numero(self, numero) :
    self.__numero = numero