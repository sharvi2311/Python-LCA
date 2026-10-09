def check(t):
    pattern = r'^[a-zA-Z0-9]+$'
    if re.match(pattern, t):
        return True
    return False

s = input("Enter a string to test: ")

if check(s):
    print(f"'{s}' contains only allowed characters (a-z, A-Z, 0-9)")
else:
    print(f"'{s}' contains invalid or special characters")
