from executions.testBH import testBH
from executions.testComplet import testComplet
from executions.utilisationPySwarms import resolutionAvecPySwarms
from executions.testTopologie import testTopologie
from executions.testResol import testResol

def main():
    # testComplet();
    # testResol();
    # resolutionAvecPySwarms();
    testBH(nEtapes = 100);
    testTopologie(nPerTopology = 100, nIter = 100);
    
main();
