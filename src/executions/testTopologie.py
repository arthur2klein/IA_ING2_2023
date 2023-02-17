from methodeResolution.MehodePSO import MethodePSO
from outils.FonctionsPSO import FonctionsPSO
from outils.Topologies import Topologie
from probleme.ProblemeEssaim import ProblemeEssaim


###############################################################################
# Médianes pour 100 tests et nIter itérations:
# ┌───────┬──────┬────────┬────────┬───────┬───────┬────────┬─────────┐
# │ nIter │ roue │ 1 × 20 │ 2 × 10 │ 4 × 5 │ 5 × 4 │ cycles │ Neumann │
# ├───────┼──────┼────────┼────────┼───────┼───────┼────────┼─────────┤
# │    10 │ 2624 │  2296  │  2472  │  2542 │  2526 │  2593  │   2562  │
# │    20 │ 2362 │  2026  │  2013  │  2152 │  2147 │  2185  │   2240  │
# │    40 │ 1834 │  1504  │  1529  │  1682 │  1716 │  1831  │   1680  │
# │    80 │ 1381 │  1151  │  1380  │  1290 │  1344 │  1463  │   1265  │
# │   160 │ 1103 │  1266  │  1078  │   957 │  1009 │  1194  │    958  │
# │   320 │ 1105 │  1155  │   955  │   779 │   879 │   802  │    852  │
# │   640 │  │  1155  │   955  │   779 │   879 │   802  │    852  │
# └───────┴──────┴────────┴────────┴───────┴───────┴────────┴─────────┘
###############################################################################
def testTopologie(nPerTopology: int, nIter: int):
    """Test of the different topologies.

    Args:
        nPerTopology (int): Number of tests per topology.
        nIter (int): Number of iteration per resolution.
    """
    print("Test des topologies:");

    print("Une seule voisine de toutes:")
    probleme = ProblemeEssaim(
        fonction = FonctionsPSO.schwefel,
        nDimensions = 10,
        borneInf = FonctionsPSO.schwefel.borneInf,
        borneSup = FonctionsPSO.schwefel.borneSup,
        estDansMemeGroupe = Topologie.roue,
        tailleEssaim = 20,
        inertie = 0.7,
        maxConfiance = 1.47
    );
    methode = MethodePSO(probleme = probleme, nEtapes = nIter);
    print(methode.tester(nIterations = nPerTopology));

    print("Tous dans un même groupe:")
    probleme = ProblemeEssaim(
        fonction = FonctionsPSO.schwefel,
        nDimensions = 10,
        borneInf = FonctionsPSO.schwefel.borneInf,
        borneSup = FonctionsPSO.schwefel.borneSup,
        estDansMemeGroupe = Topologie.tousMemeGroupe,
        tailleEssaim = 20,
        inertie = 0.7,
        maxConfiance = 1.47
    );
    methode = MethodePSO(probleme = probleme, nEtapes = nIter);
    print(methode.tester(nIterations = nPerTopology));

    print("2 groupes de 10:")
    probleme = ProblemeEssaim(
        fonction = FonctionsPSO.schwefel,
        nDimensions = 10,
        borneInf = FonctionsPSO.schwefel.borneInf,
        borneSup = FonctionsPSO.schwefel.borneSup,
        estDansMemeGroupe = Topologie.clustersDeTaille(10),
        tailleEssaim = 20,
        inertie = 0.7,
        maxConfiance = 1.47
    );
    methode = MethodePSO(probleme = probleme, nEtapes = nIter);
    print(methode.tester(nIterations = nPerTopology));

    print("4 groupes de 5:")
    probleme = ProblemeEssaim(
        fonction = FonctionsPSO.schwefel,
        nDimensions = 10,
        borneInf = FonctionsPSO.schwefel.borneInf,
        borneSup = FonctionsPSO.schwefel.borneSup,
        estDansMemeGroupe = Topologie.clustersDeTaille(5),
        tailleEssaim = 20,
        inertie = 0.7,
        maxConfiance = 1.47
    );
    methode = MethodePSO(probleme = probleme, nEtapes = nIter);
    print(methode.tester(nIterations = nPerTopology));

    print("5 groupes de 4:")
    probleme = ProblemeEssaim(
        fonction = FonctionsPSO.schwefel,
        nDimensions = 10,
        borneInf = FonctionsPSO.schwefel.borneInf,
        borneSup = FonctionsPSO.schwefel.borneSup,
        estDansMemeGroupe = Topologie.clustersDeTaille(4),
        tailleEssaim = 20,
        inertie = 0.7,
        maxConfiance = 1.47
    );
    methode = MethodePSO(probleme = probleme, nEtapes = nIter);
    print(methode.tester(nIterations = nPerTopology));

    print("Cycle:")
    probleme = ProblemeEssaim(
        fonction = FonctionsPSO.schwefel,
        nDimensions = 10,
        borneInf = FonctionsPSO.schwefel.borneInf,
        borneSup = FonctionsPSO.schwefel.borneSup,
        estDansMemeGroupe = Topologie.cycle(20),
        tailleEssaim = 20,
        inertie = 0.7,
        maxConfiance = 1.47
    );
    methode = MethodePSO(probleme = probleme, nEtapes = nIter);
    print(methode.tester(nIterations = nPerTopology));

    print("Von Neumann topology:")
    probleme = ProblemeEssaim(
        fonction = FonctionsPSO.schwefel,
        nDimensions = 10,
        borneInf = FonctionsPSO.schwefel.borneInf,
        borneSup = FonctionsPSO.schwefel.borneSup,
        estDansMemeGroupe = Topologie.vonNeumann(largeur = 4, longueur = 5),
        tailleEssaim = 20,
        inertie = 0.7,
        maxConfiance = 1.47
    );
    methode = MethodePSO(probleme = probleme, nEtapes = nIter);
    print(methode.tester(nIterations = nPerTopology));