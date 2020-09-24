import sys
import argparse
from string import ascii_lowercase, ascii_uppercase

# Provide the CLI
parser = argparse.ArgumentParser(description='A simple implementation of the caesar cipher')
parser.add_argument('message', nargs='*', type=str, help='The message to encrypt or decrypt')
parser.add_argument('--mode', '-m', type=int, help='Specifies by how many digits the alphabet gets shifted')
parser.add_argument('--encrypt', '-e', action='store_true', help='Encrypts the given message')
parser.add_argument('--decrypt', '-d', action='store_true', help='Decrypts the given message')

args = parser.parse_args()


def __shift_letters(math_op, digits, message):
    alphabet = ascii_lowercase
    alphabet_dict = dict(zip(ascii_lowercase, range(1, 27)))
    
    numerical_message = [alphabet_dict[letter] for letter in message]

    if math_op == "add":
        ciphertext = ""
        for number in numerical_message:
            ciphertext += alphabet[(number + digits % 26) - 1]
        return ciphertext
    elif math_op == "sub":
        plaintext = ""
        for number in numerical_message:
            plaintext += alphabet[(number - digits % 26) - 1]
        return plaintext
    else:
        return ''

def format_message(message):
    whitespaces = list(filter(lambda i: message[i] == ' ', range(len(message))))
    uppercase_letters = list(filter(lambda i: message[i] in ascii_uppercase, range(len(message))))
    message = message.replace(' ', '')
    message = message.lower()
    return message, whitespaces, uppercase_letters


def encrypt(plaintext, mode):
    plaintext, whitespaces, uppercase_letters = format_message(plaintext)
    cipher = list(__shift_letters("add", args.mode, plaintext))
    cipher = [cipher.insert(index, ' ') for index in whitespaces]
    cipher = [cipher[index].upper() for index in uppercase_letters]
    return cipher



def decrypt(ciphertext, mode):
    return __shift_letters("sub", args.mode, ciphertext)


if __name__ == '__main__':
    if args.encrypt:
        print(encrypt(args.message, args.mode))
    elif args.decrypt:
        print(decrypt(args.message, args.mode))