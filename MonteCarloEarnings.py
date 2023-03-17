# Nathalia De Souza -- Assignment 1: Stochastic Methods -- 2/6/2023

import math
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import numpy as np
import random
import statistics as sts
from scipy.stats import norm
from tabulate import tabulate



# triangular ditribution data from table 5.2
triDistData = {
    "unitPrice": [50, 55, 70],
    "unitSales": [2000, 2440, 3000],
    "varCosts": [50000, 55200, 65000],
    "fixCosts": [10000, 14000, 20000],
    "earnings": [40000, 65000, 125000]
}

# calculating the predicted future earnings using table 5.2
earnings = []
unit_price = []
unit_sales = []
fixed_costs = []
variable_costs = []
tries = np.linspace(0,1,10000)

for t in tries:
    # i have no idea where they got the equation for this from, but here i generate random values from the triangular distribution data
    rando = math.sqrt(random.uniform(0, 1))
    unit_price.append(((triDistData["unitPrice"][2] - triDistData["unitPrice"][0]) * rando * random.uniform(0, 1)) + triDistData["unitPrice"][1] - ((triDistData["unitPrice"][1] - triDistData["unitPrice"][0]) * rando))
    unit_sales.append(((triDistData["unitSales"][2] - triDistData["unitSales"][0]) * rando * random.uniform(0, 1)) + triDistData["unitSales"][1] - ((triDistData["unitSales"][1] - triDistData["unitSales"][0]) * rando))
    fixed_costs.append(((triDistData["fixCosts"][2] - triDistData["fixCosts"][0]) * rando * random.uniform(0, 1)) + triDistData["fixCosts"][1] - ((triDistData["fixCosts"][1] - triDistData["fixCosts"][0]) * rando))
    variable_costs.append(((triDistData["varCosts"][2] - triDistData["varCosts"][0]) * rando * random.uniform(0, 1)) + triDistData["varCosts"][1] - ((triDistData["varCosts"][1] - triDistData["varCosts"][0]) * rando))

uSP = []
for i in range(len(tries)):     
    earnings.append((unit_price[i] * unit_sales[i]) - (variable_costs[i] + fixed_costs[i]))
    uSP.append((unit_price[i] * unit_sales[i]))


mean = sts.mean(earnings) 
medi = sts.median(earnings)
vari = sts.variance(earnings)
stde = sts.stdev(earnings)
little = min(earnings)
big = max(earnings)

# my version of table 5.3
sumStatsTable = [['Mean', mean], ['Median', medi], ['Standard Deviation', stde], ['Variance', vari], ['Min', little,], ['Max', big]]
print("\n\n**************")
print("\nEarnings Summary Statistics:\n")
print(tabulate(sumStatsTable, headers=["Parameter", "Value"]), "\n") 
print("**************")


# Calculate confidence interval
alpha = 0.05
z_1alpha2 = 1.96
ci_lower_2 = mean - (z_1alpha2 * stde / np.sqrt(len(tries)))
ci_upper_2 = mean + (z_1alpha2 * stde / np.sqrt(len(tries)))


print("\nConfidence Interval for Mean Earnings:", [ci_lower_2, ci_upper_2],"\n")



# Sigma-normalized derivatives for each input
varCostDer = sts.stdev(variable_costs)/sts.stdev(earnings)
fixCostDer = sts.stdev(fixed_costs)/sts.stdev(earnings)
uSPDer = sts.stdev(uSP)/sts.stdev(earnings)

sigNorDer = [['Variable Costs', varCostDer], ['Fixed Costs', fixCostDer], ['Unit Sales x Unit Price', uSPDer]]
print ("**************")
print("\nSigma-normalized Derivatives:\n")
print (tabulate(sigNorDer, headers=["Variable", "S-squared"]),"\n")
print ("**************\n\n")


# Sensitivity scatter plots
fig, (ax1, ax2, ax3) = plt.subplots(3)
fig.suptitle('Earnings vs Input')
fig.subplots_adjust(left= 0.15 , bottom=None, right=0.95, top=None, wspace=None, hspace=0.7)

ax1.scatter(variable_costs,earnings)
ax1.set(xlabel = "Variable Costs", ylabel = "Earnings")
ax1.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))

ax2.scatter(fixed_costs, earnings)
ax2.set(xlabel = "Fixed Costs", ylabel = "Earnings")
ax2.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))


ax3.plot(uSP, earnings)
ax3.set(xlabel = "Unit Sales x Unit Price", ylabel = "Earnings")
ax3.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))

plt.show()
