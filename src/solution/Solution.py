class Solution:
    """Interface for solutions of problems.
    """
    def evaluer(self) -> float:
        """Evaluate the current solution.

        Raises:
            NotImplementedError: This is an abstract function and it is only
            implemented by its children classes.

        Returns:
            float: Evaluation of the current solution.
        """
        raise NotImplementedError;