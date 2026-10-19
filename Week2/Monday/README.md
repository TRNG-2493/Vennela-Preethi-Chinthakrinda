Week 2 - Monday Exercise 1 - Git URL: https://github.com/Venny12/Project1

-----------------------------------
OUTPUT
-----------------------------------
(.venv) PS C:\Users\chvpr\Documents\Projects\qe-foundations> python check_exercise.py --submit

Week 2 / Monday self-check - Project 1: qe-foundations kickoff
Repository root: C:\Users\chvpr\Documents\Projects\qe-foundations

== A. Environment (virtual environment + Python)
  [PASS] Python >= 3.9 (found 3.13.4)
  [PASS] this check is running INSIDE a virtual environment
  [PASS] .venv folder exists in the repo root
  [PASS] the active venv is THIS repo's .venv

== B. Repository structure (Project 1 milestone)
  [PASS] README.md exists
  [PASS] .gitignore exists
  [PASS] requirements.txt exists
  [PASS] requirements-dev.txt exists
  [PASS] qe_foundations/__init__.py exists
  [PASS] qe_foundations/utils/__init__.py exists
  [PASS] qe_foundations/utils/strings.py exists
  [PASS] qe_foundations/utils/numbers.py exists
  [PASS] qe_foundations/utils/dates.py exists
  [PASS] qe_foundations/utils/data_gen.py exists
  [PASS] tests/ exists and holds a placeholder file
  [PASS] data/ exists and holds a placeholder file
  [PASS] docs/ exists and holds a placeholder file
  [PASS] legacy_helpers.py has been removed from the repo root
  [PASS] .gitignore ignores .venv/
  [PASS] .gitignore ignores __pycache__/
  [PASS] .gitignore ignores *.pyc
  [PASS] README names the project (QE Foundations)
  [PASS] README documents creating a venv (python -m venv)
  [PASS] README shows activation for PowerShell AND bash
  [PASS] README documents pip install -r requirements.txt
  [PASS] README states the Project 1 milestone (Monday)

== C. Dependencies (requirements files)
  [PASS] requirements.txt is plain UTF-8 text
  [PASS] requirements.txt lists requests
  [PASS] requests has a version specifier
  [PASS] requirements.txt contains runtime deps only (no pytest)
  [PASS] requirements-dev.txt is plain UTF-8 text
  [PASS] requirements-dev.txt includes '-r requirements.txt'
  [PASS] requirements-dev.txt lists pytest
  [PASS] requests is installed in this environment (version 2.34.2)

== D. The qe_foundations package and the utils library
  [PASS] import qe_foundations works
  [PASS] importing qe_foundations prints nothing
  [PASS] qe_foundations.__version__ is defined
  [PASS] import qe_foundations.utils works
  [PASS] importing qe_foundations.utils prints nothing
  [PASS] import qe_foundations.utils.strings works
  [PASS] import qe_foundations.utils.numbers works
  [PASS] import qe_foundations.utils.dates works
  [PASS] import qe_foundations.utils.data_gen works
  [PASS] utils re-exports the full public API from __init__.py
  [PASS] utils/__init__.py defines __all__ with every public name
  [PASS] behaviour: slugify
  [PASS] behaviour: normalize_whitespace
  [PASS] behaviour: is_valid_email
  [PASS] behaviour: mask_email (valid)
  [PASS] behaviour: mask_email (invalid is returned unchanged)
  [PASS] behaviour: is_positive_int
  [PASS] behaviour: clamp
  [PASS] behaviour: percent
  [PASS] behaviour: add_days
  [PASS] behaviour: days_between
  [PASS] behaviour: is_weekend
  [PASS] behaviour: timestamp_for_filename
  [PASS] behaviour: make_users (same seed -> same data)
  [PASS] behaviour: make_users (different seeds differ)
  [PASS] behaviour: make_users (record shape)
  [PASS] python smoke_utils.py exits with code 0

== E. Git
  [PASS] the repo root is a Git repository
  [PASS] at least 3 commits (found 5)
  [PASS] no .venv/ or __pycache__ files are tracked
  [PASS] requirements.txt is committed
  [PASS] qe_foundations/__init__.py is committed
  [PASS] qe_foundations/utils/__init__.py is committed
  [PASS] working tree is clean (everything committed)
  [PASS] remote 'origin' is configured
  [PASS] all commits are pushed to origin

RESULT: 66/66 required checks passed, 0 warning(s).
All required checks passed.

------------------------------------
README FILE
------------------------------------
Project Name:- Exercise: Package a Utility Library and Kick Off Project 1 (QE Foundations)

One-sentence purpose - Today's exercise we create a Git repository called qe-foundations containing the importable packages.

-------------------------------------------------
Project 1 milestone - Week 2, Monday Section
-------------------------------------------------
Project 1 milestone (Monday): "Kickoff - repo + structure." By the end of today you own ONE Git repository called qe-foundations containing the importable package qe_foundations/ with its first sub-package qe_foundations/utils/, a documented virtual-environment setup, requirements.txt / requirements-dev.txt, and empty placeholder folders for the rest of the week. This same repo is used all week (Tue qe_foundations/ingestion/, Wed logging + unit tests in tests/, Thu sql/ validation queries, Fri joins validation + integration). Keep the names exactly as written here.

-------------------------------------------------
Setup Section
-------------------------------------------------
1. Create a Virtual Environment - Create venv 
    py -m venv .venv
    python -m venv .venv
2. Activate the Virtual Environment
    Windows- .venv\Scripts\Activate.ps1 
    MacOS- source .venv/bin/activate
3. Install  Dependencies
    python -m pip install -r requirements.txt   
    python -m pip install -r requirements-dev.txt
4. Verify
    python smoke_utils.py 

-------------------------------------------------    
Usage example
-------------------------------------------------
///////CODE///////
from qe_foundations.utils import slugify, mask_email
print(slugify("Hello World"))
print(mask_email("tester@example.com"))

///////EXPECTED OUTPUT///////
hello-world
t***@example.com