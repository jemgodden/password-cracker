import numpy as np
import random
import timeit
from functools import partial
from password import Password
from utils import ALLOWED_CHARS


class Cracker():
    def __init__(self, password: Password, trials: int=10000):
        self.trials = trials
        self._password = password

    @staticmethod
    def _reconstruct_password(password: str, pos: int, new_char: str) -> str:
        return password[:pos] + new_char + password[pos+1:]

    def _time_try(self, password_guess: str) -> float:
        times = timeit.repeat(
            stmt=partial(self._password.try_password, password_guess),
            number=self.trials,
            repeat=10
        )
        return min(times)

    def _crack_char(self, cur_password: str, char_pos: int) -> tuple[bool, str]:
        timings = {}

        for char in ALLOWED_CHARS:
            new_password = self._reconstruct_password(cur_password, char_pos, char)

            if self._password.try_password(new_password):
                return True, new_password
            
            min_time = self._time_try(new_password)
            timings[char] = min_time
        
        cracked_char = max(timings, key=timings.get)

        cur_password = self._reconstruct_password(cur_password, char_pos, cracked_char)

        return False, cur_password

    def _crack_chars(self, password_length: int) -> tuple[bool, str]:
        cur_password = ''.join(random.choices(ALLOWED_CHARS, k=password_length))

        for i in range(password_length):
            cracked, cur_password = self._crack_char(cur_password, i)
            print(f"Current guess: {cur_password}")
            if cracked:
                break

        return cracked, cur_password

    def _crack_length(self) -> int:
        times = []

        for i in range(self._password.max_length):
            rand_string = ''.join(random.choices(ALLOWED_CHARS, k=i))

            i_times = timeit.repeat(
                stmt=partial(self._password.try_password, rand_string),
                number=self.trials,
                repeat=10
            )
            times.append(min(i_times))

        return int(np.argmax(times))

    def crack_password(self):
        print("Cracking length of password...")
        password_length = self._crack_length()
        print("Cracked length of password.")
        print(f"Password length is {password_length}")

        print("Cracking password characters...")
        cracked, cracked_password = self._crack_chars(password_length)

        if cracked:
            print("Password characters cracked.")
            print(f"Password is: {cracked_password}")
        else:
            print("Password was not cracked.")
