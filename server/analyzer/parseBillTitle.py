#not working

#from lxml import html
import requests

def getBillTitle(url):
	main_page = requests.get(url)
	main_page_tree = html.fromstring(main_page.content)

	title = main_page_tree.xpath('//h1[@class="legDetail"]/text()')
	return title

output = open('sentiments.txt', 'w');
output.write(str(3))