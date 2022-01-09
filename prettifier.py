# 2 Factor Authentication Code Prettifier
# Turns a mess of numbers and letters into XXXX XXXX XXXX XXXX


# Prettifier subroutine
def prettify(code):

    # Removes any spaces
    code = code.replace(" ", "")

    # Splits the string into parts of 4 and joins them with spaces
    return ' '.join([code[i:i+4] for i in range(0, len(code), 4)]).upper()


# Input
print("2FA PRETTIFIER\n")
code = input("Please enter 2FA seed: ")


# Output
print("\nThe new code is:")
print(prettify(code))