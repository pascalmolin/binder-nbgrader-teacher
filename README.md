# Jupyter env for teacher

## Usage

Open the [manage assignments page](/formgrader/manage_assignments) using ``cmd+shift+c 'formgrader'``.
and follow the [nbgrader instructions](https://nbgrader.readthedocs.io/en/stable/user_guide/creating_and_grading_assignments.html).

Source assigments are in ``source/``
When student assignments are generated in ``release/``, copy them to binder of
students.



## This repository

Based on [repo2docker](https://repo2docker.readthedocs.io/en/latest/usage.html).

### Run locally

```
jupyter-repo2docker -E .
```
The -E option mounts the local directory to that changes are kept.
Of course you need repo2docker installed, plus docker, jupyter, etc.

### Run on Binder

Launch [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mastermic/binder-nbgrader-teacher/master)
