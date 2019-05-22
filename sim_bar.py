import numpy as np
import math
import random
from scipy.stats import norm

from jury import *
from matplotlib import pyplot as plt

SIMULATIONS = 100000

jury = JuryList()

def no_duplicates():
    counts = []
    for i in range(SIMULATIONS):
        jury_list = jury.create_jury()
        makeup    = jury.race_count(jury_list)['White']
        counts.append(makeup)

    # Get the height of the graph
    a      = np.array(counts)
    xs, ys = np.unique(a, return_counts=True)

    plt.subplot(1,2,1)
    f1 = plt.bar(xs, ys, width=0.4)

    for i, v in enumerate(ys):
        plt.text(xs[i], v + 0.01, str(v), va='center')

    plt.xticks(np.arange(min(xs), max(xs)+1, 1.0))
    plt.ylabel('Num. of Juries')
    plt.xlabel('White People on Jury')
    plt.title('Distribution of Juries w/o Duplicates')

def w_duplicates():
    counts = []
    for i in range(SIMULATIONS):
        jury_list = jury.create_jury(True)
        makeup    = jury.race_count(jury_list)['White']
        counts.append(makeup)

    # Get the height of the graph
    a = np.array(counts)
    xs, ys = np.unique(a, return_counts=True)
    plt.subplot(1,2,2)
    f2 = plt.bar(xs, ys, color="orange", width=0.4)
    for i, v in enumerate(ys):
        plt.text(xs[i], v + 0.01, str(v), va='center')
    plt.xticks(np.arange(min(xs), max(xs)+1, 1.0))
    plt.ylabel('Num. of Juries')
    plt.xlabel('White People on Jury')
    plt.title('Distribution of Juries w/ Duplicates')

no_duplicates()
w_duplicates()

plt.show()