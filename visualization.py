import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Cluster scatter plot
def plot_cluster(positions, title="LJ Cluster", save_path=None):
    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(positions[:, 0], positions[:, 1], positions[:, 2], c='b', s=50)
    ax.set_title(title)
    if save_path:
        plt.savefig(save_path, dpi=300)
    plt.show()

def plot_energy(best_energies, cluster_size, save_path=None, show=True):
   
    plt.figure(figsize=(8, 5))
    plt.plot(best_energies, label=f"Best Energy for LJ{cluster_size}", color='darkblue')
    plt.xlabel("Step Number")
    plt.ylabel("Best Potential Energy")
    plt.title(f"Best Energy Evolution for LJ{cluster_size}")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    
    if save_path is None:
        save_path = f"LJ{cluster_size}_best_energy.png"
    
    plt.savefig(save_path, dpi=300)
    if show:
        plt.show()


# Animation of optimization steps
def animate_cluster_evolution(positions_list, filename="cluster_evolution.gif"):
    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(111, projection='3d')
    scatter = ax.scatter([], [], [], s=50, c='blue')

    def init():
        ax.set_xlim(-5, 5)
        ax.set_ylim(-5, 5)
        ax.set_zlim(-5, 5)
        return scatter,

    def update(frame):
        pos = positions_list[frame]
        scatter._offsets3d = (pos[:, 0], pos[:, 1], pos[:, 2])
        ax.set_title(f"Step {frame}")
        return scatter,

    anim = FuncAnimation(fig, update, frames=len(positions_list),
                         init_func=init, blit=False, interval=200)

    anim.save(filename, dpi=100, writer=PillowWriter(fps=5))
    print(f"Animation saved as '{filename}'")
