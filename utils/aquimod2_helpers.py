import os
import subprocess
import pandas as pd
import matplotlib.pyplot as plt

def run_aquimod2(exe_path, working_directory):
    """
    Run AquiMod2 executable in the specified scenario folder.
    """
    if not os.path.isfile(exe_path):
        raise FileNotFoundError(f"Executable not found: {exe_path}")
    if not os.path.isdir(working_directory):
        raise FileNotFoundError(f"Scenario folder not found: {working_directory}")

    print(f"Running AquiMod2 in: {working_directory}")
    result = subprocess.run(
        [exe_path],
        cwd=working_directory,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print("AquiMod2 failed to run.")
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
    else:
        print("Simulation completed successfully.")
        print("Output:", result.stdout)

def load_gwl_output(scenario_path):
    """
    Load groundwater level simulation results from Output/GWL_sim.out
    """
    file_path = os.path.join(scenario_path, "Output", "GWL_sim.out")
    if not os.path.exists(file_path):
        raise FileNotFoundError("Output file not found: GWL_sim.out")

    df = pd.read_csv(file_path, delim_whitespace=True, header=None,
                     names=["DAY", "MONTH", "YEAR", "GWL_sim"])
    return df

def plot_gwl_results(df):
    """
    Plot groundwater level simulation results.
    """
    dates = pd.to_datetime(df[["YEAR", "MONTH", "DAY"]])
    plt.figure(figsize=(10, 4))
    plt.plot(dates, df["GWL_sim"], label="Simulated GWL")
    plt.xlabel("Date")
    plt.ylabel("Groundwater Level (m)")
    plt.title("Simulated Groundwater Levels")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
