import pandas
import matplotlib.pyplot as plt

deathXDates = pandas.read_csv("Deaths1.csv", usecols=[0])
datasetDeaths = pandas.read_csv("Deaths1.csv", usecols=[2])

print("Len deaths ",len(deathXDates))
datasetCases = pandas.read_csv("Number of Cases.csv", usecols=[1], engine='python')
print("Len new cases ",len(datasetCases))
print("DatasetCases : ",datasetCases)


file = "summaryDeath.txt"
fileOpen = open(file, 'w')
fileOpen.write(str(datasetDeaths.describe()))

file = "summaryNewCases.txt"
fileOpen = open(file, 'w')
fileOpen.write(str(datasetCases.describe()))


def produceGraph(data, title, xLabel, yLabel):
    plt.plot(data)
    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.show()

#produceGraph(datasetDeaths, "Number of Deaths", "Days", "Number of Deaths")
produceGraph(datasetCases, "Number of New Cases", "Days", "Number of Cases")



