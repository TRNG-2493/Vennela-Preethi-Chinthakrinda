Thursday pair exercise -- self-check of C:\Users\shaqa\Desktop\qe-foundations

== 1 Files
[PASS] all required files exist
[PASS] .gitignore ignores logs, databases and caches
== 2 SQL rules
[PASS] R-01: returns exactly the expected 3 row(s)
[PASS] R-02: returns exactly the expected 2 row(s)
[PASS] R-03: returns exactly the expected 4 row(s)
[PASS] R-04: returns exactly the expected 2 row(s)
[PASS] R-05: returns exactly the expected 2 row(s)
[PASS] R-06: returns exactly the expected 2 row(s)
[PASS] R-07: returns exactly the expected 3 row(s)
[PASS] R-08: returns exactly the expected 3 row(s)
[PASS] R-09: returns exactly the expected 3 row(s)
[PASS] R-10: returns exactly the expected 2 row(s)
[PASS] R-11: returns exactly the expected 3 row(s)
[PASS] R-12: returns exactly the expected 4 row(s)
[PASS] E-01: returns exactly the expected 1 row(s)
[PASS] E-02: returns exactly the expected 1 row(s)
[SKIP] S-01 stretch rule not attempted
[SKIP] S-02 stretch rule not attempted
[SKIP] S-03 stretch rule not attempted
== 3 Python runner
[PASS] ValidationFailedError is a custom Exception subclass
[PASS] ValidationFailedError carries rule_id, description, rows and a message naming the rule
[PASS] run_rule returns normally when a violation query finds nothing
[PASS] expectation rules: PASS with the expected row count, raise when the row is missing
[PASS] informational rules (expect=None) never raise
[PASS] runner prints one PASS/FAIL line per required rule
[PASS] printed PASS/FAIL agrees with what each query returns
[PASS] FAIL lines are followed by the evidence rows
[PASS] exit code is 1 when a rule fails (and 0 with --allow-failures)
[PASS] log file written: every rule logged, INFO for passes, WARNING for failures
[PASS] file handler records DEBUG detail
[PASS] setup_logging() is safe to call twice (no duplicate handlers)
== 4 Unit tests
[PASS] 7 unittest tests run and all pass
[PASS] a test covers the custom exception (assertRaises)
[PASS] a test checks specific planted defects (run_ids)
== 5 Docs
[PASS] pairing log: 5 swap blocks recorded
[PASS] retrospective complete
[PASS] defect checklist filled in and consistent with your query results
[PASS] 2 defect reports with reproducing queries
== 6 Git
[PASS] on feature branch 'feature/sql-validation-shaqayeq-vanella'
[PASS] 17 commits on this branch (vs main)
[PASS] both partners committed under their own names
[PASS] commit messages are descriptive
[PASS] working tree clean
[PASS] branch is pushed and up to date with its upstream
[PASS] no generated files tracked
[PASS] no merge-conflict markers

PASS 43 WARN 0 FAIL 0 SKIP 3
READY: no FAIL items. Review any WARN lines, then open your pull request.

https://github.com/Shaqayeq6/qe-foundations/pull/1
