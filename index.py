# Importing the matplotlb.pyplot 
import matplotlib.pyplot as plt 
import numpy as np

year = [2014, 2015, 2016, 2017, 2018, 2019]  
tutorial_premium = [0, 0, 13, 56, 39, 14]
tutorial_public = [39, 117, 98, 54, 28, 15]  
tutorial_public1 = [39, 117, 98, 54, 28, 15]  

b_tp1=list(np.add(tutorial_premium,tutorial_public))

plt.barh(year, tutorial_premium, color="#f3e151")  
# careful: notice "bottom" parameter became "left"
plt.barh(year, tutorial_public, left=tutorial_premium, color="#6c3376")
plt.barh(year, tutorial_public1, left=b_tp1, color="#f3e151") 

# we also need to switch the labels
plt.xlabel('Number of futurestud.io Tutorials')  
plt.ylabel('Year')

plt.show()  


# https://futurestud.io/tutorials/matplotlib-stacked-bar-plots
# https://matplotlib.org/3.1.3/gallery/lines_bars_and_markers/horizontal_barchart_distribution.html