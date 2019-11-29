import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn.linear_model import Lasso
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
testOutput = [i[0] for i in testOutput]

class PredictRedditPost(nn.Module):
    def __init__(self):
        super(PredictRedditPost, self).__init__()
        self.linearClassifier = nn.Sequential(nn.Linear(354, 128), nn.ReLU(), nn.Linear(128, 64), nn.ReLU(), nn.Linear(64, 1))
        self.sigmoid = nn.Sigmoid()

    def forward(self, featureVector):
        return self.sigmoid(self.linearClassifier(featureVector))


LR = 1e-3
WEIGHTDECAY=0.0005
EPOCH = 10

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model = PredictRedditPost()
model.to(device)
optimizer = optim.Adam(model.parameters(), lr=LR, weight_decay=WEIGHTDECAY)
BCEL = nn.BCELoss()

TestingAccuracy = []
TrainingLoss = []
for STEP in range(EPOCH):
    epochLoss = 0
    for batchCount, data in tqdm(enumerate(zip(trainInput, trainOutput)), total=len(trainInput)):
        handCraftedFeatures, postType = data

        handCraftedFeatures = torch.tensor(handCraftedFeatures)
        postType = torch.tensor(postType)

        handCraftedFeatures = handCraftedFeatures.to(device)
        postType = postType.to(device)

        predictedPostType = model(handCraftedFeatures)

        optimizer.zero_grad()
        Loss = BCEL(predictedPostType, postType)
        epochLoss = epochLoss + Loss.item()

        Loss.backward()
        optimizer.step()

    print("Epoch Loss: " + str(epochLoss / batchCount))
    TrainingLoss.append(epochLoss / batchCount)

    testInput = torch.tensor(testInput)
    testInput = testInput.to(device)
    predictedPostType = torch.round(model(testInput))

    predictedPostType = [int(i[0]) for i in predictedPostType.tolist()]
    Accuracy = metrics.accuracy_score(testOutput, predictedPostType)
    print("Accuracy: " + str(Accuracy))
    TestingAccuracy.append(Accuracy)

sns.lineplot(x=np.array([x for x in range(EPOCH)]), y=np.array(TrainingLoss))
plt.title("Loss Per Epoch")
plt.xlabel("Epoch #")
plt.ylabel("Loss")
plt.show()
plt.clf()

sns.lineplot(x=np.array([x for x in range(EPOCH)]), y=np.array(TestingAccuracy))
plt.title("Accuracy Per Epoch")
plt.xlabel("Epoch #")
plt.ylabel("Accuracy")
plt.show()
plt.clf()

