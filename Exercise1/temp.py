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
# reformat the date for ease of use later
data_rki["Date"] = pd.to_datetime(data_rki["Meldedatum"])
data_rki['dates'] = data_rki['Date'].dt.date

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

total_by_day = data_rki.groupby(['dates']).agg({'NeuerFall': sum}).values
dates = data_rki.groupby(['dates']).agg({'NeuerFall': sum}).NeuerFall
total_by_day_tue = tuebingen.groupby(['dates']).agg({'NeuerFall': sum}).values
dates_tue = tuebingen.groupby(['dates']).agg({'NeuerFall': sum}).NeuerFall
total_by_day_bw = bw.groupby(['dates']).agg({'NeuerFall': sum}).values
dates_bw = bw.groupby(['dates']).agg({'NeuerFall': sum}).NeuerFall

# Germany
dif_by_day = [0]
for i in range(1, total_by_day.size):
    dif_by_day.append(total_by_day[i] - total_by_day[i - 1])
plt.plot(dates._index, dif_by_day)
plt.xlabel('date')
plt.ylabel('difference between day at i and day at i - 1')
plt.title('Difference between given day and the previous in Germany')
plt.xticks(rotation=90)
plt.show()
plt.clf()


# Baden Württemberg
dif_by_day_bw = [0]
dates = []
for i in range(1, total_by_day_bw.size):
    dif_by_day_bw.append(total_by_day_bw[i] - total_by_day_bw[i - 1])
plt.plot(dates_bw._index, dif_by_day_bw)
plt.xlabel('date')
plt.ylabel('difference between day at i and day at i - 1')
plt.title('Difference between given day and the previous in Baden-Württemberg')
plt.xticks(rotation=90)
plt.show()
plt.clf()

# Tübingen
dif_by_day_tue = [0]
dates = []
for i in range(1, total_by_day_tue.size):
    dif_by_day_tue.append(total_by_day_tue[i] - total_by_day_tue[i - 1])
plt.plot(dates_tue._index, dif_by_day_tue)
plt.xlabel('date')
plt.ylabel('difference between day at i and day at i - 1')
plt.title('Difference between given day and the previous in Tübingen')
plt.xticks(rotation=90)
plt.show()
plt.clf()

# Plot timeseries
# fig, axs = plt.subplots(1, 3, figsize=(12, 3.5)) # todo fix this

# Create dataframe of number of new cases
data_rki_cases = None

# Compute number of new cases in last four days and in four days prior to that
# TODO basic reproduction number

# Estimate the basic reproduction number R0


# Show data from the previous week
# display(data_rki_cases.tail()) # todo add this back in

# Plot timeseries
# fig, axs = plt.subplots(1, 1, figsize=(10, 3.5))  # todo fix this

# Plot reproduction rate

# Link to world-wide COVID data
url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"

# Read CSV data from URL
data_owid = pd.read_csv('owid-covid-data.csv')

# Parse data
data_owid["Date"] = pd.to_datetime(data_owid["date"])
data_owid['dates'] = data_owid['Date'].dt.date


# Inspect dataframe and datatypes

# Countries of interest (CoIs)
cois = ["DEU", "GBR", "USA", "FRA", "NLD"]

# Subset worldwide data with CoIs
only_cois = data_owid.iso_code.isin(cois)
only_cois = data_owid[only_cois]

# Create CFR column
only_cois['case_fatality_rate'] = only_cois['total_deaths'] / only_cois['total_cases']
only_cois['positive_rate'] = only_cois['total_tests'] / only_cois['total_cases']


# Remove unnecessary columns
only_cois = only_cois[['iso_code', 'dates', 'new_cases', 'new_cases_per_million', 'new_cases_smoothed_per_million',
                       'case_fatality_rate', 'positive_rate']]

data_owid.head()

# fig, axs = plt.subplots(1, 3, figsize= # todo fix this

# Plotting colors
colors = dict(zip(cois, ["C0", "C1", "C2", "C3", "C4"]))
color_order = only_cois.replace({"iso_code": colors}).iso_code

# New Cases
# todo add legend?
# todo make a plot, not scatter?
plt.title("Number of new COVID cases by date")
plt.xlabel('dates')
plt.ylabel('number of new cases')
plt.scatter(only_cois.dates, only_cois.new_cases, color=color_order)
plt.xticks(rotation=90)
plt.show()

# Case fatality rate
plt.title("Fatality rate by date")
plt.xlabel('dates')
plt.ylabel('fatality rate')
plt.scatter(only_cois.case_fatality_rate, only_cois.new_cases, color=color_order)
plt.xticks(rotation=90)
plt.show()

# Rate of positive tests
# todo fix this
plt.title("Positive test rate by date")
plt.xlabel('dates')
plt.ylabel('positive test rate')
plt.yscale("log")
plt.scatter(only_cois.positive_rate, only_cois.new_cases, color=color_order)
plt.xticks(rotation=90)
plt.show()


# fig.tight_layout(w_pad=0.1) # todo fix this?
