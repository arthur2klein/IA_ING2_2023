from lectureFichier.lecteurFichier import lire
from outils.Objet import Objet
from probleme.ProblemeSac import ProblemeSac


def lireSac(path: str) -> ProblemeSac:
    res = [];
    i = 0;
    for infos in lire(path):
        if (i == 0):
            capacite = int(infos[1]);
        res += [Objet(int(infos[1]), int(infos[0]))];
        i += 1;
    return ProblemeSac(res, capacite);
