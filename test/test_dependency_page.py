import unittest
from unittest import mock
from bs4 import BeautifulSoup

# @see https://note.nkmk.me/python-relative-import/
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))
import dependency_page

import configparser
config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')

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
                config_ini['DEFAULT']['Repository']: 'https://github.com/ledermann/templatus-hotwire',
                config_ini['DEFAULT']['Star']: 6,
            },
            {
                config_ini['DEFAULT']['Repository']: 'https://github.com/ParamagicDev/rails_starter',
                config_ini['DEFAULT']['Star']: 5
            }
        ]
        self.assertEqual(self.dependency_page.popular_repos(), expect)
    
    @mock.patch("dependency_page.DependencyPage.soup", new=_mock_soup)
    def test_next_page_link(self):
        self.assertEqual(self.dependency_page.next_page_link(), "https://github.com/github/view_component/network/dependents?dependents_after=MTgzNjk2NDY2MDM")

if __name__ == "__main__":
    unittest.main()
