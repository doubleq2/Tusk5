import collections
from functools import lru_cache
import argparse
from pathlib import Path

def starter(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--string")
    parser.add_argument("-f", "--file")
    p = parser.parse_args(args)
    return check(p)

@lru_cache(maxsize=15)
def clearword(string):
    c = collections.Counter()
    for word in list(string):
        c[word] += 1
    return len(c)

def check(args):
    if args.file:
        filename = args.file
        lines = Path(filename).read_text().splitlines()
        for word in lines:
            return clearword(word)
    elif args.string and args.file ==None:
        return clearword(args.string)  