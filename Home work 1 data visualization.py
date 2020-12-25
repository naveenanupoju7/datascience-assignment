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

#date_format=mpl_dates.DateFormatter('%Y')  #formatting the dates with month,date,year

#plt.gca().xaxis.set_major_formatter(date_format)

plt.scatter(y3,y4)
plt.show()

plt.plot(x,y1,linestyle='solid',label='ANNUAL',color='Black')
plt.legend(loc='lower right',fontsize='8')
plt.xlabel('YEAR')
plt.ylabel('TEMPERATURE')
plt.title('ANNUAL')
plt.show()
plt.plot(x,y2,linestyle='solid',label='JAN-FEB',color='Green')
plt.legend(loc='lower right',fontsize='8')
plt.xlabel('YEAR')
plt.ylabel('TEMPERATURE')
plt.title('JAN-FEB')
plt.show()
plt.plot(x,y3,linestyle='solid',label='MAR-MAY',color='Blue')
plt.legend(loc='lower right',fontsize='8')
plt.xlabel('YEAR')
plt.ylabel('TEMPERATURE')
plt.title('MAR-MAY')
plt.show()
plt.plot(x,y4,linestyle='solid',label='JUN-SEP',color='Red')
plt.legend(loc='lower right',fontsize='8')
plt.xlabel('YEAR')
plt.ylabel('TEMPERATURE')
plt.title('JUN-SEP')
plt.show()
plt.plot(x,y5,linestyle='solid',label='OCT-DEC',color='Magenta')
plt.legend(loc='lower right',fontsize='8')
plt.xlabel('YEAR')
plt.ylabel('TEMPERATURE')
plt.title('OCT-DEC')
plt.show()


a=plt.boxplot(df.ANNUAL,1,showmeans=True,autorange=True,positions=[1],patch_artist=True,boxprops=dict(facecolor="Black"))
plt.ylabel('TEMPERATURE')
plt.title('ANNUAL')
plt.show()
median=np.median(y1)
print(median)

b=plt.boxplot(df['JAN-FEB'],1,showmeans=True,autorange=True,positions=[2],patch_artist=True,boxprops=dict(facecolor="Green"))
plt.ylabel('TEMPERATURE')
plt.title('JAN-FEB')
plt.show()
median=np.median(y2)
print(median)
c=plt.boxplot(df['MAR-MAY'],1,showmeans=True,autorange=True,positions=[3],patch_artist=True,boxprops=dict(facecolor="Blue"))
plt.ylabel('TEMPERATURE')
plt.title('MAR-MAY')
plt.show()
median=np.median(y3)
print(median)
d=plt.boxplot(df['JUN-SEP'],1,showmeans=True,autorange=True,positions=[4],patch_artist=True,boxprops=dict(facecolor="Red"))
plt.ylabel('TEMPERATURE')
plt.title('JUN-SEP')
plt.show()
median=np.median(y4)
print(median)
e=plt.boxplot(df['OCT-DEC'],1,showmeans=True,autorange=True,positions=[5 ],patch_artist=True,boxprops=dict(facecolor="Magenta"))
plt.ylabel('TEMPERATURE')
plt.title('OCT-DEC')
plt.show()
median=np.median(y5)
print(median)
plt.legend([a["boxes"][0], b["boxes"][0],c["boxes"][0],d["boxes"][0],e["boxes"][0]], ['ANNUAL', 'JAN-FEB','MAR-MAY','JUN-SEP','OCT-DEC'], loc='upper right')



plt.show()


