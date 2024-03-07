<p  align="center">
  <img src='logo.png' width='200'>
</p>

# Template Workshop
[![License](https://img.shields.io/github/license/akatief/template-workshop)](https://opensource.org/licenses/Apache-2.0)
[![Python Versions](https://img.shields.io/badge/Python-3.9-blue.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![CI](https://github.com/akatief/template-workshop/actions/workflows/main.yml/badge.svg)](https://github.com/akatief/template-workshop/actions/workflows/main.yml)

Welcome! In this workshop you'll learn how to set up your next research project using the official [UKP Template](https://github.com/UKPLab/ukp-project-template). This repo is actually a copy of the original template with a few changes to the README, everything else is the same.

What we will cover today:
- How to setup a project created with the repo, 
- How to add changes (which file to edit for implementing your projects),
- How you can check that development is going well with tests and [GitHub Actions](https://docs.github.com/en/actions). 

Let's get started!

## 🚦 Task 0 - Getting started

First thing first, you need to have a copy of this repository on your own GitHub account as well as on your PC.   

1. Set the repository up in your personal GitHub account by clicking **[Use this template](https://github.com/akatief/template-workshop/generate)**. It's important you set the repository as **public**, otherwise the following tasks won't work correctly.
2. Wait until the first run of CI finishes. Github Actions will commit to your new repo with a "✅ Ready to clone and code" message.
3. Open the repo folder and prepare a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
pip install .
pip install -r requirements-dev.txt
```

Congratulations, you just kickstarted your project! Now the interesting part begins.

## 💻 Task 1 - Implementing a simple command 

In this task you will learn where to implement new functionalities for your project (aka good practices on where to put your code). Additionally, you will write a command line interface (CLI) to run your function in the same way you would run your experiment.

Write a class to compute the Fibonacci sequence in an optimal way. Then, implement the necessary code to compute a Fibonacci number from command line. The Fibonacci sequence is defined recursively as `fib(n) = fib(n-1) + fib(n-2)` and its stopping condition is `fib(1) = fib(2) = 1`. To avoid re-computing previous steps you can cache them in a dictionary and re-use them. Be sure to correctly hook up your new class with the rest of the package by modifying all files listed below. 

This is the expected command line usage you should implement:
```bash
template_workshop n # Will return fib(n)
```

### What to change

You need to add your code to the following files:

- `template_workshop/__init__.py`: Defines the content of the template_workshop package. It's important to configure it properly to have a cleaner `import` structure in your code. Use it to avoid ugly [absolute imports](https://www.geeksforgeeks.org/absolute-and-relative-imports-in-python/).
- `template_workshop/cli.py`: Defines how to handle CLI arguments and calls the Fibonacci class.
- `template_workshop/fibonacci.py`: Contains the Fibonacci class.

## 🩺 Task 2 - Implementing tests

Testing is an integral part of development that ensures your code works by covering all edge cases. The percentage of your lines that are checked by tests is called *coverage*. In an ideal testing scenario you would run at every single line in your code least once. A test suite is a collection of simple functions that call different parts of your code and make some assertions. For example, here is the content of `test_base.py`, a suite for testing the (rather useless) `BaseClass` included in the package. As you can see, it runs every possible use case of BaseClass.

```py
from template_workshop import BaseClass

def test_template():
    assert True

def test_base_class():
    bc1 = BaseClass(name="test1")
    bc2 = BaseClass(name="test2")

    assert str(bc1) == "test1"
    assert repr(bc1) == "test1"
    assert bc1 != bc2
```

All your test suites can be run by calling from command line (a full list of arguments can be found [here](https://docs.pytest.org/en/8.0.x/)):

```bash
pytest -v --cov-fail-under=90 --cov=template_workshop -l --tb=short --maxfail=1 tests/
```

Let's now turn to the class you've just implemented. You want to make sure your code *actually* works and handles all cases. For example, have you thought of what would happen if someone called `template_workshop -1`? First, write code in Fibonacci to handle what to do with negative (or zero) numbers. Then, write tests for `Fibonacci` to check that your code actually works. Your test should all complete successfully and coverage (as computed by the command above) should be at least 90% (as controlled by the `--cov-fail-under=90` in the command above.

### What to change

You need to work on the following files:

- `tests/tests_fib.py`: Contains the test suite for the Fibonacci class. Change it to obtain 90% coverage.
- `template_workshop/fibonacci.py`: Contains the Fibonacci class. Change it to fix bugs found during testing.

## 🩺 Task 3 - Using GitHub Actions to check for mistakes

GitHub Actions are another component to help you manage your project. In a nutshell, they are bash scripts called on some VM on GitHub's server. They are used to provide a reference platform for your code and make sure that things like setup, testing, etc. work on _any_ device. Another use case is automatic deployment of your package on [PyPi](https://pypi.org/), your website, or your Hugging Face model. This repository already contains some.

This is an example GitHub Action that runs a linter on your code to check for formatting errors:

```yml
name: CI # Name of the action on GitHub's page

on: # What triggers the action
  push:
    branches: [ main ] # In this case a push on the main branch

jobs: # List of separate jobs to run 
  linter: # Name of a job
    runs-on: ubuntu-latest # Which OS to run the job on
    steps: # List of steps
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with: 
          python-version: 3.9
          
      - name: Install dependencies
        run: |
          pip install -r requirements-dev.txt

      - name: Analysing the code with pylint
        run: | # Long ugly scary line to run the linter on all .py files
          pylint --disable=trailing-whitespace,missing-class-docstring,missing-final-newline,trailing-newlines \
                  --fail-under=9.0 \
                  $(git ls-files '*.py') || echo "::warning::Pylint check failed, but the workflow will continue."
```
GitHub Actions are called after a specific trigger is detected, in the case above a push action on the main branch of your repo. GitHub Actions are implemented in the `.github/workflows` folder, and results of previous runs are in your repository's [Actions tab](https://github.com/akatief/template-workshop/actions). You can inspect the action output to understand why a specific action fails. 

Familiarize with the [Actions interface](https://github.com/akatief/template-workshop/actions) and understand why some of them fail. Then, apply changes to the repository to fix them. Finally, push the changes to GitHub to run the actions again. They should all show a ✅ on the page.

### What to change

Discover it yourself by reading the Action's results 😉 (Hint: it's something about missing files, and something about tests).

## Conclusion
Congrats! You made it to the end. Please take a couple of minutes to compile [this form](https://forms.gle/LHnjALL12tj35KXw7). Your feedback allows me to improve this project! 

Here are some links where you can learn more about the inner workings of this repo:

- [GitHub Actions](https://docs.github.com/en/actions)
- [Testing](https://docs.pytest.org/en/8.0.x/)
- [Pylint](https://pylint.readthedocs.io/en/stable/)
- The [ABOUT_THIS_TEMPLATE.md](ABOUT_THIS_TEMPLATE.md) file

Oh, and don't forget to bookmark the original [UKP Project template](https://github.com/UKPLab/ukp-project-template)!

Thank you, and happy coding 🤗
