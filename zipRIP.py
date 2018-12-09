# python 2.7 only
import argparse
import zipfile, time
from multiprocessing import Pool
from functools import partial
import contextlib

def check_args():
    parse = argparse.ArgumentParser()

    parse.add_argument('-z', '--zip', type=str, action='store', help='enter your encrypted zip file: -p \'your_zip\'')
    parse.add_argument('-w', '--wordlist', help='add your wordlist: -w wordlist')

    args_list = parse.parse_args()

    return args_list


def crack(pwd, f):
    try:
        print "> %s" % pwd
        pwd = pwd.strip()
        f.extractall(pwd=pwd)
        return pwd
    except:
        pass

def main():

    arguments = check_args()

    z_file = zipfile.ZipFile(arguments.zip)

    with open(arguments.wordlist, 'r') as passes:
        print "Start cracking. Wait..."
        start = time.time()

        lines = passes.readlines()
        with contextlib.closing(Pool(processes=50, maxtasksperchild=1)) as pool:
            result = pool.map(partial(crack, f=z_file), lines)

            for x in result:
                if x is not None:
                    print "Password cracked: %s" % x


        total = time.time() - start
        minutes, seconds = divmod(total, 60)
        hours, minutes = divmod(minutes, 60)

        print("Total time: %s:%s:%1.2f" % (hours, minutes, seconds))

if __name__ == '__main__':
    main()