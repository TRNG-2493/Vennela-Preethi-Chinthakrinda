# SELECTION_LOG.md (Task 7)

Fill in the "Selected" column by running the command with `--collect-only -q` and counting
test lines, or by reading the summary line. Then write one sentence on when you would use it.

| Command | Selected | When would a team run this? |
|---|---|---|
| `python -m pytest -m smoke` | 7/32 tests collected (25 deselected) in 0.01s | To quickly verify critical functionality after a new build or deployment. |
| `python -m pytest -m "regression and not slow"` | 19/32 tests collected (13 deselected) in 0.01s | To check the existing functionality still works after a code change excluding the slow runs |
| `python -m pytest -m boundary` | 10/32 tests collected (22 deselected) in 0.01s | To verify the application verifies at boundary inputs |
| `python -m pytest -k username` | 7/32 tests collected (25 deselected) in 0.01s | To run username-related tests |
| `python -m pytest -k "grade and not raises"` | 3/32 tests collected (29 deselected) in 0.01s | To run grade-related tests excluding tests whose names contain raises. |
| `python -m pytest tests/test_cart.py::TestCartTotal::test_empty_cart_total_is_zero` | 1 test collected in 0.01s | To execute one specific test when debugging or verifying a particular functionality. |

## Questions
1. Temporarily change one `@pytest.mark.smoke` to `@pytest.mark.smok` (typo) and run pytest. What happens and what exit code do you get? Why is that useful? (Undo the typo afterwards!)
'smok' not found in `markers` configuration option.
exit code 4 (usage/configuration error).
This is useful because registering markers in pytest.ini helps identify spelling mistakes and prevents using undefined markers.

2. What exit code did a run that selected zero tests give? (Try `-k zzzz`.) 
collected 32 items / 32 deselected / 0 selected 
exit code 5

3. Which test is your xfail, and what would you see if the bug were fixed (strict=True)?
test_truncate_text_exactly_max_len_is_unchanged
If we fix the bug, the test unexpectedly passes and Pytest reports: XPASS(strict)
The test suite will be marked as FAILED because strict=True treats an unexpected pass as a failure.
