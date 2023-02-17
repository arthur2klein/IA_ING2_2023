from executions.testBH import testBH
from executions.testComplet import testComplet
from executions.utilisationPySwarms import resolutionAvecPySwarms
from executions.testTopologie import testTopologie
from executions.testResol import testResol

def main():
    # testComplet();
    # testResol();
    # resolutionAvecPySwarms();
    # testBH(nEtapes = 10);
    n = 10;
    for _ in range(5):
        print(f'{n = }')
        testTopologie(nPerTopology = 100, nIter = n);
        n *= 2;
    
main();
