import math


class FonctionsPSO:
    def sphere(position: list[float]) -> float:
        """Sphere function
        f(x1, ..., xn) = ∑(xi²)

        Args:
            position (list[float]): Antecedent.

        Returns:
            float: Image of the given antecedent by the sphere function.
        """
        return sum(x * x for x in position);

    sphere.borneInf = -5.12;
    sphere.borneSup = 5.12;

    def schwefel(position: list[float]) -> float:
        """Schwefel function
        f(x1, ..., xn) = 418.9829⋅n - ∑(xi - sin(√(|xi|)))

        Args:
            position (list[float]): Antecedent.

        Returns:
            float: Image of the given antecedent by the schwefel function.
        """
        return 418.9829 * len(position) - sum(
            x * math.sin(math.sqrt(abs(x)))
            for x in position
        );

    schwefel.borneInf = -500;
    schwefel.borneSup = 500;

    def rosenbrock(position: list[float]) -> float:
        """Rosenbrock function
        f(x1, ..., xn) = ∑(100 ⋅ (x{i+1} - xi²)² + (xi - 1)²)

        Args:
            position (list[float]): Antecedent.

        Returns:
            float: Image of the given antecedent by the rosenbrock function.
        """
        def _terme(indice: int):
            xi = position[indice];
            xip1 = position[indice + 1];
            m1 = (xip1 - xi * xi);
            m2 = xi - 1;
            return 100 * m1 * m1 + m2 * m2;
        return sum(_terme(i) for i in range(len(position) - 1));

    rosenbrock.borneInf = -2.048;
    rosenbrock.borneSup = 2.048;

    def griewank(position: list[float]) -> float:
        """Griewank function
        f(x1, ..., xn) = ∏(cos(xi/√(i+1))) + ∑(xi²/4000)

        Args:
            position (list[float]): Antecedent.

        Returns:
            float: Image of the given antecedent by the griewank funtion.
        """
        return math.prod(
            math.cos(x / math.sqrt(i + 1))
            for i, x in enumerate(position)
        ) + sum(
            x * x
            for x in position
        ) /4000. + 1.;

    griewank.borneInf = -600;
    griewank.borneSup = 600;