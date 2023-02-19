import time
from methodeResolution.Methode import Methode
from probleme.ProblemeEssaim import ProblemeEssaim
from solution.Essaim import Essaim


class MethodePSOTime(Methode):
    """Method solving a continuous problem using Particule Swarms Optimisation.
    A swarm of particules are randomly placed in a space assigning a value to
    each point and the particules try to find the best points by following:
    their own inertia; the best position they have individually found; the best
    position their group has found.
    """
    def __init__(
            self,
            probleme: ProblemeEssaim,
            timeAllowed: float
        ):
        """Create a method of resolution of the given continuous problem that
        will use the PSO method using the allowed time.

        Args:
            probleme (ProblemeEssaim): Problem to solve.
            timeAllowed (float): Time allowed for the resolution (in seconds).
        """
        self.probleme = probleme;
        self.timeAllowed = timeAllowed;

    def resoudre(self) -> Essaim:
        """Solve the problem of the instance using the PSO method.
        A swarm of particules are randomly placed in a space assigning a value to
        each point and the particules try to find the best points by following:
        their own inertia; the best position they have individually found; the best
        position their group has found.

        Returns:
            Essaim: Swarm that found the best position.
        """
        timeStart = time.time();
        timeEnd = timeStart + self.timeAllowed;
        essaim = self.probleme.candidat();
        while time.time() < timeEnd:
            essaim.etape();
        return essaim;