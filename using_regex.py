import re  # regular expression - a built-in Python module used for pattern matching in strings.

email = input("Enter email: ")

# Regex pattern for validating email
pattern = r"^[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
# ^                     -> start of the string
# [A-Za-z0-9._-]+       -> username part (letters, numbers, dot, underscore, hyphen allowed, at least one character)
# @                     -> must contain exactly one @ symbol separating username and domain
# [A-Za-z0-9.-]+        -> domain name (letters, numbers, dots, and hyphens allowed)
# \.                    -> literal dot before extension (example: gmail.com)
# [A-Za-z]{2,}          -> extension must contain at least 2 alphabet characters (like com, in, org)
# $                     -> end of the string (no extra characters allowed after extension)

# r means "raw string"
# It tells Python: "Treat backslashes normally, don't interpret them as escape characters."

if re.fullmatch(pattern, email):  # checks if the entire email matches the pattern
    print("Valid email")
else:
    print("Invalid email")