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
        res: float = 0.;
        for x in position:
            res += x * x;
        return res;

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
        res: float = 0.;
        for x in position:
            res += x * math.sin(math.sqrt(math.fabs(x)));
        return 418.9829 * len(position) - res;

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
        res: float = 0.;
        for i in range(len(position) - 1):
            xi = position[i];
            xip1 = position[i + 1];
            m1 = (xip1 - xi * xi);
            m2 = xi - 1;
            res += 100 * m1 * m1 + m2 * m2;
        return res;

    rosenbrock.borneInf = -2.048;
    rosenbrock.borneSup = 2.048;

    def griewank(position: list[float]) -> float:
        """Griewank function
        f(x1, ..., xn) = ∏(cos(xi/√(i+1))) + ∑(xi²/4000)

        Args:
            position (list[float]): _description_

        Returns:
            float: _description_
        """
        res: float = 1.;
        for i in range(len(position)):
            res *= math.cos(position[i] / math.sqrt(i + 1));
        for x in position:
            res += x * x / 4000.;
        return res + 1.;

    griewank.borneInf = -600;
    griewank.borneSup = 600;