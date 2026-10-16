from collections import defaultdict

# default dictionary - supplies a defa value to key that does not exist.

marks=defaultdict(int)
marks['Alice'] = 80
marks['Bob'] = 90

print(marks['Alice'])
print(marks['Bob'])
print(marks['Charlie']) #takes the default value as '0'