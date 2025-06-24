# AquiMod2 Python Helpers

This file documents the helper functions included in `utils/aquimod2_helpers.py` and their purpose within the AquiMod2 simulation pipeline.

---

## `run_aquimod2(exe_path, working_directory)`

Runs the AquiMod2 executable inside the specified scenario folder.

**Parameters:**

* `exe_path` — Absolute path to `AquiMod2.exe`
* `working_directory` — Full path to the scenario folder (should contain `Input.txt` and `Observations.txt`)

---

## `update_output_flags(input_txt_path, new_flags="N Y Y")`

Updates the output flags line in `Input.txt` to control which output files are generated.

**Parameters:**

* `input_txt_path` — Full path to the scenario's `Input.txt`
* `new_flags` — A string like `"N Y Y"` indicating which output files should be written

---

## `load_component_gwl_output(scenario_path, component_file="Q3K3S1_TimeSeries1.out")`

Loads a time series output from a component file (like `Q3K3S1_TimeSeries1.out`) which includes `GWL(m)` and possibly flow (`Q_*`) columns.

**Returns:**
A DataFrame with parsed date and all available columns.

---

## `plot_gwl_results(df, column="GWL(m)")`

Plots a time series from a DataFrame, typically the simulated groundwater level (GWL).

**Parameters:**

* `df` — DataFrame containing a `Date` column and the target column
* `column` — The column name to plot (defaults to `GWL(m)`)

---

> 📌 These functions are designed to be reusable across multiple scenarios during calibration, evaluation, or post-processing.
