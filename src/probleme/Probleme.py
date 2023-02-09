from solution.Solution import Solution


class Probleme:
    """Interface for problems to solve.
    """
    def candidat(self) -> Solution:
        """Create a candidate that suits the current problem.

        Raises:
            NotImplementedError: This is an abstract function and it is only
            implemented by the children classes.

        Returns:
            Solution: Possible candidate to solve the problem.
        """
        raise NotImplementedError;

    def voisin(self, candidat: Solution) -> Solution:
        """Generate one neighbour of the given solution.

        Args:
            candidat (Solution): Candidate to search a neighbour of.

        Raises:
            NotImplementedError: This is an abstract method and it is only
            implemented by the children classes.

        Returns:
            Solution: Neighbour of the given solution.
        """
        raise NotImplementedError;