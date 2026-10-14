Test-Case ID Formatter
This is a small tool to format the test case IDs and also indicating if it is release ready or not based on the number of tests performed, passed tests and failed tests. The pass rate is 90%.

*Sample Output*
Tests executed: 50
Tests passed: 45
Generated ID: SIGNIN-0045
Title: Sign in feature
Failed: 5
Pass rate: 90.0%
Release ready: True

*git commits*
$ git log --oneline
3aecebb (HEAD -> master) Add README with usage instructions
9d86e89 Add failed count, pass rate and release decision
7454031 Add zero-padded test-case ID output
2573f8f Add prompts for module, number, title and test counts