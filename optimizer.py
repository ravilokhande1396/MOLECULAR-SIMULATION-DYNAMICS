import numpy as np
from scipy.optimize import minimize, basinhopping
from scipy.spatial.distance import pdist, squareform

# Globals for tracking
trial_energies = []
best_energies = []
accepted_positions = []

# Lennard-Jones potential
def lj_potential(positions):
    epsilon = 1.0
    sigma = 1.0
    positions = positions.reshape(-1, 3)
    distances = pdist(positions)
    distances = squareform(distances)
    np.fill_diagonal(distances, np.inf)
    distances[distances < 1e-6] = np.inf
    r6 = (sigma / distances) ** 6
    r12 = r6 ** 2
    energy = 4 * epsilon * np.sum(r12 - r6) / 2
    return energy

# Local minimization
def local_minimization(x0):
    res = minimize(lj_potential, x0, method='L-BFGS-B', tol=1e-6)
    return res.x, res.fun

# Callback for basin-hopping
def bh_callback(x, f, accept):
    trial_energies.append(f)
    if not best_energies or f < best_energies[-1]:
        best_energies.append(f)
    else:
        best_energies.append(best_energies[-1])
    if accept:
        accepted_positions.append(x.reshape(-1, 3))

# Global optimization
def optimize_lj_cluster(N, steps=200):
    x0 = np.random.uniform(-2, 2, (N, 3)).flatten()
    minimizer_kwargs = {"method": "L-BFGS-B"}
    result = basinhopping(lj_potential, x0, niter=steps, minimizer_kwargs=minimizer_kwargs, 
                          T=1.0, stepsize=0.5, callback=bh_callback)
    return result.x.reshape((N, 3)), result.fun, best_energies, accepted_positions
