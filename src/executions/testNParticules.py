from methodeResolution.MehodePSO import MethodePSO
from outils.FonctionsPSO import FonctionsPSO
from outils.Topologies import Topologie
from probleme.ProblemeEssaim import ProblemeEssaim


###############################################################################
# Pour 100 tests:
# ┌─────────────┬──────────┬─────────┐
# │ nParticules │  mediane │ moyenne │
# ├─────────────┼──────────┼─────────┤
# │       5     │   1856   │   1846  │ 
# │      10     │   1426   │   1445  │ 
# │      15     │   1306   │   1293  │ 
# │      20     │   1206   │   1157  │ 
# │      25     │   1047   │   1069  │ 
# │      30     │   1074   │   1053  │ 
# │      35     │    988   │   1019  │ 
# │      40     │    990   │    990  │ 
# └─────────────┴──────────┴─────────┘
###############################################################################
def testNParticules(nTest: int, nParticules: int):
    """Test of the number of particules.

    Args:
        nTest (int): Number of tests per topology.
        nParticules (int): Number of particules per resolution.
    """
    print(f"Pour {nParticules} particules:")
    probleme = ProblemeEssaim(
        fonction = FonctionsPSO.schwefel,
        nDimensions = 10,
        borneInf = FonctionsPSO.schwefel.borneInf,
        borneSup = FonctionsPSO.schwefel.borneSup,
        estDansMemeGroupe = Topologie.vonNeumann,
        tailleEssaim = nParticules,
        inertie = 0.7,
        maxConfiance = 1.47
    );
    methode = MethodePSO(probleme = probleme, nEtapes = 10_000);
    print(methode.tester(nIterations = nTest));
