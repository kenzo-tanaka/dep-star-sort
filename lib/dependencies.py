import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))
import dependency_page

class Dependencies:
    def __init__(self, github_url, min_star) -> None:
        self.github_url = github_url
        self.dep_url = f"{self.github_url}/network/dependents"
        self.min_star = min_star
    
    def popular_repos(self):
        url = self.dep_url
        result = []
        while url != None:
            result += dependency_page.DependencyPage(min_star=self.min_star, url=url).popular_repos()
            url = dependency_page.DependencyPage(min_star=self.min_star, url=url).next_page_link()
            print(url)
        return(result)

if __name__ == "__main__":
    args = sys.argv
    dependencies = Dependencies(github_url=args[1], min_star=int(args[2]))
    print(dependencies.popular_repos())
