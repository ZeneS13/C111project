import pandas as pd
import csv
import plotly.figure_factory as ff 
import statistics as st
import random
import plotly.graph_objects as go

df=pd.read_csv("School1.csv")
data=df["Math_score"].tolist()

#fig=ff.create_distplot([data],["Math_score"],show_hist=False)
#fig.show()

popMean=st.mean(data)
popStd=st.stdev(data)
print("Std of pop dist: ",popStd)
print("mean of pop dist: ",popMean)

def randSetOfMean(counter):
    datas=[]
    for i in range(0,counter):
        randIndex=random.randint(0,len(data)-1)
        val=data[randIndex]
        datas.append(val)
    mean=st.mean(datas)
    return mean

meanList=[]
for i in range(0,100):
    meansets=randSetOfMean(30)
    meanList.append(meansets)

stddev=st.stdev(meanList)
meanLmean=st.mean(meanList)


print("Std of sampling dist: ",stddev)
print("mean of sampling dist: ",meanLmean)

firStdStart, firStdEnd=meanLmean-stddev,meanLmean+stddev
secStdStart, secStdEnd=meanLmean-(stddev*2),meanLmean+(stddev*2)
thrStdStart, thrStdEnd=meanLmean-(stddev*3),meanLmean+(stddev*3)




#intervertion  1 mean calc
df1=pd.read_csv("school_1_Sample.csv")
data1=df1["Math_score"].tolist()
mean1=st.mean(data1)
""" zscore=(meanLmean-mean1)/stddev

print("z score is ",zscore)
fig=ff.create_distplot([meanList],["sampling mean"],show_hist=False)
fig.add_trace(go.Scatter(x=[meanLmean,meanLmean],y=[0,0.2],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[mean1,mean1],y=[0,0.2],mode="lines",name="mean sample"))
fig.add_trace(go.Scatter(x=[firStdEnd,firStdEnd],y=[0,0.2],mode="lines",name="stdev 1"))
fig.add_trace(go.Scatter(x=[secStdEnd,secStdEnd],y=[0,0.2],mode="lines",name="stdev 2"))
fig.add_trace(go.Scatter(x=[thrStdEnd,thrStdEnd],y=[0,0.2],mode="lines",name="stdev 3"))


fig.show() """


#intervention 2 mean calc
df2=pd.read_csv("data2.csv")
data2=df2["Math_score"].tolist()
mean2=st.mean(data2)
zscore2=(meanLmean-mean2)/stddev


print("z score is ",zscore2)
fig=ff.create_distplot([meanList],["sampling mean"],show_hist=False)
fig.add_trace(go.Scatter(x=[meanLmean,meanLmean],y=[0,0.2],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[mean2,mean2],y=[0,0.2],mode="lines",name="mean sample2"))
fig.add_trace(go.Scatter(x=[firStdEnd,firStdEnd],y=[0,0.2],mode="lines",name="stdev 1"))
fig.add_trace(go.Scatter(x=[secStdEnd,secStdEnd],y=[0,0.2],mode="lines",name="stdev 2"))
fig.add_trace(go.Scatter(x=[thrStdEnd,thrStdEnd],y=[0,0.2],mode="lines",name="stdev 3"))


fig.show()




#intervention 3 mean calc
df3=pd.read_csv("data3.csv")
data3=df3["Math_score"].tolist()
mean3=st.mean(data3)
zscore=(meanLmean-mean3)/stddev

print("z score is ",zscore)
fig=ff.create_distplot([meanList],["sampling mean"],show_hist=False)
fig.add_trace(go.Scatter(x=[meanLmean,meanLmean],y=[0,0.2],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[mean3,mean3],y=[0,0.2],mode="lines",name="mean sample"))
fig.add_trace(go.Scatter(x=[firStdEnd,firStdEnd],y=[0,0.2],mode="lines",name="stdev 1"))
fig.add_trace(go.Scatter(x=[secStdEnd,secStdEnd],y=[0,0.2],mode="lines",name="stdev 2"))
fig.add_trace(go.Scatter(x=[thrStdEnd,thrStdEnd],y=[0,0.2],mode="lines",name="stdev 3"))


fig.show()
