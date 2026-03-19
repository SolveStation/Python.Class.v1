# Ceaser Cypher
import string

letters : str = string.ascii_lowercase

alphabets = []

for letter in letters:
    alphabets.append(letter)


class Ceaser():
    """
    This is for encryption and decryption
    """
    SHIFT = 2

    def encryption(input: str) -> str:
        encypted_output = []
        # Awwal
        for char in input.lower():
            print(char)
            for i in range(0, 27):
                if alphabets[i] == char:
                    position = Ceaser.SHIFT + 1 + i
                    encypted_output.append(alphabets[position])


    def decryption() -> str:
        pass
