from bokeh.plotting import BoxPlot, output_notebook, show 
import pandas as pd
df=pd.read_excel(r'G:\TROP ICSU INTERNSHIP\India-Temp-2011.xlsx',engine='openpyxl')
p = BoxPlot(df, values = "Protein", label = "Category",  
            color = "yellow", title = "Protein Summary (grouped by category)", 
             legend = "top_right") 
  
# show the results 
show(p) 
