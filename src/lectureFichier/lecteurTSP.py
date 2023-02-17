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
    return ProblemeTSP(
          lPoints = [
              Point(nom = name, x = float(xAsString), y = float(yAsString))
              for name, xAsString, yAsString in lire(path)
          ]
     );
