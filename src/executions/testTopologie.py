from methodeResolution.MehodePSO import MethodePSO
from outils.FonctionsPSO import FonctionsPSO
from outils.Topologies import Topologie
from probleme.ProblemeEssaim import ProblemeEssaim


###############################################################################
# Médianes pour 100 tests et nIter itérations:
# ┌───────┬──────┬────────┬────────┬───────┬───────┬────────┬─────────┐
# │ nIter │ roue │ 1 × 20 │ 2 × 10 │ 4 × 5 │ 5 × 4 │ cycles │ Neumann │
# ├───────┼──────┼────────┼────────┼───────┼───────┼────────┼─────────┤
# │    10 │ 2616 │  2322  │  2490  │  2528 │  2569 │  2570  │   2588  │
# │    20 │ 2299 │  1874  │  1972  │  2086 │  2128 │  2224  │   2192  │
# │    40 │ 1840 │  1537  │  1583  │  1597 │  1636 │  1826  │   1696  │
# │    80 │ 1303 │  1358  │  1167  │  1203 │  1173 │  1505  │   1300  │
# │   160 │ 1123 │  1206  │  1118  │   943 │   992 │  1179  │    989  │
# │   320 │ 1013 │  1047  │  1001  │   742 │   818 │   841  │    802  │
# │   640 │ 1110 │  1082  │   830  │   697 │   832 │   571  │    713  │
# │  1280 │ 1119 │  1211  │   760  │   659 │   781 │   460  │    772  │
# │  2560 │ 1100 │  1156  │   735  │   715 │   935 │   356  │    746  │
# │  5120 │ 1086 │  1112  │   776  │   716 │   871 │   354  │    772  │
# │ 10240 │ 1042 │  1094  │   811  │   741 │   860 │   356  │    705  │
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
    print(methode.tester(nIterations = nPerTopology).mediane());

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
    print(methode.tester(nIterations = nPerTopology).mediane());

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
    print(methode.tester(nIterations = nPerTopology).mediane());

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
    print(methode.tester(nIterations = nPerTopology).mediane());

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
    print(methode.tester(nIterations = nPerTopology).mediane());

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
    print(methode.tester(nIterations = nPerTopology).mediane());

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
    print(methode.tester(nIterations = nPerTopology).mediane());