#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Worst case test instance generator.
"""
import argparse
import os
import sys


def main():
    """Modules's entry point.

    Parses command-line parameters and generates worst case test instances
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('some_param', type=int)
    args = parser.parse_args()

    basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    path = os.path.join(basedir, "tests", "worst_case")
    if not os.path.exists(path):
        os.makedirs(path)
    instance = generate_case(args.some_param)
    filename = "worst_case_instance_{}".format(args.some_param)
    with open(os.path.join(path, filename), 'w') as instance_file:
        instance_file.write(instance)
    return 0


def generate_case(params):
    """Generates a single worst case test instancer"""
    return "{}".format(params)


if __name__ == "__main__":
    sys.exit(main())
