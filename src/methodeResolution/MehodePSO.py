from methodeResolution.Methode import Methode
from probleme.ProblemeEssaim import ProblemeEssaim
from solution.Essaim import Essaim


class MethodePSO(Methode):
    """Method solving a continuous problem using Particule Swarms Optimisation.
    A swarm of particules are randomly placed in a space assigning a value to
    each point and the particules try to find the best points by following:
    their own inertia; the best position they have individually found; the best
    position their group has found.
    """
    def __init__(
            self,
            probleme: ProblemeEssaim,
            nEtapes: int
        ):
        """Create a method of resolution of the given continuous problem that
        will use the PSO method with a given number of steps for its resolution.

        Args:
            probleme (ProblemeEssaim): Problem to solve.
            nEtapes (int): Number of steps to use to solve the problem.
        """
        self.probleme = probleme;
        self.nEtapes = nEtapes;

    def resoudre(self) -> Essaim:
        """Solve the problem of the instance using the PSO method.
        A swarm of particules are randomly placed in a space assigning a value to
        each point and the particules try to find the best points by following:
        their own inertia; the best position they have individually found; the best
        position their group has found.

        Returns:
            Essaim: Swarm that found the best position.
        """
        essaim = None;
        return min(
            (
                essaim := self.probleme.voisin(candidat = essaim)
                for _ in range(self.nEtapes + 1)
            ),
            key = lambda x: x.evaluer()
        );