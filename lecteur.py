from personne import *

class Lecteur(Personne) :
  def __init__(self, nom, prenom, adr, num) :
    Personne.__init__(self, nom, prenom, adr)
    self.__num = num
    self.__emprunts = 0

  def __str__(self) :
    return Personne.__str__(self) + f", {self.__num}"

  def get_numero(self) :
    return self.__num

  def get_nb_emprunts(self) :
    return self.__emprunts

  def set_numero(self, num) :
    self.__num = num

  def set_nb_emprunts(self, nb) :
    self.__emprunts = nb

if __name__ == "__main__" :
    l = Lecteur("Durand","Marie","Ecully",13)

    print(l)

    l.set_nom("Dupond")
    print(l.get_nom())

    l.set_prenom("Emilie")
    print(l.get_prenom())

    l.set_adresse("Lyon")
    print(l.get_adresse())

    l.set_numero(14)
    print(l.get_numero())

    l.set_nb_emprunts(2)
    print(l.get_nb_emprunts())

    print(l)
