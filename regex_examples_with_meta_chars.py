import re  # Import regex module

# ---------- METACHARACTER EXAMPLES ----------
# Meta characters are special characters used in regex patterns.

# \d : any digit (0–9)
# \D : any non-digit character
# \w : any alphanumeric character (letters, digits, underscore)
# \W : any non-alphanumeric character
# \s : any whitespace character (space, tab, newline)
# \S : any non-whitespace character
# .  : any character except newline
# +  : one or more repetitions
# *  : zero or more repetitions
# ?  : zero or one repetition (optional)
# ^  : start of string
# $  : end of string
# {} : specify exact number of repetitions
# [] : set of characters
# |  : or
# () : grouping

# ---------- EXAMPLE: Matching Dates, Emails, Phones ----------
text = """
Welcome to r00thidar Academy!
Course Dates: 01-Jan-2025, 02.Jan.2025, 03/Jan/2025, 04.01.2025
Phone Numbers: +44-789-123-4567, +44 789 123 4567
Email Contacts: john.doe@example.com, support@r00thidar.co.uk, hello@info.org
"""

# Match dates in formats like: 01-Jan-2025, 02.Jan.2025, 04.01.2025
date_pattern = r"\d{2}[-./]([a-zA-Z]{3}|\d{2})[-./]\d{4}"  # Match day-month-year in various formats

# Match email addresses like: name@domain.com or domain.co.uk
email_pattern = r"\w+([.-]?\w+)*@[a-zA-Z]+\.[a-z]{2,3}(\.[a-z]{2})?"  # Match common email formats

# Match phone numbers like: +44-789-123-4567 or +44 789 123 4567
phone_pattern = r"\+\d{2}[-\s]\d{3}[-\s]\d{3}[-\s]\d{4}"  # Match phone numbers with different separators

# Find all matches in the text for each pattern
date_matches = re.finditer(date_pattern, text)
email_matches = re.finditer(email_pattern, text)
phone_matches = re.finditer(phone_pattern, text)

print("Matched Dates:")
for match in date_matches:
    print("  ➤", match.group())  # Print matched date

print("\nMatched Emails:")
for match in email_matches:
    print("  ➤", match.group())  # Print matched email

print("\nMatched Phone Numbers:")
for match in phone_matches:
    print("  ➤", match.group())  # Print matched phone number
