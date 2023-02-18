from methodeResolution.MehodePSO import MethodePSO
from outils.FonctionsPSO import FonctionsPSO
from outils.Topologies import Topologie
from probleme.ProblemeEssaim import ProblemeEssaim


###############################################################################
# Médianes pour 100 tests et 20 particules:
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
# Médianes pour 1000 then 100 tests et 60 particules:
# ┌───────┬──────┬────────┬────────┬────────┬────────┬────────┬─────────┐
# │ nIter │ roue │ 1 × 60 │ 2 × 30 │ 5 × 12 │ 10 × 6 │ cycles │ Neumann │
# ├───────┼──────┼────────┼────────┼────────┼────────┼────────┼─────────┤
# │    10 │ 2387 │  1951  │  2045  │  2095  │  2202  │  2327  │   2277  │
# │    20 │ 2045 │  1541  │  1558  │  1676  │  1793  │  1967  │   1902  │
# │    40 │ 1540 │  1153  │  1138  │  1218  │  1354  │  1512  │   1385  │
# │    80 │ 1087 │   936  │   905  │   885  │   998  │  1081  │    918  │
# │   160 │  783 │   852  │   712  │   554  │   691  │   742  │    575  │
# │   320 │  724 │   888  │   593  │   279  │   454  │   415  │    435  │
# │   640 │  714 │   869  │   415  │   237  │   380  │   218  │    336  │
# │  1280 │  680 │   869  │   337  │   217  │   474  │     1  │    296  │
# │  2560 │  752 │   869  │   355  │   217  │   355  │     0  │    336  │
# │  5120 │  709 │   869  │   355  │   119  │   415  │     0  │    336  │
# │ 10240 │  684 │   869  │   355  │   118  │   475  │     0  │    244  │
# │ 20480 │  790 │   888  │   238  │   119  │   415  │     0  │    355  │
# └───────┴──────┴────────┴────────┴────────┴────────┴────────┴─────────┘
###############################################################################
def testTopologie(nPerTopology: int, nRepeat: int):
    """Test of the different topologies.

    Args:
        nPerTopology (int): Number of tests per topology.
        nRepeat (int): Number of lines to do.
    """
    print("Test topologie:")
    print(
        '┌───────'
        '┬──────'
        '┬────────'
        '┬────────'
        '┬────────'
        '┬────────'
        '┬────────'
        '┬─────────┐'
    );
    print(
        '│ nIter '
        '│ roue '
        '│ 1 × 60 '
        '│ 2 × 30 '
        '│ 5 × 12 '
        '│ 10 × 6 '
        '│ cycles '
        '│ Neumann │'
    );
    print(
        '├───────'
        '┼──────'
        '┼────────'
        '┼────────'
        '┼────────'
        '┼────────'
        '┼────────'
        '┼─────────┤'
    );
    n: int = 10;
    tailleEssaim: int = 60;
    for _ in range(nRepeat):
        probleme = ProblemeEssaim(
            fonction = FonctionsPSO.schwefel,
            nDimensions = 10,
            borneInf = FonctionsPSO.schwefel.borneInf,
            borneSup = FonctionsPSO.schwefel.borneSup,
            estDansMemeGroupe = Topologie.roue,
            tailleEssaim = tailleEssaim,
            inertie = 0.7,
            maxConfiance = 1.47
        );
        methode = MethodePSO(probleme = probleme, nEtapes = n);
        medianeRoue = methode.tester(nIterations = nPerTopology).mediane();

        probleme = ProblemeEssaim(
            fonction = FonctionsPSO.schwefel,
            nDimensions = 10,
            borneInf = FonctionsPSO.schwefel.borneInf,
            borneSup = FonctionsPSO.schwefel.borneSup,
            estDansMemeGroupe = Topologie.tousMemeGroupe,
            tailleEssaim = tailleEssaim,
            inertie = 0.7,
            maxConfiance = 1.47
        );
        methode = MethodePSO(probleme = probleme, nEtapes = n);
        medianeEtoile = methode.tester(nIterations = nPerTopology).mediane();

        probleme = ProblemeEssaim(
            fonction = FonctionsPSO.schwefel,
            nDimensions = 10,
            borneInf = FonctionsPSO.schwefel.borneInf,
            borneSup = FonctionsPSO.schwefel.borneSup,
            estDansMemeGroupe = Topologie.clustersDeTaille(30),
            tailleEssaim = tailleEssaim,
            inertie = 0.7,
            maxConfiance = 1.47
        );
        methode = MethodePSO(probleme = probleme, nEtapes = n);
        medianeGroupe1 = methode.tester(nIterations = nPerTopology).mediane();

        probleme = ProblemeEssaim(
            fonction = FonctionsPSO.schwefel,
            nDimensions = 10,
            borneInf = FonctionsPSO.schwefel.borneInf,
            borneSup = FonctionsPSO.schwefel.borneSup,
            estDansMemeGroupe = Topologie.clustersDeTaille(12),
            tailleEssaim = tailleEssaim,
            inertie = 0.7,
            maxConfiance = 1.47
        );
        methode = MethodePSO(probleme = probleme, nEtapes = n);
        medianeGroupe2 = methode.tester(nIterations = nPerTopology).mediane();

        probleme = ProblemeEssaim(
            fonction = FonctionsPSO.schwefel,
            nDimensions = 10,
            borneInf = FonctionsPSO.schwefel.borneInf,
            borneSup = FonctionsPSO.schwefel.borneSup,
            estDansMemeGroupe = Topologie.clustersDeTaille(6),
            tailleEssaim = tailleEssaim,
            inertie = 0.7,
            maxConfiance = 1.47
        );
        methode = MethodePSO(probleme = probleme, nEtapes = n);
        medianeGroupe3 = methode.tester(nIterations = nPerTopology).mediane();

        probleme = ProblemeEssaim(
            fonction = FonctionsPSO.schwefel,
            nDimensions = 10,
            borneInf = FonctionsPSO.schwefel.borneInf,
            borneSup = FonctionsPSO.schwefel.borneSup,
            estDansMemeGroupe = Topologie.cycle(60),
            tailleEssaim = tailleEssaim,
            inertie = 0.7,
            maxConfiance = 1.47
        );
        methode = MethodePSO(probleme = probleme, nEtapes = n);
        medianeCycle = methode.tester(nIterations = nPerTopology).mediane();

        probleme = ProblemeEssaim(
            fonction = FonctionsPSO.schwefel,
            nDimensions = 10,
            borneInf = FonctionsPSO.schwefel.borneInf,
            borneSup = FonctionsPSO.schwefel.borneSup,
            estDansMemeGroupe = Topologie.vonNeumann(largeur = 4, longueur = 5),
            tailleEssaim = tailleEssaim,
            inertie = 0.7,
            maxConfiance = 1.47
        );
        methode = MethodePSO(probleme = probleme, nEtapes = n);
        medianeNeumann = methode.tester(nIterations = nPerTopology).mediane();

        print(
            f'│ {n:>5} '
            f'│ {medianeRoue:>4.0f} '
            f'│  {medianeEtoile:>4.0f}  '
            f'│  {medianeGroupe1:>4.0f}  '
            f'│  {medianeGroupe2:>4.0f}  '
            f'│  {medianeGroupe3:>4.0f}  '
            f'│  {medianeCycle:>4.0f}  '
            f'│   {medianeNeumann:>4.0f}  │'
        );
        n *= 2;
    print(
        '└───────'
        '┴──────'
        '┴────────'
        '┴────────'
        '┴────────'
        '┴────────'
        '┴────────'
        '┴─────────┘'
    );