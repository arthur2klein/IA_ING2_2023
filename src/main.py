from executions.testBH import testBH
from executions.testComplet import testComplet
from executions.utilisationPySwarms import resolutionAvecPySwarms
from executions.testTopologie import testTopologie
from executions.testResol import testResol
from executions.testNParticules import testNParticules

def main():
    testComplet();
    testResol();
    resolutionAvecPySwarms();
    testBH(nEtapes = 10);
    testTopologie(nPerTopology = 10, nRepeat = 5);
    testNParticules(
        nTest = 10,
        nParticulesMax = 100,
        tempsParResolution = 0.3,
        nLignes = 5
    );
    
main();
