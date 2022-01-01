import unittest
from unittest import mock
from bs4 import BeautifulSoup

# @see https://note.nkmk.me/python-relative-import/
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))
import dependency_page

class DependencyPageTest(unittest.TestCase):
    def setUp(self) -> None:
        self.dependency_page = dependency_page.DependencyPage(url='https://github.com/github/view_component/network/dependents', min_star=5)

    def tearDown(self) -> None:
        pass

    def _mock_soup(self):
        with open('./test/index.html') as f:
            return(BeautifulSoup(f, "html.parser"))

    @mock.patch("dependency_page.DependencyPage.soup", new=_mock_soup)
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
        self.assertEqual(self.dependency_page.popular_repos(), expect)
    
    @mock.patch("dependency_page.DependencyPage.soup", new=_mock_soup)
    def test_next_page_link(self):
        self.assertEqual(self.dependency_page.next_page_link(), "https://github.com/github/view_component/network/dependents?dependents_after=MTgzNjk2NDY2MDM")

if __name__ == "__main__":
    unittest.main()
