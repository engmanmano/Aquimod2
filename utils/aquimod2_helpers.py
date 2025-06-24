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
    


def plot_gwl_results(df, column):
    """
    Plot groundwater level or other selected variable from component output.
    """
    plt.figure(figsize=(10, 4))

    if "Date" in df.columns:
        x = df["Date"]
    else:
        x = df.index  # fallback to row index

    plt.plot(x, df[column], label=f"Simulated {column}", color="royalblue")
    plt.xlabel("Date" if "Date" in df.columns else "Index")
    plt.ylabel(column)
    plt.title(f"Component Output: {column}")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def update_output_flags(input_txt_path, new_flags="N Y Y"):
    """
    Updates the 'Write model output files' line in Input.txt

    Parameters:
    - input_txt_path (str): Full path to Input.txt
    - new_flags (str): New flag string, e.g. 'N Y Y'
    """
    update_input_option(input_txt_path, "Write model output files", new_flags)



def update_input_option(input_txt_path, keyword, new_value):
    """
    Generic updater for any block in Input.txt.
    Finds a keyword and replaces the line following it with the given value.

    Parameters:
    - input_txt_path (str): Path to Input.txt
    - keyword (str): The exact label/heading to find (e.g. 'Simulation mode')
    - new_value (str): The new string to place after the keyword line
    """
    with open(input_txt_path, "r") as f:
        lines = f.readlines()

    for i in range(len(lines)):
        if lines[i].strip() == keyword:
            lines[i + 1] = new_value + "\n"
            break
    else:
        raise ValueError(f"Could not find '{keyword}' in Input.txt")

    with open(input_txt_path, "w") as f:
        f.writelines(lines)

    print(f"Updated '{keyword}' to: {new_value}")

from ipywidgets import interact, Dropdown



def interactive_component_plot(df, exclude=["Day", "Month", "Year", "Date"]):
    """
    Displays an interactive dropdown to plot any numeric column from a component output DataFrame.

    Parameters:
    - df (pd.DataFrame): Time series DataFrame with a 'Date' column
    - exclude (list): Columns to ignore in the dropdown (e.g., non-numeric or index columns)
    """
    options = [col for col in df.columns if col not in exclude]

    def plot_selected(column):
        plot_gwl_results(df, column=column)

    interact(plot_selected, column=Dropdown(options=options, description="Plot:"));


def get_input_value(input_txt_path, keyword):
    """
    Retrieves the value line that follows a keyword in Input.txt.

    Parameters:
    - input_txt_path (str): Path to Input.txt
    - keyword (str): Header label to search for

    Returns:
    - str: The value string following the keyword line
    """
    with open(input_txt_path, "r") as f:
        lines = f.readlines()

    for i in range(len(lines)):
        if lines[i].strip() == keyword:
            return lines[i + 1].strip()
    
    raise ValueError(f"Keyword '{keyword}' not found in Input.txt")


def summarize_input_file(input_txt_path, fields=None):
    """
    Prints a summary of selected Input.txt settings.

    Parameters:
    - input_txt_path (str): Path to Input.txt
    - fields (list of str): Keywords to summarize (optional)
    """
    default_fields = [
        "Simulation mode",
        "Monte Carlo parameters",
        "SCE-UA parameters",
        "Evaluation parameters",
        "Objective function and parameters",
        "Spin-up period",
        "Write model output files"
    ]
    fields = fields or default_fields

    print("📋 AquiMod2 Configuration Summary\n" + "-" * 40)
    for field in fields:
        try:
            value = get_input_value(input_txt_path, field)
            print(f"{field}: {value}")
        except Exception as e:
            print(f"{field}: ❌ Not found or invalid")

from ipywidgets import interact, Dropdown
import os
import pandas as pd  # make sure this is imported at the top of your file

def interactive_file_plot(scenario_path):
    """
    Interactive tool to select an .out file from the Output folder,
    then choose a column to plot using a dropdown.

    Parameters:
    - scenario_path (str): Full path to the scenario folder
    """
    output_folder = os.path.join(scenario_path, "Output")
    files = [f for f in os.listdir(output_folder) if f.endswith(".out")]

    def choose_file(file):
        file_path = os.path.join(output_folder, file)
        df = pd.read_csv(file_path, sep=r'\s+')

        # Only create a Date column if all three fields are present
        if {"Day", "Month", "Year"}.issubset(df.columns):
            df["Date"] = pd.to_datetime(df[["Year", "Month", "Day"]])
        else:
            print("⚠️ This file does not have Day/Month/Year columns — plotting may not work.")

        interactive_component_plot(df)

    interact(choose_file, file=Dropdown(options=files, description="File:"))

