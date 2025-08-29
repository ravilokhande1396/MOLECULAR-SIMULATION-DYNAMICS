def save_xyz(filename, positions):
    N = len(positions)
    with open(filename, 'w') as f:
        f.write(f"{N}\nLennard-Jones cluster\n")
        for (x, y, z) in positions:
            f.write(f"X {x:.6f} {y:.6f} {z:.6f}\n")
def save_xyz_trajectory(filename, all_positions):
    with open(filename, 'w') as f:
        for positions in all_positions:
            f.write(f"{len(positions)}\n")
            f.write("Lennard-Jones trajectory frame\n")
            for (x, y, z) in positions:
                f.write(f"X {x:.6f} {y:.6f} {z:.6f}\n")
