# for the next month 
# St+1 is the predicted value for the next time period
# St is the most recent predicted value
# yt is the most recent actual value
# a (alpha) is the smoothing factor between 0 and 1

from statsmodels.tsa.api import SimpleExpSmoothing
import pandas as pd
import plotly.express as px

df = pd.read_csv('AirPassengers.csv')

