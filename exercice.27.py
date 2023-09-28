def SalaireTotal(H1, H2, HoraireDebout, MontantSalaire, HoraireFin):
    if H1 > H2:
        SalaireTotale = MontantSalaire * 50 / 100
        HoraireSupplementaire = HoraireDebout + HoraireFin
        print(SalaireTotale)
        print(HoraireSupplementaire)
    else:
        HoraireNormale = HoraireDebout - HoraireFin
        SalaireTotale = MontantSalaire * 15 / 100
        print(HoraireNormale)
        print(SalaireTotale)
    return SalaireTotale
#test de la fonction Salaire Totale Heure
H1 =int(input("Entrez la valuer de l horaire1."))
H2 =int(input("Entrez la valuer de l horaire2:"))
MontantSalaire = float(input("Entrez la valuer de le MOntantSalaire:"))
HoraireDebout =int(input("Entrez la valur de horaire du debout"))
HoraireFin = int(input("Entrez la valuer de l horaire de la fin"))
print(SalaireTotal(H1, H2, HoraireDebout, MontantSalaire, HoraireFin))
print("le resultat final pour nos calcule effectue")
