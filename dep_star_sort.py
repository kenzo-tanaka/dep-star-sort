import sys
import requests
from bs4 import BeautifulSoup

class DepStarSort:
    def __init__(self, github_url, min_star) -> None:
        self.github_url = github_url
        self.dep_url = f"{self.github_url}/network/dependents"
        self.min_star = min_star
    
    def popular_repos(self):
        url = self.dep_url
        result = []
        while url != None:
            result += self.evaluate_repos(url)
            url = self.next_page_link(url)
        return(result)

    def next_page_link(self, url):
        page_links = self.soup(url).find(attrs={"data-test-selector": "pagination"}).find_all('a')
        # Prev, Next リンクがある
        if len(page_links) == 2:
            return(page_links[1]['href'])
        # Nextリンクのみ
        elif len(page_links) == 1 and page_links[0].text == 'Next':
            return(page_links[0]['href'])
        else:
            return(None)
            
    
    def evaluate_repos(self, url):
        result = []
        for box in self.soup(url).find_all(class_="Box-row"):
            repo = 'https://github.com' + box.find_all('a')[1]['href']
            star = int(box.find(class_='octicon-star').parent.text.replace('\n','').replace(',', '').strip())
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
    print(dep_star_sort.popular_repos())
