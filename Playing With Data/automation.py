import re

with open(r'D:\Data Science\Playing With Data\text.txt', 'r', encoding='utf-8') as f:
    text = f.read()  # Read the entire file once and store it in a variable

emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)

print(emails)  # Print the list of extracted emails
