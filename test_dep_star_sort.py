import unittest
from unittest import mock
import dep_star_sort
from bs4 import BeautifulSoup

class DepStarSortTest(unittest.TestCase):
    def setUp(self) -> None:
      self.executor = dep_star_sort.DepStarSort("https://github.com/github/view_component")

    def tearDown(self) -> None:
        pass

    def _mock_get_soup(self):
        return(BeautifulSoup(open('index.html'), "html.parser"))

    def test_dep_url(self):
        self.assertEqual(self.executor.dep_url(), "https://github.com/github/view_component/network/dependents")

    def test_response_code(self):
        self.assertEqual(self.executor.response_code(), 200)

    @mock.patch("dep_star_sort.DepStarSort.get_soup", new=_mock_get_soup)
    def test_get_repo_href(self):
        self.assertEqual(self.executor.get_repo_href(), "/ledermann/templatus-hotwire")

    @mock.patch("dep_star_sort.DepStarSort.get_soup", new=_mock_get_soup)
    def test_get_repo_star(self):
        self.assertEqual(self.executor.get_repo_star(), 6)

if __name__ == "__main__":
    unittest.main()
