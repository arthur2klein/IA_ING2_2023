from testBH import testBH
from testComplet import testComplet
from utilisationPySwarms import resolutionAvecPySwarms
from testTopologie import testTopologie


def main():
    # testComplet();
    # resolutionAvecPySwarms();
    # testBH(1_000);
    # for i in (10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000):
    #     print("Après {} étapes:".format(i));
    #     testTopologie(100, i);
    testTopologie(100, 10000);
    
main();
