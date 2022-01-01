import unittest
from unittest import mock
import dep_star_sort
from bs4 import BeautifulSoup

class DepStarSortTest(unittest.TestCase):
    def setUp(self) -> None:
      self.executor = dep_star_sort.DepStarSort("https://github.com/github/view_component")

    def tearDown(self) -> None:
        pass

    def _mock_soup(self, url):
        with open('index.html') as f:
            return(BeautifulSoup(f, "html.parser"))

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
        self.assertEqual(self.executor.evaluate_repos(5), expect)

    @mock.patch("dep_star_sort.DepStarSort.soup", new=_mock_soup)
    def test_next_page_link(self):
        self.assertEqual(self.executor.next_page_link(), "https://github.com/github/view_component/network/dependents?dependents_after=MTgzNjk2NDY2MDM")

if __name__ == "__main__":
    unittest.main()
