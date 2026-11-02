============
Exercise 1
============
1. Rewrite this requirement so it is testable, and list two questions you'd ask the author: "Users should be able to reset their password easily."
Answer: When a registered user selects 'Forgot Password' and enters a valid registered email
address, the system shall send a password reset link to that email. The link can be used only once.
2 questions to ask the author: 
(i) What is meant by easily, because password reset should verify the user?
(ii) What should happen if a user enters an email address that is not registered in system?

2. Classify each requirement as functional or non-functional:
(a) "The user can download an invoice as PDF." - Functional
(b) "The app works on Chrome, Firefox and Safari." - Non-functional
(c) "The system sends an SMS when an order ships." - Functional

3. Label each as QA or QC:
(a) Running test cases on a build - QC
(b) Introducing a code review checklist - QA
(c) Training developers on secure coding - QA
(d) Inspecting a release candidate for defects - QC

4. Label each as verification or validation:
(a) Reviewing the design document - Verification
(b) A customer trying the app in user acceptance testing - Validation
(c) A peer reviewing code against the spec - Verification

5. Identify the error, defect, and failure: A developer thought VAT was 5% instead of 15%. The code calculates price * 1.05. Customers' invoices show too little tax.
error - developer thought the VAT was 5% instead of 15%
defect - formula in code is price*1.05. It should be price*1.15
failure - the result is showing the incorrect tax price on invoices.

============
Exercise 2
============
1. Match each scenario to a testing principle:
(a) "We ran the same 50 tests for a year and found nothing new." - Pesticide paradox
(b) "Most bugs came from the payment module." - defect clustering
(c) "The app passed every test, but users found it useless." - Absence-of-Errors Fallacy

2. Manual or automated?
(a) Checking a new logo looks right on mobile - Manual
(b) Running 400 regression tests every night - Automatic
(c) Exploring a brand-new feature for the first time - Manual

3. Write two positive and three negative test cases for a "Sign up" form with Email and Password (password must be 8–16 characters).
(i) Valid email + Valid password(Training123)
(ii) Valid email + Valid password(Train#123456)

(iii) Invalid email(abc.com) + Valid password
(iv) Valid email + Invalid password(Train)(Password is not in 8-16 characters)
(v) Invalid email + Invalid password

4. A movie ticket site gives prices by age: 0–12 = child, 13–59 = adult, 60+ = senior. Identify the equivalence partitions (valid and invalid) and one test value for each.
Below 0 - Invalid - Invalid age
0-12 - Valid - child
13-59 - Valid - adult
60 and above - Valid - senior

============
Exercise 3
============
1. BVA: A text field accepts a username of 6 to 20 characters. List the boundary values to test (three-value BVA) and the expected result for each.

No. of characters         Result
5                         Invalid
6                         Valid
7                         Valid
19                        Valid
20                        Valid
21                        Invalid

2. Decision table: A bank approves a loan if the applicant has a salary over $30,000 and a good credit score. Applicants with only one of these are sent for manual review. Applicants with neither are rejected. Build the decision table.
-----------------------------------------------------------------------------
Conditions          Rule 1         Rule 2          Rule 3          Rule 4
-----------------------------------------------------------------------------
Salary over
$30,000             Yes              Yes              No             No

Good credit
score               Yes              No               Yes            No

Approve loan        Yes              -                -              -                
 
Manual review        -               Yes              Yes            -

Reject loan          -               -                -              Yes
------------------------------------------------------------------------------

3. State transition: A document can go Draft → Submitted → Approved, or Submitted → Rejected → Draft (edited and resubmitted). List the valid transitions and one invalid transition to test.
                                 Draft
                                   |
                                Submitted
                                    |
                            -------------------
                            |                  |
                        Approved              Rejected
                                                |
                                            Edit and resubmit
                                                (Draft)


4. Use case: For "User withdraws cash from an ATM", write the main flow (4–6 steps) and two exception flows.
    1. User insert the ATM card
    2. ATM requests PIN and User enter valid PIN
    3. ATM displays the available banking options and user select Withdraw option
    4. User enters the withdrawal amount
    5. ATM verifies the account balance, dispenses the requested cash
    6. ATM updates the correct baalnce and prints receipt and ATM return the card
Exception flow:
    1. User might have requested the more amount than their available balance
    2. ATM displays insufficient funds
    3. User enters different amount or camcel the transaction.

    1. User enters an invalid PIN
    2. ATM says error, or incorrect PIN - enter again
    3. User is allowed to retry within an attempt limit.
    4. If user failed to provide correct PIN, the card may be blocked.

5. Error guessing: List five error-guessing tests for a "Phone number" field.
    1. Enter strings/letter
    2. Enter special characters
    3. Enter a very long number than usual
    4. Enter with hypens, spaces
    5. Not entering - keeping it blank