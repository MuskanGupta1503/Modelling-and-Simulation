# Importing the matplotlb.pyplot 
import matplotlib.pyplot as plt 
import numpy as np
import random
from numpy import random

# y-axis
vehicle_no = [ 1 , 2 , 3 , 4 , 5 , 6]

# gannt chart content
# parking = [10, 20, 15, 30, 25, 40]
parking = []
for i in range(0,6):
    n = random.choice([10,15,20,25,30,35,40])
    parking.append(n)
print("Parking Time: " + str(parking))

# loading = [100, 70, 70, 50, 80, 90]  
loading = []
for i in range(0,6):
    n = random.randint(5,10)
    n=n*10
    loading.append(n)
print("Loading Time: "+str(loading))

# TRIP1
# moving1 = [160, 270, 250, 190, 250, 180]
moving1=[]
for i in range(0,6):
    n = random.randint(15,30)
    n=n*10
    moving1.append(n)
print(moving1)

# unloading1 = [40, 30, 40, 50, 35, 40]
unloading1=[]
for i in range(0,6):
    n = random.randint(3,5)
    n=n*10
    unloading1.append(n)
print(unloading1)

# idle1=[25, 20, 30, 100, 0, 60]
idle1=[]
for i in range(0,6):
      n=random.choice([25, 20, 30, 100, 0, 60])
      idle1.append(n)
print("Idle time 1 is: " + str(idle1))

# Add to plot for trip1
add1=list(np.add(parking,loading))
add2=list(np.add(add1,moving1))
add3=list(np.add(add2,unloading1))


# TRIP2
# moving2 = [70, 30, 240, 200, 150, 210]
moving2=[]
for i in range(0,6):
    n = random.randint(3,25)
    n=n*10
    moving2.append(n)
print("Moving 2: "+str(moving2))
  
# unloading2 = [40, 20, 25, 50, 30, 20]
unloading2=[]
for i in range(0,6):
    n = random.randint(2,5)
    n=n*10
    unloading2.append(n)
print("Unloading 2: "+str(unloading2))

idle2=[0, 0, 10, 120, 0, 60]
print("Idle 2 is :" + str(idle2))

# Add to plot for trip2
add4=list(np.add(add3,idle1))
add5=list(np.add(add4,moving2))
add6=list(np.add(add5,unloading2))


# TRIP3
# moving3 = [140, 130, 60, 20, 0, 0]
moving3 = random.choice(
      [0, 70, 60, 130, 140], 
      # p=[0.25, 0.18 , 0.19 , 0.19, 0.19  ], 
      size=(6)
      )
print("Moving 3 is :" + str(moving3))

# unloading3 = [20, 40, 30, 10, 0, 0]
unloading3=[]
for i in range(0,6):
      if(moving3[i]==0):
            unloading3.append(0)
      else:
            n = random.randint(2,5)
            n=n*10
            unloading3.append(n)     
print("Unloading 3: "+str(unloading3))

# idle3=[195, 170, 30, 80, 230, 100]

# Add to plot for trip3
add7=list(np.add(add6,idle2))
add8=list(np.add(add7,moving3))
add9=list(np.add(add8,unloading3))
# print(add9)

#Idle time 3
idle3=[]
for i in range(0,6):
      n=add9[i]
      if(n<=950):
            idle3.append(950-n)
      else:
            idle3.append(0)
print("Idle 3: " + str(idle3))

# GANNT CHART MAKING
plt.barh(vehicle_no, parking, color="grey")  
# careful: notice "bottom" parameter became "left"
plt.barh(vehicle_no, loading, left=parking, color="green")

#plotting trip 1
plt.barh(vehicle_no, moving1, left=add1, color="blue") 
plt.barh(vehicle_no, unloading1, left=add2, color="red") 
plt.barh(vehicle_no, idle1, left=add3, color="grey") 

#plotting trip 2
plt.barh(vehicle_no, moving2, left=add4, color="blue") 
plt.barh(vehicle_no, unloading2, left=add5, color="red") 
plt.barh(vehicle_no, idle2, left=add6, color="grey")

#plotting trip 3
plt.barh(vehicle_no, moving3, left=add7, color="blue") 
plt.barh(vehicle_no, unloading3, left=add8, color="red") 
plt.barh(vehicle_no, idle3, left=add9, color="grey") 

# we also need to switch the labels
plt.xlabel('Time in mins')  
plt.ylabel('Vehicle Number')

plt.show()
# plt.savefig('gantt.png')
print("\n")

# Report Generation Program
def ReportGeneration():

      # IDLE time for all vehicles
      idle_list = [] 
      for i in range(0, len(parking)): 
            idle_list.append(parking[i] + 
            idle1[i] + 
            idle2[i] 
            # idle3[i]
            )
      
      print("Idle time:")
      for i in range(0,len(parking)):
            print("Vehicle no " + str(i+1)+ ": " +str(idle_list[i]))
      print("\n")

      #USED time for all vehicles
      used_list=[]
      for i in range(0, len(parking)): 
            used_list.append(loading[i]+
            moving1[i]+
            unloading1[i]+
            moving2[i]+
            unloading2[i]+
            moving3[i]+
            unloading3[i]
            )
      print("Used time:")
      for i in range(0,len(parking)):
            print("Vehicle no " + str(i+1)+ ": " +str(used_list[i]))
      # print(used_list)
      print("\n")

      # ANALYSIS for all vehicles
      print("Analysis For all vehicles")
      # Total Idle Time
      sum_idle=0
      for i in range(0,len(parking)):
            sum_idle=sum_idle+idle_list[i]
      print("Total Idle Time: " 
      + str(sum_idle))

      # Total Used Time
      sum_used=0
      for i in range(0,len(parking)):
            sum_used=sum_used+used_list[i]
      print("Total Used Time: " 
      + str(sum_used))

      #Average Loading Time
      avg_loading=0;
      for i in range(0, len(parking)): 
            avg_loading=loading[i]+avg_loading
      avg_loading=avg_loading/6
      print("Average Loading Time: " + str(avg_loading))

ReportGeneration()

# https://futurestud.io/tutorials/matplotlib-stacked-bar-plots
# https://matplotlib.org/3.1.3/gallery/lines_bars_and_markers/horizontal_barchart_distribution.html
