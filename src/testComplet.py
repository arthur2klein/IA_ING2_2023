from lectureFichier.lecteurSac import lireSac
from lectureFichier.lecteurTSP import lireTSP
from methodeResolution.MehodePSO import MethodePSO
from methodeResolution.MethodeRecuit import MethodeRecuit
from methodeResolution.methodeLAHCMax import MethodeLAHCMax
from methodeResolution.methodeLAHCMin import MethodeLAHCMin
from methodeResolution.methodeSac.MethodeSacAleatoire import MethodeSacAleatoire
from methodeResolution.methodeSac.MethodeSacDensite import MethodeSacDensite
from methodeResolution.methodeSac.MethodeSacMasse import MethodeSacMasse
from methodeResolution.methodeSac.MethodeSacValeur import MethodeSacValeur
from methodeResolution.methodeTSP.MethodeCheminAleatoire import MethodeCheminAleatoire
from methodeResolution.methodeTSP.MethodeCheminHillClimbing import MethodeCheminHillClimbing
from probleme.ProblemeEssaim import ProblemeEssaim, Topologie, FonctionsPSO


def testComplet():
    """Go through all the methods and problems of the td to display their
    performance with arbitrary paramters.
    """
    nIterations = 10;

    print("TSP:");
    path = "ressources/tsp/48.tsp";
    probleme = lireTSP(path);
    print("Methode aléatoire:")
    methode = MethodeCheminAleatoire(probleme);
    print(methode.tester(nIterations));
    print("\nMethode hill climbing:")
    methode = MethodeCheminHillClimbing(probleme);
    print(methode.tester(nIterations));
    print("\nMethode recuit:")
    methode = MethodeRecuit(probleme, 0.95, 300, 0.001, 20);
    print(methode.tester(nIterations));
    print("\nMethode lahc:")
    methode = MethodeLAHCMin(probleme, 50, 20_000);
    print(methode.tester(nIterations));
    print("\n----------\n");
     
    print("Sac:");
    path = "ressources/sac/ks_400_0";
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
    methode = MethodeLAHCMax(probleme, 50, 20_000);
    print(methode.tester(nIterations));
    print("\n----------\n");

    print("Essaim:")
    print("Probleme sphere:")
    probleme = ProblemeEssaim(
        FonctionsPSO.sphere,
        10,
        FonctionsPSO.sphere.borneInf,
        FonctionsPSO.sphere.borneSup,
        Topologie.tousMemeGroupe,
        15,
        0.7,
        1.47
    );
    methode = MethodePSO(probleme, 1000);
    print(methode.tester(nIterations));
    print("Probleme Griewank:")
    probleme = ProblemeEssaim(
        FonctionsPSO.griewank,
        5,
        FonctionsPSO.griewank.borneInf,
        FonctionsPSO.griewank.borneSup,
        Topologie.nombreGroupe(5),
        15,
        0.7,
        1.47
    );
    methode = MethodePSO(probleme, 1000);
    print(methode.tester(nIterations));
    print("Probleme Rosenbrock:")
    probleme = ProblemeEssaim(
        FonctionsPSO.rosenbrock,
        5,
        FonctionsPSO.rosenbrock.borneInf,
        FonctionsPSO.rosenbrock.borneSup,
        Topologie.clustersDeTaille(5),
        15,
        0.7,
        1.47
    );
    methode = MethodePSO(probleme, 2000);
    print(methode.tester(nIterations));
    print("Probleme Schwefel:")
    probleme = ProblemeEssaim(
        FonctionsPSO.schwefel,
        2,
        FonctionsPSO.schwefel.borneInf,
        FonctionsPSO.schwefel.borneSup,
        Topologie.tousMemeGroupe,
        20,
        0.7,
        1.47
    );
    methode = MethodePSO(probleme, 2000);
    print(methode.tester(nIterations));
    print("\n----------\n");