import sys
import requests
from bs4 import BeautifulSoup

class DepStarSort:
    def __init__(self, github_url, min_star) -> None:
        self.github_url = github_url
        self.dep_url = f"{self.github_url}/network/dependents"
        self.min_star = min_star
    
    def popular_repos(self):
        return([
            {
                'repo': 'https://github.com/ledermann/templatus-hotwire',
                'star': 6,
            },
            {
                'repo': 'https://github.com/ParamagicDev/rails_starter',
                'star': 5
            }
        ])

    def next_page_link(self, url):
        page_links = self.soup(url).find(attrs={"data-test-selector": "pagination"}).find_all('a')
        # Nextリンクのみ
        if len(page_links) == 1 and page_links[0].text == 'Next':
            return(page_links[0]['href'])
        # Prevリンクもある
        else:
            return(page_links[1]['href'])
    
    def evaluate_repos(self, url):
        result = []
        for box in self.soup(url).find_all(class_="Box-row"):
            repo = 'https://github.com' + box.find_all('a')[1]['href']
            star = int(box.find(class_='octicon-star').parent.text.replace('\n','').strip())
            if star >= self.min_star:
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
    dep_star_sort = DepStarSort(github_url=args[1], min_star=int(args[2]))
