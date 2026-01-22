# SCOAS: Status Code Analysis in OpenAPI Specifications

Repository for the tool SCOAS.

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