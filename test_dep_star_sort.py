import unittest
from unittest import mock
import dep_star_sort

class DepStarSortTest(unittest.TestCase):
    def setUp(self) -> None:
      self.executor = dep_star_sort.DepStarSort("https://github.com/github/view_component")

    def tearDown(self) -> None:
        pass

    def _mock_get_repo_href(self):
        return("/ledermann/templatus-hotwire")

    def test_dep_url(self):
        self.assertEqual(self.executor.dep_url(), "https://github.com/github/view_component/network/dependents")

    def test_response_code(self):
        self.assertEqual(self.executor.response_code(), 200)

    @mock.patch("dep_star_sort.DepStarSort.get_repo_href", new=_mock_get_repo_href)
    def test_get_repo_href(self):
        self.assertEqual(self.executor.get_repo_href(), "/ledermann/templatus-hotwire")

    def test_get_repo_star(self):
        self.assertEqual(self.executor.get_repo_star(), 6)

if __name__ == "__main__":
    unittest.main()
