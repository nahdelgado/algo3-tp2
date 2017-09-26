#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Experiment-data generator.

Wrapper for the solver that executes it with every
generated test to collect data for analysis.
"""
import os
import subprocess
import sys


BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTSDIR = os.path.join(BASEDIR, "tests")
RESULTS_PATH = os.path.join(BASEDIR, "results")
EXECUTABLE = os.path.join(BASEDIR, "bin", "ej3")
BENCHMARK_FLAG = "-b"
ARGS = (EXECUTABLE, BENCHMARK_FLAG)


def main():
    """Module's entry point.

    Executes the solver with every generated instance
    and saves times to a csv.
    """
    if not os.path.exists(RESULTS_PATH):
        os.makedirs(RESULTS_PATH)
    try:
        generate_results()
    except FileExistsError:
        print("csv file already exists, skipping...")
    return 0


def generate_results():
    """Write results from solving every instance in the dataset.
    """
    filename = "results.csv"
    with open(os.path.join(RESULTS_PATH, filename), "x") as results_file:
        results_file.write("parameters,time\n")
        dirlist = sorted(os.listdir(TESTSDIR))
        for instance_file in dirlist:
            with open(os.path.join(TESTSDIR, instance_file)) as instance:
                instance_str = instance.read()
                time = call_solver(ARGS, instance_str)
                results_file.write("{},{}\n".format("param", time))


def call_solver(args, instance):
    """Call solver executable for a given instance.
    """
    popen = subprocess.Popen(
        args,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        encoding="utf-8",
        errors="utf-8"
    )
    out, _ = popen.communicate(instance)
    return int(out)


if __name__ == "__main__":
    sys.exit(main())
