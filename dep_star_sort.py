import requests
from bs4 import BeautifulSoup

class DepStarSort:
    def __init__(self, github_url) -> None:
        self.github_url = github_url

    def dep_url(self):
        return(f"{self.github_url}/network/dependents")

    def response_code(self):
        return(requests.get(self.dep_url()).status_code)
    
    def get_repo_href(self):
        html = requests.get(self.dep_url())
        soup = BeautifulSoup(html.content, "html.parser")
        return(soup.find(class_="Box-row").find_all('a')[1]['href'])

    def get_repo_star(self):
        html = requests.get(self.dep_url())
        soup = BeautifulSoup(html.content, "html.parser")
        return(int(soup.find(class_="Box-row").find(class_='octicon-star').parent.text.replace('\n','').strip()))
