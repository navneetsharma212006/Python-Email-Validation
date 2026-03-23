email = input("Enter your email: ")

valid = True

# Rule 1: Minimum length
if len(email) < 6:
    print("Invalid email (too short)")
    valid = False

# Rule 2: Exactly one @
if email.count("@") != 1:
    print("Invalid email (must contain exactly one @)")
    valid = False

if valid:
    username, domain = email.split("@")

    # Rule 3: Username and domain must not be empty
    if username == "" or domain == "":
        print("Invalid email (username or domain missing)")
        valid = False

# Rule 4: Username cannot start or end with dot
if valid:
    if username[0] == "." or username[-1] == ".":
        print("Invalid email (username cannot start or end with '.')")
        valid = False

# Rule 5: Username cannot contain double dots
if valid:
    if ".." in username:
        print("Invalid email (username cannot contain consecutive dots)")
        valid = False

# Rule 6: Allowed characters in username
if valid:
    for ch in username:
        if not (ch.isalnum() or ch in "._-"):
            print("Invalid email (username contains invalid character)")
            valid = False
            break

# Rule 7: Domain must contain dot
if valid:
    if "." not in domain:
        print("Invalid email (domain must contain '.')")
        valid = False

# Rule 8: Domain cannot start or end with dot
if valid:
    if domain[0] == "." or domain[-1] == ".":
        print("Invalid email (domain cannot start or end with '.')")
        valid = False

# Rule 9: Domain cannot contain double dots
if valid:
    if ".." in domain:
        print("Invalid email (domain contains consecutive dots)")
        valid = False

# Rule 10: Extension length check
if valid:
    extension = domain.split(".")[-1]
    if len(extension) < 2:
        print("Invalid email (extension too short)")
        valid = False

# Final result
if valid:
    print("Valid email")
