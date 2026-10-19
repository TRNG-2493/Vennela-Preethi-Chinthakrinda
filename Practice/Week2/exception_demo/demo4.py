# Simulate a banking operation of withdrawal if the withdrawal is more than 500 raise exception 
# withdrawal limit exceeded, one with custom expection and other
from bankerror import LimitExceedError
try:
    withdraw=int(input("Enter the withdrawal amount: "))
    if withdraw>500:
        raise LimitExceedError("Withdraw limit Exceeded")
    print("Withdraw amount is: ", withdraw)
    
except ValueError as error:
    print("Please enter the amount in numbers")
    
except LimitExceedError as error:
    print("Limit is 500 only, please enter a amount less than 500")
    
finally:
    print("Transaction completed")