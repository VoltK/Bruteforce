import string
import sys

if len(sys.argv) > 1:
    encrypted_msg = sys.argv[1]
else:
    encrypted_msg = input("You didn't enter encrypted message. Enter it now: ")


def bruteforce(msg):

    for key in range(len(string.ascii_lowercase)):
        translation = ""
        for letter in msg:
            if letter.lower() in string.ascii_lowercase:
                index = string.ascii_lowercase.find(letter.lower()) - key
                if index < 0:
                    index += len(string.ascii_lowercase)
                translation += string.ascii_lowercase[index]
            else:
                translation += letter
        print(f"Key {key}: {msg} -> {translation}")


bruteforce(encrypted_msg)
