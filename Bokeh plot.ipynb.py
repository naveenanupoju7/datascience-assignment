from bokeh.plotting import figure,output_file,show


import pandas as pd
import numpy as np
df=pd.read_excel(r'G:\TROP ICSU INTERNSHIP\India-Temp-2011.xlsx',engine='openpyxl')

x= list(df['YEAR'])
y1= list(df['ANNUAL'])
y2= list(df['JAN-FEB'])
y3= list(df['MAR-MAY'])
y4= list(df['JUN-SEP'])
y5= list(df['OCT-DEC'])
output_file('rod.html')
p=figure()
line_dash='solid'

p.line(x,y1,line_width=2,legend_label='ANNUAL',line_color='black')
p.line(x,y2,line_width=2,legend_label='JAN-FEB',color='blue')
p.line(x,y3,line_width=2,legend_label='MAR-MAY',line_color='green')
p.line(x,y4,line_width=2,legend_label='JUN-SEP',line_color='orange')
p.line(x,y5,line_width=2,legend_label='OCT-DEC',line_color='red')


show(p)
