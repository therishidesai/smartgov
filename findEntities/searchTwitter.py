import twitter
from watson import findSentiment

api = twitter.Api(consumer_key = 'EjLOdtH7Gmr0FEpwnVSNojkuS',
				  consumer_secret = 'cV0eXVgH6nU5e9PmS7G0IhlD5CievQiKzEmdtMEyrg2CPTwtmD',
				  access_token_key = '1592933448-zjL4coZd83Bjmsg0xNEnPPuUAEGI1Kkd45UtGjo',
				  access_token_secret = 'UhvYQ6hBZ1NIOSMV7gGbx9smr2ntQ7OMBPepgVJ7l0hhs')

def searchTwitter(word):
	'''print word
	word = 'federal disaster declarations'
	print word'''
	results = api.GetSearch(word)
	total = ''
	for tweet in results:
		total += tweet.text + '\n'

	print total
	return findSentiment(total)
	