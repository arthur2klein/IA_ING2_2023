from executions.testBH import testBH
from executions.testComplet import testComplet
from executions.utilisationPySwarms import resolutionAvecPySwarms
from executions.testTopologie import testTopologie
from executions.testResol import testResol
from executions.testNParticules import testNParticules

def main():
    testComplet();
    # testResol();
    # resolutionAvecPySwarms();
    # testBH(nEtapes = 10);
    # testTopologie(nPerTopology = 100, nIter = 200);
    # testNParticules(nTest = 10, nParticules = 20);
    
main();
