import unittest
import dep_star_sort

class DepStarSortTest(unittest.TestCase):
    def setUp(self) -> None:
      self.executor = dep_star_sort.DepStarSort("https://github.com/github/view_component")

    def tearDown(self) -> None:
        pass

    def test_dep_url(self):
        self.assertEqual(self.executor.dep_url(), "https://github.com/github/view_component/network/dependents")

    def test_response_code(self):
        self.assertEqual(self.executor.response_code(), 200)

if __name__ == "__main__":
    unittest.main()
