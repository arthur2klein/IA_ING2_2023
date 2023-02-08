from lectureFichier.lecteurFichier import lire
from outils.Point import Point
from probleme.ProblemeTSP import ProblemeTSP


def lireTSP(path: str) -> ProblemeTSP:
    res = [];
    for infos in lire(path):
            res += [Point(infos[0], float(infos[1]), float(infos[2]))];
    return ProblemeTSP(res);
