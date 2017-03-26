from watson import findEntities
from searchTwitter import searchTwitter

def main():
  with open('billLinks.txt') as f:
	overall_reaction = 0
	counter = 0
	for line in f:
		print line
		wordList = findEntities(line)
		for word in wordList:
			print 'Word: ', word
			overall_reaction += searchTwitter(word)
			counter = counter + 1
		print counter
		print overall_reaction / counter
  
if __name__== "__main__":
  main()