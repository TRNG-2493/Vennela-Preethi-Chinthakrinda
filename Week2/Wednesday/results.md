=======================
Part - A result
=======================

PS C:\Users\chvpr\Documents\Projects\week2-wed\starter_code> python run_report.py  
BUG-1 (BUG-1: median of an even-sized list): 2.5
BUG-2 (BUG-2: top 3 slowest tests): [340, 210, 150]
BUG-3 (BUG-3: counting outcomes per suite): {'login': {'pass': 2, 'fail': 1}, 'search': {'pass': 1}}
BUG-4 (BUG-4: two separate reports each keep a flaky list): (['t2'], ['t9'])
BUG-5 (BUG-5: the id for the first report): 'RUN-0001'
BUG-6 (BUG-6: the dashboard summary, 'latest' test duration): {'run_id': 'RUN-0001', 'total': 4, 'by_suite': {'login': {'pass': 2, 'fail': 1}, 'search': {'pass': 1}}, 'median_ms': 135.0, 'slowest_ms': [340, 210, 150], 'latest_ms': 80}
BUG-7 (BUG-7: a night where no tests produced a timing): {'run_id': 'RUN-0001', 'total': 4, 'by_suite': {'login': {'pass': 2, 'fail': 1}, 'search': {'pass': 1}}, 'median_ms': None, 'slowest_ms': [], 'latest_ms': None}


PS C:\Users\chvpr\Documents\Projects\week2-wed\starter_code> python check_exercise.py --part A

Part A - Debugging: do all 7 tickets behave as specified?
  [PASS] BUG-1 median of an even-sized list is the mean of the two middle values
  [PASS] BUG-2 slowest(durations, n) returns exactly n items (n == 0 gives [])
  [PASS] BUG-3 group_by_suite counts per suite/status; missing suite goes to 'unknown'
  [PASS] BUG-4 note_flaky() calls without a list do not share state
  [PASS] BUG-5 next_run_id() returns RUN-0001, RUN-0002, ...
  [PASS] BUG-6 summarise_run reports latest_ms 150 and leaves the caller's list in order
  [PASS] BUG-7 median([]) raises ValueError; summarise_run(results, []) gives median_ms None
  [PASS] no breakpoint() or pdb.set_trace() left in run_stats.py
  [PASS] debug_log.md has an Evidence line filled in for at least 5 tickets
  [PASS] debug_log.md has a reflection

Summary
  Part A: 10/10 checks pass

ALL CHECKS PASS


=======================
Part - B result
=======================
PS C:\Users\chvpr\Documents\Projects\week2-wed\starter_code> python check_exercise.py --part B

Part B - Logging: run_stats.py logs, run_report.py configures
  [PASS] run_stats.py creates a module logger with logging.getLogger(__name__)
  [PASS] run_stats.py does not call logging.basicConfig or add handlers
  [PASS] run_stats.py has no print() calls
  [PASS] module has a variable named `logger` that is a logging.Logger
  [PASS] median() emits at least one DEBUG record
  [PASS] group_by_suite() emits a WARNING for a result with no suite
  [PASS] summarise_run() emits an INFO record
  [PASS] log messages use %-style arguments, not f-strings, in at least one call
  [PASS] python run_report.py runs and writes run_report.log
  [PASS] the file log contains DEBUG lines
  [PASS] the console shows INFO but no DEBUG lines
  [PASS] configuring logging twice does not duplicate lines (handlers added once)

Summary
  Part B: 12/12 checks pass

ALL CHECKS PASS

=======================
Part - C result
=======================
PS C:\Users\chvpr\Documents\Projects\week2-wed\starter_code> python check_exercise.py --part C

Part C - Unit tests for run_stats.py
  [PASS] at least 12 test methods (found 16)
  [PASS] uses assertRaises at least once
  [PASS] at least 3 tests of bad or unusual input (3+ of: empty, zero, missing, unknown, None)
  [PASS] uses setUp so tests stay independent
  [PASS] uses assertLogs at least once
  [PASS] no test is an empty placeholder (no leftover 'pass' only classes)
  [PASS] your tests PASS against your fixed run_stats.py
  [PASS] your tests FAIL against the original buggy file in _baseline/ (found 15 failing, need 7)

Summary
  Part C: 8/8 checks pass

ALL CHECKS PASS

=======================
Part - D result
=======================
(.venv) PS C:\Users\chvpr\Documents\Projects\week2-wed\starter_code> python check_exercise.py --part D --conflict-repo ..\conflict-lab

Part D - Merge conflict resolved in: ..\conflict-lab
  [PASS] no unmerged files remain (git ls-files -u is empty)
  [PASS] the merge is finished (no MERGE_HEAD)
  [PASS] HEAD is a merge commit (2 parents)
  [PASS] history keeps both teammates' commits
  [PASS] no conflict markers (<<<<<<<, =======, >>>>>>>) in any file
  [PASS] PASS_THRESHOLD is 95 (the QA lead's decision, see README)
  [PASS] SUITES has all four: login, search, checkout, payments (in that order)
  [PASS] report.py keeps BOTH new functions (summary_line and failing_suites)
  [PASS] python report.py prints the expected two lines
  [PASS] CHANGELOG.md keeps both teammates' lines (it merged automatically; do not lose it)

Summary
  Part D: 10/10 checks pass

ALL CHECKS PASS
