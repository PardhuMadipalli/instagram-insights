#!/usr/bin/env python3

from getopt import getopt
from getopt import error
import sys

from instagram import instagram_data
from insights import hashtags
from insights import timings

options = "mh"
long_options = ["machine-learning", "help"]


def main():
    instagram_data.get_insights()
    timings.get_timing_insights()
    hashtags.get_best_tags()


if __name__ == "__main__":
    try:
        arguments, values = getopt(sys.argv[1:], options, long_options)
        for currentArgument, currentValue in arguments:
            if currentArgument in ["-h", "--help"]:
                with open('README', 'r') as readme:
                    print(readme.read())
                sys.exit(0)
            if currentArgument in ["-m", "--machine-learning"]:
                raise RuntimeError('Machine learning is not supported yet. Use -h for help.')
        main()
    except error as err:
        print('Run the script with -h option for help.')
        raise error
