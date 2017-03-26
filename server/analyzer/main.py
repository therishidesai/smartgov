from watson import findKeyWords
from searchTwitter import searchTwitter

def main():
	output = open('sentiments.txt', 'w');

	with open('billLinks.txt') as f:
		total_reaction = []
		for line in f:
			print line
			wordList = findKeyWords(line)
			print "# of Words: ", len(wordList)
			print wordList
			for word in wordList:
				print 'Word: ', word
				temp = searchTwitter(word) # could be false because searchTwitter returned nothing
				if temp == False:
					continue
				total_reaction.extend(temp)

			total_reaction.sort()
			print "# of reactions: ", len(total_reaction)
			print total_reaction
			print float(sum(total_reaction) / len(total_reaction))
			output.write(str(float(sum(total_reaction) / len(total_reaction))))


if __name__ == "__main__":
	main()