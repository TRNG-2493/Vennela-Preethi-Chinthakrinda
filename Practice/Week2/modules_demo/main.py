import validators
#import the name of filename without the extension

print(validators.is_valid_username("JohnDoe")) #True
print(validators.is_valid_username("")) #False

# there are multiple ways to import. (4 ways)
# 1. is using import

# 2. is using "from" keyword. 
# EX: from validators import is_valid_username
# print(is_valid_username("JohnDoe")) #True
# can import 2 functions separated by comma - from validators import is_valid_username, is_valid_email

# 3. import validators as v
# print(v.is_valid_username("JohnDoe")) #True

# 4. from validators import * #avoid this style 

# guidelines or conventions in python comes from PEP 8 - is the official python style guide


#PACKAGES - is a directory which can contain multiple modules