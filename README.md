Project Structure: 
molecular_simulation_code/ 
optimizer.py                 # Core optimization logic (LJ potential + basin-hopping)
visualization.py             # Cluster plotting, energy evolution, animation
io_utils.py                  # XYZ saving, trajectory output 
main.py                      # Run script to launch optimization and generate results 
outputs/                     # Saved figures, XYZ files, GIF animations    
        
Python package dependencies: 
numpy 
scipy 
matplotlib 

How to Run the Code: 
1. Install Dependencies: 
Make sure Python 3.8+ is installed.
Then run: 
pip install -r requirements.txt 
2. Run the Optimization: 
python main.py

This will:
- Optimize the LJ cluster (default: LJ38)
- Save final XYZ structure 
3. Output Files (saved in outputs/):
- LJ38_best_energy.png               (Energy vs. Step plot) 
- LJ38_final.xyz                     (Final optimized coordinates)
- LJ38_trajectory.xyz                (Trajectory of accepted steps)
- LJ38_animation.gif                 (Structure evolution animation)   

Configuration: 
You can modify main.py to: 

- Change number of atoms (e.g., N = 38)
- Adjust number of optimization steps
- Enable or disable visualizat

- ## Download results:
- [Google Drive Folder](https://drive.google.com/drive/folders/1DTMo7RLcVHj8YP78-d_yzcTuiwmO0XU3?usp=sharing)

