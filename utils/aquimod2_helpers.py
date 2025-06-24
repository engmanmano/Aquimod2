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
        [exe_path, working_directory],
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


def load_component_gwl_output(scenario_path, component_file="Q3K3S1_TimeSeries1.out"):
    """
    Load GWL time series from a component-specific TimeSeries1.out file.
    Default is Q3K3S1_TimeSeries1.out
    """
    file_path = os.path.join(scenario_path, "Output", component_file)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Output file not found: {component_file}")

    df = pd.read_csv(file_path, sep=r'\s+')
    df["Date"] = pd.to_datetime(df[["Year", "Month", "Day"]])
    return df
    


def plot_gwl_results(df, column="GWL(m)"):
    """
    Plot groundwater level or other selected variable from component output.
    """
    plt.figure(figsize=(10, 4))
    plt.plot(df["Date"], df[column], label=f"Simulated {column}", color="royalblue")
    plt.xlabel("Date")
    plt.ylabel(column)
    plt.title(f"Simulated {column} Over Time")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


def update_output_flags(input_txt_path, new_flags="N Y Y"):
    """
    Updates the 'Write model output files' line in Input.txt
    
    Parameters:
    - input_txt_path (str): Full path to Input.txt
    - new_flags (str): New flag string, e.g. 'N Y Y'
    """
    with open(input_txt_path, "r") as f:
        lines = f.readlines()

    for i in range(len(lines)):
        if lines[i].strip() == "Write model output files":
            lines[i + 1] = new_flags + "\n"
            break
    else:
        raise ValueError("Could not find 'Write model output files' block in Input.txt")

    with open(input_txt_path, "w") as f:
        f.writelines(lines)

    print(f"Updated output flags to: {new_flags}")

