# Recipes & Shopping List Management API

## Overview
This API allows users to manage a collection of recipes and generate shopping lists based on the 
ingredients needed for these recipes. 
Users can create, read, update, and delete both recipes and shopping lists.

It is developed with FAST API.

## Build and run API with Docker

### Prerequisites (Windows)

1 - Install wsl (https://learn.microsoft.com/windows/wsl/install)
2 - Install DockerDesktop (https://docs.docker.com/desktop/install/windows-install/)

### Build and run

1 - Open DockerDesktop
2 - Build image by running this command in your terminal:
`docker build -t recipes-app .`

3 - Run the container by running this command:
`docker run -p 8080:8080 recipes-app`

4 - API must be running at: http://127.0.0.1:8080/

5 - API docs  available here:

* Swagger UI: http://127.0.0.1:8080/docs
* ReDoc: http://127.0.0.1:8080/redoc 
 
- ToDo: complete instructions.


## Installation for developers

### Prerequisites

1 - Install Python 3.11+ (https://www.python.org/downloads/)

2 - Install pipx (https://pipx.pypa.io/stable/installation/)

*Linux:*  
`python3 -m pip install --user pipx`

*Windows:*
`py -m pip install --user pipx`

It is possible the above finishes with a WARNING looking similar to this:
WARNING: The script pipx.exe is installed in `<USER folder>\AppData\Roaming\Python\Python3x\Scripts` which is not on PATH

If so, go to the mentioned folder, allowing you to run the pipx executable directly. Enter the following line 
(even if you did not get the warning):
.\pipx.exe ensurepath
This will add both the mentioned above path and the %USERPROFILE%\.local\bin folder to your search path. 
Restart your terminal session and verify pipx does run.


**For other installation options check the link above.**


3 - Install Poetry for dependency management (https://python-poetry.org/docs/#installation):
`pipx install poetry`

### Setup

1 - Clone the repository

`git clone https://github.com/antobarbero/my-recipes-shopping-list.git`

2 - Create a virtualenvironment and install dependencies with poetry by running this command:

`poetry install`

3 - Activate the created virtual environment (.venv) 

Windows: `.venv\Scripts\activate`

Or set the created virtual environment as your project interpreter and open a new terminal to have it activated.

(in pycharm: Settings -> Python Interpreter -> add local 
  -> Select 'Existing'-> Select "my-recipes-shopping-list\.venv\Scripts\python.exe)

4 - Run the server:

`uvicorn app.main:app`

5 - Open your browser at

http://127.0.0.1:8000/

6 - Before contributing, install the pre-commit hooks by running the following command:

`pre-commit install`

This will automatically execute some hooks when you commit your changes
to format the code, checking complexity, typehints, etc.
You can see all the activated hooks in the `.pre-commit-config.yaml` file.

### API Documentation

API docs  available here:

* Swagger UI: http://127.0.0.1:8000/docs
* ReDoc: http://127.0.0.1:8000/redoc


### Run tests

`pytest tests`
