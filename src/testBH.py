from methodeResolution.MehodePSO import MethodePSO
from outils.Particule import Particule, EnumBH
from probleme.ProblemeEssaim import ProblemeEssaim, Topologie, griewank


###############################################################################
# 1000 itérations pour schwefel:
# ┌────────────┬────────────┬────────┬─────────────┬────────────┬───────┐
# │ Strategie  │ périodique │ rebond │ plus proche │ limitation │ arrêt │  
# ├────────────┼────────────┼────────┼─────────────┼────────────┼───────┤
# │ moyenne    │   1.532    │ 1.652  │    1.722    │   2.176    │ 3.215 │  
# │ mediane    │   1.296    │ 1.290  │    1.358    │   1.750    │ 2.319 │  
# │ ecart type │   0.989    │ 1.276  │    1.352    │   1.655    │ 3.067 │  
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
        griewank,
        10,
        griewank.borneInf,
        griewank.borneSup,
        Topologie.tousMemeGroupe,
        20,
        0.7,
        1.47
    );
    methode = MethodePSO(probleme, 200);
    print(methode.tester(nEtapes));

    print("Arrêt aux frontières:")
    Particule.bhMethod = EnumBH.ARRET_FRONTIERE;
    probleme = ProblemeEssaim(
        griewank,
        10,
        griewank.borneInf,
        griewank.borneSup,
        Topologie.tousMemeGroupe,
        20,
        0.7,
        1.47
    );
    methode = MethodePSO(probleme, 200);
    print(methode.tester(nEtapes));

    print("Limitation de la vitesse:")
    Particule.bhMethod = EnumBH.LIMITE_VITESSE;
    probleme = ProblemeEssaim(
        griewank,
        10,
        griewank.borneInf,
        griewank.borneSup,
        Topologie.tousMemeGroupe,
        20,
        0.7,
        1.47
    );
    methode = MethodePSO(probleme, 200);
    print(methode.tester(nEtapes));

    print("Rebond aux frontieres:")
    Particule.bhMethod = EnumBH.REBOND_FRONTIERE;
    probleme = ProblemeEssaim(
        griewank,
        10,
        griewank.borneInf,
        griewank.borneSup,
        Topologie.tousMemeGroupe,
        20,
        0.7,
        1.47
    );
    methode = MethodePSO(probleme, 200);
    print(methode.tester(nEtapes));

    print("Plus proche de la frontières:")
    Particule.bhMethod = EnumBH.PLUS_PROCHE_FRONTIERE;
    probleme = ProblemeEssaim(
        griewank,
        10,
        griewank.borneInf,
        griewank.borneSup,
        Topologie.tousMemeGroupe,
        20,
        0.7,
        1.47
    );
    methode = MethodePSO(probleme, 200);
    print(methode.tester(nEtapes));

    