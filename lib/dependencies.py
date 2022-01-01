import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))
import dependency_page
import md_formatter

class Dependencies:
    def __init__(self, github_url, min_star) -> None:
        self.github_url = github_url
        self.dep_url = f"{self.github_url}/network/dependents"
        self.min_star = min_star
    
    def popular_repos(self):
        url = self.dep_url
        result = []
        while url != None:
            page = dependency_page.DependencyPage(min_star=self.min_star, url=url)
            result += page.popular_repos()
            url = page.next_page_link()
        return(result)

if __name__ == "__main__":
    args = sys.argv
    dependencies = Dependencies(github_url=args[1], min_star=int(args[2]))
    popular_repos = dependencies.popular_repos()
    print(md_formatter.MdFormatter(popular_repos).display())
