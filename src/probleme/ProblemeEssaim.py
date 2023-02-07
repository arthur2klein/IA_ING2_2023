import math
from outils.Particule import Particule
from probleme.Probleme import Probleme
from solution.Essaim import Essaim

class ProblemeEssaim(Probleme):
    def __init__(
        self,
        fonction,
        nDimensions: int,
        borneInf: float,
        borneSup: float,
        estDansMemeGroupe,
        tailleEssaim: int,
        inertie: float,
        maxConfiance: float
    ):
        self.fonction = fonction;
        self.tailleEssaim = tailleEssaim;
        self.borneInf = borneInf;
        self.borneSup = borneSup;
        self.estDansMemeGroupe = estDansMemeGroupe;
        self.nDimensions = nDimensions;
        self.inertie = inertie;
        self.maxConfiance = maxConfiance;

    def candidat(self) -> Essaim:
        return Essaim(
            self,
            self.tailleEssaim,
            self.inertie,
            self.maxConfiance
        );

    def voisin(self, candidat: Essaim) -> Essaim:
        candidat.etape();
        return candidat;

class Topologie:
    def tousMemeGroupe(particule1: Particule, particule2: Particule) -> bool:
        return True;
    def tousDifferents(particule1: Particule, particule2: Particule) -> bool:
        return False;
    def etoile(particule1: Particule, particule2: Particule) -> bool:
        return particule1.id == 0 or particule2.id == 0;
    def _nMemeGroupe(n: int, particule1: Particule, particule2: Particule) -> bool:
        return particule1.id // n == particule2.id // n;
    def _nGroupes(n: int, particule1: Particule, particule2: Particule) -> bool:
        return particule1.id % n == particule2.id % n;
    def nombreParGroupe(n: int):
        return lambda p1, p2: Topologie._nMemeGroupe(n, p1, p2);
    def nombreGroupe(n: int):
        return lambda p1, p2: Topologie._nGroupes(n, p1, p2);

# Probleme Sphere
def sphere(position: list[float]):
    res: float = 0.;
    for x in position:
        res += x * x;
    return res;

sphere.borneInf = -5.12;
sphere.borneSup = 5.12;

# Probleme Schwefel
def schwefel(position: list[float]):
    res: float = 0.;
    for x in position:
        res += x * math.sin(math.sqrt(x if (x >= 0) else -x));
    return 418.9829 * len(position) - res;

schwefel.borneInf = -500;
schwefel.borneSup = 500;

# Probleme Rosenbrock
def rosenbrock(position: list[float]):
    res: float = 0.;
    for i in range(len(position) - 1):
        xi = position[i];
        xip1 = position[i + 1];
        m1 = (xip1 - xi * xi);
        m2 = xi - 1;
        res += 100 * m1 * m1 + m2 * m2;
    return res;

rosenbrock.borneInf = -2.048;
rosenbrock.borneSup = 2.048;

# Probleme Griewank
def griewank(position: list[float]):
    res: float = 1.;
    for i in range(len(position)):
        res *= math.cos(position[i] / math.sqrt(i + 1));
    for x in position:
        res += x * x / 4000.;
    return res + 1.;

griewank.borneInf = -600;
griewank.borneSup = 600;