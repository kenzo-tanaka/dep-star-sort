import sys
import requests
from bs4 import BeautifulSoup

class DepStarSort:
    def __init__(self, github_url) -> None:
        self.github_url = github_url
        self.dep_url = f"{self.github_url}/network/dependents"

    def next_page_link(self, url):
        page_links = self.soup(url).find(attrs={"data-test-selector": "pagination"}).find_all('a')
        # Nextリンクのみ
        if len(page_links) == 1:
            return(page_links[0]['href'])
        # Prevリンクもある
        else:
            return(page_links[1]['href'])
    
    def evaluate_repos(self, min_star):
        result = []
        for box in self.soup(self.dep_url).find_all(class_="Box-row"):
            repo = 'https://github.com' + box.find_all('a')[1]['href']
            star = int(box.find(class_='octicon-star').parent.text.replace('\n','').strip())
            if star >= min_star:
                result.append(
                    {
                        'repo': repo,
                        'star': star
                    }
                )
            
        return(result)

    # TODO: private
    def soup(self, url):
        html = requests.get(url)
        return(BeautifulSoup(html.content, "html.parser"))

if __name__ == "__main__":
    args = sys.argv
    dep_star_sort = DepStarSort(args[1])
    print(dep_star_sort.evaluate_repos(int(args[2])))
