import requests
from bs4 import BeautifulSoup

class DepStarSort:
    def dep_url(self, url):
        return(f"{url}/network/dependents")

    def response_code(self):
        # TODO: urlをinitializeで受け取る
        url = self.dep_url("https://github.com/github/view_component")
        return(requests.get(url).status_code)
    
    # WIP
    # def get_html(self):
    #     url = self.dep_url("https://github.com/github/view_component")
    #     html = requests.get(url)
    #     soup = BeautifulSoup(html.content, "html.parser")
    #     return(soup.find('title'))
