from main import run

from src.costs import (
    B1HomogeneityCost,
    B1SARHomogeneityCost,
    masked_borders_B1SARHomogeneityCost,
    B1HomogeneityMinMaxCost,
)
from src.data import Simulation
from src.utils import evaluate_coil_config
import plot_final_results as group3_plt

import numpy as np
import json

if __name__ == "__main__":
    # Load simulation data
    simulation = Simulation("data/simulations/children_3_tubes_10_id_6299.h5")

    # Define cost function
    # cost_function = B1HomogeneityCost()
    cost_function = B1HomogeneityMinMaxCost()

    # Run optimization
    best_coil_config = run(simulation=simulation, cost_function=cost_function)

    # cost_function = masked_borders_B1SARHomogeneityCost()
    # best_coil_config = run(simulation=simulation, cost_function=cost_function, start_config = best_coil_config)

    # Evaluate best coil configuration
    # result = evaluate_coil_config(best_coil_config, simulation, cost_function)
    result = evaluate_coil_config(best_coil_config, simulation, cost_function)

    # Save results to JSON file
    with open("results.json", "w") as f:
        json.dump(result, f, indent=4)
    print("end")
