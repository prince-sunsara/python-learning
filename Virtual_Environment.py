"""
PYTHON VIRUTAL ENVIRONMENT 

    > it is a tools used to isolate specific python environments on a single machine, allowing you to work on miltiple project with different dependencies and packages without conflicts.
    > this can be especially useful when working on project that have conflicting package versions or packages that are not compatible with each other.
    > to create virtual environement in python, you can use the venv module that comes with python.
    
    # Create a virtual environment
    python -m venv myenv

    # Activate the virtual environment (Linux/macOS)
    source myenv/bin/activate
    
    # Activate the virtual environment (Windows)
    source myenv\Scripts\activate.bat
    source myenv\Scripts\activate.ps # in powershall


    > Once the virtual environment is activated, any packages that you install using pip will be installed in the virtual environment, rather than in the global Python environment. 
    > This allows you to have a separate set of packages for each project, without affecting the packages installed in the global environment.

    > To deactivate the virtual environment, you can use the deactivate command:

    # Deactivate the virtual environment
    deactivate


THE "REQUIREMENTS.TXT" FILE

    > In addition to creating and activating a virtual environment, it can be useful to create a requirements.txt file that lists the packages and their versions that your project depends on. 
    > This file can be used to easily install all the required packages in a new environment.
    
    > To create a requirements.txt file, you can use the pip freeze command, which outputs a list of installed packages and their versions.
    
    # Output the list of installed packages and their versions to a file
    pip freeze > requirements.txt
    
    > To install the packages listed in the requirements.txt file, you can use the pip install command with the -r flag:
    
    # Install the packages listed in the requirements.txt file
    pip install -r requirements.txt

    > Using a virtual environment and a requirements.txt file can help you manage the dependencies for your Python projects and ensure that your projects are portable and can be easily set up on a new machine.
"""

import pandas as pd
print(pd.__version__)