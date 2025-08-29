from optimizer import optimize_lj_cluster
from visualization import plot_cluster, plot_energy, animate_cluster_evolution
from io_utils import save_xyz
from io_utils import save_xyz_trajectory

def main():
    print("Starting LJ Cluster Optimization...")
    N = 40
    steps = 500

    positions, energy, best_energies, accepted_positions = optimize_lj_cluster(N, steps)

    plot_cluster(positions, title=f"LJ{N} Cluster", save_path=f"LJ{N}_cluster.png")
    save_xyz(f"LJ{N}.xyz", positions)
    save_xyz_trajectory(f"LJ{N}_trajectory.xyz", accepted_positions)
    plot_energy(best_energies,cluster_size=N)
    animate_cluster_evolution(accepted_positions, filename=f"LJ{N}_animation.gif")

    print(f"Optimised energy: {energy}")
    print("All done!")

if __name__ == "__main__":
    main()
