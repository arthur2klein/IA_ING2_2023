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
    lecture = lire(path);
    capacite = int(next(lecture)[1]);
    return ProblemeSac(
        lObjets = [
            Objet(masse = int(infos[1]), valeur = int(infos[0]))
            for infos in lecture
        ],
        capacite = capacite
    );
