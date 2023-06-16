# Etudes de communautés dans un réseau social

# Question préliminaire: Modélisation d'un réseau par un tableau

amis = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Denis"]

p_amis = ["Thomas","Carole","Thomas","Daria","Thomas","Yasmine","Muriel","Yasmine","Joël","Muriel","Yasmine","Joël",
            "Nassim","Joël","Ali","Nassim","Andréa","Nassim","Joël", "Ali","Andréa","Ali","Joël","Andréa",
            "Valentin","Léo","Thierry","Axel","Léo","Axel","Thierry","Léo","Valentin","Andréa"]


# Question 1: Nombre d'amis d'une personne:
def nb_amis(amis,prenom):
    ''' Retourne le nombre d'amis d'une personne à partir du tableau amis
        Compteur = compte le nombre d'amis

        :param amis: le tableau dont on parcourt les éléments
        :type amis: list
        :param prenom: element que l'on cherche dans le tableau pour compter son nombre d'appariton
        :type prenom: str
        :return: le nombre d'amis d'une personne (prenom)
        :rtype: int
    '''
    compteur = 0
    for x in amis:
        if x == prenom:
            compteur +=1
    return compteur

def test_nb_amis():
        assert nb_amis(p_amis,"Valentin") == 2
        assert nb_amis(p_amis,"Andréa") == 4
        assert (nb_amis(amis,"Fulya") == 5) == False
        print ("La fonction nb_amis fonctionne.")


# Question 2: Nombre de membres d'un réseau social
def taille_reseau(amis):
    '''Retourne le nombre de personnes différentes du réseau.
    On parcourt le tableau amis et si le nom n'est pas déja présent dans le tableau tab que nous avons créé il est ajouté dans ce dernier.
    :param amis: le tableau dont on parcourt les éléments
    :type amis: list
    :return: nombre de personnes différetentes du réseau
    :rtype: int
    '''
    tab = []
    i = 0
    while i < len(amis):
        if amis[i] not in tab:
            tab.append(amis[i])
        i +=1
    return len(tab)

def test_taille_reseau():
    assert taille_reseau(p_amis) == 13
    assert taille_reseau(amis) == 4
    print ("La fonction taille_reseau fonctionne.")


# Question 3: Lecture des données d'un réseau à partir d'un fichier
def lecture_reseau(path):
    '''
    Permet de lire un fichier csv et de retourner son contenu sous forme de tableau (ici les interactions entre les personnes du fichier)
    :param path: chemin vers le fichier csv
    :type path: str
    :return: retourne les interations du fichier sous forme d'un tableau
    :rtype: list '''
    fichier = open(path,encoding = 'utf-8', mode = 'r')
    tab = []
    reseau = []
    ligne = fichier.readline()

    while ligne != '':
        ligne = ligne.strip()
        ligne = ligne.split(';')
        tab.append(ligne)
        ligne = fichier.readline()
    fichier.close()
    for i in range(len(tab)):
        reseau.append(tab[i][0])
        reseau.append(tab[i][1])
    return reseau

def test_lecture_reseau():
    assert lecture_reseau("reseauShango.csv") == ['Abou', 'Kavu', 'Abou', 'Fulya', 'Abou', 'Samia', 'Ghani', 'Abou', 'Kavu', 'Samia', 'Fulya', 'Kavu', 'Badhan', 'Abou', 'Djibryl',
                                        'Kavu', 'Kemo', 'Kavu', 'Fulya', 'Samia', 'Fulya', 'Djibryl', 'Sofiane', 'Abou', 'Djibryl', 'Abou', 'Emryc', 'Fulya', 'Kemo', 'Emryc', 'Kemo',
                                        'Abou', 'Djibryl', 'Emryc', 'Abou', 'India', 'Emryc', 'Abou', 'Lina', 'Ilyes', 'Samba', 'Ilyes', 'Marya', 'Abou', 'Ilyes', 'Abou', 'Ghani', 'Badhan',
                                        'Daniel', 'Badhan', 'Sofiane', 'Djibryl', 'Hiba', 'Lina', 'Samba', 'Hiba', 'Samba', 'Lina', 'Nour', 'Hiba', 'Badhan', 'Marya', 'Badhan', 'Nour', 'Sofiane',
                                        'Marya', 'Sofiane', 'Kemo', 'India', 'Marya', 'Daniel', 'Marya', 'Lina', 'Badhan', 'Hiba', 'Marya', 'Nour', 'Lina', 'India', 'Daniel', 'Kemo', 'Djibryl',
                                        'Samia', 'Hiba', 'Badhan', 'Hiba', 'Badhan', 'Sofiane']
    print("La fonction lecture_reseau fonctionne.")


# Question 4: Modélisation d'un réseau par dictionnaire
def dico_reseau(amis):
    '''
    à partir d'un tableau amis, retourne un dictionnaire dont les clés sont les
        prénoms des membres du réseau et les valeurs le tableau de leurs amis

    :param amis: le tableau dont on parcourt les éléments
    :type amis: list
    :return: dictionnaire avec prenom en clé et un tableau de leurs amis en valeur
    :rtype: dict
    '''
    d = {}
    t = []
    for i in range(len(amis)): # Première boucle, pour choisir les amis dont on va faire le tableau
        if amis[i] not in d: # si l'ami est déjà présent dans d, alors son tableau d'amis a déjà été fait
            for s in range(len(amis)): #Deuxième boucle, pour créer le tableau de amis[i]

                if s%2 == 0: # si l'indice est pair, alors l'ami correspondant est le suivant
                    if amis[s] ==  amis[i]:
                        t.append(amis[s+1])

                elif s%2 == 1: # si l'indice est impair, il faut prendre l'ami précédent
                    if amis[s] == amis[i]:
                        t.append(amis[s-1])
            d[amis[i]] = t
            t = [] # on réinitialise le tableau pour ne pas avoir des amis appartenant à la personne précédente
    return d

def test_dico_reseau():
    assert dico_reseau(amis) == {'Alice': ['Bob', 'Charlie'], 'Bob': ['Alice', 'Denis'], 'Charlie': ['Alice'], 'Denis': ['Bob']}
    assert dico_reseau(p_amis) == {'Thomas': ['Carole', 'Daria', 'Yasmine'], 'Carole': ['Thomas'], 'Daria': ['Thomas'], 'Yasmine': ['Thomas', 'Muriel', 'Joël'],
                                'Muriel': ['Yasmine', 'Joël'], 'Joël': ['Muriel', 'Yasmine', 'Nassim', 'Ali', 'Andréa'], 'Nassim': ['Joël', 'Ali', 'Andréa'], 'Ali': ['Nassim', 'Joël', 'Andréa'],
                                'Andréa': ['Nassim', 'Ali', 'Joël', 'Valentin'], 'Valentin': ['Léo', 'Andréa'], 'Léo': ['Valentin', 'Axel', 'Thierry'], 'Thierry': ['Axel', 'Léo'], 'Axel': ['Thierry', 'Léo']}
    print("La fonction dico_reseau fonctionne.")


# Question 5: Nombre d'amis des personnes les plus populaires
def nb_amis_plus_pop (dico_reseau):
    '''
    Retourne le nombre d'amis des membres les plus populaires du réseau.
    On parcourt les valeurs du dictionnaire en paramètre.
    On va déterminer quel tableau est le plus grand et retourner sa valeur dans la variable maxi.
    Ce nombre correspondra au nombre d'amis des personnes les plus populaires.

    :param dico_reseau: dictionnaire que l'on va parcourir
    :type dico_reseau: dict
    :return: nombre d'amis des personnes les plus populaires
    :rtype: int
    '''
    maxi = 0
    for i in dico_reseau.values():
        if len(i) > maxi:
            maxi = len(i)
    return maxi

def test_nb_amis_plus_pop():
    assert nb_amis_plus_pop(dico_reseau(p_amis)) == 5
    assert nb_amis_plus_pop(dico_reseau(lecture_reseau("Communaute1.csv"))) == 11
    assert nb_amis_plus_pop(dico_reseau(lecture_reseau("Communaute2.csv"))) == 19
    assert nb_amis_plus_pop(dico_reseau(lecture_reseau("reseauShango.csv"))) == 12
    print("La fonction nb_amis_plus_pop fonctionne.")


# Question 6: Personnes les plus populaires
def les_plus_pop(dico_reseau):
    ''' renvoie , à partir d'un dictionnaire modélisant un réseau, un tableau contenant les membres les plus populaires c'est-à-dire les membres qui ont le plus d'amis
    :param dico_reseau: dictionnaire que l'on va parcourir
    :type dico_reseau: dict
    :return: tableau avec les prénoms des personnes les plus populaires du réseau
    :rtype: list
    '''
    tab_pop = []
    nb_max = nb_amis_plus_pop(dico_reseau)
    for cle,valeur in dico_reseau.items():
        if len(valeur) == nb_max:
            tab_pop.append(cle)
    return tab_pop

def test_les_plus_pop():
    assert les_plus_pop(dico_reseau(p_amis)) == ["Joël"]
    assert (les_plus_pop(dico_reseau(lecture_reseau("Communaute1.csv"))) == ['Rufino']) == False
    assert les_plus_pop(dico_reseau(lecture_reseau("reseauShango.csv"))) == ["Abou"]
    print("La fonction les_plus_pop fonctionne.")

