# Description

Insert here description of the app

# Installation

## Create a virtual environment

python -m venv venv

## Activate the virtual environment (Windows)

venv\Scripts\activate

## Or (Unix or MacOS)

source venv/bin/activate

## Install your package

pip install -e .

# Run

Now you can run the taxcalculator in the terminal:

```
taxcalculator
```

# Generate wheel

```
python setup.py sdist bdist_wheel
```

Now anyone can install the taxcalculator by using pip and the generated whl file:

```
pip install taxcalculator-1.0.0-py3-none-any.whl
```

And run it

```
taxcalculator
```

# Known issues

MacOS devices have known bugs with the tkinter library. It is suggested to use the python.org version of Python instead of the MacOS one.
