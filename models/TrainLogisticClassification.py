import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn.linear_model import LogisticRegression
from scipy import stats
import sklearn.metrics as metrics
from tqdm import tqdm
from sklearn.model_selection import train_test_split
import numpy as np
import pdb

dataSet = pd.read_csv("~/Documents/CMSC320/RedditDataScience/data/dataSet.csv")
subRedditOneHotEncoding = pd.read_csv("~/Documents/CMSC320/RedditDataScience/data/subRedditOneHotEncoding.csv")

inputData = []
outputData = []

for tableRow in dataSet.iterrows():
    subReddit = tableRow[1]["subreddit"]
    SR_oneHotEncoding = subRedditOneHotEncoding["subReddit_" + subReddit].to_list()
    numComments = tableRow[1]["num_comments"]
    originalContent = tableRow[1]["is_oc"]
    nsfw = tableRow[1]["is_nsfw"]
    spoiler = tableRow[1]["is_spoiler"]
    lenTitle = tableRow[1]["len_title"]
    titleSentiment = tableRow[1]["title_sentiment"]
    titleSubjectivity = tableRow[1]["title_subjectivity"]
    lenBody = tableRow[1]["len_body"]
    ratio = tableRow[1]["upvote_ratio"]

    post_type = tableRow[1]["post_type"]

    inputData.append(SR_oneHotEncoding + [lenTitle, titleSentiment, titleSubjectivity, lenBody, numComments, originalContent, nsfw, spoiler, ratio])
    outputData.append([post_type])


trainInput, testInput, trainOutput, testOutput = train_test_split(inputData, outputData, test_size=0.1)
ratioRegression = LogisticRegression().fit(np.array(trainInput), np.array(trainOutput))
predictedOutput = ratioRegression.predict(np.array(testInput))
modelPerformance = []

testOutput = [i[0] for i in testOutput]
predictedOutput = predictedOutput.tolist()

for i, output in enumerate(zip(testOutput, predictedOutput)):
    target, prediction = output
    modelPerformance.append({"Example" : i, "True Class" : target , "Predicted Class" : prediction})
    
modelPerformance = pd.DataFrame(modelPerformance)
Accuracy = metrics.accuracy_score(testOutput, predictedOutput)
print("Accuracy: " + str(Accuracy))