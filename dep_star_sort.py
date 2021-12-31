import requests
from bs4 import BeautifulSoup

class DepStarSort:
    def dep_url(self, url):
        return(f"{url}/network/dependents")
    
    def get_html(self):
        url = self.dep_url("https://github.com/github/view_component")
        html = requests.get(url)
        soup = BeautifulSoup(html.content, "html.parser")
        return(soup)
