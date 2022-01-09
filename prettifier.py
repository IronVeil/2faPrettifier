# 2 Factor Authentication Code Prettifier
# Turns a mess of numbers and letters into XXXX XXXX XXXX XXXX


# Tries to import copy module
try:
    import pyperclip
    copy = True

except:
    print("PYPERCLIP IS NOT INSTALLED, INSTALLING IT THROUGH PIP IS ADVISED")
    copy = False


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
code = prettify(code)
print("\nThe new code is:")
print(code)


# Autocopy if possible
if copy:
    pyperclip.copy(code)
    print("\nCode copied to clipboard\n")
else:
    print("\nCode not copied to clipboard\n")