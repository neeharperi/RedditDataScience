import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from scipy import stats
import sklearn.metrics as metrics
from tqdm import tqdm
import numpy as np
import pdb

#Implementation by https://gist.github.com/brentp/5355925
class LinearRegression(LinearRegression): #Modify built-in sklearn Linear Regression to return t-test and p values
    def __init__(self, *args, **kwargs):
        super(LinearRegression, self).__init__(*args, **kwargs)

    def fit(self, X, y, n_jobs=1):
        self = super(LinearRegression, self).fit(X, y, n_jobs)

        sse = np.sum((self.predict(X) - y) ** 2, axis=0) / float(X.shape[0] - X.shape[1])
        se = np.array([np.sqrt(np.diagonal(sse[i] * np.linalg.inv(np.dot(X.T, X)))) for i in range(sse.shape[0])])
        self.t = self.coef_ / se #Calculate T Test (Large magnitude is significant)
        self.p = 2 * (1 - stats.t.cdf(np.abs(self.t), y.shape[0] - X.shape[1])) #Calculate P Value (Value < 0.05 is significant)
        
        return self

dataSet = pd.read_csv("~/Documents/CMSC320/RedditDataScience/data/dataSet.csv")
subRedditOneHotEncoding = pd.read_csv("~/Documents/CMSC320/RedditDataScience/data/subRedditOneHotEncoding.csv")

inputData = []
outputData = []

for tableRow in dataSet.iterrows():
    subReddit = tableRow[1]["subreddit"]
    SR_oneHotEncoding = subRedditOneHotEncoding["subReddit_" + subReddit].to_list()
    numComments = tableRow[1]["num_comments"]
    originalContent = tableRow[1]["is_self"]
    nsfw = tableRow[1]["over_18"]
    spoiler = tableRow[1]["spoiler"]
    post_type = tableRow[1]["post_type"]
    lenTitle = tableRow[1]["len_title"]
    titleSentiment = tableRow[1]["title_sentiment"]
    titleSubjectivity = tableRow[1]["title_subjectivity"]
    lenBody = tableRow[1]["len_body"]

    ratio = tableRow[1]["upvote_ratio"]

    input = SR_oneHotEncoding + [lenTitle, titleSentiment, titleSubjectivity, lenBody, numComments, originalContent, nsfw, spoiler, post_type]
    output = [ratio]

    
    pdb.set_trace()
