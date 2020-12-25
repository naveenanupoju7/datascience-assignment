import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('seaborn') #style used to plot

dates=[
    datetime(2019,5,24),
    datetime(2019,5,25),   #creating time series data follows year month and date format
    datetime(2019,5,26),
    datetime(2019,5,27),
    datetime(2019,5,28),
    datetime(2019,5,29),
    datetime(2019,5,30),
    ]

y=[0,1,9,3,12,5,6]        #creating y values for it

plt.plot_date(dates,y,linestyle='solid',marker='None') #to plot time series data plot_date is used


plt.gcf().autofmt_xdate()  #for auto adjusting the dates on the axis line from horizontal to slant

date_format=mpl_dates.DateFormatter('%b %d %Y')  #formatting the dates with month,date,year

plt.gca().xaxis.set_major_formatter(date_format)

plt.tight_layout()
plt.show()
