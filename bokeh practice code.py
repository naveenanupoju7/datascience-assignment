from bokeh.plotting import figure,output_file,show

import pandas as pd
import numpy as np
x=[1,2,3,4,5]
y=[5,6,7,8,9]
print(x.shape)
p=figure()
p.line(x,y)
show(p)
