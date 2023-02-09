from lectureFichier.lecteurFichier import lire
from outils.Point import Point
from probleme.ProblemeTSP import ProblemeTSP


def lireTSP(path: str) -> ProblemeTSP:
    """Read a file containing a list of coordinates to create a TSP.

   Args:
        path (str): Path of the file containing the coordinates of the points
        of the TSP.

   Returns:
        ProblemeTSP: TSP corresponding to the points of the file
   """
    res = [];
    for infos in lire(path):
            res += [Point(infos[0], float(infos[1]), float(infos[2]))];
    return ProblemeTSP(res);
