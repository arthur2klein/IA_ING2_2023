from methodeResolution.MehodePSO import MethodePSO
from probleme.ProblemeEssaim import ProblemeEssaim, Topologie, schwefel


###############################################################################
# 100 tests et 2000 itérations:
# ┌────────────┬──────┬───────────┬───────────┬───────────┬───────────┬──
# │ Topology   │ roue │ un groupe │ 2 groupes │ 4 groupes │ 5 groupes │  
# ├────────────┼──────┼───────────┼───────────┼───────────┼───────────┼──
# │ moyenne    │ 1131 │    1130   │    1223   │    1436   │    1531   │  
# │ mediane    │ 1114 │    1115   │    1227   │    1431   │    1556   │  
# │ ecart type │  355 │     393   │     338   │     297   │     300   │  
# └────────────┴──────┴───────────┴───────────┴───────────┴───────────┴──
# ──┬────────────┬─────────────┐
#   │ 20 groupes │ von neumann |
# ──┼────────────┼─────────────┤
#   │    2824    │     792     │
#   │    2839    │     758     │
#   │     267    │     316     │
# ──┴────────────┴─────────────┘
###############################################################################
# 1000 tests et 100 itérations:
# ┌────────────┬──────┬───────────┬───────────┬───────────┬───────────┬──
# │ Topology   │ roue │ un groupe │ 2 groupes │ 4 groupes │ 5 groupes │  
# ├────────────┼──────┼───────────┼───────────┼───────────┼───────────┼──
# │ moyenne    │ 1281 │    1205   │    1237   │    1439   │    1556   │  
# │ mediane    │ 1300 │    1217   │    1243   │    1454   │    1561   │  
# │ ecart type │  374 │     380   │     346   │     319   │     315   │  
# └────────────┴──────┴───────────┴───────────┴───────────┴───────────┴──
# ──┬────────────┬─────────────┐
#   │ 20 groupes │ von neumann |
# ──┼────────────┼─────────────┤
#   │    2880    │     1115    │
#   │    2903    │     1135    │
#   │     278    │      345    │
# ──┴────────────┴─────────────┘
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
        schwefel,
        10,
        schwefel.borneInf,
        schwefel.borneSup,
        Topologie.roue,
        20,
        0.7,
        1.47
    );
    methode = MethodePSO(probleme, nIter);
    print(methode.tester(nPerTopology));

    print("Tous dans un même groupe:")
    probleme = ProblemeEssaim(
        schwefel,
        10,
        schwefel.borneInf,
        schwefel.borneSup,
        Topologie.tousMemeGroupe,
        20,
        0.7,
        1.47
    );
    methode = MethodePSO(probleme, nIter);
    print(methode.tester(nPerTopology));

    print("2 groupes de 10:")
    probleme = ProblemeEssaim(
        schwefel,
        10,
        schwefel.borneInf,
        schwefel.borneSup,
        Topologie.nombreGroupe(2),
        20,
        0.7,
        1.47
    );
    methode = MethodePSO(probleme, nIter);
    print(methode.tester(nPerTopology));

    print("4 groupes de 5:")
    probleme = ProblemeEssaim(
        schwefel,
        10,
        schwefel.borneInf,
        schwefel.borneSup,
        Topologie.nombreGroupe(4),
        20,
        0.7,
        1.47
    );
    methode = MethodePSO(probleme, nIter);
    print(methode.tester(nPerTopology));

    print("5 groupes de 4:")
    probleme = ProblemeEssaim(
        schwefel,
        10,
        schwefel.borneInf,
        schwefel.borneSup,
        Topologie.nombreGroupe(5),
        20,
        0.7,
        1.47
    );
    methode = MethodePSO(probleme, nIter);
    print(methode.tester(nPerTopology));

    print("10 groupes de 2:")
    probleme = ProblemeEssaim(
        schwefel,
        10,
        schwefel.borneInf,
        schwefel.borneSup,
        Topologie.nombreGroupe(10),
        20,
        0.7,
        1.47
    );
    methode = MethodePSO(probleme, nIter);
    print(methode.tester(nPerTopology));

    print("Tous dans différents:")
    probleme = ProblemeEssaim(
        schwefel,
        10,
        schwefel.borneInf,
        schwefel.borneSup,
        Topologie.tousDifferents,
        20,
        0.7,
        1.47
    );
    methode = MethodePSO(probleme, nIter);
    print(methode.tester(nPerTopology));

    print("Von Neumann topology:")
    probleme = ProblemeEssaim(
        schwefel,
        10,
        schwefel.borneInf,
        schwefel.borneSup,
        Topologie.vonNeumann(4, 5),
        20,
        0.7,
        1.47
    );
    methode = MethodePSO(probleme, nIter);
    print(methode.tester(nPerTopology));