import numpy as np
import math
import random
import seaborn as sns
from scipy import stats
import pandas as pd

from jury import *
from matplotlib import pyplot as plt

SIMULATIONS = 100000
# SIMULATIONS = 10000

BANDWIDTH = .5
# BANDWIDTH = 'silverman'

# CUMULATIVE = False
CUMULATIVE = True

jury = JuryList()

def no_duplicates():
    counts = []
    for i in range(SIMULATIONS):
        jury_list = jury.create_jury()
        makeup    = jury.race_count(jury_list)['White']
        counts.append(makeup)
    counts = pd.Series(counts, name="KDE w/o Duplicates")
    sns.kdeplot(counts, shade=True, color="b", bw=BANDWIDTH, cumulative=CUMULATIVE)

def w_duplicates():
    counts = []
    for i in range(SIMULATIONS):
        jury_list = jury.create_jury(True)
        makeup    = jury.race_count(jury_list)['White']
        counts.append(makeup)
    counts = pd.Series(counts, name="KDE w/ Duplicates")
    sns.kdeplot(counts, shade=True, color="r", bw=BANDWIDTH, cumulative=CUMULATIVE)

no_duplicates()
w_duplicates()

plt.grid(which='both')
plt.title("Likelihood of # of White people on a Jury with " + str(SIMULATIONS) + " simulations")

if CUMULATIVE:
    plt.savefig('cumulative.png')
else:
    plt.savefig('non_cumulative.png')