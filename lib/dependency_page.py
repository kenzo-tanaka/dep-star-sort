import requests
from bs4 import BeautifulSoup

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
						'repo': self.__repository_url(box),
						'star': self.__star_count(box) 
					}
				)
		return(repositories)
		
	def soup(self):
		html = requests.get(self.url)
		return(BeautifulSoup(html.content, "html.parser"))

	def __repositories(self):
		return(self.soup().find_all(class_="Box-row"))

	def __star_count(self, box):
		return(int(box.find(class_='octicon-star').parent.text.replace('\n','').replace(',', '').strip()))
	
	def __repository_url(self, box):
		return('https://github.com' + box.find_all('a')[1]['href'])
