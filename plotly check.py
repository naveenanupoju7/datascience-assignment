import plotly.express as px
import pandas as pd
  
df=pd.read_excel(r'G:\TROP ICSU INTERNSHIP\India-Temp-2011.xlsx',usecols=['ANNUAL','JAN-FEB','MAR-MAY','JUN-SEP','OCT-DEC'],engine='openpyxl')
df.shape
print(df.describe())
print(df.quality.unique())
#df.quality.value_counts()
fig = px.box(df,points="all",title="Boxplot ",labels={"value":"Temperature(°C)","variable":"Time range"})

fig.show()
