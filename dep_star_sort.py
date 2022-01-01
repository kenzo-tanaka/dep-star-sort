import sys
import requests
from bs4 import BeautifulSoup

class DepStarSort:
    def __init__(self, github_url) -> None:
        self.github_url = github_url
        self.dep_url = f"{self.github_url}/network/dependents"
    
    def evaluate_repos(self, min_star):
        result = []
        for box in self.get_soup().find_all(class_="Box-row"):
            repo = 'https://github.com' + box.find_all('a')[1]['href']
            star = int(box.find(class_='octicon-star').parent.text.replace('\n','').strip())
            if star > min_star:
                result.append(
                    {
                        'repo': repo,
                        'star': star
                    }
                )
            
        return(result)

    # TODO: private
    def get_soup(self):
        html = requests.get(self.dep_url)
        return(BeautifulSoup(html.content, "html.parser"))

if __name__ == "__main__":
    args = sys.argv
    dep_star_sort = DepStarSort(args[1])
    print(dep_star_sort.evaluate_repos(int(args[2])))
