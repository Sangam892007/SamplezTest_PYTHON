import pandas as pd
import plotly.figure_factory as pff
import statistics as st
import random 
import plotly.graph_objects as pg

data = pd.read_csv("../CSVFiles/studentMarks.csv")
Score = data["Math_score"].tolist()
def SamplingDistribution():
    dataSet = []
    for i in range(0,1000):
        index = random.randint(0,len(data)-1)
        val = Score[index]
        dataSet.append(val)

    Mean = st.mean(dataSet)
    return Mean

MeanList = []

for i in range(0,1000):
    SampleMean = SamplingDistribution()
    MeanList.append(SampleMean)

graph = pff.create_distplot([MeanList], ["Score of different students in math"], show_hist = False)


mean = st.mean(Score)
StandardDV = st.stdev(Score)
FinalMean = st.mean(MeanList)
FinalStandardDV = st.stdev(MeanList)

#print("Mean of the data is: {}\nStandard Deviation of the data is: {}".format(mean, StandardDV))
print(FinalMean, FinalStandardDV)

FirstRegionSTDVStart,FirstRegionSTDVEnd = FinalMean - FinalStandardDV,  FinalMean + FinalStandardDV
SecondRegionSTDVStart,SecondRegionSTDVEnd = FinalMean - 2*FinalStandardDV, FinalMean + 2*FinalStandardDV
ThirdRegionSTDVStart,ThirdRegionSTDVEnd = FinalMean - 3*FinalStandardDV, FinalMean + 3*FinalStandardDV

#FirstInterVention
FirstIntervention = pd.read_csv("../CSVFiles/intervention1.csv")
Score1 = FirstIntervention["Math_score"]

mean1 = st.mean(Score1)

#SecondInterVention
SecondIntervention = pd.read_csv("../CSVFiles/InterVention2.csv")
Score2 = SecondIntervention["Math_score"]

mean2 = st.mean(Score2)

#ThirdInterVention
ThirdIntervention = pd.read_csv("../CSVFiles/InterVention3.csv")
Score3 = ThirdIntervention["Math_score"]

mean3 = st.mean(Score3)

# graph.add_trace(pg.Scatter(x = [mean, mean], y = [0, 0.65], mode = "lines", name = "mean"))
# graph.add_trace(pg.Scatter(x = [FirstRegionSTDVStart, FirstRegionSTDVStart], y = [0,0.65], mode = "lines", name = "FirstRegionStart"))
# graph.add_trace(pg.Scatter(x = [FirstRegionSTDVEnd, FirstRegionSTDVEnd], y = [0,0.65], mode = "lines", name = "FirstRegionEnd"))
# graph.add_trace(pg.Scatter(x = [SecondRegionSTDVStart, SecondRegionSTDVStart], y = [0,0.65], mode = "lines", name = "SecondRegionStart"))
# graph.add_trace(pg.Scatter(x = [SecondRegionSTDVEnd, SecondRegionSTDVEnd], y = [0,0.65], mode = "lines", name = "SecondRegionEnd"))
graph.add_trace(pg.Scatter(x = [ThirdRegionSTDVStart, ThirdRegionSTDVStart], y = [0,0.65], mode = "lines", name = "ThirdRegionStart"))
graph.add_trace(pg.Scatter(x = [ThirdRegionSTDVEnd, ThirdRegionSTDVEnd], y = [0,0.65], mode = "lines", name = "ThirdRegionEnd"))
graph.add_trace(pg.Scatter(x = [mean1, mean1], y = [0,0.65], mode = "lines", name = "FirstInterVention"))
graph.add_trace(pg.Scatter(x = [mean2, mean2], y = [0,0.65], mode = "lines", name = "SecondInterVention"))
graph.add_trace(pg.Scatter(x = [mean3, mean3], y = [0,0.65], mode = "lines", name = "ThirdInterVention"))

graph.show()

zScore1 = (mean1 - FinalMean)/FinalStandardDV
zScore2 = (mean2 - FinalMean)/FinalStandardDV
zScore3 = (mean3 - FinalMean)/FinalStandardDV

print(zScore1, zScore2, zScore3)