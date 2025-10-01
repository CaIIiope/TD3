from datetime import date
from lecteur import *
from livre import *
from emprunt import *
from bibliothecaire import *

class Bibliotheque() :
  def __init__(self, nom, conservateur) :
    self.__conservateur = conservateur
    self.__nom = nom
    self.__bibliothecaires = []
    self.__lecteurs = []
    self.__livres = []
    self.__emprunts = []

# ---------- Setters/Getters ----------
  def get_nom(self) :
    return self.__nom

  def set_nom(self, nom) :
    self.__nom = nom

# ---------- Fonctions pour les lecteurs ----------
  def ajout_lecteur(self, nom, prenom, adr, num) :
    self.__lecteurs.append(Lecteur(nom, prenom, adr, num))

  def chercher_lecteur_nom(self, nom, prenom) :
    for lecteur in self.__lecteurs:
      if lecteur.get_nom() == nom and lecteur.get_prenom() == prenom:
        return lecteur
    return None

  def chercher_lecteur_numero(self, numero) :
    for lecteur in self.__lecteurs:
      if lecteur.get_numero() == numero:
        return lecteur
    return None


  def affiche_lecteurs(self):
    if not self.__lecteurs :
      print('Il n\'as pas des lecteurs!')
    else :
      for i in self.__lecteurs :
        print(i)

  def retrait_lecteur(self,numero):
    # On cherche le lecteur
    lecteur = self.chercher_lecteur_numero(numero)
    if lecteur is None:
        return False
    # On verifie qu'il n'a pas d'emprunt en cours
    for e in self.__emprunts:
        if e.get_numero_lecteur()==numero:
            return False
    # On peut ici retirer le lecteur de la liste
    self.__lecteurs.remove(lecteur)
    return True

# ---------- Fonctions pour les livres ----------
  def ajout_livre(self, titre, auteur, num, nb_ex) :
    self.__livres.append(Livre(titre, auteur, num, nb_ex))

  def chercher_livre_titre(self, titre) :
    for livre in self.__livres:
      if livre.get_titre() == titre:
        return livre
    return None

  def chercher_livre_numero(self, numero) :
    for livre in self.__livres:
      if livre.get_numero() == numero:
        return livre
    return None


  def affiche_livres(self) :
    if not self.__livres :
      print('La bibliotheque est vide !')
    else :
      for i in self.__livres :
        print(i)

  def retrait_livre(self,numero):
    # On cherche le livre
    livre = self.chercher_livre_numero(numero)
    if livre is None:
        return False

    # On verifie que le livre n'est pas en cours d'emprunt
    for e in self.__emprunts:
        if e.get_numero_livre()==numero:
            return False

    # En retirant le livre
    self.__livres.remove(livre)
    return True

  def retour_livre(self, numero_lecteur, numero_livre):
    e = self.chercher_emprunt(numero_lecteur, numero_livre)

    if e is not None: # l'emprunt existe, on le retire de la liste et on met a jour nb_emprunt pour le lecteur et nb_dispo pour le livre
        self.__emprunts.remove(e)
        lecteur = self.chercher_lecteur_numero(numero_lecteur)
        if lecteur is not None : lecteur.set_nb_emprunts(lecteur.get_nb_emprunts()-1)
        livre = self.chercher_livre_numero(numero_livre)
        if livre is not None: livre.set_nb_dispo(livre.get_nb_dispo()+1)
        print('Retour effectue')
        return True
    else:
        print('Aucun emprunt ne correspond a ces informations')
        return False


# ---------- Fonctions pour les emprunts ----------
  def chercher_emprunt(self, num_lecteur, num_livre):
    for emprunt in self.__emprunts:
      if emprunt.get_numero_lecteur() == num_lecteur and emprunt.get_numero_livre() == num_livre:
        return emprunt
    return None

  def affiche_emprunts(self):
    if not self.__emprunts :
      print('Il n\'as pas des emprunts!')
    else :
      for i in self.__emprunts :
        print(i)

  def emprunt_livre(self, num_lecteur, num_livre) :
    livre = self.chercher_livre_numero(num_livre)

    # Verifier si existe un livre avec le numero donnee
    if (livre is None) :
      print ('Le livre n\'existe pas.')
      return None

    # Verifier si le livre est disponible
    elif (livre.get_nb_dispo() == 0) :
      print('Il n\'a pas des exemplaires disponibles. ')
      return None

    lecteur = self.chercher_lecteur_numero(num_lecteur)

    # Verifier si existe un lecteur
    if (lecteur is None) :
      print ('Le lecteur n\'existe pas')
      return None

    # Verifier si deja existe un emprunt
    e = self.chercher_emprunt(num_lecteur, num_livre)
    if e is not None:
      print('Emprunt impossible : deja en cours')
      return None

    self.__emprunts.append(Emprunt(num_lecteur, num_livre))
    livre.set_nb_dispo(livre.get_nb_dispo()-1)
    lecteur.set_nb_emprunts(lecteur.get_nb_emprunts()+1)
    return self.__emprunts[-1] # Retourne le derniere element de la liste
  
  # ---------- Fonctions pour les bibliothecaires ----------
  
  
if __name__ == "__main__" :
    # Creation d'une bibliotheque
    b = Bibliotheque('Bibliotheque ECL')

    # Ajout de lecteurs
    b.ajout_lecteur('Duval','Pierre','rue de la Paix',1)
    b.ajout_lecteur('Dupond','Laurent','rue de la Gare',2)
    b.ajout_lecteur('Martin','Marie','rue La Fayette',3)
    b.ajout_lecteur('Dubois','Sophie','rue du Stade',4)

    # Ajout de livres
    b.ajout_livre('Le Pere Goriot','Honore de Balzac',101,2)
    b.ajout_livre('Les Hauts de Hurlevent','Emilie Bronte',102,2)
    b.ajout_livre('Le Petit Prince','Antoine de Saint Exupery',103,2)
    b.ajout_livre('L\'Etranger','Albert Camus',104,2)

    # Affichage des lecteurs et des livres
    print('\n--- Liste des lecteurs :')
    print('-------------------------------')
    b.affiche_lecteurs()
    print('\n--- Liste des livres :')
    print('-------------------------------')
    b.affiche_livres()

    # Recherches de lecteurs par numero
    print('\n--- Recherche de lecteurs :')
    print('-------------------------------')
    lect = b.chercher_lecteur_numero(1)
    if lect != None:
        print(lect)
    else:
        print('Lecteur non trouve')

    lect = b.chercher_lecteur_numero(6)
    if lect != None:
        print(lect)
    else:
        print('Lecteur non trouve')

    # Recherches de lecteurs par nom
    lect = b.chercher_lecteur_nom('Martin','Marie')
    if lect != None:
        print(lect)
    else:
        print('Lecteur non trouve')

    lect = b.chercher_lecteur_nom('Le Grand','Paul')
    if lect != None:
        print(lect)
    else:
        print('Lecteur non trouve')

    # Recherches de livres par numero
    print('\n--- Recherche de livres :')
    print('-------------------------------')
    livre = b.chercher_livre_numero(101)
    if livre != None:
        print('Livre trouve :',livre)
    else:
        print('Livre non trouve')

    livre = b.chercher_livre_numero(106)
    if livre != None:
        print('Livre trouve :',livre)
    else:
        print('Livre non trouve')

    # Recherches de livres par titre
    livre = b.chercher_livre_titre('Les Hauts de Hurlevent')
    if livre != None:
        print('Livre trouve :',livre)
    else:
        print('Livre non trouve')

    livre = b.chercher_livre_titre('Madame Bovarie')
    if livre != None:
        print('Livre trouve :',livre)
    else:
        print('Livre non trouve')

    # Quelques emprunts
    print('\n--- Quelques emprunts :')
    print('-------------------------------')
    b.emprunt_livre(1,101)
    b.emprunt_livre(1,104)
    b.emprunt_livre(2,101)
    b.emprunt_livre(2,105)
    b.emprunt_livre(3,101)
    b.emprunt_livre(3,104)
    b.emprunt_livre(4,102)
    b.emprunt_livre(4,103)

    # Affichage des emprunts, des lecteurs et des livres
    print('\n--- Liste des emprunts :')
    print('-------------------------------')
    b.affiche_emprunts()
    print('\n--- Liste des lecteurs :')
    print('-------------------------------')
    b.affiche_lecteurs()
    print('\n--- Liste des livres :')
    print('-------------------------------')
    b.affiche_livres()

    # Quelques retours de livres
    print('\n--- Quelques retours de livres :')
    print('-------------------------------')
    b.retour_livre(1,101)
    b.retour_livre(1,102)
    b.retour_livre(3,104)
    b.retour_livre(10,108)

    # Affichage des emprunts, des lecteurs et des livres
    print('\n--- Liste des emprunts :')
    print('-------------------------------')
    b.affiche_emprunts()
    print('\n--- Liste des lecteurs :')
    print('-------------------------------')
    b.affiche_lecteurs()
    print('\n--- Liste des livres :')
    print('-------------------------------')
    b.affiche_livres()

    # Suppression de quelques livres
    rep = b.retrait_livre(101)
    if not rep:
        print('Retrait du livre impossible')
    else:
        print('Retrait du livre effectue')

    b.retour_livre(2,101)

    rep = b.retrait_livre(101)
    if not rep:
        print('Retrait du livre impossible')
    else:
        print('Retrait du livre effectue')

    # Suppression de quelques lecteurs
    rep = b.retrait_lecteur(1)
    if not rep:
        print('Retrait du lecteur impossible')
    else:
        print('Retrait du lecteur effectue')

    b.retour_livre(1,104)

    rep = b.retrait_lecteur(1)
    if not rep:
        print('Retrait du lecteur impossible')
    else:
        print('Retrait du lecteur effectue')

    # Affichage des emprunts, des lecteurs et des livres
    print('\n--- Liste des emprunts :')
    print('-------------------------------')
    b.affiche_emprunts()
    print('\n--- Liste des lecteurs :')
    print('-------------------------------')
    b.affiche_lecteurs()
    print('\n--- Liste des livres :')
    print('-------------------------------')
    b.affiche_livres()
