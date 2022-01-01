import unittest
from unittest import mock
import dep_star_sort
from bs4 import BeautifulSoup

class DepStarSortTest(unittest.TestCase):
    def setUp(self) -> None:
      self.executor = dep_star_sort.DepStarSort(
                        github_url="https://github.com/github/view_component",
                        min_star=5
                    )

    def tearDown(self) -> None:
        pass

    def _mock_soup(self, url):
        with open('./test/index.html') as f:
            return(BeautifulSoup(f, "html.parser"))

    def _mock_next_page_link(self, url):
        return(None)

    @mock.patch("dep_star_sort.DepStarSort.soup", new=_mock_soup)
    def test_evaluate_repos(self):
        expect = [
            {
                'repo': 'https://github.com/ledermann/templatus-hotwire',
                'star': 6,
            },
            {
                'repo': 'https://github.com/ParamagicDev/rails_starter',
                'star': 5
            }
        ]
        self.assertEqual(self.executor.evaluate_repos(url='https://github.com/github/view_component/network/dependents'), expect)

    @mock.patch("dep_star_sort.DepStarSort.soup", new=_mock_soup)
    def test_next_page_link(self):
        self.assertEqual(self.executor.next_page_link(url='https://github.com/github/view_component/network/dependents'), "https://github.com/github/view_component/network/dependents?dependents_after=MTgzNjk2NDY2MDM")
    
    @mock.patch("dep_star_sort.DepStarSort.soup", new=_mock_soup)
    @mock.patch("dep_star_sort.DepStarSort.next_page_link", new=_mock_next_page_link)
    def test_popular_repos(self):
        expect = [
            {
                'repo': 'https://github.com/ledermann/templatus-hotwire',
                'star': 6,
            },
            {
                'repo': 'https://github.com/ParamagicDev/rails_starter',
                'star': 5
            }
        ]
        self.assertEqual(self.executor.popular_repos(), expect)

if __name__ == "__main__":
    unittest.main()
