def Day(jour,mois):
    if jour!=mois:
        print(jour,mois)
    else:
        print("Erreur")
    return jour,mois
        
#test de la fonction
jour=input("Entrez le jour:")
mois=int(input("Entrez le mois:"))
print(Day(jour,mois))
