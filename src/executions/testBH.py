from methodeResolution.MehodePSO import MethodePSO
from outils.FonctionsPSO import FonctionsPSO
from outils.Particule import Particule, EnumBH
from outils.Topologies  import Topologie
from probleme.ProblemeEssaim import ProblemeEssaim


###############################################################################
# 1000 itérations pour griewank:
# ┌────────────┬────────────┬────────┬─────────────┬────────────┬───────┐
# │ Strategie  │ périodique │ rebond │ plus proche │ limitation │ arrêt │  
# ├────────────┼────────────┼────────┼─────────────┼────────────┼───────┤
# │ moyenne    │   1.524    │ 1.681  │    1.678    │   2.200    │ 3.263 │  
# │ mediane    │   1.226    │ 1.283  │    1.342    │   1.693    │ 2.322 │  
# │ ecart type │   1.047    │ 1.368  │    1.255    │   1.749    │ 2.933 │  
# └────────────┴────────────┴────────┴─────────────┴────────────┴───────┘
###############################################################################
def testBH(nEtapes: int):
    """Test of the different boundary handling strategies for the griewank
    function.

    Args:
        nEtapes (int): Number of tests per strategy.
    """
    print("Test des méthodes de traitement des limites:");
    print("Espace périodique:")
    Particule.bhMethod = EnumBH.ESPACE_PERIODIQUE;
    probleme = ProblemeEssaim(
        fonction = FonctionsPSO.griewank,
        nDimensions = 10,
        borneInf = FonctionsPSO.griewank.borneInf,
        borneSup = FonctionsPSO.griewank.borneSup,
        estDansMemeGroupe = Topologie.tousMemeGroupe,
        tailleEssaim = 20,
        inertie = 0.7,
        maxConfiance = 1.47
    );
    methode = MethodePSO(probleme = probleme, nEtapes = 200);
    print(methode.tester(nIterations = nEtapes));

    print("Arrêt aux frontières:")
    Particule.bhMethod = EnumBH.ARRET_FRONTIERE;
    probleme = ProblemeEssaim(
        fonction = FonctionsPSO.griewank,
        nDimensions = 10,
        borneInf = FonctionsPSO.griewank.borneInf,
        borneSup = FonctionsPSO.griewank.borneSup,
        estDansMemeGroupe = Topologie.tousMemeGroupe,
        tailleEssaim = 20,
        inertie = 0.7,
        maxConfiance = 1.47
    );
    methode = MethodePSO(probleme = probleme, nEtapes = 200);
    print(methode.tester(nIterations = nEtapes));

    print("Limitation de la vitesse:")
    Particule.bhMethod = EnumBH.LIMITE_VITESSE;
    probleme = ProblemeEssaim(
        fonction = FonctionsPSO.griewank,
        nDimensions = 10,
        borneInf = FonctionsPSO.griewank.borneInf,
        borneSup = FonctionsPSO.griewank.borneSup,
        estDansMemeGroupe = Topologie.tousMemeGroupe,
        tailleEssaim = 20,
        inertie = 0.7,
        maxConfiance = 1.47
    );
    methode = MethodePSO(probleme = probleme, nEtapes = 200);
    print(methode.tester(nIterations = nEtapes));

    print("Rebond aux frontieres:")
    Particule.bhMethod = EnumBH.REBOND_FRONTIERE;
    probleme = ProblemeEssaim(
        fonction = FonctionsPSO.griewank,
        nDimensions = 10,
        borneInf = FonctionsPSO.griewank.borneInf,
        borneSup = FonctionsPSO.griewank.borneSup,
        estDansMemeGroupe = Topologie.tousMemeGroupe,
        tailleEssaim = 20,
        inertie = 0.7,
        maxConfiance = 1.47
    );
    methode = MethodePSO(probleme = probleme, nEtapes = 200);
    print(methode.tester(nIterations = nEtapes));

    print("Plus proche de la frontières:")
    Particule.bhMethod = EnumBH.PLUS_PROCHE_FRONTIERE;
    probleme = ProblemeEssaim(
        fonction = FonctionsPSO.griewank,
        nDimensions = 10,
        borneInf = FonctionsPSO.griewank.borneInf,
        borneSup = FonctionsPSO.griewank.borneSup,
        estDansMemeGroupe = Topologie.tousMemeGroupe,
        tailleEssaim = 20,
        inertie = 0.7,
        maxConfiance = 1.47
    );
    methode = MethodePSO(probleme = probleme, nEtapes = 200);
    print(methode.tester(nIterations = nEtapes));

    