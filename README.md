# Recipes & Shopping List Management API

## Overview
This API allows users to manage a collection of recipes and generate shopping lists based on the 
ingredients needed for these recipes. 
Users can create, read, update, and delete both recipes and shopping lists.

It is developed with FAST API.

## Installation

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
This will add both the above mentioned path and the %USERPROFILE%\.local\bin folder to your search path. 
Restart your terminal session and verify pipx does run.


**For other installation options check the link above.**


3 - Install Poetry for dependency management and packaging (https://python-poetry.org/docs/#installation):
`pipx install poetry`

### Setup

1 - Clone the repository

`git clone https://github.com/antobarbero/my-recipes-shopping-list.git`

2 - Create a virtualenvironment and activate it with poetry.

``

3 - Install dependencies with poetry:

`poetry install`
