import string

ALPHABET = [char for char in string.ascii_letters]
NUMBERS = [str(x) for x in range(10)]
SPECIAL_CHARS = [".", ",", "-", "_", "(", ")", "*", "@", "£", "$", "?", "!"]

ALLOWED_CHARS = ALPHABET + NUMBERS + SPECIAL_CHARS
