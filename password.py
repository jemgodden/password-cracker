from utils import ALLOWED_CHARS

class Password():
    def __init__(self, password: str):
        self.max_length = 30
        self.allowed_chars = ALLOWED_CHARS
        self._password = self._set_password(password)

    def _set_password(self, password) -> str:
        n = len(password)
        if n == 0:
            raise Exception("Error - Password is empty.")
        if n > self.max_length:
            raise Exception("Error - Password is too long. Max number of characters is 30.")
        for char in password:
            if char not in self.allowed_chars:
                raise Exception(f"Error - Password cannot contain character {char}.")
        return password

    def try_password(self, password_attempt: str) -> bool:
        if len(password_attempt) != len(self._password):
            return False
        
        for i in range(len(password_attempt)):
            if password_attempt[i] != self._password[i]:
                return False
            
        return password_attempt == self._password
