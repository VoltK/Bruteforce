import string
import argparse
import sys


def arguments():
    parser = argparse.ArgumentParser(
        description='Caesar encryption',
    )

    parser.add_argument('-s', '--string', nargs='*', help='enter string to encrypt: -s encrypt me')
    parser.add_argument('-k', '--key', type=int, help='key to shift: -k 5')

    args_list = parser.parse_args()

    return args_list


def encrypt(message, shift):
    encrypted = ""
    for word in message:
        encrypted_word = ""
        for letter in word:
            if letter.lower() in string.ascii_lowercase:
                index = string.ascii_lowercase.index(letter.lower()) + shift
                if index > 25:
                    index -= 26
                encrypted_letter = string.ascii_lowercase[index]
                encrypted_word += encrypted_letter
            else:
                encrypted_word = letter

        encrypted += encrypted_word + " "

    return encrypted


def main():
    c_args = arguments()
    if len(c_args.string) == 0:
        sys.exit("You didn\'t enter string to encrypt. Try again")
    encrypted_message = encrypt(c_args.string, c_args.key)
    print(f"Your encrypted message is: \"{encrypted_message}\"")


if __name__ == '__main__':
    main()

