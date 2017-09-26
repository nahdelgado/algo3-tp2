#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Random test instances generator.
"""
import argparse
import os
import sys


def main():
    """Modules's entry point.

    Parses command-line parameters and generates random test instances
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('some_param', type=int)
    args = parser.parse_args()

    basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    path = os.path.join(basedir, "tests", "random")
    if not os.path.exists(path):
        os.makedirs(path)
    instance = generate_case(args.some_param)
    filename = "random_instance_{}".format(args.some_param)
    with open(os.path.join(path, filename), 'w') as instance_file:
        instance_file.write(instance)
    return 0


def generate_case(params):
    """Generates a single random random instance"""
    return "{}".format(params)


if __name__ == "__main__":
    sys.exit(main())
