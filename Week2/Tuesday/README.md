python check_exercise.py reports all core checks passed (stretch checks are optional)
-----------------------------------------------------------------------------------------

(.venv) PS C:\Users\chvpr\Documents\Projects\qe-foundations> python check_exercise.py
========================================================================
Week 2 Day 2 - ingestion module self-check
Repo: C:\Users\chvpr\Documents\Projects\qe-foundations
Python 3.13.4
========================================================================

Task 2 - exception hierarchy
  [PASS] hierarchy: parents and siblings
  [PASS] source errors carry path/suffix/missing + readable message
  [PASS] record errors carry row/field/value/test_id
  [PASS] every exception is caught by `except IngestionError`

Task 3 - context managers
  [PASS] open_source: reads UTF-8, strips BOM, closes file
  [PASS] open_source: closes the file and re-raises when the body fails
  [PASS] open_source: missing file -> SourceNotFoundError (from FileNotFoundError)
  [PASS] open_source: a folder -> SourceUnreadableError (not 'not found')
  [PASS] open_source: bad encoding -> MalformedSourceError
  [PASS] LoadSession: outcome 'completed' + elapsed
  [PASS] LoadSession: outcome 'failed', exception NOT swallowed

Task 4 - readers (CSV / JSON / XML)
  [PASS] CSV reader: BOM, quotes, CRLF, blank line, raw strings
  [PASS] CSV reader: missing columns reported in required order
  [PASS] CSV reader: empty file / header-only file
  [PASS] CSV reader: short rows survive for validation
  [PASS] JSON reader: returns the tests list untouched
  [PASS] JSON reader: malformed JSON (with line number) and empty file
  [PASS] JSON reader: wrong shapes -> MalformedSourceError
  [PASS] XML reader: any depth, attributes + children, None when absent
  [PASS] XML reader: malformed and empty files
  [PASS] CSV/JSON readers: non-UTF-8 bytes -> MalformedSourceError
  [PASS] all readers: missing file -> SourceNotFoundError

Task 5 - validate_record
  [PASS] validate_record: clean + normalised output
  [PASS] validate_record: does not mutate its input
  [PASS] validate_record: missing / None / blank fields
  [PASS] validate_record: invalid status values
  [PASS] validate_record: invalid durations (nan, inf, bool, negative, text)
  [PASS] validate_record: a record that is not a dict
  [PASS] validate_record: which problem is reported first
  [PASS] validate_record: still rejects under `python -O`

Task 6 - loader, assertions, batch, rejected-records CSV
  [PASS] load_test_cases: messy CSV
  [PASS] load_test_cases: messy JSON (same data as CSV)
  [PASS] load_test_cases: messy XML (same data as CSV)
  [PASS] load_test_cases: right exception class per rejected row
  [PASS] load_test_cases: unusable files raise the right SourceError
  [PASS] load_test_cases: accepts str and Path
  [PASS] IngestionReport: summary() and rejected_rows()
  [PASS] check_invariants: three assertions fire on inconsistent reports
  [PASS] load_directory + BatchResult.totals
  [PASS] write_rejected_csv
  [PASS] command line: python -m qe_foundations.ingestion

Task 7 - code hygiene and notes
  [PASS] no bare / swallowing `except Exception`
  [PASS] no `assert` in validation.py
  [PASS] at least 3 asserts in loader.py
  [PASS] library modules do not print()
  [PASS] open() only inside `with` in readers/loader
  [PASS] docs/ingestion_notes.md answered

------------------------------------------------------------------------
  Task 2 - exception hierarchy                                   4/4
  Task 3 - context managers                                      7/7
  Task 4 - readers (CSV / JSON / XML)                            11/11
  Task 5 - validate_record                                       8/8
  Task 6 - loader, assertions, batch, rejected-records CSV       11/11
  Task 7 - code hygiene and notes                                6/6
------------------------------------------------------------------------
CORE CHECKS PASSED: 47/47  (100%)
All core checks pass. Now work through the Definition of Done in README.md and commit.



------------------------------------------------------------------------------------------
python -m qe_foundations.ingestion data/ingestion prints 7 files OK / 7 failed / 23 valid / 16 rejected
-------------------------------------------------------------------------------------------
(.venv) PS C:\Users\chvpr\Documents\Projects\qe-foundations> python -m qe_foundations.ingestion data/ingestion
test_cases_clean.csv: 5 rows seen, 5 valid, 0 rejected
test_cases_excel_bom.csv: 3 rows seen, 3 valid, 0 rejected
test_cases_messy.csv: 10 rows seen, 3 valid, 7 rejected
    rejected - Row 3: Required field 'title' is missing
    rejected - Row 4: Invalid value 'passed' for 'status'; expected one of ('pass', 'fail', 'blocked')
    rejected - Row 5: Duplicate test ID 'TC-101'
    rejected - Row 7: Invalid value '-4' for 'duration'; expected a finite, non-negative number
    rejected - Row 8: Invalid value 'n/a' for 'duration'; expected a valid number
    rejected - Row 9: Required field 'duration' is missing
    rejected - Row 10: Required field 'id' is missing
test_results_clean.json: 4 rows seen, 4 valid, 0 rejected
test_results_clean.xml: 3 rows seen, 3 valid, 0 rejected
test_results_messy.json: 8 rows seen, 3 valid, 5 rejected
    rejected - Row 2: Required field 'status' is missing
    rejected - Row 3: Required field 'duration' is missing
    rejected - Row 4: Invalid value 'unknown' for 'status'; expected one of ('pass', 'fail', 'blocked')
    rejected - Row 6: Invalid value True for 'duration'; expected a finite, non-negative number
    rejected - Row 7: Invalid value 'TC-707' for 'record'; expected an object with the test fields
test_results_messy.xml: 6 rows seen, 2 valid, 4 rejected
    rejected - Row 2: Required field 'duration' is missing
    rejected - Row 3: Required field 'id' is missing
    rejected - Row 4: Invalid value 'twelve' for 'duration'; expected a valid number
    rejected - Row 5: Invalid value 'skipped' for 'status'; expected one of ('pass', 'fail', 'blocked')
SOURCE FAILED - notes.txt: the file extension .txt is not supported.
SOURCE FAILED - test_cases_empty.csv: Missing required columns: id, title, status, duration
SOURCE FAILED - test_cases_latin1.csv: Invalid encoding
SOURCE FAILED - test_cases_missing_column.csv: Missing required columns: duration
SOURCE FAILED - test_results_malformed.json: Illegal trailing comma before end of array: line 5 column 90 (char 219)
SOURCE FAILED - test_results_malformed.xml: mismatched tag: line 10, column 4
SOURCE FAILED - test_results_wrong_shape.json: JSON root must be an object
TOTAL for ingestion: {'files_ok': 7, 'files_failed': 7, 'valid': 23, 'rejected': 16}
