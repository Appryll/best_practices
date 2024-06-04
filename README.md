# BioSeq

## Description

From a CSV file, this project converts the DNA string into RNA. It also generates the reverse complementary chain and find restriction sites in a DNA sequence for given restriction enzymes.

## Installation

I) Create a virtual environment

- Navigate to your project directory in your terminal.
- Create the virtual environment:
    ```bash
    python -m venv env
    ````
-  Activate the Virtual Environment
    - On Windows
        ```bash
        .\env\Scripts\activate
        ````
    - On macOS and Linux
        ```bash
        source env/bin/activate
        ````

II) Install dependencies from requirements.txt:

```bash
pip install -r requirements.txt
```

III) Run script
- On Windows
    ```bash
    python BioSeq.py
    ````
- On macOS and Linux
    ```bash
    python3 BioSeq.py
    ````

IV) Deactivate the virtual environment

```bash
deactivate
```
------
### Check Your Code with flake8

- To check all Python files in a directory
```bash
flake8 .
```

- To check a single file:
```bash
flake8 your_script.py
```
------


## License
Open source
