# A Color API written in Python

This is a sample project that implement the Color API with Python/Flask. It
is useful to demonstrate [go-crzy/crzy](https://github.com/go-crzy/crzy). To
test the project, we assume you have Python3

Start by configuring venv and doanloading the required libraries:

```bash
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

To test the project, run:

```bash
. venv/bin/activate
python -m unittest test_*.py -v
```

The artifact is named color.jar and is located in the `build/jar` directory.
To use it, simply run:

```bash
. venv/bin/activate
export FLASK_APP=color.py
python -m flask run
```
