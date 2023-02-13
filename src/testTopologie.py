from methodeResolution.MehodePSO import MethodePSO
from probleme.ProblemeEssaim import ProblemeEssaim, Topologie, FonctionsPSO


###############################################################################
# Médianes pour 100 tests et nIter itérations:
# ┌───────┬──────┬────────┬────────┬───────┬────────┬─────────┐
# │ nIter │ roue │ 1 × 20 │ 2 × 10 │ 5 × 4 │ cycles │ Neumann |
# ├───────┼──────┼────────┼────────┼───────┼────────┼─────────┤
# │    10 │ 2412 │  2274  │  2254  │  2380 │  2436  │   2344  │
# │    20 │ 2134 │  1831  │  1925  │  2018 │  2111  │   2121  │
# │    50 │ 1701 │  1395  │  1439  │  1460 │  1586  │   1477  │
# │   100 │ 1294 │  1329  │  1216  │  1314 │  1258  │   1096  │
# │   200 │ 1175 │  1205  │  1043  │   986 │   991  │    857  │
# │   500 │  992 │  1120  │   890  │   855 │   669  │    810  │
# │  1000 │ 1102 │  1148  │   858  │   720 │   467  │    806  │
# │  2000 │ 1096 │  1204  │   805  |   849 │   435  │    739  │
# │  5000 │ 1084 │  1108  │   773  │   786 │   312  │    713  │
# │ 10000 │      │        │        │       │        │         │
# └───────┴──────┴────────┴────────┴───────┴────────┴─────────┘
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
    methode = MethodePSO(probleme, nIter);
    print(methode.tester(nPerTopology));

    print("Tous dans un même groupe:")
    probleme = ProblemeEssaim(
        FonctionsPSO.schwefel,
        10,
        FonctionsPSO.schwefel.borneInf,
        FonctionsPSO.schwefel.borneSup,
        Topologie.tousMemeGroupe,
        20,
        0.7,
        1.47
    );
    methode = MethodePSO(probleme, nIter);
    print(methode.tester(nPerTopology));

    print("2 groupes de 10:")
    probleme = ProblemeEssaim(
        FonctionsPSO.schwefel,
        10,
        FonctionsPSO.schwefel.borneInf,
        FonctionsPSO.schwefel.borneSup,
        Topologie.clustersDeTaille(10),
        20,
        0.7,
        1.47
    );
    methode = MethodePSO(probleme, nIter);
    print(methode.tester(nPerTopology));

    print("5 groupes de 4:")
    probleme = ProblemeEssaim(
        FonctionsPSO.schwefel,
        10,
        FonctionsPSO.schwefel.borneInf,
        FonctionsPSO.schwefel.borneSup,
        Topologie.clustersDeTaille(4),
        20,
        0.7,
        1.47
    );
    methode = MethodePSO(probleme, nIter);
    print(methode.tester(nPerTopology));

    print("Cycle:")
    probleme = ProblemeEssaim(
        FonctionsPSO.schwefel,
        10,
        FonctionsPSO.schwefel.borneInf,
        FonctionsPSO.schwefel.borneSup,
        Topologie.cycle(20),
        20,
        0.7,
        1.47
    );
    methode = MethodePSO(probleme, nIter);
    print(methode.tester(nPerTopology));

    print("Von Neumann topology:")
    probleme = ProblemeEssaim(
        FonctionsPSO.schwefel,
        10,
        FonctionsPSO.schwefel.borneInf,
        FonctionsPSO.schwefel.borneSup,
        Topologie.vonNeumann(4, 5),
        20,
        0.7,
        1.47
    );
    methode = MethodePSO(probleme, nIter);
    print(methode.tester(nPerTopology));