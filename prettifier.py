# Prettifier
def prettify(code):
    return ' '.join([code[i:i+4] for i in range(0, len(code), 3)]).upper()

# Input
print("2FA PRETTIFIER\n")
code = input("Please enter 2FA seed: ")

# Output
print("\nThe new code is:")
print(prettify(code))

# TODO - auto copy (w/ module detection)
# TODO - clean up README.md