import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
from methodeResolution.MehodePSO import MethodePSO
from outils.FonctionsPSO import FonctionsPSO
from outils.Topologies import Topologie
from probleme.ProblemeEssaim import ProblemeEssaim

#pipenv run pip install pyswarms
def resolutionAvecPySwarms():
    """Solve the same PSO Rosenbrock problem with the pyswarm library as well
    as the method defined in this project.
    """
    options = {
        'c1': 1.47,
        'c2': 1.47,
        'w': 0.7
    };
    optimizer_10particules = ps.single.GlobalBestPSO(
        n_particles = 10,
        dimensions = 10,
        options = options,
        ftol = 1e-8
    );
    best_cost, best_pos = optimizer_10particules\
        .optimize(objective_func = fx.rosenbrock, iters = 1000);
    print(f"best_cost: {best_cost}\nbest_pos: {best_pos}");

    print("Comparaison:")
    probleme = ProblemeEssaim(
        fonction = FonctionsPSO.rosenbrock,
        nDimensions = 10,
        borneInf = FonctionsPSO.rosenbrock.borneInf,
        borneSup = FonctionsPSO.rosenbrock.borneSup,
        estDansMemeGroupe = Topologie.roue,
        tailleEssaim = 10,
        inertie = 0.7,
        maxConfiance = 1.47
    );
    methode = MethodePSO(probleme = probleme, nEtapes = 1000);
    solution = methode.resoudre();
    best_cost, best_pos = solution.evaluer(), solution.meilleurPos();
    print(
        f'best_cost: {best_cost:0.5f}'
        f'\nbest_pos: {[f"{x:0.5f}" for x in best_pos]}'
    );
