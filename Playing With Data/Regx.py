import re  # Import the 're' module, which provides functions for working with regular expressions.

# Statement containing a Pincode (used as an example)
statement = 'This is the Pincode to my city - 454775'

# Define a regular expression pattern to match a 6-digit number (Pincode)
pattern = r'\d\d\d\d\d\d'  # '\d' matches any digit; this pattern expects exactly 6 digits in a row.

# Search for the pattern (6-digit number) in the statement
result = re.search(pattern, statement)

# If a match is found, it will print the matched Pincode.
if result:
    print('We got the pincode of that pattern : {}'.format(result.group()))
    # result.group() retrieves the matched text (the Pincode in this case).
    
# Now, we want to replace the old Pincode with a new one in the statement.
replace = '454775'  # The old Pincode to be replaced.
withh = '391760'  # The new Pincode that will replace the old one.

# Perform the replacement using re.sub(). The 'flags=re.IGNORECASE' ensures case-insensitivity, but here it doesn't affect much.
new_result = re.sub(replace, withh, statement, flags=re.IGNORECASE)

# Print the new statement with the replaced Pincode
print(new_result)

# Split the statement into a list of words using the regular expression '\s' (whitespace) as a delimiter.
list = re.split(r'\s', statement)

# Print the list of words in the statement. Each word is a separate element in the list.
print(list)
