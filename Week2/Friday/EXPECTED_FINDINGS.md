# Data-quality findings (expected-findings template)

Copy this file to `docs/DATA_QUALITY_FINDINGS.md` in your qe-foundations repo and fill it in. `check_exercise.py --repo` (F8) requires:
all 20 check ids present (at least 18), and no `TODO` left. Replace every TODO with your own words. Plain ASCII text only.

## 1. Prediction round (do this BEFORE you run Part E, 5 minutes)

Open `sql/seed.sql` (or run `SELECT * FROM builds;` and the other three tables with `python lab_runner.py`) and read the data like a tester.
List up to 8 problems you can already SEE, and which check category you expect to catch each one.

| # | What I see (table, row, column) | Category I expect (reconciliation / missing rows / uniqueness / completeness / referential / validity / business rule) |
|---|---|---|
| 1 | builds, build_id 2: reported_total is 10 but only 9 runs exist | reconciliation |
| 2 | builds, build_id 6: reported_total is 8 but no test runs exist | missing rows |
| 3 | test_runs, run_id 44: repeats build_id 3 and case_id 3 from run 18 | uniqueness |
| 4 | test_runs, run_id 5: tester is NULL | completeness |
| 5 | test_cases, case_id 10: priority is P4, which is invalid| completeness |
| 6 | test_runs, run_id 39: case_id 99 does not exist in test_cases | referential |
| 7 | test_runs, run_id 3: duration_sec is 86400, above the allowed range | validity |
| 8 | defects, deefect_id 13: linked to run 19, which passed | business rule |


After Part E: how many of your predictions did the suite confirm? Which defects did you NOT see by eye? TODO

## 2. Findings per check (fill in after `python lab_runner.py --checks sql/part_e_checks.sql --show`)

Severity: High = wrong results or lost data reach users, Medium = reports are wrong in places, Low = cosmetic / hygiene.
Draft bug title: one line a developer could act on (what is wrong, where, how many).

| Check | Category | Violations | Offending ids | Severity | Suspected root cause | Draft bug title |
|---|---|---|---|---|---|---|
| E-01 | reconciliation | 2 | 2,6 | Medium | Reported totals not updated correctly | Run totals mismatch for 2 builds |
| E-02 | reconciliation | 2 | 4,6 | Medium | Passed and failed counts are inaccurate | Pass/fail summaries incorrect for 2 builds |
| E-03 | missing rows | 1 | 6 | High | Build created without execution records | Build 6 has no test runs |
| E-04 | missing rows | 2 | 13,14 | High | Active test cases were not executed | 2 active test cases have no runs |
| E-05 | uniqueness | 2 | 44,45 | Medium | Duplicate execution records | 2 surplus test runs found |
| E-06 | uniqueness | 1 | 15 | Medium | Duplicate title validation missing | Duplicate cart test case title |
| E-07 | completeness | 2 | 10,11 | Medium | Priority validation missing | 2 test cases have invalid or missing priority |
| E-08 | completeness | 5 | 4,5,6,8,41 | High | Mandatory run fields not validated | 5 runs have missing required fields |
| E-09 | completeness + validity | 2 | 3,4 | Medium | Severity validation missing | 2 defects have invalid or missing severity |
| E-10 | referential | 2 | 39,40 | High | Foreign key enforcement disabled | 2 runs reference nonexistent test cases |
| E-11 | referential | 1 | 42 | High | Invalid build reference accepted | Run 42 references nonexistent build 9 |
| E-12 | referential | 1 | 14 | High | Missing run reference validation | Defect 14 references nonexistent run 500 |
| E-13 | referential | 1 | 15 | High | Missing case reference validation | Defect 15 references nonexistent case 77 |
| E-14 | validity | 1 | 1 | Medium | Result values not standardized | Run 1 has invalid result PASSED |
| E-15 | validity | 2 | 2,3 | Medium | Duration range not validated | 2 runs have invalid durations |
| E-16 | business rule | 1 | 9 | High | Run date earlier than build date | Run 9 predates its build |
| E-17 | business rule | 2 | 7,11 | High | Failed runs missing defect records | 2 failed runs have no defects |
| E-18 | business rule | 1 | 13 | Medium | Defect logged against passed run | Defect 13 references a passing run |
| E-19 | cross-table consistency | 1 | 5 | High | Defect assigned incorrect case ID | Defect 5 case ID disagrees with run 15 |
| E-20 | business rule | 3 | 6,7,8 | Medium | Defect lifecycle validation missing | 3 defects have inconsistent dates or status |

## 3. Questions the data asked you (one or two sentences each)

1. **A1:** `PRAGMA foreign_key_check` listed 5 violations. Which of E-10 .. E-13 are they, and why did the database accept those rows in the first place?
The 5 foriegn key violations are E-10(2), E-11(1), E-12(1), and E-13(1). The database accepted these records because SQLite foreign key enforcement was disabled when the data was inserted.

2. **B4 vs E-10:** B4 returned 3 runs, E-10 only 2. Which run is the difference and in which check does it belong? Why?
Run 41 is the difference because its case_id is NULL. B4 includes runs without a matching test case, including NULL values, but E-10 only identifies invalid non-NULL references. Run 41 belongs in the completeness check E-08.

3. **C2:** Why did the `NOT IN` query return zero rows?
The NOT IN query returns zero rows because the subquery contains a NULL case_id, causing comparisons 
for nonmatching values to evaluate to UNKNOWN instead of TRUE, so the WHERE clause excludes them.

4. **B2 vs E-04:** B2 returned 3 cases, E-04 only 2. Which case is excluded and why is that correct?
Case 12 is excluded because its status is retired. B2 includes all cases that have never been executed, but E-04 only checks active cases. Retired cases are allowed to have no test runs.

5. **C4a vs C4b:** why does one out-of-range duration change which runs look "slow"?
Run 3 has an unusually high duration of 86400 seconds, which increases the average duration and changes which runs appear slow. Removing invalid durations gives a more realistic average and more reliable slow-run detection.

## 4. Top 3 risks for the release (the message you would give the team lead)

1. High - Missing test coverage: Build 6 has no test runs, and two active test cases have never been executed. This creates a risk of releasing features without sufficient testing.
2. High - Data integrity problems: Test runs and defects reference records that do not exist. These broken relationships could lead to incomplete or incorrect reports.
3. High - Incorrect test and defect reporting: Some failed runs have no defects, a defect is linked to a passed run, and some reported build totals are inaccurate. These problems could mislead the team when evaluating release readiness.


Notes:
Part - C
The NOT IN query returns zero rows because the subquery contains a NULL case_id, causing comparisons for nonmatching values to evaluate to UNKNOWN rather than TRUE, so the WHERE clause excludes them.
