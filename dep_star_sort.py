import requests
from bs4 import BeautifulSoup

class DepStarSort:
    def __init__(self, github_url) -> None:
        self.github_url = github_url

    def dep_url(self):
        return(f"{self.github_url}/network/dependents")

    def response_code(self):
        return(requests.get(self.dep_url()).status_code)
    
    # WIP
    # def get_html(self):
    #     url = self.dep_url("https://github.com/github/view_component")
    #     html = requests.get(url)
    #     soup = BeautifulSoup(html.content, "html.parser")
    #     return(soup.find('title'))
