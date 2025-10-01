from datetime import date

class Emprunt :
  def __init__(self, num_lect, num_livre) :
    self.__num_lect = num_lect
    self.__num_livre = num_livre
    self.__date = date.isoformat(date.today())

  def __str__(self) :
    return f"Emprunt de livre numero : {self.__num_livre} a lecteur numero : {self.__num_lect}, au jour: {self.__date}"

  def get_numero_lecteur(self) :
    return self.__num_lect

  def get_numero_livre(self) :
    return self.__num_livre

  def get_date(self) :
    return self.__date

  def set_numero_lecteur(self, num) :
    self.__num_lect = num

  def set_numero_livre(self, num) :
    self.__num_livre = num

if __name__ == "__main__" :
    e = Emprunt(3,5)

    print(e)

    print(e.get_numero_lecteur())
    print(e.get_numero_livre())
    print(e.get_date())
