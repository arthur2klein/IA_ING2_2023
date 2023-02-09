from lectureFichier.lecteurFichier import lire
from outils.Objet import Objet
from probleme.ProblemeSac import ProblemeSac


def lireSac(path: str) -> ProblemeSac:
    """Read a file containing a number of Objet and a capacity in the first
    line and a masse and value for each following line.

    Args:
        path (str): File that contains a number of Objet and a capacity in the
        first line and a masse and value for each following line.

    Returns:
        ProblemeSac: Knoapsack problem corresponding to the given capacity and
        list of Objet.
    """
    res = [];
    i = 0;
    for infos in lire(path):
        if (i == 0):
            capacite = int(infos[1]);
        res += [Objet(int(infos[1]), int(infos[0]))];
        i += 1;
    return ProblemeSac(res, capacite);
