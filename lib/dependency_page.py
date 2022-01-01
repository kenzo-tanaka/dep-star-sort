import requests
from bs4 import BeautifulSoup
import configparser
config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')

class DependencyPage:
	def __init__(self, url, min_star) -> None:
		self.url = url
		self.min_star = min_star

	def popular_repos(self):
		repositories = []
		for box in self.__repositories():
			if self.__star_count(box) >= self.min_star:
				repositories.append(
					{ 
						config_ini['DEFAULT']['Repository']: self.__repository_url(box),
						config_ini['DEFAULT']['Star']: self.__star_count(box) 
					}
				)
		return(repositories)

	def next_page_link(self):
		page_links = self.__pagination_links()
		if len(page_links) == 2:
				return(page_links[1]['href'])
		elif len(page_links) == 1 and page_links[0].text == 'Next':
				return(page_links[0]['href'])
		else:
				return(None)
		
	def soup(self):
		html = requests.get(self.url)
		return(BeautifulSoup(html.content, "html.parser"))

	def __repositories(self):
		return(self.soup().find_all(class_="Box-row"))

	def __star_count(self, box):
		return(int(box.find(class_='octicon-star').parent.text.replace('\n','').replace(',', '').strip()))
	
	def __repository_url(self, box):
		return('https://github.com' + box.find_all('a')[1]['href'])

	def __pagination_links(self):
		return(self.soup().find(attrs={"data-test-selector": "pagination"}).find_all('a'))

	def __prev_link_present(self):
		return(len(self.__pagination_links()) == 2)

	def __only_next_link_present(self):
		return(len(self.__pagination_links()) == 1 and self.__pagination_links()[0].text == 'Next')
