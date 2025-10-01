class Livre :
  def __init__(self, titre, auteur, num, nb_ex) :
    self.__titre = titre
    self.__auteur = auteur
    self.__num = num
    self.__nb_total = nb_ex
    self.__nb_dispo = nb_ex

  def __str__(self) :
    return f'{self.__titre}, {self.__auteur}, {self.__num}, {self.__nb_total}, {self.__nb_dispo}'

  def get_titre(self) :
    return self.__titre

  def get_auteur(self) :
    return self.__auteur

  def get_numero(self) :
    return self.__num

  def get_nb_total(self) :
    return self.__nb_total

  def get_nb_dispo(self) :
    return self.__nb_dispo

  def set_titre(self, titre) :
    self.__titre = titre

  def set_auteur(self, auteur) :
    self.__auteur = auteur

  def set_numero(self, num) :
    self.__num = num

  def set_nb_total(self, nb_ex) :
    self.__nb_total = nb_ex

  def set_nb_dispo(self, nb_ex) :
    self.__nb_dispo = nb_ex

if __name__ == "__main__" :
    l = Livre('Le Pere Goriot','Honore de Balzac',101,2)
    print(l)

    l.set_auteur("Emilie Bronte")
    print(l.get_auteur())

    l.set_titre("Les Hauts de Hurlevent")
    print(l.get_titre())

    l.set_numero(102)
    print(l.get_numero())

    l.set_nb_total(5)
    print(l.get_nb_total())

    l.set_nb_dispo(4)
    print(l.get_nb_dispo())

    print(l)
