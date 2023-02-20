from methodeResolution.MehodePSOTime import MethodePSOTime
from outils.FonctionsPSO import FonctionsPSO
from outils.Topologies import Topologie
from probleme.ProblemeEssaim import ProblemeEssaim


###############################################################################
# Pour schwefel avec 10 dimension.
# Pour 10 tests, 1000 particules max, 1 seconde par résolution et 15 lignes:
# ┌─────────────┬───────────────┐
# │ nParticules │    Mediane    │
# ├─────────────┼───────────────┤
# │          2  │   2.7189e+03  │
# │          3  │   2.5711e+03  │
# │          4  │   2.2308e+03  │
# │          6  │   1.5011e+03  │
# │         10  │   1.0570e+03  │
# │         16  │   1.2623e+03  │
# │         25  │   1.0100e+03  │
# │         40  │   1.0280e+03  │
# │         63  │   5.7249e+02  │
# │        100  │   8.0933e+02  │
# │        158  │   7.5012e+02  │
# │        251  │   5.5272e+02  │
# │        398  │   1.1944e+02  │
# │        631  │   5.2713e+02  │
# │       1000  │   8.2831e+02  │
# └─────────────┴───────────────┘
###############################################################################
def testNParticules(
    nTest: int,
    nParticulesMax: int,
    tempsParResolution: float,
    nLignes: int
):
    """Test of the number of particules.

    Args:
        nTest (int): Number of tests per topology.
        nParticulesMax (int): Maximal number of particules to try.
        tempsParResolution (int): Time for each resolution.
        nLignes (int): Number of number of particules to try.
    """
    print(
        f'┌─────────────┬───────────────┐\n'
        f'│ nParticules │    Mediane    │\n'
        f'├─────────────┼───────────────┤'
    );
    for i in range(1, nLignes + 1):
        nParticule = round(nParticulesMax ** (i / nLignes));
        probleme = ProblemeEssaim(
            fonction = FonctionsPSO.griewank,
            nDimensions = 5,
            borneInf = FonctionsPSO.griewank.borneInf,
            borneSup = FonctionsPSO.griewank.borneSup,
            estDansMemeGroupe = Topologie.vonNeumann,
            tailleEssaim = nParticule,
            inertie = 0.7,
            maxConfiance = 1.47
        );
        methode = MethodePSOTime(
            probleme = probleme,
            timeAllowed = tempsParResolution
        );
        mediane = methode.tester(nIterations = nTest).mediane();
        print(
            f'│  {nParticule:>9}  '
            f'│  {mediane:^ 11.4e}  │'
        );
    print(f'└─────────────┴───────────────┘');

