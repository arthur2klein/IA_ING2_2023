from lectureFichier.lecteurSac import lireSac
from lectureFichier.lecteurTSP import lireTSP
from methodeResolution.methodeLAHCMax import MethodeLAHCMax
from methodeResolution.methodeLAHCMin import MethodeLAHCMin
from methodeResolution.methodeSac.MethodeSacAleatoire import MethodeSacAleatoire
from methodeResolution.methodeSac.MethodeSacDensite import MethodeSacDensite
from methodeResolution.methodeSac.MethodeSacMasse import MethodeSacMasse
from methodeResolution.methodeSac.MethodeSacValeur import MethodeSacValeur
from methodeResolution.methodeTSP.MethodeCheminAleatoire import mehodeCheminAleatoire
from methodeResolution.methodeTSP.MethodeCheminHillClimbing import MethodeCheminHillClimbing
from methodeResolution.MethodeRecuit import MethodeRecuit


def __main__():
    nIterations = 20;
    
    print("TSP:");
    path = "ressources/tsp/16.tsp";
    probleme = lireTSP(path);
    print("Methode aléatoire:")
    methode = mehodeCheminAleatoire(probleme);
    print(methode.tester(nIterations));
    print("\nMethode hill climbing:")
    methode = MethodeCheminHillClimbing(probleme);
    print(methode.tester(nIterations));
    print("\nMethode recuit:")
    methode = MethodeRecuit(probleme, 0.9, 300, 0.001, 20);
    print(methode.tester(nIterations));
    print("\nMethode lahc:")
    methode = MethodeLAHCMin(probleme, 30, 5000);
    print(methode.tester(nIterations));
    print("\n----------\n");
     
    print("Sac:");
    path = "ressources/sac/ks_40_0";
    probleme = lireSac(path);
    print("Methode aléatoire:")
    methode = MethodeSacAleatoire(probleme);
    print(methode.tester(nIterations));
    print("Methode par masse:")
    methode = MethodeSacMasse(probleme);
    print(methode.tester(nIterations));
    print("Methode par valeur:")
    methode = MethodeSacValeur(probleme);
    print(methode.tester(nIterations));
    print("Methode par densite:")
    methode = MethodeSacDensite(probleme);
    print(methode.tester(nIterations));
    print("Methode lahc:")
    methode = MethodeLAHCMax(probleme, 20, 1000);
    print(methode.tester(nIterations));
    print("\n----------\n");
    
__main__();
