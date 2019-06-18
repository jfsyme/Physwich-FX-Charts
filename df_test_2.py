import pandas as pd
import numpy as np
import sys
from scipy import stats
from datetime import datetime
import matplotlib.pyplot as plt

###This is temp code creating the data df
cabaldf = pd.DataFrame([[10,2],[20,4],[30,8],[50,8]])
cabaldf.columns = ['XA','XB']

###This is temp code creating the data df
actdf = pd.DataFrame([[100,1],[140,3],[230,6],[150,8]])
actdf.columns = ['ZA','ZB']

###This is a lookup of the codes, signif potential for error
countries = ['AR','BR']
codedf = pd.DataFrame([['XA','XB'],['ZA','ZB']],columns=countries)

codenamesdf = pd.DataFrame([['Arg CAB','Braz CAB'],['Arg Activ','Braz Unempl']],
                           columns=countries)


for i in range(len(countries)):
    #Get the countrycode
    ctrycode = countries [i]
    #Get the datacodes for that country
    cab = codedf.loc[0,ctrycode]
    act = codedf.loc[1,ctrycode]
    #pull the data dfs for those codes
    cabaldf1 = cabaldf[cab]
    actdf1 = actdf[act]
    #merge the pulled data dfs into one
    #frames is a temp list of data dfs to be merged and shouldn't be used elsewhere
    frames = [cabaldf1, actdf1]
    result = pd.concat(frames, axis=1)
    result.columns = ['CAB','ACT']
#    resultnames = pd.DataFrame([codenamesdf.loc[0,ctrycode],
#                               codenamesdf.loc[1,ctrycode]],[0,0])
#    resultnames.columns = ['CAB','ACT']
    #This will be where the plot and pdf save goes
    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('Date')
    ax1.set_ylabel(codenamesdf.loc[0,ctrycode], color=color)
    ax1.plot(result.index, result.CAB, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax2.set_ylabel(codenamesdf.loc[1,ctrycode], color=color)  # we already handled the x-label with ax1
    ax2.plot(result.index, result.ACT, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.show()


