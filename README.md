# AquiMod 2 Automation Pipeline

This repository contains a modular, scriptable pipeline to prepare, run, and analyze groundwater simulations using the [AquiMod 2](https://www.bgs.ac.uk/software/aquimod/) model.

Designed by and for hydrologists, researchers, and data scientists, it enables full automation of:

- Input file generation (`Input.txt`, `Observations.txt`, calibration files)
- Model execution (via `subprocess`)
- Post-processing of simulation results
- Optional integration with online sources (e.g., ECMWF, Holykell IoT)

---

Folder Structure
Aquimod2/
├── notebooks/ # Jupyter notebooks for controlling the workflow
│ └── aquimod2_pipeline.ipynb
├── utils/ # Python functions (input generation, run, parse)
│ └── aquimod2_helpers.py
├── scenarios/ # Model folders for active simulations
│ ├── CHexample/
│ └── CFexample/
├── examples/ # Reference inputs from AquiMod manual
│ ├── CHexample/
│ └── CFexample/
├── selenium_bot/ # Scripts to automate downloading sensor data
│ └── holykell_downloader.py
├── data/ # Optional: raw data inputs or examples
├── requirements.txt
└── README.md


How to Use

1. Clone the repository or set it up in D:\Github\Aquimod2
2. Activate your Python environment and install dependencies:

	pip install -r requirements.txt

3. Run the notebook:
	cd notebooks
	jupyter lab aquimod2_pipeline.ipynb

4. Customize scenario folders and configurations using the utility functions.


Tools Used
Python 3.9+
Pandas, Matplotlib
Selenium (for sensor portal automation)
Git + GitHub
AquiMod 2 (precompiled Windows executable)


Data Sources
ECMWF Copernicus API (optional)
Holykell IoT portal dashboard (in progress integration)


Notes
This project is in active development
Designed for modular growth: you can add support for more models, UI widgets, and parameter batch runners
Parameter sensitivity, batch evaluation, and scenario comparison features are coming


License
This repository is intended for research and educational use. Please credit the AquiMod2 developers where appropriate.



Made with Python by EOM
hehe oink oink
