#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Plot generator.

Creates plots from the experiments and saves them into pdf files.
"""
import sys
import pandas as pd
import matplotlib.pyplot as plt


def main():
    """Module's entry point.
    """
    random = pd.read_csv("../results/results.csv")

    plt.clf()
    splots = random.plot(x="parameters", y="time")
    plt.legend(["Tiempos"])
    plt.xlabel("Cantidad de PARAM")
    plt.ylabel("Tiempos en microsegundos")
    fig = splots.get_figure()
    fig.savefig("../tex/plots/plot.pdf")

    return 0


if __name__ == "__main__":
    sys.exit(main())
