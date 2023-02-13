class Objet:
    """Object of the knapsack problem.
    """
    def __init__(
        self,
        masse: int,
        valeur: int
    ):
        """Create a new object with the given weight and value.

        Args:
            masse (int): Weight of the object.
            valeur (int): Value of the object.
        """
        self.masse = masse;
        self.valeur = valeur;

    def densite(self) -> float:
        """Determine the density of value of the current object.

        Returns:
            float: Density of value of the current object.
        """
        return self.valeur / self.masse;

    def __str__(self) -> str:
        """Create a string containing all the informations of the object.

        Returns:
            str: String containing all the informations of the objects.
        """
        return f'Objet de masse {self.masse} et de valeur {self.valeur}';