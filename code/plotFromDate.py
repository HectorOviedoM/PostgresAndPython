from getDataFromIexCloud import DataIexCloud
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import pandas as pd


#obtains the data
con= DataIexCloud()
dataframe = con.DataToPlot()

#cast the date column and filter the last 30 days
dataframe['date'] = pd.to_datetime(dataframe['date'])
first_date = datetime.now() - timedelta(days=30)
filtred_dataframe = dataframe[dataframe.date > first_date ]

#plot the filtred_dataframe
df = filtred_dataframe[['uOpen', 'uClose', 'date']].copy()
df = df.set_index('date')
ax = df.plot(secondary_y='uClose')
plt.savefig(f'save_results/plots/OpenAndClosePrices.png')