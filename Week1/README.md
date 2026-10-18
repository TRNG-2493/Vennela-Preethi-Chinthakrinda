# Week 1 Summary: Python Programming and Git Foundations

<!-- Copy this file to README.md at the ROOT of your week-1 repo and replace every
     <angle bracket> and TODO. Delete these comments. Keep it short and honest. -->

**Name:** Vennela Preethi Chinthakrinda | **Cohort:** TRNG - 2493 | **Tag:** 'week1-complete'

## What this repo contains

| Day | Program / folder | What it does (one line) | Python topics used | Git skill practised |
|---|---|---|---|---|
| Mon | 'Exercise-1-Git.md, and test-case-id-formatter/' | Formats and validates test case IDs using basic Python operations | variables, types, input/output | init, add, commit, log |
| Tue | 'Exercise2' | Implements a number guessing game and analyzes log files to identify errors & warning | if/elif/else, loops, break/continue | .gitignore, clone, push, pull, Pull Request |
| Wed | 'Day3/' | Processes and organizes test case data using Python collections | lists, dicts, sets, collections | branch, merge, Collabration |
| Thu | 'Thursday/' | Builds reusable test utilities for validation, generating test data, and measuring execution | functions, lambdas, decorators | Feature branches, pull, merge |
| Fri | 'Friday/' | Builds an OOP-based test-reporting system with validation, suite statistics, and text/CSV reports (TestResult, Suite, Reporter) | classes, encapsulation, inheritance | week-1 summary branch, PR |

## How to run the Friday program

'''bash
cd Friday
python check_exercise.py     # expected: 24/24 checks passed
python run_report.py
'''

## What I learned this week

- Python: This week helped me strengthen my understanding of Python fundamentals, inclusing data structures, functions, exception handling, OOPS. I learned how to organize code into reusable components and apply validation to improve reliability. In test reporting system, I used property setters to validate test statues and durations, and inheritance and polymorphism to generate different report formats.

- Git: I learned hpw to manage repositories, create feature branches and how important to have good commit messages, understanding the merge conflicts and resolving them. Working with a teammate helped me understand the importance of syncing changes, resolving issues and maintaining an organized commit history.

- Testing mindset: I learned that validating inputs is esstential for preventing incorrect results. In the friday exer, I encountered an issue where 'NotImplementedError' remained in a completed setter causing multiple tests to fails, debugging it helped me understand execution flow and the importance of running automated checks after implementing each method.

## What was hardest, and what I would do differently

The challenging part was implementing OOP concepts such as property setters, class methods, and polymorphism. Going forward, I would work in smaller steps, run test checks and review error messages before making changes.

## My commit history, honestly

- Best commit message I wrote this week: 'Checkpoint 2 - Add TestResult with validation and alternative constructors', 'Exercise1-git commands used to complete the exercise'
- A vague message I wrote and the better version I would write now:
  '577003e update prac files' -> 'Add In-class practice files on Practice/'

## Next steps

- Before week 2, I want to prac OOP concepts further, while becoming more cofindent with git branching, pull requests and merge conflicts resolution.
