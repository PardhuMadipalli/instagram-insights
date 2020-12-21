#!/usr/bin/env python3

from instagram import instagram_data
from insights import hashtags


def main():
    instagram_data.get_insights()
    hashtags.get_best_tags()


if __name__ == "__main__":
    main()
