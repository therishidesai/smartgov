import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as \
    features


natural_language_understanding = NaturalLanguageUnderstandingV1 (
    version='2017-02-27',
    username='8e51b75b-34db-49fb-8956-45460617145b',
    password='gbGtti8UPm4Y'
)

def findEntities(link):
	response = natural_language_understanding.analyze(
	    url = link,
	    features = [features.Keywords(), features.Entities()]
	)

	f = open('words.txt', 'w')

	total = []

	for keyword in response["keywords"]:
		if keyword["relevance"] < 0.5:
			break
		total.append(keyword["text"])

	for entities in response["entities"]:
		if entities["relevance"] < 0.5:
			break
		total.append(entities["text"])

	print total
	return total

def findSentiment(totalTweets):
	print 'hi'
	sentiment = natural_language_understanding.analyze(
		text = totalTweets,
		features = [features.Sentiment()]
	)
	print sentiment
	return sentiment['sentiment']['document']['score']