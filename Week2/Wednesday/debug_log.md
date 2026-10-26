# Debug log (Part A)

Name: Vennela Preethi   Date: 10/21/2026

Fill one block per ticket, in the order you fixed them. Use the method from the lesson: Reproduce, Read,
Isolate, Hypothesise, Test, Fix, Verify. Short answers are fine, but the EVIDENCE line must be something
you actually saw (a pdb command and its output, or a print line).

## BUG-1
- Symptom (what I saw): When I ran python run_report.py 1, The output is 3. Expected output is 2.5
- Family (syntax / runtime / logic): Logic error
- Hypothesis (before I looked): I think median function is only selecting the middle element even for the list of even numbers.
- Evidence (pdb command + output, or print output): I added breakpoint to the median function, inspected the variables using p, pp locals(). The {'ordered': [1, 2, 3, 4], 'values': [4, 1, 3, 2]}, the function selected the element at the index of "ordered[len(ordered)//2]"

-> breakpoint()
(Pdb) p values
[4, 1, 3, 2]
(Pdb) p ordered
[1, 2, 3, 4]
(Pdb) pp locals()
{'ordered': [1, 2, 3, 4], 'values': [4, 1, 3, 2]}
(Pdb) p len(ordered) //2
2
(Pdb) ordered[2]
3
(Pdb) w
  c:\users\chvpr\documents\projects\week2-wed\starter_code\run_report.py(84)<module>()
-> main(sys.argv)
  c:\users\chvpr\documents\projects\week2-wed\starter_code\run_report.py(74)main()
-> print(TICKETS[number]())          # a crash shows the full traceback on purpose
  c:\users\chvpr\documents\projects\week2-wed\starter_code\run_report.py(27)ticket_1()
-> return run_stats.median([4, 1, 3, 2])
> c:\users\chvpr\documents\projects\week2-wed\starter_code\run_stats.py(38)median()
-> breakpoint()
(Pdb) c
3
- Root cause (one sentence): For even numbered list of elements, instead of averaging the middle 2 values, the result is taking the middle value only, that is ordered[len(ordered)//2]
- Fix (one sentence): Even number list: take average of 2 middle values, Odd number list: take the middle value
- Verified by:  I re-ran python run_report.py 1 and confirmed that the result was 2.5.

## BUG-2
- Symptom (what I saw): When I ran run_report.py 2 the output is [340, 210], but the n value is 3 and expected output list should contain n values, but it is returning a list with n-1 values
- Family (syntax / runtime / logic): logic
- Hypothesis (before I looked): The list is sorting from high to low but returning only n-1 values instead of n values.
- Evidence (pdb command + output, or print output): -> breakpoint()
(Pdb) pp locals()
{'durations': [340, 210, 150, 120, 95, 80], 'n': 3}
(Pdb) n
> c:\users\chvpr\documents\projects\week2-wed\starter_code\run_stats.py(58)slowest()
-> return durations[:n - 1]
(Pdb) s
--Return--
> c:\users\chvpr\documents\projects\week2-wed\starter_code\run_stats.py(58)slowest()->[340, 210]
-> return durations[:n - 1]
(Pdb) c
[340, 210]

- Root cause (one sentence): return durations[:n-1] is the root cause
- Fix (one sentence): return durations[0:n]
- Verified by: I re-ran python run_report.py 2 and confirmed that the result is top 3 slowest tests list is displayed on output that is [340, 210, 150]

## BUG-3
- Symptom (what I saw): When I ran python run_report.py 3, the program crashed with KeyError: 'login' instead of returning the count of pass and fail tests grouped by suite.
- Family (syntax / runtime / logic): runtime - keyerror
- Hypothesis (before I looked): I thought the function was trying to access a suite name in the dictionary before initializing it.
- Evidence (pdb command + output, or print output): PS C:\Users\chvpr\Documents\Projects\week2-wed\starter_code> python run_report.py 3           
BUG-3: BUG-3: counting outcomes per suite
> c:\users\chvpr\documents\projects\week2-wed\starter_code\run_stats.py(79)group_by_suite()
-> breakpoint()
(Pdb) p grouped
{}
(Pdb) p result
{'test': 't1', 'suite': 'login', 'status': 'pass'}
(Pdb) p result["suite"]
'login'
(Pdb) p result["status"]
'pass'
(Pdb) n
> c:\users\chvpr\documents\projects\week2-wed\starter_code\run_stats.py(80)group_by_suite()
-> grouped[result["suite"]][result["status"]] += 1
(Pdb) c
Traceback (most recent call last):
  File "C:\Users\chvpr\Documents\Projects\week2-wed\starter_code\run_report.py", line 83, in <module>
    main(sys.argv)
    ~~~~^^^^^^^^^^
  File "C:\Users\chvpr\Documents\Projects\week2-wed\starter_code\run_report.py", line 73, in main
    print(TICKETS[number]())          # a crash shows the full traceback on purpose
          ~~~~~~~~~~~~~~~^^
  File "C:\Users\chvpr\Documents\Projects\week2-wed\starter_code\run_report.py", line 37, in ticket_3
    return run_stats.group_by_suite(RESULTS)
           ~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^
  File "C:\Users\chvpr\Documents\Projects\week2-wed\starter_code\run_stats.py", line 80, in group_by_suite
    grouped[result["suite"]][result["status"]] += 1
    ~~~~~~~^^^^^^^^^^^^^^^^^
KeyError: 'login'
- Root cause (one sentence): The grouped dictionary was initially empty, and the function tried to increment a status counter for the "login" suite without first creating the nested dictionary and initializing its counter.
- Fix (one sentence): I added conditions to check whether the suite and status exist in the dictionary, initialize them if missing, and then increment the status count.
- Verified by: After fixing the function, I reran the program and confirming it returns correct output

## BUG-4
- Symptom (what I saw): Two separate calls to note_flaky() returned the same flaky test list instead of independent lists.
- Family (syntax / runtime / logic): logic
- Hypothesis (before I looked): The function maybe using the mutable list that is shared across multiple function calls
- Evidence (pdb command + output, or print output):-> breakpoint()
(Pdb) p test_name
't2'
(Pdb) p flaky
[]
(Pdb) n
> c:\users\chvpr\documents\projects\week2-wed\starter_code\run_stats.py(100)note_flaky()
-> flaky.append(test_name)
(Pdb) p flaky
[]
(Pdb) c
-> breakpoint()
(Pdb) c
(['t2', 't9'], ['t2', 't9'])

- Root cause (one sentence):  The default list flaky=[] was created once when the function was defined and reused across multiple calls, causing both variables to reference the same list.
- Fix (one sentence): I replaced flaky=[] with flaky=None and created a new empty list inside the function whenever no list was passed.
- Verified by: Rerun python run_report.py 4 and confirm that the output is (['t2'], ['t9']).

## BUG-5
- Symptom (what I saw): When I ran python run_report.py 5, the program crashed with UnboundLocalError instead of generating the first run ID RUN-0001.
- Family (syntax / runtime / logic): Runtime - UnboundLocalError
- Hypothesis (before I looked): I thought the function was trying to modify the module-level run_counter variable without declaring it as global.
- Evidence (pdb command + output, or print output):-> breakpoint()
(Pdb) pp locals()
{}
(Pdb) p globals()["run_counter"]
0
(Pdb) n
-> run_counter += 1

- Root cause (one sentence): Python treated run_counter as a local variable because it was assigned inside the function, but the function tried to increment it before the local variable had a value.
- Fix (one sentence): I added global run_counter inside next_run_id()
- Verified by: Rerun python run_report.py 5 and confirm that it returns RUN-0001.

## BUG-6
- Symptom (what I saw): When I ran python run_report.py 6, the dashboard displayed latest_ms as 80 instead of 150, even though 150 was the duration of the last executed test
- Family (syntax / runtime / logic): logic
- Hypothesis (before I looked): Hypothesis (before I looked): I suspected that the slowest() function was modifying the original durations list before latest_ms was calculated.
- Evidence (pdb command + output, or print output):-> breakpoint()
(Pdb) p durations
[120, 80, 340, 95, 210, 150]
(Pdb) p durations[-1]
150

- Root cause (one sentence): The slowest() function used durations.sort(reverse=True), which modified the original list and changed the value accessed by durations[-1]
- Fix (one sentence):  I replaced the in-place sort() operation with sorted(durations, reverse=True)[:n] to return the slowest durations without modifying the original list.
- Verified by: Rerun python run_report.py 6 and confirm that latest_ms is 150 and slowest_ms is [340, 210, 150].

## BUG-7
- Symptom (what I saw): When I ran python run_report.py 7, the program crashed while generating a summary because the durations list was empty.
- Family (syntax / runtime / logic): runtime
- Hypothesis (before I looked):  I suspected the function was trying to calculate the median or access the last element of an empty durations list.
- Evidence (pdb command + output, or print output):-> breakpoint()
(Pdb) p durations
[]
(Pdb) p len(durations)
0
(Pdb) p bool(durations)
False
(Pdb) pp locals()
{'durations': [],
 'results': [{'status': 'pass', 'suite': 'login', 'test': 't1'},
             {'status': 'fail', 'suite': 'login', 'test': 't2'},
             {'status': 'pass', 'suite': 'login', 'test': 't3'},
             {'status': 'pass', 'suite': 'search', 'test': 't4'}]}

- Root cause (one sentence): The summarise_run() function did not handle an empty durations list and attempted to calculate a median or access the
- Fix (one sentence): I added conditional expressions to return None for median_ms and latest_ms when durations is empty, while keeping slowest_ms as an empty list.
- Verified by: Rerun python run_report.py 7 and confirm that the summary is generated without crashing, with median_ms = None, slowest_ms = [], and latest_ms = None.

## Reflection (3 sentences)

BUG-4 was the hardest for me because I didn't know that a default list in a function could be shared between multiple calls.

Using breakpoint() and pdb commands like p, n, and pp locals() helped me check variable values and understand what was going wrong.

Next time, I will debug step by step, find the cause of the error, fix it, and test again to make sure everything works correctly.