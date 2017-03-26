import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as \
	features


natural_language_understanding = NaturalLanguageUnderstandingV1 (
	version='2017-02-27',
	username='2c7840f9-8c5b-4126-8314-1f7a5b4034bd',
	password='ofZZiD1tGNmx'
)

def findKeyWords(link):
	response = natural_language_understanding.analyze(
		url = link,
		features = [features.Keywords(), features.Entities()]
	)

	total = []
	for keyword in response["keywords"]:
		if keyword["relevance"] < 0.5:
			break
		total.append(keyword["text"])

	for entities in response["entities"]:
		if entities["relevance"] < 0.5:
			break
		total.append(entities["text"])

	return total

def findSentiment(tweets):
	if tweets == 0:
		return False
	tweets = tweets.replace('Affordable', '')
	sentiment = natural_language_understanding.analyze(
		text = tweets,
		features = [features.Sentiment()]
	)
	print sentiment['sentiment']['document']['score'], tweets
	return sentiment['sentiment']['document']['score']

#findSentiment("#KillTheBill")