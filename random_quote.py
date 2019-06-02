from bs4 import BeautifulSoup
import requests
from random import randint

def get_random_quote():
	page_num = str(randint(1, 55807))
	# print(page_num)
	source = requests.get('https://www.goodreads.com/quotes/tag/inspirational?page=' + page_num).text
	soup = BeautifulSoup(source, 'lxml')
	list_of_quotes = soup.find_all('div', class_='quoteText')

	# print(i)
	list_of_author = soup.find_all('span', class_='authorOrTitle')

	i = randint(0, 29)

	quote = list_of_quotes[i].text
	author = list_of_author[i].text

	x = quote.find('―')
	quote = quote[:x]
	quote = quote.replace('\n', '')
	quote = quote.replace('  ', '')
	author = author.replace('\n', '')
	author = author.replace('  ', ' ')
	author = author.replace(',', '')

	final_comment = '*' + quote + '*' + ' ―' + author
	# print(final_comment)

	return final_comment

# get_random_quote()