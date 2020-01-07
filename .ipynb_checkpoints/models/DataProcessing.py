import pandas as pd
import numpy as np
from textblob import TextBlob
import pdb

top1KPosts = pd.read_csv("~/Documents/CMSC320/RedditDataScience/data/top1kPosts.csv")
controvertial1kPosts = pd.read_csv("~/Documents/CMSC320/RedditDataScience/data/controvertial1kPosts.csv")
controvertial1kPosts = controvertial1kPosts.drop("Unnamed: 0", axis=1)

for tableRow in top1KPosts.iterrows():
     top1KPosts.at[tableRow[0], "post_type"] = 1

for tableRow in controvertial1kPosts.iterrows():
    controvertial1kPosts.at[tableRow[0], "post_type"] = 0

dataSet = pd.concat([top1KPosts, controvertial1kPosts])
dataSet = dataSet.reset_index()
dataSet = dataSet.drop(["index", "id", "url", "created", "author"], axis=1)

uniqueSubReddits = {"subReddit" : []}

for tableRow in dataSet.iterrows():
    title = tableRow[1]["title"]
    subReddit = tableRow[1]["subreddit"]
    body = tableRow[1]["body"]

    originalContent = tableRow[1]["is_self"]
    nsfw = tableRow[1]["over_18"]
    spoiler = tableRow[1]["spoiler"]

    titleBlob = TextBlob(title)

    lenTitle = len(title)
    titleSentiment = titleBlob.sentiment.polarity
    titleSubjectivity = titleBlob.sentiment.subjectivity

    if subReddit not in uniqueSubReddits["subReddit"]:
        uniqueSubReddits["subReddit"].append(subReddit)

    lenBody = 0
    try:
        if np.isnan(body):
            body = ""
            lenBody = 0
    except:
        lenBody = len(body)

    dataSet.at[tableRow[0], "len_title"] = lenTitle
    dataSet.at[tableRow[0], "title_sentiment"] = titleSentiment
    dataSet.at[tableRow[0], "title_subjectivity"] = titleSubjectivity
    dataSet.at[tableRow[0], "body"] = body
    dataSet.at[tableRow[0], "len_body"] = lenBody
    
    dataSet.at[tableRow[0], "is_oc"] = 0
    if originalContent:
        dataSet.at[tableRow[0], "is_oc"] = 1


    dataSet.at[tableRow[0], "is_nsfw"] = 0
    if nsfw:
        dataSet.at[tableRow[0], "is_nsfw"] = 1

    dataSet.at[tableRow[0], "is_spoiler"] = 0
    if spoiler:
        dataSet.at[tableRow[0], "is_spoiler"] = 1

dataSet = dataSet.drop(["is_self", "over_18", "spoiler",], axis=1)
subRedditLookUp = pd.DataFrame(uniqueSubReddits)
subRedditOneHotEncoding = pd.get_dummies(subRedditLookUp)

dataSet.to_csv("dataSet.csv", index=False)
subRedditLookUp.to_csv("subRedditLookUp.csv", index=False)
subRedditOneHotEncoding.to_csv("subRedditOneHotEncoding.csv", index=False)    