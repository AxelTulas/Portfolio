# Créé par Eleve, le 08/11/2022 en Python 3.7

# SAE 1.02: Comparaison d'approches algorithmiques

tab = ["Alice", "Bob","Dominique","Alice","Bob","Charlie"]

def create_network(tab):
    dico = {}
    liste = []
    for i in range(len(tab)):

        if i%2 == 0:

            if tab[i] not in dico:

                dico[tab[i]] = [tab[i+1]]

            elif tab[i] in dico:
                dico[tab[i]].append(tab[i+1])

        elif i%2 == 1:
            if tab[i] not in dico:

                dico[tab[i]] = [tab[i-1]]

            elif tab[i] in dico:
                dico[tab[i]].append(tab[i-1])


    return dico

# Question 2: comparer les 2 fonctions théoriquement et expérimentalement (complexité, et vrai calcul : time())


def get_people(network):
    tab = []
    for k in network.keys():
        tab.append(k)
    return tab


def are_friends(network, person1, person2):
    if person2 in network[person1]:
        return True
    return False

def all_his_friends(network, person, group):
    for i in range(len(group)):
        if group[i] not in network[person]:
            return False
    return True

def is_a_community(network, group):
    for i in range(len(group)):
        for j in range(len(group)):
            if group[j] not in network[group[i]] and group[i] != group[j]:
                return False
    return True


def find_community(network, group):
    com = []
    t = []
    for i in range(len(group)):

        t.append(group[i])

        if is_a_community(network,t):

            com.append(group[i])

        elif not is_a_community(network, t):
            t.pop()

    return com

def order_by_decreasing_popularity(network, group):
    tab = []
    for i in range(len(group)-1):
        if len(network[group[i]])< len(network[group[i+1]]):
            group[i], group[i+1] = group[i+1], group[i]

    return group

def find_community_by_decreasing_popularity(network):

    tab = get_people(network)
    popu = order_by_decreasing_popularity(network, tab)
    return find_community(network,popu)


def find_community_from_person(network, person):

    com = [person]
    popu = order_by_decreasing_popularity(network,network[person])

    for i in range(len(popu)):
        if all_his_friends(network,popu