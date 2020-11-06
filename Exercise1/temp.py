# Plotting setup
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime


# Make inline plots vector graphics
from IPython.display import set_matplotlib_formats

set_matplotlib_formats("pdf", "svg")


# matplotlib.rc("font", **{"family": "serif", "serif": ["Computer Modern"]})
# plt.rcParams["text.usetex"] = True
# plt.rcParams["text.latex.preamble"] = r"\usepackage{amsfonts} \usepackage{amsmath}"

# Link to current data of the RKI

url = "https://www.arcgis.com/sharing/rest/content/items/f10774f1c63e40168479a1feb6c7ca74/data"

# Read CSV data from URL
data_rki = pd.read_csv('RKI_COVID19_small.csv')

# Inspect first few rows of the data

# Compute the cumulative number of cases

cases_germany = sum(data_rki.NeuerFall)
print(f"Total confirmed cases of COVID-19 in Germany: \t{cases_germany:,}")

# Compute the cumulative number of cases in Tübingen

bw = data_rki[data_rki['Bundesland'] == 'Baden-Württemberg']
tuebingen = data_rki[data_rki['Landkreis'] == 'LK Tübingen']
cases_tuebingen = sum(tuebingen.NeuerFall)
print(f"Total confirmed cases of COVID-19 in Tübingen: \t{cases_tuebingen:,}")

# Population sizes
population_sizes = {"Germany": 83783942,
                   "Baden-Württemberg": 11023424,
                   "Tübingen": 228678}

total_by_day = data_rki.groupby(['Meldedatum']).agg({'NeuerFall': sum}).values
total_by_day_tue = tuebingen.groupby(['Meldedatum']).agg({'NeuerFall': sum}).values
total_by_day_bw = bw.groupby(['Meldedatum']).agg({'NeuerFall': sum}).values
# print(total_by_day)

# Germany
# TODO fix dates
dif_by_day = []
dates = []
for i in range(1, total_by_day.size):
    dif_by_day.append(total_by_day[i] - total_by_day[i - 1])
plt.plot(dif_by_day)
plt.xticks(rotation=90)
plt.show()
plt.clf()


# Baden Württemberg
# todo fix this
dif_by_day_bw = []
dates = []
for i in range(1, total_by_day_bw.size):
    dif_by_day.append(total_by_day_bw[i] - total_by_day_bw[i - 1])
plt.plot(dif_by_day_bw)
plt.xticks(rotation=90)
plt.show()
plt.clf()

# Tübingen
# todo fix this
dif_by_day_tue = []
dates = []
for i in range(1, total_by_day_tue.size):
    dif_by_day_tue.append(total_by_day_tue[i] - total_by_day_tue[i - 1])
plt.plot(dif_by_day_tue)
plt.xticks(rotation=90)
plt.show()
plt.clf()

# Plot timeseries
fig, axs = plt.subplots(1, 3, figsize=(12, 3.5))

# Create dataframe of number of new cases
data_rki_cases = None

# Compute number of new cases in last four days and in four days prior to that


# Estimate the basic reproduction number R0


# Show data from the previous week
display(data_rki_cases.tail())

# Plot timeseries
fig, axs = plt.subplots(1, 1, figsize=(10, 3.5))

# Plot reproduction rate

# Link to world-wide COVID data
url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"

# Read CSV data from URL
data_owid = None

# Parse data


# Inspect dataframe and datatypes

# Countries of interest (CoIs)
cois = ["DEU", "GBR", "USA", "FRA", "NLD"]

# Subset worldwide data with CoIs


# Create CFR column


# Remove unnecessary columns

data_owid.head()

fig, axs = plt.subplots(1, 3, figsize=(10, 3.5))

# Plotting colors
colors = dict(zip(cois, ["C0", "C1", "C2", "C3", "C4"]))

# New Cases


# Case fatality rate


# Rate of positive tests


# Date formatting


fig.tight_layout(w_pad=0.1)