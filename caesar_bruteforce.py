import string


def bruteforce(encrypted_msg):

    for key in range(len(string.ascii_lowercase)):
        translation = ""
        for letter in encrypted_msg:
            if letter.lower() in string.ascii_lowercase:
                index = string.ascii_lowercase.find(letter.lower()) - key
                if index < 0:
                    index += len(string.ascii_lowercase)
                translation += string.ascii_lowercase[index]
            else:
                translation += letter
        print(f"Key {key}: {translation}")


bruteforce("okci dy lboku drsc xygknkic")
