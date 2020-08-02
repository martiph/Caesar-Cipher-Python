import sys

# example caesar_enc.py 0 6
# first argument is the operation (0 for encryption and 1 for decryption)
# second argument is the mode of operation (by how many digits the alphabet gets shifted)

if len(sys.argv) != 3:
    sys.exit(1)

print(sys.argv)

operation = int(sys.argv[1])
mode = int(sys.argv[2])


def __shift_letters(math_op, digits, text):
    alphabet = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
                "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21,
                "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}
    numerical_alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                          "T", "U", "V", "W", "X", "Y", "Z"]
    numerical_text = []
    for letter in text:
        numerical_text.append(alphabet[letter])

    if math_op == "+":
        ciphertext = ""
        for number in numerical_text:
            ciphertext += numerical_alphabet[(number + digits % 26) - 1]
        return ciphertext
    elif math_op == "-":
        plaintext = ""
        for number in numerical_text:
            plaintext += numerical_alphabet[(number - digits % 26) - 1]
        return plaintext


def encode(plaintext, mode):
    ciphertext = __shift_letters("+", mode, plaintext)
    return ciphertext


def decode(ciphertext, mode):
    plaintext = __shift_letters("-", mode, ciphertext)
    return plaintext


if operation == 0:
    plaintext = input("Plaintext: ").upper()
    print(encode(plaintext, mode))
elif operation == 1:
    ciphertext = input("Ciphertext: ").upper()
    print(decode(ciphertext, mode))
