# AquiMod2 Output File Reference

This document provides an overview and interpretation guide for the most commonly generated output files from AquiMod2, based on both the official manual and observed output behavior.

---

## 📁 Output File Overview

Output files are written to the `Output/` folder of each scenario, depending on simulation mode and `Input.txt` flags.

### 🧪 Evaluation Mode (`e`)

Produces:

* `fit_eval.out`: Performance score per parameter set
* `*_TimeSeries1.out`: Time series for each model component (e.g. `Q3K3S1_TimeSeries1.out`)

### 🔁 Calibration Modes (`m`, `s`)

Produces:

* `fit_calib.out`: Objective scores for calibration sets
* `*_calib.out`: Parameter sets generated during calibration (e.g. `Weibull_calib.out`)

---

## 📊 Time Series Output (`*_TimeSeries1.out`)

Each file corresponds to one component (soil, aquifer, recharge) for one parameter set.

### Example Columns:

| Column Name          | Description                              |
| -------------------- | ---------------------------------------- |
| `Day` `Month` `Year` | Date of the record                       |
| `Q_3(m3/d)`          | Discharge from top aquifer layer (z₃)    |
| `Q_2(m3/d)`          | Discharge from middle aquifer layer (z₂) |
| `Q_1(m3/d)`          | Discharge from bottom aquifer layer (z₁) |
| `GWL(m)`             | Simulated groundwater level (meters)     |

📌 Not all components produce the same variables. For example:

* Aquifer component → includes `Q_*`, `GWL`
* Recharge component → may produce head levels, recharge flux
* Soil component → may output soil water storage or deficit

### Notes:

* Units for discharge: cubic meters per day (`m³/d`)
* Units for GWL: meters above datum

---

## 📈 `fit_eval.out` / `fit_calib.out`

Text file listing objective function scores for each parameter set.

| Column  | Description                             |
| ------- | --------------------------------------- |
| `Index` | Parameter set index                     |
| `Score` | RMSE or other selected objective metric |

Used to evaluate how well each parameter set matches observed data.

---

## 📄 Calibration Outputs (`*_calib.out`)

Match the structure of evaluation input files (`*_eval.txt`) and contain the sampled/calibrated parameter values.

* One file per component (e.g., `FAO_calib.out`)
* Only produced in Monte Carlo (`m`) or SCE-UA (`s`) mode

---

## 📌 Tips for Interpretation

* Compare `GWL(m)` in simulated vs observed to assess accuracy
* Review `Q_*` trends to understand aquifer dynamics across layers
* Use `fit_eval.out` scores to rank and select parameter sets

---

📖 Based on: *AquiMod2 User Manual (2024)* and verified output behavior
