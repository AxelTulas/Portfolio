# Créé par utilisateur, le 26/10/2022 en Python 3.7

tab = ['Abou', 'Kavu', 'Abou', 'Fulya', 'Abou', 'Samia', 'Ghani', 'Abou', 'Kavu', 'Samia', 'Fulya', 'Kavu', 'Badhan', 'Abou', 'Djibryl', 'Kavu', 'Kemo', 'Kavu', 'Fulya', 'Samia', 'Fulya', 'Djibryl', 'Sofiane', 'Abou', 'Djibryl', 'Abou', 'Emryc', 'Fulya', 'Kemo', 'Emryc', 'Kemo', 'Abou', 'Djibryl', 'Emryc', 'Abou', 'India', 'Emryc', 'Abou', 'Lina', 'Ilyes', 'Samba', 'Ilyes', 'Marya', 'Abou', 'Ilyes', 'Abou', 'Ghani', 'Badhan', 'Daniel', 'Badhan', 'Sofiane', 'Djibryl', 'Hiba', 'Lina', 'Samba', 'Hiba', 'Samba', 'Lina', 'Nour', 'Hiba', 'Badhan', 'Marya', 'Badhan', 'Nour', 'Sofiane', 'Marya', 'Sofiane', 'Kemo', 'India', 'Marya', 'Daniel', 'Marya', 'Lina', 'Badhan', 'Hiba', 'Marya', 'Nour', 'Lina', 'India', 'Daniel', 'Kemo', 'Djibryl', 'Samia', 'Hiba', 'Badhan', 'Hiba', 'Badhan', 'Sofiane']

def reseau_csv(path):
    fichier = open(path, mode = 'x')
    sep = ';'
    i = 0
    modele = "{0}" + sep + "{1}" + "\n"
    while i<len(tab):
        fichier.write(modele.format(tab[i],tab[i+1]))
        i +=2
    fichier.close()

reseau_csv("reseauShango.csv")