#!/usr/bin/env python3

from getopt import getopt
from getopt import error
import sys
import os

from instagram import instagram_data
from insights import hashtags
from insights import timings
from insights import htmlutils

options = "mh"
long_options = ["machine-learning", "help", "page-id=", "token="]


def main(token, page_id):
    instagram_data.get_insights(token, page_id)

    htmlutils.create_html()

    timings.get_timing_insights(max_indices=3)
    hashtags.get_best_tags(max_indices=5)

    htmlutils.end_html()


if __name__ == "__main__":
    try:
        arguments, values = getopt(sys.argv[1:], options, long_options)
        token, page_id = None, None
        for currentArgument, currentValue in arguments:
            if currentArgument in ["-h", "--help"]:
                with open('README', 'r') as readme:
                    print(readme.read())
                sys.exit(0)
            if currentArgument in ["-m", "--machine-learning"]:
                raise RuntimeError('Machine learning is not supported yet. Use -h for help.')
            if currentArgument == "--page-id":
                page_id = currentValue
            if currentArgument == "--token":
                token = currentValue
        if token is None:
            token = os.environ.get("FB_TOKEN")
        if page_id is None:
            page_id = os.environ.get("FB_PAGE_ID")
        main(token, page_id)
    except error as err:
        print('Run the script with -h option for help.')
        raise error
