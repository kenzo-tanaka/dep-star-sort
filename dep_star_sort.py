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
        return(self.get_soup().find(class_="Box-row").find_all('a')[1]['href'])

    def get_repo_star(self):
        return(int(self.get_soup().find(class_="Box-row").find(class_='octicon-star').parent.text.replace('\n','').strip()))

    def evaluate_repos(self):
        result = []
        for box in self.get_soup().find_all(class_="Box-row"):
            repo = 'https://github.com' + box.find_all('a')[1]['href']
            star = int(box.find(class_='octicon-star').parent.text.replace('\n','').strip())
            if star > 5:
                result.append(
                    {
                        'repo': repo,
                        'star': star
                    }
                )
            
        return(result)

    # TODO: private
    def get_soup(self):
        html = requests.get(self.dep_url())
        return(BeautifulSoup(html.content, "html.parser"))
