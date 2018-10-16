import string


def encrypt(message, shift):
    words = message.split()
    encrypted = ""
    for word in words:
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


print(encrypt("caesar cipher 1", 5))



