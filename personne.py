class Personne :
  def __init__(self, nom, prenom, adr) :
    self.__nom = nom
    self.__prenom = prenom
    self.__adr = adr

  def __str__(self) :
    return f"{self.__nom}, {self.__prenom}, {self.__adr}"

  def get_nom(self) :
    return self.__nom

  def get_prenom(self) :
    return self.__prenom

  def get_adresse(self) :
    return self.__adr

  def set_nom(self, nom):
    self.__nom = nom

  def set_prenom(self, prenom):
    self.__prenom = prenom

  def set_adresse(self, adr):
    self.__adr = adr

if __name__ == "__main__" :
    p = Personne("Durand","Marie","Ecully")

    print(p)

    p.set_nom("Dupond")
    print(p.get_nom())

    p.set_prenom("Emilie")
    print(p.get_prenom())

    p.set_adresse("Lyon")
    print(p.get_adresse())

    print(p)
