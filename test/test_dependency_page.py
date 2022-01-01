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
        self.dependency_page = dependency_page.DependencyPage(url='https://github.com/github/view_component/network/dependents')

    def tearDown(self) -> None:
        pass

    def _mock_soup(self, url):
        with open('./test/index.html') as f:
            return(BeautifulSoup(f, "html.parser"))

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

if __name__ == "__main__":
    unittest.main()
