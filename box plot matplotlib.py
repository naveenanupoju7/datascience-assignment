from  datetime import datetime,timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
import pandas as pd
import numpy as np
import seaborn as sns



df=pd.read_excel(r'G:\TROP ICSU INTERNSHIP\India-Temp-2011.xlsx',engine='openpyxl')

x= df[['YEAR']].to_numpy()
y1= df[['ANNUAL']].to_numpy()
y2= df[['JAN-FEB']].to_numpy()
y3= df[['MAR-MAY']].to_numpy()
y4= df[['JUN-SEP']].to_numpy()
y5= df[['OCT-DEC']].to_numpy()







a=plt.boxplot(df.ANNUAL,1,showmeans=True,autorange=True,positions=[1],patch_artist=True,boxprops=dict(facecolor="Black"))



b=plt.boxplot(df['JAN-FEB'],1,showmeans=True,autorange=True,positions=[2],patch_artist=True,boxprops=dict(facecolor="Green"))

c=plt.boxplot(df['MAR-MAY'],1,showmeans=True,autorange=True,positions=[3],patch_artist=True,boxprops=dict(facecolor="Blue"))

d=plt.boxplot(df['JUN-SEP'],1,showmeans=True,autorange=True,positions=[4],patch_artist=True,boxprops=dict(facecolor="Red"))

e=plt.boxplot(df['OCT-DEC'],1,showmeans=True,autorange=True,positions=[5 ],patch_artist=True,boxprops=dict(facecolor="Magenta"))

plt.title('Box Plots ')
plt.legend([a["boxes"][0], b["boxes"][0],c["boxes"][0],d["boxes"][0],e["boxes"][0]], ['ANNUAL', 'JAN-FEB','MAR-MAY','JUN-SEP','OCT-DEC'], loc='upper right')



plt.show()
