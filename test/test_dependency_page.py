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
        self.dependecy_page = dependency_page.DepedencyPage()

    def tearDown(self) -> None:
        pass

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
        self.assertEqual(self.dependecy_page.popular_repos(), expect)

if __name__ == "__main__":
    unittest.main()
