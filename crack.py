# Breaks UNIX password that uses DES algorithm using dict based attack
# Also breaks sha512 hashed passwords from /etc/shadow file in Linux

import crypt
import argparse
import sys
import time


def check_args():
    parse = argparse.ArgumentParser()

    parse.add_argument('-p', '--password', type=str, action='store', help='enter your hashed password: -p \'your_hash\'')
    parse.add_argument('-w', '--wordlist', help='add your wordlist: -w wordlist')
    parse.add_argument('-f', '--file', help='file with hashes: -f your_hashes')

    args_list = parse.parse_args()

    return args_list


def check_pass(encrypted_pass, wordlist):
    salt = encrypted_pass[0:2]

    # check for sha512
    if salt == "$6":
        i = encrypted_pass.rfind('$')
        salt = encrypted_pass[:i]

    # check for wordlist file
    if wordlist:
        file = wordlist
    else:
        file = 'words.dic'

    # read wordlist
    with open(file, 'r') as keys:
        for key in keys.readlines():
                # encrypt each word with salt from hashed password
                encrypt_word = crypt.crypt(key.strip(), salt)
                # compare them, if yes -> save to file
                if encrypt_word == encrypted_pass:
                    print("[+] Password found: %s" % key)
                    with open('cracked.txt', 'a') as crack:
                        crack.write(encrypted_pass + ":" + key + "\n")
                        print("Saved to cracked.txt")
                    return
        print("[-] Password Not Found")
    return


# if we have file with hashes
def hashes(file, wordlist):
    with open(file, "r") as pass_file:
        for index, line in enumerate(pass_file.readlines()):
            psw =line.strip('\n').strip(' ')
            print("*** Cracking hash %d:%s" % (index, psw))
            check_pass(psw, wordlist)


def main():
    try:
        start = time.time()

        c_arg = check_args()

        psw = c_arg.password
        wordlist = c_arg.wordlist
        file = c_arg.file

        if psw and file:
            sys.exit("You can pass either single hash option or file with hashes.")

        elif psw:
            print('.' * 130)
            print('\tStart cracking %s ' % psw)
            print('.' * 130)


            check_pass(psw, wordlist)


        elif file:
            hashes(file, wordlist)
        else:
            sys.exit('Blank command line. For help enter "--help"')

        total = time.time() - start
        minutes, seconds = divmod(total, 60)
        hours, minutes = divmod(minutes, 60)

        print("Total time: %s:%s:%1.2f" % (hours, minutes, seconds))

    except KeyboardInterrupt:
        sys.exit('\nCtrl+C was pressed. Exiting...')

    except Exception as e:
        print("Error %s. Exiting..." % e)


if __name__ == '__main__':
    main()

