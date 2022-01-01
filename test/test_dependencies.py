import unittest
from unittest import mock

# @see https://note.nkmk.me/python-relative-import/
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))
import dependencies
import dependency_page
from bs4 import BeautifulSoup

class DependenciesTest(unittest.TestCase):
    def setUp(self) -> None:
      self.executor = dependencies.Dependencies(
                        github_url="https://github.com/github/view_component",
                        min_star=5
                    )

    def tearDown(self) -> None:
        pass

    def _mock_soup(self):
        with open('./test/index.html') as f:
            return(BeautifulSoup(f, "html.parser"))

    def _mock_next_page_link(self):
        return(None)

    @mock.patch("dependency_page.DependencyPage.soup", new=_mock_soup)
    @mock.patch("dependency_page.DependencyPage.next_page_link", new=_mock_next_page_link)
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
