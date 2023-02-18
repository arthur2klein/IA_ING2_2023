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
from outils.FonctionsPSO import FonctionsPSO
from outils.Topologies import Topologie
from probleme.ProblemeEssaim import ProblemeEssaim


def testComplet():
    """Go through all the methods and problems of the td to display their
    performance with arbitrary paramters.
    """
    nIterations = 10;

    print("TSP:");
    path = "ressources/tsp/48.tsp";
    probleme = lireTSP(path = path);
    print("Methode aléatoire:")
    methode = MethodeCheminAleatoire(problemeTSP = probleme);
    print(methode.tester(nIterations = nIterations));
    print("\nMethode hill climbing:")
    methode = MethodeCheminHillClimbing(probleme = probleme);
    print(methode.tester(nIterations = nIterations));
    print("\nMethode recuit:")
    methode = MethodeRecuit(
        probleme = probleme,
        refroidissement = 0.95,
        tempInitiale = 300,
        tempMin = 0.001,
        iterationsParTemp = 20
    );
    print(methode.tester(nIterations = nIterations));
    print("\nMethode lahc:")
    methode = MethodeLAHCMin(
        probleme = probleme,
        tailleMem = 50,
        nIter = 20_000
    );
    print(methode.tester(nIterations = nIterations));
    print("\n----------\n");
     
    print("Sac:");
    path = "ressources/sac/ks_400_0";
    probleme = lireSac(path = path);
    print("Methode aléatoire:")
    methode = MethodeSacAleatoire(probleme = probleme);
    print(methode.tester(nIterations = nIterations));
    print("Methode par masse:")
    methode = MethodeSacMasse(probleme = probleme);
    print(methode.tester(nIterations = nIterations));
    print("Methode par valeur:")
    methode = MethodeSacValeur(probleme = probleme);
    print(methode.tester(nIterations = nIterations));
    print("Methode par densite:")
    methode = MethodeSacDensite(probleme = probleme);
    print(methode.tester(nIterations = nIterations));
    print("Methode lahc:")
    methode = MethodeLAHCMax(
        probleme = probleme,
        tailleMem = 50,
        nIter = 20_000
    );
    print(methode.tester(nIterations = nIterations));
    print("\n----------\n");

    print("Essaim:")
    print("Probleme sphere:")
    probleme = ProblemeEssaim(
        fonction = FonctionsPSO.sphere,
        nDimensions = 10,
        borneInf = FonctionsPSO.sphere.borneInf,
        borneSup = FonctionsPSO.sphere.borneSup,
        estDansMemeGroupe = Topologie.tousMemeGroupe,
        tailleEssaim = 15,
        inertie = 0.7,
        maxConfiance = 1.47
    );
    methode = MethodePSO(probleme = probleme, nEtapes = 1000);
    print(methode.tester(nIterations = nIterations));
    print("Probleme Griewank:")
    probleme = ProblemeEssaim(
        fonction = FonctionsPSO.griewank,
        nDimensions = 5,
        borneInf = FonctionsPSO.griewank.borneInf,
        borneSup = FonctionsPSO.griewank.borneSup,
        estDansMemeGroupe = Topologie.clustersDeTaille(4),
        tailleEssaim = 15,
        inertie = 0.7,
        maxConfiance = 1.47
    );
    methode = MethodePSO(probleme = probleme, nEtapes = 1000);
    print(methode.tester(nIterations = nIterations));
    print("Probleme Rosenbrock:")
    probleme = ProblemeEssaim(
        fonction = FonctionsPSO.rosenbrock,
        nDimensions = 5,
        borneInf = FonctionsPSO.rosenbrock.borneInf,
        borneSup = FonctionsPSO.rosenbrock.borneSup,
        estDansMemeGroupe = Topologie.clustersDeTaille(5),
        tailleEssaim = 15,
        inertie = 0.7,
        maxConfiance = 1.47
    );
    methode = MethodePSO(probleme = probleme, nEtapes = 2000);
    print(methode.tester(nIterations = nIterations));
    print("Probleme Schwefel:")
    probleme = ProblemeEssaim(
        fonction = FonctionsPSO.schwefel,
        nDimensions = 2,
        borneInf = FonctionsPSO.schwefel.borneInf,
        borneSup = FonctionsPSO.schwefel.borneSup,
        estDansMemeGroupe = Topologie.tousMemeGroupe,
        tailleEssaim = 30,
        inertie = 0.7,
        maxConfiance = 1.47
    );
    methode = MethodePSO(probleme = probleme, nEtapes = 2000);
    print(methode.tester(nIterations = nIterations));
    print("\n----------\n");