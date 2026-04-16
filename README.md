# SCOAS: Status Code Analysis in OpenAPI Specifications

Repository for the tool SCOAS.

## Citation

If you use this tool in your research or find it useful in your work, please cite our paper:

Decrop, A., Papadakis, M. and Perrouin, G. 2026. Analyzing Status Code Misuses in REST API Specifications. In Proceedings of the 26th International Conference on Web Engineering, ICWE 2026.

```bibtex
@inproceedings{decrop2026analyzing,
    title={Analyzing Status Code Misuses in REST API Specifications},
    author={Decrop, Alix and Papadakis, Mike and Perrouin, Gilles},
    booktitle={Proceedings of the 26th International Conference on Web Engineering, ICWE 2026},
    year={2026}
}
```

## Installation

To install and use the tool, you can follow the instructions below.

### 1. Clone the Repository

First, clone the repository of the tool and navigate to it with:

```bash
git clone https://github.com/alixdecr/scoas
cd <your-repository-folder>
```

### 2. Create a Virtual Environment

To use the tool, a Python virtual environment is recommended to avoid messing up your main Python interpreter. To do so, execute the following command in your repository folder:

```bash
python -m venv .venv
```

Which will create a Python virtual environment in the `.venv` folder. Depending on your Python installation and operation system, you might need to replace `python` with `py`, `python3`, or something else.

### 3. Activate the Virtual Environment

To activate the newly created virtual environment, execute the following command depending on your operating system:

#### Linux / macOS

```bash
source .venv/bin/activate
```

#### Windows

##### CMD

```bash
.venv\Scripts\activate.bat
```

##### PowerShell

```bash
.venv\Scripts\Activate.ps1
```

### 4. Install the Requirements

Before using the tool, you must upgrade pip and install the requirements using:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Execute the Tool

After installation, you can execute the tool with the following command:

```bash
python src/main.py
```

Steps 4 and 5 need to be done with the virtual environment activated (which should be the case if you followed step 3 correctly).

## Using the Tool

### 1. OAS File Folder

To execute SCOAS on OpenAPI Specifications, insert their files (must be in JSON `.json` format) in the `data/oas` folder. If for any reason you wish to use another OAS folder, modify the `OAS_PATH` variable located in `src/config.py`.

### 2. Execute the Tool

Execute the tool with the following command:

```bash
python src/main.py
```

### 3. Visualize Results

Once the execution is finished, you will be able to visualize the following:

- The execution logs, located in the `logs` folder.
- The execution raw data, located in the `outputs/<oas-name>/execution.json` file.
- The execution report, located in the `outputs/<oas-name>/report.html` file.


### 4. Fix the Status Code Misuses

After analyzing the execution report, feel free to modify your OpenAPI Specification based on the rule violations that were identified.