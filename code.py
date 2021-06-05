import csv 
import pandas  as pd
import plotly.graph_objects as go
import plotly.figure_factory as ff
import statistics
import random

df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()
fig=ff.create_distplot([data],["reading_time"],show_hist=False)
fig.show()

mean=statistics.mean(data)
sd=statistics.stdev(data)
print("the mean of population is: ",mean)
print("The sd of population is: ",sd)
def randomSetOfMeans(counter):
  dataset=[]
  for i in range(0,counter):
    random_index=random.randint(0,len(data)-1)
    value=data[random_index]
    dataset.append(value)
  mean=statistics.mean(dataset)
  return mean

meanList=[]
for i in range(0,100):
  setOfMean=randomSetOfMeans(30)
  meanList.append(setOfMean)
ssd=statistics.stdev(meanList)
smean=statistics.mean(meanList)
print("The Sampling sd is: ",ssd)
print("the sampling mean is: ",smean)
sfig=ff.create_distplot([meanList],["reading_time"],show_hist=False)
sfig.add_trace(go.Scatter(x=[smean,smean],y=[0,0.3],mode="lines",name="Sampling Means"))
sfig.show()
f_sd_start,f_sd_end=smean-ssd,smean+ssd
s_sd_start,s_sd_end=smean-(2*ssd),smean+(2*ssd)
t_sd_start,t_sd_end=smean-(3*ssd),smean+(3*ssd)
sfig=ff.create_distplot([meanList],["reading_time"],show_hist=False)
sfig.add_trace(go.Scatter(x=[smean,smean],y=[0,0.17],mode="lines",name="Sampling Means"))
sfig.add_trace(go.Scatter(x=[f_sd_start,f_sd_start],y=[0,0.17],mode="lines",name="sd 1"))
sfig.add_trace(go.Scatter(x=[f_sd_end,f_sd_end],y=[0,0.17],mode="lines",name="sd 1"))
sfig.add_trace(go.Scatter(x=[s_sd_start,s_sd_start],y=[0,0.17],mode="lines",name="sd 2"))
sfig.add_trace(go.Scatter(x=[s_sd_end,s_sd_end],y=[0,0.17],mode="lines",name="sd 2"))
sfig.add_trace(go.Scatter(x=[t_sd_start,t_sd_start],y=[0,0.17],mode="lines",name="sd 3"))
sfig.add_trace(go.Scatter(x=[t_sd_end,t_sd_end],y=[0,0.17],mode="lines",name="sd 3"))
sfig.show()
df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()
meanOfSample1=statistics.mean(data)
sfig=ff.create_distplot([meanList],["reading_time"],show_hist=False)
sfig.add_trace(go.Scatter(x=[smean,smean],y=[0,0.3],mode="lines",name="Sampling Means"))
sfig.add_trace(go.Scatter(x=[meanOfSample1,meanOfSample1],y=[0,0.17],mode="lines",name=" Means of Sample one"))
sfig.add_trace(go.Scatter(x=[f_sd_end,f_sd_end],y=[0,0.17],mode="lines",name="sd 1"))

sfig.show()

# df=pd.read_csv("data3.csv")
# data=df["reading_time"].tolist()
# meanOfSample3=statistics.mean(data)
# sfig=ff.create_distplot([meanList],["reading_time"],show_hist=False)
# sfig.add_trace(go.Scatter(x=[smean,smean],y=[0,0.3],mode="lines",name="Sampling Means"))
# sfig.add_trace(go.Scatter(x=[meanOfSample3,meanOfSample3],y=[0,0.17],mode="lines",name=" Means of Sample three"))
# sfig.add_trace(go.Scatter(x=[t_sd_end,t_sd_end],y=[0,0.17],mode="lines",name="sd 3"))

# sfig.show()
zscore=(meanOfSample1-smean)/ssd
print("the zscore is: ",zscore)