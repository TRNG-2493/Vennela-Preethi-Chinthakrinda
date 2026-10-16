#write logic that returns the number of occurrence of a number occurs in this list
from collections import Counter
numbers = [1,2,2,3,3,3,4,4,5]
result = Counter(numbers)
print(result)

# counter class - counts the no of occurence in list returns the dictonary.
print(f"Count of 2 is {result[2]}")
print(result.most_common(2)) # returns the two most common elements

text = "banana"
letters = Counter(text)
print(letters)