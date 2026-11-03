import re

# Input text containing emails
text = """
Contact us at support@gmail.com
or info@yahoo.com.
For queries, mail shreyaa123@college.edu
"""

# Regex pattern for email addresses
pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# Find all email addresses
emails = re.findall(pattern, text)

# Display emails
print("Email addresses found:")
for email in emails:
    print(email)

